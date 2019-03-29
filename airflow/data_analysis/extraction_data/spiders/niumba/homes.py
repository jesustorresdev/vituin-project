# -*- coding: UTF-8 -*-

"""Extracción de viviendas en Niumba
"""

__authors__ = 'Sergio Díaz, Jesús Torres'
__organization__ = 'Universidad de La Laguna'
__licensed__ = 'UNLICENSED'
__contact__ = "jmtorres@ull.edu.es, sdiazgon@ull.edu.es"
# __copyright__ = f"Copyright 2017-2018 {__organization__}"

from scrapy import Request
from extraction_data.urls import NiumbaURLs
from extraction_data.items import ListNiumbaHomeItem
from extraction_data.required_fields import ListNiumbaHomeRequiredFields
from extraction_data.scrapy_spider import ScrapySpider
from extraction_data.utils import split_try

ELASTICSEARCH_INDEX = 'niumba_homes'
ELASTICSEARCH_DOC_TYPE = 'unstructured'

#TODO use loaders
class NiumbaSpider(ScrapySpider):
    name = "niumba_listHomes"
    def __init__(self, place=''):
        self.place = place
        self.start_urls = NiumbaURLs(place)
        self.first_searched = self.get_if_first_searched(ELASTICSEARCH_INDEX, ELASTICSEARCH_DOC_TYPE)

    def parse(self, response):
        current_page = self.xpath(response,"//div[@class ='pagination listView']/span[@class='hidden-xs']", type='text')
        homes = self.xpath(response,"//div[@id='mainSrpResults']/div[contains(@class,'data-tracking-tree-N group')]", type='object',
                           stop_if_error=True)
        for home in homes:
            url=self.xpath(home, './', type='attribute', attribute='data-rental-unit-url')
            id=self.xpath(home, './', type='attribute', attribute='id')[4:]
            place = self.xpath(home,'.//p[@class="mobile shortBreadCrumb"]', type='text')
            lat = self.xpath(home,'.//div[@class="map-container"]', type='attribute', attribute='data-lat')
            lng = self.xpath(home,'.//div[@class="map-container"]', type='attribute', attribute='data-lng')

            if url != 'https://www.niumba.com' and url:
                request = Request(url, callback=self.parse_home)
                request.meta['id'] = id
                request.meta['place'] = place.strip()
                request.meta['lat'] = lat
                request.meta['lng'] = lng

                print(' id=', id, ', url=', url, 'place=', place)

                if self.first_searched:
                    yield request
                elif not self.exist_item(ELASTICSEARCH_INDEX, url):
                    yield request

        total_of_apartments = self.xpath(response, "//span[@class='data-tracking-tree-NG']", type='attribute',
                                         attribute='data-tracking-tree').replace(',','')
        print('')
        print('')
        print('')
        print('current_page',current_page)
        print('')
        print('')
        print('')
        if float(current_page) < (float(total_of_apartments) / 50):
            next_page_url = 'https://www.niumba.com'+ \
                            self.xpath(response, '//a[@class="next hidden-xs"]', type='attribute', attribute='href')
            yield Request(
                next_page_url, callback=self.parse
            )

    def parse_home(self, response):

        item = ListNiumbaHomeItem()

        title = self.xpath(response, "//meta[@property='og:title']", type='attribute', attribute='content')
        title = title[:title.find('Alojamiento')-5]
        description = self.xpath(response, "//meta[@name='description']", type='attribute', attribute='content')
        price = self.xpath(response, "//div[@class='nonRap']/strong", type='text')[1:]

        numberReviewsTripadvisor = split_try(self.xpath(response, "//span[@itemprop='reviewCount']", type='text'), 0)
        if numberReviewsTripadvisor:
            numberReviewsTripadvisor = split_try(numberReviewsTripadvisor, 0)
        mainBubblesTripadvisor = self.xpath(response, "//meta[@itemprop='ratingValue']", type='attribute', attribute='content')

        bathrooms = split_try(self.xpath(response, ".//i[@class='icon icon-bath']/..", type='text'), 0)

        type_residence = self.xpath(response, "//i[@class='icon icon-house']/parent::li", type='text')
        capacity = self.xpath(response, "//i[@class='icon icon-sleeps']/../span", type='text', pos_array=0)
        min_stay = self.xpath(response, "//i[@class='icon icon-min-stay']/../span", type='text')
        if min_stay:
            try:
                min_stay = int(min_stay)
            except:
                min_stay = 'Varía'.decode('UTF-8')
        rooms = self.xpath(response, "//i[@class='icon icon-bed']/../span[1]", type='text')

        tourist_license = self.xpath(response, "//p[@class='touristLicence']", type='text',pos_extract=1).strip()

        attributes_response = self.xpath(response, "//dl[@class='group']", type='object', pos_array=0)
        attributes_name = self.get_attributes_array_tripadvisor_rentals(self.xpath(attributes_response,".//dt", type='text', pos_extract=None))
        attributes_value = self.get_attributes_array_tripadvisor_rentals(self.xpath(attributes_response,".//dd", type='text', pos_extract=None))

        attributes = self.get_attribute_tripadvisor_rentals(attributes_name,attributes_value)
        list_attributes = {'response_rate':'','years_advertising':'','last_update':'', 'average_response_time':''}
        for key in attributes:
            list_attributes.update({key:attributes[key]})

        item['id'] = response.meta['id']
        item['url'] = response.url
        item['title'] = title
        item['description'] = description
        item['type_residence'] = type_residence
        item['rooms'] = rooms
        item['min_stay'] = min_stay
        item['price'] = price
        item['capacity'] = capacity
        item['bathrooms'] = bathrooms
        item['number_reviews_tripadvisor'] = numberReviewsTripadvisor
        item['main_bubbles_tripadvisor'] = mainBubblesTripadvisor
        item['tourist_license'] = tourist_license
        item['average_response_time'] = list_attributes['average_response_time']
        item['response_rate'] = list_attributes['response_rate']
        item['years_advertising'] = list_attributes['years_advertising']
        item['last_update'] = list_attributes['last_update']
        item['lat'] = response.meta['lat']
        item['lng'] = response.meta['lng']
        item['place'] = response.meta['place']
        item['place_searched'] = self.place

        self.check_item(item, ListNiumbaHomeRequiredFields())
        self.update_database(item, ELASTICSEARCH_INDEX, ELASTICSEARCH_DOC_TYPE, self.first_searched)
        if self.first_searched:
            self.first_searched = False

        return item
