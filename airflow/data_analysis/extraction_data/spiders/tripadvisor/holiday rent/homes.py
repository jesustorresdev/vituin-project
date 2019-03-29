# -*- coding: UTF-8 -*-

"""Extracción de viviendas en Tripadvisor
"""

__authors__ = 'Sergio Díaz, Jesús Torres'
__organization__ = 'Universidad de La Laguna'
__licensed__ = 'UNLICENSED'
__contact__ = "jmtorres@ull.edu.es, sdiazgon@ull.edu.es"
# __copyright__ = f"Copyright 2017-2018 {__organization__}"

import urlparse
from scrapy import Request
from extraction_data.urls import TripadvisorHolidaysRentURLs
from extraction_data.items import ListTripadvisorHomesItem
from extraction_data.required_fields import ListTripadvisorHomesRequiredFields
from extraction_data.scrapy_spider import ScrapySpider
from extraction_data.utils import split_try
from extraction_data.selenium_spider import SeleniumSpider

ELASTICSEARCH_INDEX = 'tripadvisor_homes'
ELASTICSEARCH_DOC_TYPE = 'unstructured'

#TODO use loaders
class TripadvisorSpider(ScrapySpider):
    name = "tripadvisor_listHomes"
    def __init__(self, place=''):
        self.place = place
        self.start_urls = TripadvisorHolidaysRentURLs(place)
        self.first_searched = self.get_if_first_searched(ELASTICSEARCH_INDEX, ELASTICSEARCH_DOC_TYPE)

    def parse(self, response):
        homes = self.xpath(response,'//div[@class="vr_listing"]', type='object', stop_if_error=True)
        for home in homes:
            url = self.xpath(home,'.//div[@class="property_title"]/a', type='attribute', attribute='href', stop_if_error=True)
            id = self.xpath(home,'./', type='attribute', attribute='id')
            print('url=', url, 'id=', id)
            request = Request(urlparse.urljoin(response.url, url), callback=self.parse_home)
            request.meta['id'] = id
            if self.first_searched:
                yield request
            elif not self.exist_item(ELASTICSEARCH_INDEX, url):
                yield request
            break
        next_page = self.xpath(response,'//a[@class="ui_button primary nav next"]',type='attribute', attribute='href')
        print('')
        print('')
        print('')
        print('next_page_url',next_page)
        print('')
        print('')
        print('')
        if next_page:
            next_page_url = 'https://www.tripadvisor.es'+next_page
            yield Request(
                next_page_url, callback=self.parse
            )

    def parse_home(self, response):

        item = ListTripadvisorHomesItem()

        meta_data = self.xpath(response,'//script[@type="application/ld+json"]', type='text', stop_if_error=True, pos_extract=0, extract_json=True)
        title=self.try_json(meta_data,"name").encode('UTF-8')
        description = self.try_json(meta_data,"description").encode('UTF-8')
        type_residence = self.try_json(meta_data,"@type").encode('UTF-8')
        score = self.try_json(meta_data,"aggregateRating","ratingValue")
        review_count = self.try_json(meta_data,"aggregateRating","reviewCount")

        description_items = self.xpath(response,'//div[starts-with(@class,"vr-overview-Overview__propertyInfoLabel")]', type='object')
        rooms = split_try(self.xpath(description_items,'./', type='text', pos_extract=0),0)
        bathrooms = split_try(self.xpath(description_items,'./', type='text', pos_extract=1),0)
        n_people = split_try(self.xpath(description_items,'./', type='text', pos_extract=2),0)
        min_stay = split_try(self.xpath(description_items,'./', type='text', pos_extract=3),0)

        place = self.xpath(response, '//meta[@property="og:title"]',type='attribute', attribute='content')
        place = place[place.find('Alquileres vacacionales en')+27:place.find('Tripadvisor')-13]
        selenium = SeleniumSpider(width=500,height=300)
        selenium.set_url(response.url)
        (lat,lng) = selenium.get_coordinates_google_map()
        price = split_try(selenium.xpath('//span[starts-with(@class,"vr-rap-RapFooter__periodCost")]', type='text', number_of_attemps=0),0)
        selenium.quit_browser()

        item['url']=response.url
        item['id'] = response.meta['id']
        item['title']=title
        item['description'] = description.decode('UTF-8')
        item['type_residence'] = type_residence
        item['score'] = score
        item['review_count'] = review_count
        item['price'] = price
        item['rooms']=rooms
        item['bathrooms']=bathrooms
        item['n_people']=n_people
        item['lat']=lat
        item['lng']=lng
        item['min_stay']=min_stay
        item['place'] = place
        item['place_searched'] = self.place

        self.check_item(item, ListTripadvisorHomesRequiredFields())
        self.update_database(item, ELASTICSEARCH_INDEX, ELASTICSEARCH_DOC_TYPE, self.first_searched)
        if self.first_searched:
            self.first_searched = False

        return item
