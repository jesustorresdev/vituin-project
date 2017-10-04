
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
es = Elasticsearch(['elasticsearch:9200'])


class BookingSpider(scrapy.Spider):
    name = "booking_listHotels"
#    start_urls = [
#        "https://www.booking.com/searchresults.en-gb.html?aid=356984;label=gog235jc-country-en-gb-gb-unspec-es-com-L%3Aen-O%3Ax11-B%3Achrome-N%3Ayes-S%3Abo-U%3Ac-H%3As;sid=3d9a779adf10f3e6b7e0a80e5c9500df;region=777"
#    ]
    start_urls = BookingZoneURLs()
    pageNumber = 1

    #for every hotel
    def parse(self, response):
        for hotelurl in response.xpath('//a[@class="hotel_name_link url"]/@href'):
            url = response.urljoin(hotelurl.extract())
            request = scrapy.Request(url, callback=self.parse_hotel)
            
	    res = es.search(index="index_listhotels_booking", doc_type="hotels_unit",body={
                "query": {
                        "match_phrase": {
                                "url": url
                                }
                        }
                })
            repeat=''
            for hit in res['hits']['hits']:
                repeat = hit["_source"]
            #Si no esta ya en la lista(determinada URL) se extraen sus datos
            if repeat == '':
                yield request
           
            parse_is_ok = 1

        next_page = response.xpath('//a[starts-with(@class,"paging-next")]/@href')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)

        if parse_is_ok != 1:

                listErrors=listErrors + ['def parse']
                #self.send_email(listErrors)
                raise CloseSpider('Error scraping')


    #get its reviews page
    def parse_hotel(self, response):

        reviewsurl = response.xpath('//a[@class="show_all_reviews_btn"]/@href')
        item = ListHotelsBookingItem()
        listErrors=[]


        url = response.urljoin(reviewsurl[0].extract())
        item['url']=url

        name = response.xpath('//div[@class="hp__hotel-title"]/h2/text()')
	if name:
          item['name']=name.extract()[0]
        else:
           listErrors=listErrors + ['name']


        address = response.xpath('//span[@class="hp_address_subtitle jq_tooltip"]/text()')
        if address:
          item['address']=address.extract()[0]
        else:
           listErrors=listErrors + ['address']

	score = response.xpath('//span[@class="review-score-badge"]/text()')
        if score:
          item['score']=score.extract()[0]
        else:
           listErrors=listErrors + ['score']

        if reviewsurl:
          item['has_reviews'] = 1
        else:
          item['has_reviews'] = 0

        self.pageNumber = 1

        if len(listErrors)>0:

          #self.send_email(listErrors)
          raise CloseSpider('Error spider Parse Hotel')

        return item


    def send_email(self, listErrors):

        global exceptionErrorItem

        if exceptionErrorItem == False:
            message = 'Al hacer el scrapy de Booking no existen los campos '

            for elementError in listErrors:
                message = message + elementError + ', '

            message = re.sub(', $', '.' , message)

            #Mandar un correo informando si hay un error
            mailer = MailSender(mailfrom="erroresSpider@gmail.com",smtphost="smtp.gmail.com",smtpport=587,smtpuser="erroresSpider@gmail.com",smtppass="errores1234")
            #mailer.send(to=["erroresSpider@gmail.com"], subject='Errores en el Spider', body=message)
            exceptionErrorItem=True

            #eliminar el archivo extraido hasta entonces
            os.remove('listhotelsBooking.csv')


