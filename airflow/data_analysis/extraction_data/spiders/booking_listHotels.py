# -*- coding: utf-8 -*-
import scrapy, datetime, os, re
from scrapy.loader import ItemLoader
from extraction_data.items import ListHotelsBookingItem
from extraction_data.urls import BookingZoneURLs
from scrapy.mail import MailSender
from scrapy.exceptions import CloseSpider
from datetime import timedelta
from elasticsearch import Elasticsearch
import ast
import json
#crawl up to 6 pages of review per hotel
max_pages_per_hotel = 6
exceptionErrorItem=False
es = Elasticsearch(
   [
     'elastic:vituinproject@elasticsearch:9200/',
   ]
)

class BookingSpider(scrapy.Spider):
    name = "booking_listEstablishments"
#    start_urls = [
#        "https://www.booking.com/searchresults.en-gb.html?aid=356984;label=gog235jc-country-en-gb-gb-unspec-es-com-L%3Aen-O%3Ax11-B%3Achrome-N%3Ayes-S%3Abo-U%3Ac-H%3As;sid=3d9a779adf10f3e6b7e0a80e5c9500df;region=777"
#    ]
    start_urls = BookingZoneURLs('Adeje')
    pageNumber = 1

    #for every hotel
    def parse(self, response):
        listErrors=[]
        print 'eeeeeeeee'
        print 'eeeeeeeee'
        print 'eeeeeeeee'
        print 'eeeeeeeee'
        print 'eeeeeeeee'
        print 'eeeeeeeee'
        print 'eeeeeeeee'
        for establishment in response.xpath('//a[@class="hotel_name_link url"]/@href'):
            url = response.urljoin(establishment.extract())
            url2 = 'https://www.booking.com/' + establishment.extract()[1:]
            request = scrapy.Request(url2, self.parse_hotel)
            try:
                res = es.search(index="index_list_homes_booking", doc_type="unstructured",body={
                    "query": {
                            "match_phrase": {
                                    "url": url
                                    }
                            }
                    })
                repeat=''
                for hit in res['hits']['hits']:
                    repeat = hit["_source"]
                    print hit


            #If the hotel doesnt have in the list, it will extract its data
                if repeat == '':
                    yield request

            #if not exists index
            except:
                yield request
            parse_is_ok = 1

        next_page = response.xpath('//a[contains(@class,"paging-next")]/@href')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)

        if parse_is_ok != 1:

            listErrors=listErrors + ['def parse']
            #self.send_email(listErrors)
            raise CloseSpider('Error scraping')


    def parse_hotel(self, response):

        reviewsurl = response.xpath('//a[@class="show_all_reviews_btn"]/@href')
        item = ListHotelsBookingItem()
        listErrors=[] #Bugs list, if it exists

        meta_data_str = response.xpath('//script[@type="application/ld+json"]/text()').extract()[0]
        try:
            # meta_data = ast.literal_eval((meta_data_str))
            meta_data = json.loads(meta_data_str)
        except Exception as error:
            print error
            print 'type metadata-->',type(meta_data_str)
            print 'error-->',meta_data_str
            print response.url
            raise CloseSpider('error')
        # url = response.urljoin(reviewsurl[0].extract())
        item['url']=response.url
        item['id_booking'] = response.xpath('//input[@name="hotel_id"]/@value').extract()[0]

        # name = response.xpath('//div[@class="hp__hotel-title"]/h2/text()')
        # if name:
        #     item['name']=name.extract()[0]
        # else:
        #     listErrors=listErrors + ['name']

        try:
            item['name']=meta_data["name"].encode('UTF-8')
            item['description'] = meta_data["description"].encode('UTF-8')
            item['type_establishment'] = meta_data["@type"].encode('UTF-8')

            try:
                item['score'] = meta_data["aggregateRating"]["ratingValue"]
            except:
                item['score'] = False

            try:
                item['review_count'] = meta_data["aggregateRating"]["reviewCount"]
            except:
                item['review_count'] = False

            item['address'] = meta_data["address"]["streetAddress"].encode('UTF-8')
            item['postalCode'] = meta_data["address"]["postalCode"]
            item['region'] = meta_data["address"]["addressRegion"].encode('UTF-8')
            try:
                price_min = item['price_min'].encode('UTF-8')
                item['price_min'] = price_min[price_min.find('£')+len('£'):].split()[0]
            except:
                item['price_min'] = False

            has_map = meta_data["hasMap"].encode('UTF-8')
            has_map_since_center = has_map[(has_map.find('center')+len('center')+1):]
            coordinates = has_map_since_center[:has_map_since_center.find('&')]
            item['lat']  = coordinates.split(',')[0]
            item['lng']  = coordinates.split(',')[1]
        except Exception as error:
            print 'meta_data-->', meta_data
            print 'type meta_data-->', type(meta_data)
            print 'url-->', response.url
            print 'error--->', error
            import sys
            print 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno)
            raise CloseSpider('ooo')



        # address = response.xpath('//span[contains(@class,"hp_address_subtitle")]/text()')
        # if address:
        #   item['address']=address.extract()[0]
        # else:
        #    listErrors=listErrors + ['address']

        # score = response.xpath('//span[@class="review-score-badge"]/text()')
        # if score:
        #   item['score']=score.extract()[0]
        # else:
        #     item['score']="no score"

        stars = response.xpath('//span[@class="hp__hotel_ratings__stars nowrap"]/i/@title')
        if stars:
            item['stars']=stars.extract()[0]
        else:
            item['stars']= 'no stars'

        #Its fields isn't ever.
        score_cleanliness = response.xpath('//li[@data-question="hotel_clean"]/p[@class="review_score_value"]/text()')
        if score_cleanliness:
          item['cleanliness_rating']=score_cleanliness.extract()[0]

        score_comfort = response.xpath('//li[@data-question="hotel_comfort"]/p[@class="review_score_value"]/text()')
        if score_comfort:
          item['comfort_rating']=score_comfort.extract()[0]

        score_facilities = response.xpath('//li[@data-question="hotel_services"]/p[@class="review_score_value"]/text()')
        if score_facilities:
          item['facilities_rating']=score_facilities.extract()[0]

        score_staff = response.xpath('//li[@data-question="hotel_staff"]/p[@class="review_score_value"]/text()')
        if score_staff:
            item['staff_rating']=score_staff.extract()[0]

        score_value_for_money = response.xpath('//li[@data-question="hotel_value"]/p[@class="review_score_value"]/text()')
        if score_value_for_money:
          item['value_for_money_rating']=score_value_for_money.extract()[0]

        score_wifi = response.xpath('//li[@data-question="hotel_wifi"]/p[@class="review_score_value"]/text()')
        if score_wifi:
          item['wifi_rating']=score_wifi.extract()[0]

        score_location = response.xpath('//li[@data-question="hotel_location"]/p[@class="review_score_value"]/text()')
        if score_location:
          item['location_rating']=score_location.extract()[0]



        self.pageNumber = 1

        if len(listErrors)>0:

          print ""
          print ""
          print ""
          print ""
          print "ERROR"
          print item["name"]
          print item["url"]
          print listErrors
          #self.send_email(listErrors)
          raise CloseSpider('Error spider Parse Hotel')

        return item


    # def send_email(self, listErrors):
    #
    #     global exceptionErrorItem
    #
    #     if exceptionErrorItem == False:
    #         message = 'Al hacer el scrapy de Booking no existen los campos '
    #
    #         for elementError in listErrors:
    #             message = message + elementError + ', '
    #
    #         message = re.sub(', $', '.' , message)
    #
    #         #Send a email saying if some bug have ocurred
    #         mailer = MailSender(mailfrom="erroresSpider@gmail.com",smtphost="smtp.gmail.com",smtpport=587,smtpuser="erroresSpider@gmail.com",smtppass="errores1234")
    #         #mailer.send(to=["erroresSpider@gmail.com"], subject='Errores en el Spider', body=message)
    #         exceptionErrorItem=True
    #
    #         #In this case we delete the extract file until this moment
    #         os.remove('listhotelsBooking.csv')
    #

# a ='{"hasMap" : "https://maps.googleapis.com/maps/api/staticmap?markers=color:blue%7c28.4167488,-16.5417624&size=1600x1200&sensor=false&zoom=15&center=28.4167488,-16.5417624&client=gme-booking&channel=booking-frontend&signature=Iiftf0Kyxc8JOVyytz8rpHcmV10=", "url" : "https://www.booking.com/hotel/es/bahia-principe-san-felipe.en-gb.html",    "@type" : "Hotel",   "image" : "https://t-ec.bstatic.com/images/hotel/max500/394/39427948.jpg",    "aggregateRating" : {        "ratingValue" : 8.1,        "@type" : "AggregateRating",        "reviewCount" : 552,        "bestRating" : 10    },    "@context" : "http://schema.org",    "name" : "Sunlight Bahia Principe San Felipe",    "priceRange" : "Prices for upcoming dates start at £77 per night (We Price Match)","address" : {        "streetAddress" : "Avenida de Colón, 22, 38400 Puerto de la Cruz, Spain",        "addressRegion" : "Tenerife",        "postalCode" : "38400",        "addressCountry" : "Spain",        "addressLocality" : "Avenida de Colón, 22",        "@type" : "PostalAddress"},"description" : "Bahia Principe San Felipe is located on the seafront, just 400 metres from the Martíanez Lakes."}'
# o = '{' \
#     '' \
#     '' \
#     '"name" : "Villa Syrah","@type" : "Hotel","priceRange" : null' \
#     '' \
#     '' \
#     '' \
#     '}'