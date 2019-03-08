# -*- coding: UTF-8 -*-

"""Extracción de viviendas en Atraveo
"""

__authors__ = 'Sergio Díaz, Jesús Torres'
__organization__ = 'Universidad de La Laguna'
__licensed__ = 'UNLICENSED'
__contact__ = "jmtorres@ull.edu.es, sdiazgon@ull.edu.es"
# __copyright__ = f"Copyright 2017-2018 {__organization__}"

import time
from scrapy import Request
from extraction_data.urls import AtraveoURLs
from extraction_data.items import ListAtraveoHomeItem
from extraction_data.required_fields import ListAtraveoHomeRequiredFields
from extraction_data.scrapy_spider import ScrapySpider
from extraction_data.selenium_spider import SeleniumSpider
from extraction_data.utils import split_try

ELASTICSEARCH_INDEX = 'atraveo_homes'
ELASTICSEARCH_DOC_TYPE = 'unstructured'

#TODO use loaders
class AtraveoSpider(ScrapySpider):
    name = "atraveo_listHomes"

    def __init__(self, place=''):
        self.place = place
        self.start_urls = AtraveoURLs(place)
        self.first_searched = self.get_if_first_searched(ELASTICSEARCH_INDEX, ELASTICSEARCH_DOC_TYPE)

    def parse(self, response):
        selenium = SeleniumSpider()
        selenium.set_url(response.url)
        more_pages = True
        while more_pages:
            homes = selenium.xpath("//div[@id='searchResults']/ul/li", type='object', stop_if_error=True, time_sleep_if_error=True)
            for home in homes:
                url = selenium.xpath( ".//div[@class='resultlinks']/a", selenium_object=home, type='attribute', attribute='href', stop_if_error=True)
                id = selenium.xpath( "./", selenium_object=home, type='attribute', attribute='data-accommodation-id')
                title = selenium.xpath( ".//h3[@class='resulthead']", selenium_object=home, type='text')
                lat = selenium.xpath( "./", selenium_object=home, type='attribute', attribute='data-lat')
                lng = selenium.xpath( "./", selenium_object=home, type='attribute', attribute='data-lng')
                price = split_try(selenium.xpath(".//div[@class='price']/span", selenium_object=home, type='text'), -1)

                request = Request(url, callback=self.parse_home)
                request.meta['id'] = id
                request.meta['title'] = title
                request.meta['lat'] = lat
                request.meta['lng'] = lng
                request.meta['price'] = price

                if self.first_searched:
                    yield request
                elif not self.exist_item(ELASTICSEARCH_INDEX, url):
                    yield request

            next_page_url = selenium.xpath("//a[@class='forward']", type='attribute', attribute='href')

            try:
                selenium.set_url(next_page_url)
            except:
                more_pages = False

        selenium.close_and_kill_browser()


    def parse_home(self, response):
        item = ListAtraveoHomeItem()
        description = self.xpath(response, "//meta[@name='description']", type='attribute', attribute='content')
        description=description[:description.find('|')-1]

        selenium = SeleniumSpider()
        selenium.set_url(response.url)
        place =  selenium.xpath("//span[@class='geotext']", type='text')
        summary = selenium.xpath("//span[@class='watchlistContent']", type='text', number_of_attemps=0)
        numberReviews = split_try(summary, 0)
        mainBubbles = split_try(summary, 3)
        price = response.meta['price']
        if not price:
            price = split_try(selenium.xpath("//div[@id='totalPrice']", type='text', number_of_attemps=0), -1)

        title = response.meta['title']
        capacity = split_try(title, -2)
        type_residence = title[:title.find('para')-1]
        attributes = split_try(selenium.xpath("//div[@class='featuresText']", type='text'), splitline=True)
        list_attributes= {'rooms':'','bathrooms':''}
        m2 = split_try(attributes, 1, pos_aray=0)
        for i in range(1,3):
            name_element = self.get_attribute_description(split_try(attributes[i], -1))
            if name_element:
                list_attributes.update({name_element:split_try(attributes[i], -0)})

        selenium.close_browser()

        item['id'] = response.meta['id']
        item['title'] = title
        item['description'] = description
        item['url'] = response.url
        item['lat'] = response.meta['lat']
        item['lng'] = response.meta['lng']
        item['price'] = price
        item['main_bubbles'] = mainBubbles
        item['number_reviews'] = numberReviews
        item['type_residence'] = type_residence
        item['capacity'] = capacity
        item['m2'] = m2
        item['rooms'] = list_attributes['rooms']
        item['bathrooms'] = list_attributes['bathrooms']
        item['place_searched'] = self.place
        item['place'] = place

        self.check_item(item, ListAtraveoHomeRequiredFields())
        self.update_database(item, ELASTICSEARCH_INDEX, ELASTICSEARCH_DOC_TYPE, self.first_searched)
        if self.first_searched:
            self.first_searched = False

        return item
