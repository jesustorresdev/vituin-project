
import scrapy, datetime, os, re
from scrapy.loader import ItemLoader
from hotel_sentiment.items import ListHotelsBookingItem
from hotel_sentiment.urls import BookingZoneURLs
from scrapy.mail import MailSender
from scrapy.exceptions import CloseSpider
from datetime import timedelta
from elasticsearch import Elasticsearch

#crawl up to 6 pages of review per hotel
max_pages_per_hotel = 6
exceptionErrorItem=False
es = Elasticsearch(
   [
     'elastic:vituinproject@elasticsearch:9200/',
   ]
)

class BookingSpider(scrapy.Spider):
    name = "booking_listHotels"
#    start_urls = [
#        "https://www.booking.com/searchresults.en-gb.html?aid=356984;label=gog235jc-country-en-gb-gb-unspec-es-com-L%3Aen-O%3Ax11-B%3Achrome-N%3Ayes-S%3Abo-U%3Ac-H%3As;sid=3d9a779adf10f3e6b7e0a80e5c9500df;region=777"
#    ]
    start_urls = BookingZoneURLs()
    pageNumber = 1

    #for every hotel
    def parse(self, response):
        listErrors=[]

        for hotelurl in response.xpath('//a[@class="hotel_name_link url"]/@href'):
            url = response.urljoin(hotelurl.extract())
            url2 = 'https://www.booking.com/' + hotelurl.extract()[1:]
            request = scrapy.Request(url2, self.parse_hotel)
            try:
                res = es.search(index="index_booking_hotels_establishments", doc_type="unstructured",body={
                    "query": {
                            "match_phrase": {
                                    "url": url
                                    }
                            }
                    })
                repeat=''
                for hit in res['hits']['hits']:
                    repeat = hit["_source"]
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

        # url = response.urljoin(reviewsurl[0].extract())
        item['url']=response.url

        # url = "https://www.booking.com/" + response.urljoin(reviewsurl[0].extract())
        name = response.xpath('//div[@class="hp__hotel-title"]/h2/text()')
        if name:
            item['name']=name.extract()[0]
        else:
            listErrors=listErrors + ['name']


        address = response.xpath('//span[contains(@class,"hp_address_subtitle")]/text()')
        if address:
          item['address']=address.extract()[0]
        else:
           listErrors=listErrors + ['address']

        score = response.xpath('//span[@class="review-score-badge"]/text()')
        if score:
          item['score']=score.extract()[0]
        else:
            item['score']="no score"

        stars = response.xpath('//span[@class="hp__hotel_ratings__stars nowrap"]/i/@title')
        if stars:
            item['stars']=stars.extract()[0]
        else:
            item['stars']= 'no stars'

        #Its fields isn't ever.
        score_cleanliness = response.xpath('//li[@data-question="hotel_clean"]/p[@class="review_score_value"]/text()')
        if score_cleanliness:
          item['cleanliness']=score_cleanliness.extract()[0]

        score_comfort = response.xpath('//li[@data-question="hotel_comfort"]/p[@class="review_score_value"]/text()')
        if score_comfort:
          item['comfort']=score_comfort.extract()[0]

        score_facilities = response.xpath('//li[@data-question="hotel_services"]/p[@class="review_score_value"]/text()')
        if score_facilities:
          item['facilities']=score_facilities.extract()[0]

        score_staff = response.xpath('//li[@data-question="hotel_staff"]/p[@class="review_score_value"]/text()')
        if score_staff:
            item['staff']=score_staff.extract()[0]

        score_value_for_money = response.xpath('//li[@data-question="hotel_value"]/p[@class="review_score_value"]/text()')
        if score_value_for_money:
          item['value_for_money']=score_value_for_money.extract()[0]

        score_wifi = response.xpath('//li[@data-question="hotel_wifi"]/p[@class="review_score_value"]/text()')
        if score_wifi:
          item['wifi']=score_wifi.extract()[0]

        score_location = response.xpath('//li[@data-question="hotel_location"]/p[@class="review_score_value"]/text()')
        if score_location:
          item['location']=score_location.extract()[0]



        if reviewsurl:
          item['has_reviews'] = 1
        else:
          item['has_reviews'] = 0


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

