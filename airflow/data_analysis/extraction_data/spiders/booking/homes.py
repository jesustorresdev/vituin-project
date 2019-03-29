# -*- coding: UTF-8 -*-

"""Extracción de viviendas en Booking
"""

__authors__ = 'Sergio Díaz, Jesús Torres'
__organization__ = 'Universidad de La Laguna'
__licensed__ = 'UNLICENSED'
__contact__ = "jmtorres@ull.edu.es, sdiazgon@ull.edu.es"
# __copyright__ = f"Copyright 2017-2018 {__organization__}"

from scrapy import Request
from extraction_data.urls import BookingURLs
from extraction_data.items import ListBookingHomeItem
from extraction_data.required_fields import ListBookingHomeRequiredFields
from extraction_data.scrapy_spider import ScrapySpider
from extraction_data.utils import split_try
from extraction_data.selenium_spider import SeleniumSpider

ELASTICSEARCH_INDEX = 'booking_homes'
ELASTICSEARCH_DOC_TYPE = 'unstructured'



#TODO use loaders
class BookingSpider(ScrapySpider):
    name = "booking_listHomes"
    def __init__(self, place=''):
        self.place = place
        self.start_urls = BookingURLs(place)

        self.first_searched = self.get_if_first_searched(ELASTICSEARCH_INDEX, ELASTICSEARCH_DOC_TYPE)

    def parse(self, response):
        homes = self.xpath(response,'//a[@class="hotel_name_link url"]', type='object', stop_if_error=True)
        if 'n_home' in response.meta:
            n_home = response.meta['n_home']
            n_page = response.meta['n_page']
        else:
            n_home = 0
            n_page = 0
        for home in homes:
            n_home += 1
            url = self.xpath(home,'./', type='attribute', attribute='href', stop_if_error=True)
            url = 'https://www.booking.com' + url[1:]
            print('url=', url, ', n_home=', n_home, ', n_page', n_page, ', url buscada=', str(response.url))
            print('')
            request = Request(url, self.parse_home)
            if self.first_searched:
                yield request
            elif not self.exist_item(ELASTICSEARCH_INDEX, url):
                yield request

        next_page = self.xpath(response,'//a[contains(@class,"paging-next")]',type='attribute', attribute='href')
        print('')
        print('')
        print('')
        print('next_page',next_page)
        print('')
        print('')
        print('')
        if next_page:
            request =  Request(
                next_page, callback=self.parse
            )
            request.meta['n_home'] = n_home
            request.meta['n_page'] = n_page
            yield request

    def parse_home(self, response):

        item = ListBookingHomeItem()


        id = self.xpath(response, '//input[@name="hotel_id"]',type='attribute', attribute='value')

        meta_data = self.xpath(response,'//script[@type="application/ld+json"]', type='text', stop_if_error=True, extract_json=True)
        title=self.try_json(meta_data,"name").encode('UTF-8').decode('UTF-8')
        description = self.try_json(meta_data,"description").encode('UTF-8').decode('UTF-8')
        type_residence = self.try_json(meta_data,"@type").encode('UTF-8').decode('UTF-8')
        score = self.try_json(meta_data,"aggregateRating","ratingValue")
        review_count = self.try_json(meta_data,"aggregateRating","reviewCount")
        address = self.try_json(meta_data,"address","streetAddress").encode('UTF-8').decode('UTF-8')
        postalCode = self.try_json(meta_data,"address","postalCode")
        region = self.try_json(meta_data,"address","addressRegion").encode('UTF-8').decode('UTF-8')
        price_min = self.try_json(meta_data,"priceRange")

        if price_min:
           price_min =  price_min[price_min.find('$')+1:price_min.find('per')-1]

        has_map = self.try_json(meta_data,"hasMap").encode('UTF-8')
        coordinates = ''
        if has_map:
            has_map_since_center = has_map[(has_map.find('center')+len('center')+1):]
            coordinates = has_map_since_center[:has_map_since_center.find('&')]

        lat = split_try(coordinates, 0, separator=',')
        lng = split_try(coordinates, 1, separator=',')


        selenium = SeleniumSpider()
        selenium.set_url(response.url)
        stars = selenium.xpath('//span[@class="hp__hotel_ratings"]/span/i', type='text', number_of_attemps=0)
        selenium.quit_browser()

        cleanliness_rating = self.xpath(response, '//li[@data-question="hotel_clean"]/p[@class="review_score_value"]', type='text')
        comfort_rating = self.xpath(response, '//li[@data-question="hotel_comfort"]/p[@class="review_score_value"]', type='text')
        facilities_rating = self.xpath(response, '//li[@data-question="hotel_services"]/p[@class="review_score_value"]', type='text')
        staff_rating = self.xpath(response, '//li[@data-question="hotel_staff"]/p[@class="review_score_value"]', type='text')
        value_for_money_rating = self.xpath(response, '//li[@data-question="hotel_value"]/p[@class="review_score_value"]', type='text')
        wifi_rating = self.xpath(response, '//li[@data-question="hotel_wifi"]/p[@class="review_score_value"]', type='text')
        location_rating = self.xpath(response, '//li[@data-question="hotel_location"]/p[@class="review_score_value"]', type='text')

        item['url']=response.url
        item['id'] = id
        item['title']=title
        item['description'] = description
        item['type_residence'] = type_residence
        item['score'] = score
        item['review_count'] = review_count
        item['address'] = address
        item['postal_code'] = postalCode
        item['region'] = region
        item['price_min'] = price_min
        item['lat'] = lat
        item['lng'] = lng
        item['stars'] = stars
        item['cleanliness_rating'] = cleanliness_rating
        item['comfort_rating'] = comfort_rating
        item['facilities_rating'] = facilities_rating
        item['staff_rating'] = staff_rating
        item['value_for_money_rating'] = value_for_money_rating
        item['wifi_rating'] = wifi_rating
        item['location_rating'] = location_rating
        item['place_searched'] = self.place

        if id:
            self.check_item(item, ListBookingHomeRequiredFields())
            self.update_database(item, ELASTICSEARCH_INDEX, ELASTICSEARCH_DOC_TYPE, self.first_searched)
            if self.first_searched:
                self.first_searched = False

            return item

