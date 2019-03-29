# -*- coding: UTF-8 -*-

"""Extracción de viviendas en Rentalia
"""

__authors__ = 'Sergio Díaz, Jesús Torres'
__organization__ = 'Universidad de La Laguna'
__licensed__ = 'UNLICENSED'
__contact__ = "jmtorres@ull.edu.es, sdiazgon@ull.edu.es"
# __copyright__ = f"Copyright 2017-2018 {__organization__}"

from scrapy import Request
from extraction_data.urls import RentaliaURLs
from extraction_data.items import ListRentaliaHomeItem
from extraction_data.required_fields import ListRentaliaHomeRequiredFields
from extraction_data.scrapy_spider import ScrapySpider
from extraction_data.selenium_spider import SeleniumSpider
from extraction_data.utils import split_try

ELASTICSEARCH_INDEX = 'rentalia_homes'
ELASTICSEARCH_DOC_TYPE = 'unstructured'

#TODO use loaders
class RentaliaSpider(ScrapySpider):
    name = "rentalia_listHomes"

    def __init__(self, place=''):
        self.place = place
        self.start_urls = RentaliaURLs(place)
        self.first_searched = self.get_if_first_searched(ELASTICSEARCH_INDEX, ELASTICSEARCH_DOC_TYPE)

    def parse(self, response):
        n_home = 0
        n_page = 0
        selenium = SeleniumSpider()
        selenium.set_url(response.url)
        last_home = selenium.xpath("//div[@class='title']/h1", type='text')
        last_home = split_try(last_home,0)
        more_pages = True
        next_page_url = response.url
        while more_pages:
            n_page += 1
            current_page = selenium.xpath("//li[@class='active waves-effect']/a", type='text')
            selenium.scroll_to_element('end')
            attemps = 0
            homes = []
            while attemps < 3:
                homes = selenium.xpath("//div[@class='itemContent']/..", type='object', stop_if_error=True)
                if len(homes) == 30:
                    attemps = 3
                else:
                    attemps += 1

            for home in homes:

                id = selenium.xpath("./", selenium_object=home, type='attribute', attribute='id', stop_if_error=True)
                url ='https://es.rentalia.com/'+id
                place = selenium.xpath(".//div[contains(@class,'title')]/a/h4", selenium_object=home, type='text')
                title = selenium.xpath(".//div[contains(@class,'title')]/a/h3", selenium_object=home, type='text')
                n_home += 1
                print(n_home, ' id=', id, ', url=', url, ', pagina: ', current_page, 'numero de apartamentos total:', last_home, 'url busqueda general:', str(next_page_url))
                print('')
                request = Request(url, callback=self.parse_home)
                request.meta['id'] = id
                request.meta['place'] = place[1:-1]
                request.meta['title'] = title
                if self.first_searched:
                    yield request
                elif not self.exist_item(ELASTICSEARCH_INDEX, url):
                    yield request

            next_page_url = selenium.xpath("//div[contains(@class, 'pagCount')]/ul/li/a", type='attribute',
                                           attribute='href', pos_array =-1)

            next_page = next_page_url[next_page_url.find('page')+5:-1]
            print('')
            print('')
            print('next_page',next_page)
            print('next_page_url',next_page_url)
            print('current_page',current_page)
            print('')
            print('')
            if not next_page:
                next_page = 1000
            if not current_page:
                current_page = 0
            if int(next_page) > int(current_page):
                selenium.set_url(next_page_url)
            else:
                more_pages = False
                print 'Fin n_page=',n_page,':', str(response.url)

        selenium.quit_browser()

    def parse_home(self, response):
        item = ListRentaliaHomeItem()

        #Atributos
        type_residence = self.xpath(response,"//span[@class='lastBreadcrumb']", type='text')
        type_residence = type_residence[:type_residence.find('Ref')].replace(" ", "")
        capacity = self.xpath(response,"//span[contains(@class,'icon-personas')]/parent::div/p", type='text').replace(" ", "")
        rooms = self.xpath(response,"//span[contains(@class,'icon-habitaciones')]/parent::div/p", type='text').replace(" ", "")
        bathrooms = self.xpath(response,"//span[contains(@class,'icon-completo')]/parent::div/p", type='text').replace(" ", "")
        beds = self.xpath(response,"//span[contains(@class,'icon-cama-b-blue')]/parent::div/p", type='text').replace(" ", "")

        #Coordenadas
        controller =  self.xpath(response,"//div[@ng-controller='HouseController']", type='attribute', attribute='ng-init')
        pos_longitude = controller.find('"longitude"')
        controller_coordinates_dict =controller[controller.find('{') : controller[pos_longitude:].find('}')+pos_longitude+1]
        coor =  controller_coordinates_dict[controller_coordinates_dict.find('"latitude"'):]
        lat = coor[coor.find(':')+1:coor.find(',')].replace('"','')
        lng = coor[coor.find('"longitude"')+len("longitude")+3:-1].replace('"','')

        #Reviews y rating
        numberReviews = self.xpath(response,"//div[contains(@class,'valuations')]/span", type='text', pos_array=0)
        if int(numberReviews) != 0:
            mainBubbles = self.xpath(response,"//div[contains(@class,'stars')]/div[@class='percentage']", type='attribute', attribute='style')
            mainBubbles = float(mainBubbles[mainBubbles.find(':')+1:-1]) / (2 * 10)
        else:
            mainBubbles = 0

        #Estancia mínima
        pos_min_stay = controller.rfind('"nights_min":')-1
        min_stay = controller[pos_min_stay+1:]
        min_stay = min_stay[min_stay.find(':')+1:min_stay.find(',')]

        #Precio
        pos_price = controller.rfind('"price_night":')-1
        price = controller[pos_price+1:]
        price = price[price.find(':')+1:price.find(',')].replace('"','')

        item['title'] = response.meta['title']
        item['id'] = response.meta['id']
        item['place'] = response.meta['place']
        item['url'] = response.url
        item['lat'] = lat
        item['lng'] = lng
        item['type_residence'] = type_residence
        item['main_bubbles'] = mainBubbles
        item['number_reviews'] = numberReviews
        item['min_stay'] = min_stay
        item['capacity'] = capacity
        item['rooms'] = rooms
        item['bathrooms'] = bathrooms
        item['beds'] = beds
        item['price'] = price
        item['place_searched'] = self.place

        self.check_item(item, ListRentaliaHomeRequiredFields())
        self.update_database(item, ELASTICSEARCH_INDEX, ELASTICSEARCH_DOC_TYPE, self.first_searched)
        if self.first_searched:
            self.first_searched = False

        return item
