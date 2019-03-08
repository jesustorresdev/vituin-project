# -*- coding: UTF-8 -*-

"""Extracción de hoteles en Tripadvisor
"""

__authors__ = 'Sergio Díaz, Jesús Torres'
__organization__ = 'Universidad de La Laguna'
__licensed__ = 'UNLICENSED'
__contact__ = "jmtorres@ull.edu.es, sdiazgon@ull.edu.es"
# __copyright__ = f"Copyright 2017-2018 {__organization__}"

import urlparse
from scrapy import Request
from extraction_data.urls import TripAdvisorHotelsURLs
from extraction_data.items import ListTripadvisorHotelsItem
from extraction_data.required_fields import ListTripadvisorHotelsRequiredFields
from extraction_data.scrapy_spider import ScrapySpider
from extraction_data.utils import split_try, type_try

ELASTICSEARCH_INDEX = 'tripadvisor_hotels'
ELASTICSEARCH_DOC_TYPE = 'unstructured'


def get_value_from_bubble(element):
    element = split_try(element, 1)
    element = type_try(element[element.find('_')+1:], float)
    try:
        return element/10
    except:
        return ''

def get_number_ratings(percentage, number_reviews):
    return type_try(percentage[:-2], float)*type_try(number_reviews, int) / 100


#TODO use loaders
class TripadvisorSpider(ScrapySpider):
    name = "tripadvisor_listHotels"
    def __init__(self, place=''):
        self.place = place
        self.start_urls = TripAdvisorHotelsURLs(place)
        self.first_searched = self.get_if_first_searched(ELASTICSEARCH_INDEX, ELASTICSEARCH_DOC_TYPE)

    def parse(self, response):
        hotels = self.xpath(response,'//div[@class="listing_title"]/a', type='object', stop_if_error=True)

        for hotel in hotels:
            url = self.xpath(hotel,'./', type='attribute', attribute='href', stop_if_error=True)
            id = self.xpath(hotel,'./', type='attribute', attribute='id')
            print('url=', url)
            request = Request(urlparse.urljoin(response.url, url), callback=self.parse_hotel)
            request.meta['id'] = id
            if self.first_searched:
                yield request
            elif not self.exist_item(ELASTICSEARCH_INDEX, url):
                yield request

        next_page = self.xpath(response,'//a[@class="nav next taLnk ui_button primary"]',type='attribute', attribute='href')
        if next_page:
            next_page_url = 'https://www.tripadvisor.es'+next_page
            yield Request(
                next_page_url, callback=self.parse
            )

    def parse_hotel(self, response):

        item = ListTripadvisorHotelsItem()

        meta_data = self.xpath(response,'//script[@type="application/ld+json"]', type='text', stop_if_error=True, extract_json=True)
        title=self.try_json(meta_data, "name").encode('UTF-8')
        description = self.xpath(response, '//meta[@name="description"]', type='attribute', attribute='content')
        street_address = self.try_json(meta_data, "address","streetAddress")
        extended_address = self.xpath(response, '//span[@class="extended-address"]',type='text')
        locality_address = self.try_json(meta_data, "address", "addressLocality")

        postal_code = self.try_json(meta_data, "address", "postalCode")
        score = self.try_json(meta_data, "aggregateRating", "ratingValue")
        review_count = self.try_json(meta_data, "aggregateRating", "reviewCount")

        price_range = self.try_json(meta_data, "priceRange")
        price_range =  price_range[:price_range.find('(')-1]


        (lat, lng) = self.api_coordinates(street_address+', '+locality_address)

        stars = get_value_from_bubble(self.xpath(response,'//div[starts-with(@class,"hotels-hotel-review-about-with-photos-layout-TextItem__textitem")]/span'\
                           , type='attribute', attribute='class'))

        ratings =  self.xpath(response, '//div[starts-with(@class, "hotels-hotel-review-about-with-photos-Reviews__subratingRating")]/span', type='object')
        location_rating = get_value_from_bubble(self.xpath(ratings, './', type='attribute', attribute='class', pos_extract=0))
        cleanliness_rating = get_value_from_bubble(self.xpath(ratings, './', type='attribute', attribute='class', pos_extract=1))
        services_rating = get_value_from_bubble(self.xpath(ratings, './', type='attribute', attribute='class', pos_extract=2))
        value_rating =  get_value_from_bubble(self.xpath(ratings, './', type='attribute', attribute='class', pos_extract=3))


        excelent = self.xpath(response, '//label[@for="ReviewRatingFilter_5"]/../span', type='text', pos_extract=0)
        very_good = self.xpath(response, '//label[@for="ReviewRatingFilter_4"]/../span', type='text', pos_extract=0)
        average = self.xpath(response, '//label[@for="ReviewRatingFilter_3"]/../span', type='text', pos_extract=0)
        poor = self.xpath(response, '//label[@for="ReviewRatingFilter_2"]/../span', type='text', pos_extract=0)
        terrible = self.xpath(response, '//label[@for="ReviewRatingFilter_1"]/../span', type='text', pos_extract=0)

        if not excelent and review_count:
            try:
                excelent = get_number_ratings(self.xpath(response, '//span[contains(text(),"Excelente")]/../span[@class="row_count row_cell"]', type='text', pos_extract=0), review_count)
                very_good = get_number_ratings(self.xpath(response, '//span[contains(text(),"Muy bueno")]/../span[@class="row_count row_cell"]', type='text', pos_extract=0), review_count)
                average = get_number_ratings(self.xpath(response, '//span[contains(text(),"Normal")]/../span[@class="row_count row_cell"]', type='text', pos_extract=0), review_count)
                poor = get_number_ratings(self.xpath(response, '//span[contains(text(),"Malo")]/../span[@class="row_count row_cell"]', type='text', pos_extract=0), review_count)
                terrible = get_number_ratings(self.xpath(response, '//span[contains(text(),"'+'Pésimo'.decode('UTF-8')+'")]/../span[@class="row_count row_cell"]', type='text', pos_extract=0), review_count)
            except:
                pass

        item['url']=response.url
        item['id'] = response.meta['id']
        item['title']=title
        item['description'] = description
        item['street_address'] = street_address
        item['extended_address'] = extended_address
        item['locality_address'] = locality_address
        item['postal_code'] = postal_code
        item['price_range'] = price_range
        item['stars'] = stars
        item['score'] = score
        item['cleanliness'] = cleanliness_rating
        item['location'] = location_rating
        item['service'] = services_rating
        item['value'] = value_rating
        item['excelent'] = excelent
        item['very_good'] = very_good
        item['average'] = average
        item['poor'] = poor
        item['terrible'] = terrible
        item['lat'] = lat
        item['lng'] = lng
        item['review_count'] = review_count
        item['place_searched'] = self.place

        self.check_item(item, ListTripadvisorHotelsRequiredFields())
        self.update_database(item, ELASTICSEARCH_INDEX, ELASTICSEARCH_DOC_TYPE, self.first_searched)
        if self.first_searched:
            self.first_searched = False

        return item
