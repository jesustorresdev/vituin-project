# -*- coding: UTF-8 -*-

"""Extracción de viviendas en Airbnb
"""

__authors__ = 'Sergio Díaz, Jesús Torres'
__organization__ = 'Universidad de La Laguna'
__licensed__ = 'UNLICENSED'
__contact__ = "jmtorres@ull.edu.es, sdiazgon@ull.edu.es"
# __copyright__ = f"Copyright 2017-2018 {__organization__}"

from scrapy import Request
from extraction_data.urls import AirbnbURLs ###############################
from extraction_data.items import ListRestaurantsTripadvisorItem
from extraction_data.required_fields import ListAirbnbHomeRequiredFields #################3
from extraction_data.selenium_spider import SeleniumSpider
from extraction_data.scrapy_spider import ScrapySpider
from extraction_data.utils import type_try, split_try

ELASTICSEARCH_INDEX = 'tripadvisor_restaurants'
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
class AibrnbSpider(ScrapySpider):
    name = "tripadvisor_listRestaurants1"

    def __init__(self, place=''):
        self.place = place
        # self.start_urls = TripadvisorRestaurantsURLs(place)
        start_urls = [
            #"https://www.tripadvisor.co.uk/Restaurants-g187481-Puerto_de_la_Cruz_Tenerife_Canary_Islands.html"
            #"https://www.tripadvisor.co.uk/Restaurants-g187479-Tenerife_Canary_Islands.html"
            "https://www.tripadvisor.co.uk/Restaurants-g187475-La_Palma_Canary_Islands.html"
            #"https://www.tripadvisor.co.uk/Restaurants-g187473-El_Hierro_Canary_Islands.html"
            #"https://www.tripadvisor.co.uk/Restaurants-g187469-La_Gomera_Canary_Islands.html"
            #"https://www.tripadvisor.co.uk/Restaurants-g187471-Gran_Canaria_Canary_Islands.html"
            #"https://www.tripadvisor.co.uk/Restaurants-g187477-Lanzarote_Canary_Islands.html"
            #"https://www.tripadvisor.co.uk/Restaurants-g187467-Fuerteventura_Canary_Islands.html"

        ]
        self.first_searched = self.get_if_first_searched(ELASTICSEARCH_INDEX, ELASTICSEARCH_DOC_TYPE)

    def parse(self, response):
        selenium = SeleniumSpider(width=200,height=350)
        selenium.set_url(response.url)
        n = 0
        i=0
        more_pages = True
        while more_pages:
            i+=1
            restaurants = selenium.xpath("//div[starts-with(@class, 'listing rebrand')]", type='object', stop_if_error=True)
            print restaurants
            for restaurant in restaurants:
                link = selenium.xpath("./div[@class='title']/a", selenium_object=restaurant, type='attribute', attribute='href')
                id = selenium.xpath("./", selenium_object=restaurant, type='attribute', attribute='id')
                n+=1
                url = response.urljoin(link)
                print ''
                print ''
                print ''
                print(n, ' id=', id, ', url=', url, '------->n:',n,'links=',len(restaurants))
                print ''
                print ''
                print ''
                request = Request(url, callback=self.parse_restaurant)

                request.meta['id']=id
                # If the hotel doesnt have in the list, it will extract its data
                if self.first_searched:
                    yield request
                elif not self.exist_item(ELASTICSEARCH_INDEX, url):
                    yield request

            next_page = selenium.xpath('//a[@class="nav next rndBtn ui_button primary taLnk"]', number_of_attemps=0)


            if next_page:
                next_page.click()
            else:
                more_pages = False
                print 'Fin i=',i,':', str(response.url)

        selenium.quit_browser()


    def parse_restaurant(self, response):
        item = ListRestaurantsTripadvisorItem()

        meta_data = self.xpath(response,'//script[@type="application/ld+json"]', type='text', stop_if_error=True,
                               extract_json=True)
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

        stars = get_value_from_bubble(self.xpath(response,'//div[starts-with(@class,"hotels-hotel-review-about-with-photos-layout-TextItem__textitem")]/span' \
                                                 , type='attribute', attribute='class'))

        ratings =  self.xpath(response, '//span[starts-with(@class, "restaurants-detail-overview-cards-RatingsOverviewCard__ratingQuestionRow")]', type='object')
        list_attributes = {'food':'','service':'','value':'', 'atmosphere':''}
        for element in ratings:
            attribute = self.xpath(element, './span[starts-with(@class, "restaurants-detail-overview-cards-RatingsOverviewCard__ratingText")]', type='text')
            value = get_value_from_bubble(self.xpath(element, './span[starts-with(@class, "restaurants-detail-overview-cards-RatingsOverviewCard__ratingBubbles")]',
                                                     type='attribute', attribute='class'))
            list_attributes.update({self.get_attribute_description(attribute):value})


        # food_rating = get_value_from_bubble(self.xpath(ratings, './', type='attribute', attribute='class', pos_extract=0))
        # atmosphere_rating = get_value_from_bubble(self.xpath(ratings, './', type='attribute', attribute='class', pos_extract=1))
        # service_rating = get_value_from_bubble(self.xpath(ratings, './', type='attribute', attribute='class', pos_extract=2))
        # value_rating =  get_value_from_bubble(self.xpath(ratings, './', type='attribute', attribute='class', pos_extract=3))


        excelent = self.xpath(response, '//label[@for="ReviewRatingFilter_5"]/../span', type='text', pos_extract=0)
        very_good = self.xpath(response, '//label[@for="ReviewRatingFilter_4"]/../span', type='text', pos_extract=0)
        average = self.xpath(response, '//label[@for="ReviewRatingFilter_3"]/../span', type='text', pos_extract=0)
        poor = self.xpath(response, '//label[@for="ReviewRatingFilter_2"]/../span', type='text', pos_extract=0)
        terrible = self.xpath(response, '//label[@for="ReviewRatingFilter_1"]/../span', type='text', pos_extract=0)

        if not excelent and review_count:
            try:
                excelent = get_number_ratings(self.xpath(response, '//span[contains(text(),"Excelente")]/../span[@class="row_count row_cell"]',
                                                         type='text', pos_extract=0), review_count)
                very_good = get_number_ratings(self.xpath(response, '//span[contains(text(),"Muy bueno")]/../span[@class="row_count row_cell"]',
                                                          type='text', pos_extract=0), review_count)
                average = get_number_ratings(self.xpath(response, '//span[contains(text(),"Normal")]/../span[@class="row_count row_cell"]',
                                                        type='text', pos_extract=0), review_count)
                poor = get_number_ratings(self.xpath(response, '//span[contains(text(),"Malo")]/../span[@class="row_count row_cell"]',
                                                     type='text', pos_extract=0), review_count)
                terrible = get_number_ratings(self.xpath(response, '//span[contains(text(),"'+'Pésimo'.decode('UTF-8')+'")]/../span[@class="row_count row_cell"]',
                                                         type='text', pos_extract=0), review_count)
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
        item['food'] = list_attributes['food']
        item['atmosphere'] = list_attributes['atmosphere']
        item['service'] = list_attributes['service']
        item['value'] = list_attributes['value']
        item['excelent'] = excelent
        item['very_good'] = very_good
        item['average'] = average
        item['poor'] = poor
        item['terrible'] = terrible
        item['lat'] = lat
        item['lng'] = lng
        item['review_count'] = review_count
        item['place_searched'] = self.place

        # self.check_item(item, ListTripadvisorHotelsRequiredFields())
        self.update_database(item, ELASTICSEARCH_INDEX, ELASTICSEARCH_DOC_TYPE, self.first_searched)
        if self.first_searched:
            self.first_searched = False

        return item

