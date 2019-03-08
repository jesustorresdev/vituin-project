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

        current_page = self.xpath(response,"//li[@class='active waves-effect']/a", type='text')
        selenium = SeleniumSpider(width=333, height=200)
        selenium.set_url(response.url)
        import time
        time.sleep(5)
        from selenium.webdriver.common.action_chains import ActionChains
        time.sleep(5)
        element = selenium.xpath("//ul[@class='pagination']", type='object')
        element = element[0]
        print('')
        print('element--> ',element)
        print('')
        ActionChains(selenium.driver).move_to_element(element).perform()
        homes = selenium.xpath("//div[@class='listContainer col s12']/div", type='object', stop_if_error=True)
        homes2 = self.xpath(response, "//div[@class='listContainer col s12']/div", type='object', stop_if_error=True)
        #SOLO COGE 12
        #
        # for home in homes:
        #
        #     id = selenium.xpath("./", selenium_object=home, type='attribute', attribute='id')
        #     url ='https://es.rentalia.com/'+id
        #     place = selenium.xpath(".//div[contains(@class,'title')]/a/h4", selenium_object=home, type='text')
        #     title = selenium.xpath(".//div[contains(@class,'title')]/a/h3", selenium_object=home, type='text')
        #
        #     request = Request(url, callback=self.parse_home)
        #     request.meta['id'] = id
        #     request.meta['place'] = place[1:-1]
        #     request.meta['title'] = title
        #     if place.find(self.place) != -1:
        #         yield request
        #     # if place.find(self.place) != -1:
        #     #     yield request
        #     if self.first_searched:
        #         yield request
        #     elif not self.exist_item(ELASTICSEARCH_INDEX, url):
        #         yield request
        selenium.close_browser()

        next_page_url = self.xpath(response,"//ul[@class='pagination']/li/a", type='attribute', attribute='href',
                                   pos_extract=-1)
        next_page = next_page_url[next_page_url.find('page')+5:-2]
        next_page_url = str('https://es.rentalia.com'+next_page_url[1:-1])
        print('')
        print('')
        print('homes',len(homes))
        print('homes2',len(homes2))
        print('next_page',next_page)
        print('current_page',current_page)
        print('')
        print('')
        # if int(next_page) > int(current_page):
        #     yield Request(
        #         next_page_url, callback=self.parse
        #     )
        #


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
