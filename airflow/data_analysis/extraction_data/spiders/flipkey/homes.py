# -*- coding: UTF-8 -*-

"""Extracción de viviendas en Flipkey
"""

__authors__ = 'Sergio Díaz, Jesús Torres'
__organization__ = 'Universidad de La Laguna'
__licensed__ = 'UNLICENSED'
__contact__ = "jmtorres@ull.edu.es, sdiazgon@ull.edu.es"
# __copyright__ = f"Copyright 2017-2018 {__organization__}"

from scrapy import Request
from extraction_data.urls import FlipkeyURLs
from extraction_data.items import ListFlipkeyHomeItem
from extraction_data.required_fields import ListFlipkeyHomeRequiredFields
from extraction_data.scrapy_spider import ScrapySpider
from extraction_data.utils import split_try
from extraction_data.selenium_spider import SeleniumSpider

ELASTICSEARCH_INDEX = 'flipkey_homes'
ELASTICSEARCH_DOC_TYPE = 'unstructured'


#TODO use loaders
class FlipkeySpider(ScrapySpider):
    name = "flipkey_listHomes"
    def __init__(self, place=''):
        self.place = place
        self.start_urls = FlipkeyURLs(place)
        self.first_searched = self.get_if_first_searched(ELASTICSEARCH_INDEX, ELASTICSEARCH_DOC_TYPE)

    def parse(self, response):
        current_page = self.xpath(response,"//div[@class ='pagination listView']/span[@class='hidden-xs']", type='text')
        homes = self.xpath(response,"//div[@id='mainSrpResults']/div[contains(@class,'data-tracking-tree-N group')]", type='object',
                           stop_if_error=True)

        for home in homes:
            id=self.xpath(home, './', type='attribute', attribute='id')[4:]
            url='https://www.flipkey.com/properties/'+id
            place = self.xpath(home,'.//p[@class="mobile shortBreadCrumb"]', type='text')
            type_residence = split_try(self.xpath(home,'.//div[@class="accomTypeDescription mobileHidden"]', type='text'),-1)
            lat = self.xpath(home,'.//div[@class="map-container"]', type='attribute', attribute='data-lat')
            lng = self.xpath(home,'.//div[@class="map-container"]', type='attribute', attribute='data-lng')
            aa = self.xpath(home,".//ul[@class='accomType mobileHidden']", type='text')
            min_stay = self.xpath(home,".//p[@class='accomType mobile']/span", type='text')

            if min_stay:
                try:
                    min_stay = int(split_try(min_stay,0))
                except:
                    min_stay = 'Varía'.decode('UTF-8')

            print(' id=', id, ', url=', url, 'place=', place, 'lat=', lat, 'lng=', lng)

            print('')
            print('')
            print('aaa->',aa)
            print('')
            print('')
            if url != 'https://www.holidaylettings.co.uk/' and url:
                request = Request(url, callback=self.parse_home)
                request.meta['id'] = id
                request.meta['place'] = place.strip()
                request.meta['lat'] = lat
                request.meta['lng'] = lng
                request.meta['type_residence'] = type_residence
                request.meta['min_stay'] = min_stay
                #
                if self.first_searched:
                    yield request
                elif not self.exist_item(ELASTICSEARCH_INDEX, url):
                    yield request

        # total_of_apartments = self.xpath(response, "//span[@class='data-tracking-tree-NG']", type='attribute',
        #                                  attribute='data-tracking-tree').replace(',','')
        # if float(current_page) < (float(total_of_apartments) / 50):
        #     next_page_url = 'https://www.flipkey.com'+ \
        #                     self.xpath(response, '//a[@class="next hidden-xs"]', type='attribute', attribute='href')
        #     yield Request(
        #         next_page_url, callback=self.parse
        #     )

    def parse_home(self, response):

        item = ListFlipkeyHomeItem()

        title = self.xpath(response, "//title", type='text')
        title = title[:title.find('|')-1]
        description = self.xpath(response, "//meta[@name='description']", type='attribute', attribute='content')
        price = self.xpath(response, "//div[@class='nonRap']/strong", type='text')[1:]

        numberReviewsTripadvisor = split_try(self.xpath(response, "//span[@itemprop='reviewCount']", type='text'), 0)
        if numberReviewsTripadvisor:
            numberReviewsTripadvisor = split_try(numberReviewsTripadvisor, 0)
        mainBubblesTripadvisor = self.xpath(response, "//meta[@itemprop='ratingValue']", type='attribute', attribute='content')

        selenium = SeleniumSpider(width=300,height=200)
        selenium.set_url(response.url)

        attributes = selenium.xpath("//div[@class='property-description-details mobile inlineBlock']/span", type='object')
        list_attributes_description = {'rooms':'','bathrooms':'','capacity':''}
        print('')
        print('')
        print('aquiiIIIIIIIIIIII')
        print('aquiiIIIIIIIIIIII')
        print('aquiiIIIIIIIIIIII')
        print(attributes)
        print('')
        print('')
        for i in range(0,len(attributes)-1):
            element = selenium.xpath("./", selenium_object=attributes[i], type='text')
            name_element = self.get_attribute_description(element[:element.find(':')].strip())
            value_element = element[element.find(':')+1:]
            list_attributes_description.update({name_element:value_element.strip()})

        selenium.close_and_kill_browser()

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
        item['type_residence'] = response.meta['type_residence']
        item['rooms'] = list_attributes_description['rooms']
        item['min_stay'] = response.meta['min_stay']
        item['price'] = price
        item['capacity'] = list_attributes_description['capacity']
        item['bathrooms'] =list_attributes_description['bathrooms']
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

        self.check_item(item, ListFlipkeyHomeRequiredFields())
        self.update_database(item, ELASTICSEARCH_INDEX, ELASTICSEARCH_DOC_TYPE, self.first_searched)
        if self.first_searched:
            self.first_searched = False

        return item
