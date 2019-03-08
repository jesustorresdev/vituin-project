# -*- coding: UTF-8 -*-

"""Extracción de viviendas en Airbnb
"""

__authors__ = 'Sergio Díaz, Jesús Torres'
__organization__ = 'Universidad de La Laguna'
__licensed__ = 'UNLICENSED'
__contact__ = "jmtorres@ull.edu.es, sdiazgon@ull.edu.es"
# __copyright__ = f"Copyright 2017-2018 {__organization__}"

from scrapy import Request
from extraction_data.urls import AirbnbURLs
from extraction_data.items import ListAirbnbHomeItem
from extraction_data.required_fields import ListAirbnbHomeRequiredFields
from extraction_data.selenium_spider import SeleniumSpider
from extraction_data.scrapy_spider import ScrapySpider
from extraction_data.utils import type_try, split_try

ELASTICSEARCH_INDEX = 'airbnb_homes'
ELASTICSEARCH_DOC_TYPE = 'unstructured'

def get_coordinates(coordinates):
    str_coor = str(coordinates)
    pos1 = str_coor.find("center")+7
    pos2 = str_coor.find("scale")-1
    coor = str_coor[pos1:pos2]
    coor = coor.split(',')
    lat = coor[0]
    lng = coor[1]

    return (lat, lng)

#TODO use loaders
class AibrnbSpider(ScrapySpider):
    name = "airbnb_listHomes"

    def __init__(self, place=''):
        self.place = place
        self.start_urls = AirbnbURLs(place)
        self.first_searched = self.get_if_first_searched(ELASTICSEARCH_INDEX, ELASTICSEARCH_DOC_TYPE)

    def parse(self, response):
        print 'INICIO'
        print response.url
        selenium = SeleniumSpider()
        selenium.set_url(response.url)
        n = 0
        more_pages = True
        while more_pages:
            last_page = selenium.xpath("//div[@class='_1bdke5s']", pos_extract=-1)
            print 'Last_Page', last_page
            links = selenium.xpath("//a[contains(@class, '_1ol0z3h')]", type='object', stop_if_error='Links')
            print links
            for link in links:
                link = selenium.xpath("./", selenium_object=link, type='attribute', attribute='href')
                id = link[link.find('rooms')+6:link.find('?')]
                n+=1
                url = response.urljoin(link)
                print ''
                print ''
                print ''
                print(n, ' id=', id, ', url=', url, '------->n:',n,'links=',len(links))
                print ''
                print ''
                print ''
                request = Request(url, callback=self.parse_home)

                request.meta['id']=id
                # If the hotel doesnt have in the list, it will extract its data
                if self.first_searched:
                    yield request
                elif not self.exist_item(ELASTICSEARCH_INDEX, url):
                    yield request


            url_new_page = selenium.xpath("//a[@class='_1ip5u88']", type='attribute', attribute='href', pos_array=-1)
            last_page = type_try(selenium.xpath("//div[@class='_1bdke5s']", type='text', pos_array=-1), int)-1
            current_page = type_try(selenium.xpath("//div[@class='_e602arm']", type='text', pos_array=-1), int)-1

            print('')
            print('')
            print('')
            print 'Current',current_page, ', last', last_page
            print 'Current',type(current_page), ', last', type(last_page)
            print('')
            print('')
            print('')
            if last_page>current_page:
                selenium.set_url(url_new_page)
            else:
                more_pages = False
                print 'Fin'

        selenium.close_browser()
        selenium.kill_chrome()
        selenium.kill_chromedriver()

    def parse_home(self, response):
        item = ListAirbnbHomeItem()
        name = self.xpath(response, "//meta[@property='og:title']", type='attribute', attribute='content')
        description = self.xpath(response, "//meta[@name='description']", type='attribute', attribute='content')

        selenium = SeleniumSpider(width=330,height=350)
        selenium.set_url(response.url)
        url_coordinates = selenium.xpath("//div[@class='_59m2yxn']/img", type='attribute', attribute='src')
        (lat, lng) = get_coordinates(url_coordinates)
        type_residence = selenium.xpath("//span[@class='_1xxanas2']/span", type='text', pos_array=-1).lower()
        attributes = selenium.xpath("//div[@class='_n5lh69r']/div/div/span[@class='_czm8crp']", type='object')

        list_attributes = {'capacity':'','rooms':'','bathrooms':'', 'beds':''}
        for element in attributes:
            attribute = selenium.xpath("./", selenium_object=element, type='text')
            list_attributes.update({self.get_attribute_description(split_try(attribute,1)):split_try(attribute,0)})

        place = selenium.xpath("//a[@href='#neighborhood']", type='attribute', attribute='aria-label')
        place = place[place.find(":")+1:]

        selenium.close_browser()

        item['name'] = name
        item['id'] = response.meta['id']
        item['url'] = response.url
        item['description'] = description
        item['lat'] = lat
        item['lng'] = lng
        item['type_residence'] = type_residence
        item['capacity'] = list_attributes['capacity']
        item['rooms'] = list_attributes['rooms']
        item['bathrooms'] = list_attributes['bathrooms']
        item['beds'] = list_attributes['beds']
        # item['min_stay'] = min_stay
        # item['price'] = price
        item['place'] = place
        item['place_searched'] = self.place

        self.check_item(item, ListAirbnbHomeRequiredFields())
        self.update_database(item, ELASTICSEARCH_INDEX, ELASTICSEARCH_DOC_TYPE, self.first_searched)
        if self.first_searched:
            self.first_searched = False

        return item

