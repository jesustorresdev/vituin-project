# -*- coding: UTF-8 -*-

"""Extracción de viviendas en Homeway
"""

__authors__ = 'Sergio Díaz, Jesús Torres'
__organization__ = 'Universidad de La Laguna'
__licensed__ = 'UNLICENSED'
__contact__ = "jmtorres@ull.edu.es, sdiazgon@ull.edu.es"
# __copyright__ = f"Copyright 2017-2018 {__organization__}"

from scrapy import Request
from extraction_data.urls import Flats9URLs
from extraction_data.items import List9FlatHomeItem
from extraction_data.required_fields import List9FlatHomeRequiredFields
from extraction_data.scrapy_spider import ScrapySpider
from extraction_data.selenium_spider import SeleniumSpider
from extraction_data.utils import split_try


#TODO use loaders
class Flats9Spider(ScrapySpider):
    name = "9Flats_listHomes"

    def __init__(self, place=''):
        self.place = place
        self.start_urls = Flats9URLs(place)
        # self.start_urls = ['https://www.homeaway.es/p1630351?noDates=true&petIncluded=false&uni_id=3231485']
        # self.first_searched = self.get_if_first_searched(ELASTICSEARCH_INDEX, ELASTICSEARCH_DOC_TYPE)

    def parse(self, response):
        selenium = SeleniumSpider()
        selenium.set_url(response.url)
        more_pages = True
        n=0
        while more_pages:
            n+=1
            links = selenium.xpath("//h4[contains(@class, 'HitInfo__headline')]", type='object', stop_if_error=True)
            for link in links:
                url = selenium.xpath( "./", selenium_object=link, type='attribute', attribute='href', stop_if_error=True)
                id = url[1:]
                url='https://www.homeaway.es'+url
                print(' id=', id, ', url=', url)
                request = Request(url, callback=self.parse_home)
                request.meta['id'] = id
                yield request

            next_page_url = selenium.xpath( "//a[@label='Next page']", type='attribute', attribute='href', stop_if_error=True)
            if next_page_url:
                print('pagina siguiente', next_page_url)
                selenium.set_url(next_page_url)
            else:
                more_pages = False
                print ''
                print ''
                print ''
                print 'Fin------------->', n
                print ''
                print ''
                print ''
        selenium.close_browser()


    def parse_home(self, response):
        item = List9FlatHomeItem()


        selenium = SeleniumSpider()
        selenium.set_url(response.url)
        tourist_license = selenium.xpath("//div[@class='registration-number']", type='text', number_of_attemps=0)
        tourist_license = tourist_license[tourist_license.find(':')+1:].strip()
        (lat,lng) = selenium.get_coordinates_google_map()
        place = selenium.xpath("//input[@id='react-destination-typeahead']", type='attribute', attribute='value')
        selenium.close_browser()

        title = self.xpath(response, "//meta[@property='og:title']", type='attribute', attribute='content')
        title = title[:title.find('- HomeAway')-1]
        description = self.xpath(response, "//meta[@property='og:description']", type='attribute', attribute='content')
        price = self.xpath(response, "//meta[@property='og:price:amount']", type='attribute', attribute='content')
        mainBubbles = self.xpath(response, "//meta[@property='og:rating']", type='attribute', attribute='content')
        if mainBubbles:
            numberReviews = self.xpath(response, "//strong[@class='reviews-summary__num-reviews']", type='text')
            numberReviews = split_try(numberReviews,1)
        else:
            numberReviews = 0

        attributes = self.xpath(response, "//li[@class='listing-bullets__list-item']", type='object')
        type_and_m2 = self.xpath(attributes, "./", type='object', pos_array=0)
        type_residence = self.xpath(type_and_m2, "./", type='text')
        m2 = self.xpath(type_and_m2, "./span[@class='listing-bullets__span']", type='text', pos_extract=1).replace('"','')

        list_attributes = {'capacity':'','rooms':'','bathrooms':'','min_stay':'','toilets':''}
        for i in range(1,len(attributes)):
            element = self.xpath(attributes, "./", type='object', pos_array=i)
            element = self.xpath(element, "./span[@class='listing-bullets__span']", type='text')
            name_element = self.get_attribute_description(element[:element.find(':')].strip())
            value_element = element[element.find(':')+1:]
            list_attributes.update({name_element:value_element.strip()})

        item['id'] = response.meta['id']
        item['title'] = title
        item['description'] = description
        item['url'] = response.url
        item['lat'] = lat
        item['lng'] = lng
        item['price'] = price
        item['main_bubbles'] = mainBubbles
        item['number_reviews'] = numberReviews
        item['type_residence'] = type_residence
        item['m2'] = m2
        item['capacity'] = list_attributes['capacity']
        item['rooms'] = list_attributes['rooms']
        item['bathrooms'] = list_attributes['bathrooms']
        item['toilets'] = list_attributes['toilets']
        item['min_stay'] = list_attributes['min_stay']
        item['tourist_license'] = tourist_license

        self.check_item(item, List9FlatHomeRequiredFields())

        # if place == self.place:
        #     return item
        return item