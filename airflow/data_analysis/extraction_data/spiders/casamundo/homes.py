# -*- coding: UTF-8 -*-

"""Extracción de viviendas en Casamundo
"""

__authors__ = 'Sergio Díaz, Jesús Torres'
__organization__ = 'Universidad de La Laguna'
__licensed__ = 'UNLICENSED'
__contact__ = "jmtorres@ull.edu.es, sdiazgon@ull.edu.es"
# __copyright__ = f"Copyright 2017-2018 {__organization__}"

from scrapy import Request
from extraction_data.urls import CasamundoURLs
from extraction_data.items import ListCasamundoHomeItem
from extraction_data.required_fields import ListCasamundoHomeRequiredFields
from extraction_data.selenium_spider import SeleniumSpider
from extraction_data.scrapy_spider import ScrapySpider
from extraction_data.utils import split_try

ELASTICSEARCH_INDEX = 'casamundo_homes'
ELASTICSEARCH_DOC_TYPE = 'unstructured'

#TODO use loaders
class CasamundoSpider(ScrapySpider):
    name = "casamundo_listHomes"
    def __init__(self, place=''):
        self.place = place
        self.start_urls = CasamundoURLs(place)

        self.first_searched = self.get_if_first_searched(ELASTICSEARCH_INDEX, ELASTICSEARCH_DOC_TYPE)

    def parse(self, response):
        homes = self.xpath(response,"//div[@class='objectdetail-offer-inner']/span/a", type='object')

        for home in homes:
            url=self.xpath(home, './', type='attribute', attribute='href')

            print('url=', url,)
            yield Request(
                url, self.parse_home
            )


        next_page = self.xpath(response, "//span[@class='button forward']", type='attribute', attribute='href')
        if next_page:
            next_page_url = 'https://www.casamundo.com'+next_page
            yield Request(
                next_page_url, callback=self.parse
            )

    def parse_home(self, response):

        item = ListCasamundoHomeItem()

        meta_data = self.xpath(response,'//script[@type="application/ld+json"]', type='text', stop_if_error=True, extract_json=True)
        title=self.try_json(meta_data,"description").encode('UTF-8')
        id=self.try_json(meta_data,"mpn")
        place=title[title.find(',')+1:]
        type_residence=split_try(title, 0)

        price = self.xpath(response,'//span[@data-bind="text: cm.cm_spa.odp.formatPrice($root.odp.price.price_min(), $root.odp.price.currency())"]', type='text')[-2]
        capacity = self.xpath(response,'//span[@class="cm_icons cm_icon_people"]/..', type='text')
        m2 = self.xpath(response,'//span[@class="cm_icons cm_icon_size"]/..', type='text')
        bathrooms = self.xpath(response,'//span[@class="cm_icons cm_icon_bath"]/..', type='text')
        beds = self.xpath(response,'//span[@class="cm_icons cm_icon_bed"]/..', type='text')

        main_bubbles = self.xpath(response,'//span[@data-bind="text: $parent.scoreFormatted"]', type='text')
        number_reviews = self.xpath(response,'//span[@class="review_score_count"]', type='text')
        equipment_rating = self.xpath(response,'//div[@class="review_bar"]/span[@span="value"]', type='text', pos_extract=0)
        location_rating = self.xpath(response,'//div[@class="review_bar"]/span[@span="value"]', type='text', pos_extract=1)
        general_impression_rating = self.xpath(response,'//div[@class="review_bar"]/span[@span="value"]', type='text', pos_extract=2)
        cleanliness_rating = self.xpath(response,'//div[@class="review_bar"]/span[@span="value"]', type='text', pos_extract=3)
        kindness_services_rating = self.xpath(response,'//div[@class="review_bar"]/span[@span="value"]', type='text', pos_extract=4)
        value_rating = self.xpath(response,'//div[@class="review_bar"]/span[@span="value"]', type='text', pos_extract=5)

        # #coordinates
        # selenium = SeleniumSpider()
        # selenium.set_url(response.url)
        # (lat,lng) = selenium.get_coordinates_google_map(pos_above="//section[@class ='map-content']")
        # selenium.quit_browser()

        # WebDriver driver = new FirefoxDriver();
        # driver.get(URL);
        # Actions act = new Actions(driver);
        # WebElement linkpath = driver.Findelement(by.xpath(path of the link));
        # act.contextclick(linkpath).perform();  // right click
        # act.sendkeys("T").perform(); // click on new tab

        item['id'] = id
        item['url'] = response.url
        item['title'] = title
        item['price'] = price
        item['bathrooms'] = bathrooms
        item['beds'] = beds
        item['capacity'] = capacity
        item['m2'] = m2
        item['type_residence'] = type_residence
        item['number_reviews'] = number_reviews
        item['main_bubbles'] = main_bubbles
        item['equipment_rating'] = equipment_rating
        item['location_rating'] = location_rating
        item['general_impression_rating'] = general_impression_rating
        item['cleanliness_rating'] = cleanliness_rating
        item['kindness_services_rating'] = kindness_services_rating
        item['value_rating'] = value_rating
        # item['lat'] = lat
        # item['lng'] = lng
        item['place'] = place
        item['place_searched'] = self.place

        self.check_item(item, ListCasamundoHomeRequiredFields())

        return item
