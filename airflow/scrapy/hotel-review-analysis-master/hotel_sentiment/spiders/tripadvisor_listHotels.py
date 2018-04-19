import scrapy, datetime, os, re
#from hotel_sentiment.items import HotelSentimentItem
# utilizo la clase del review en vez de la del hotel
from hotel_sentiment.items import ListHotelsTripadvisorItem
from hotel_sentiment.urls import TripAdvisorZoneURLs
from scrapy.mail import MailSender
from scrapy.exceptions import CloseSpider
from elasticsearch import Elasticsearch

exceptionErrorItem=False
es = Elasticsearch(
   [
     'elastic:vituinproject@elasticsearch:9200/',
   ]
)



#TODO use loaders
class TripadvisorSpider(scrapy.Spider):
    name = "tripadvisor_listHotels"
    #start_urls = [
    #    "https://www.tripadvisor.co.uk/Hotels-g187479-Tenerife_Canary_Islands-Hotels.html"
    #]
    start_urls = TripAdvisorZoneURLs()

    def parse(self, response):
        parse_is_ok = 0
        listErrors=[]

        for href in response.xpath('//div[@class="ui_column titleBox"]/a/@href'):

            url = response.urljoin(href.extract())
            request = scrapy.Request(url, callback=self.parse_hotel)
            res = es.search(index="index_listhotels_tripadvisor", doc_type="hotels_unit",body={
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
            parse_is_ok = 1


        next_page = response.xpath('//div[@class="unified pagination standard_pagination"]/child::*[2][self::a]/@href')

        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)

        if parse_is_ok != 1:

                listErrors=listErrors + ['def parse']
                #self.send_email(listErrors)
                raise CloseSpider('Error scraping')


    def parse_hotel(self, response):
        item = ListHotelsTripadvisorItem()
        listErrors=[] #Bugs list, if it exists

        name = response.xpath('//div[@id="taplc_location_detail_header_hotels_0"]/h1/text()')
        if name:
            item['name'] = name.extract()[0]
        else:
            listErrors=listErrors + ['name']

        item['url']=response.url

        street = response.xpath('//span[@class="street-address"]/text()')
        if street:
            item['street_address']= street.extract()[0]
        else:
            listErrors=listErrors + ['street_address']

        extended = response.xpath('//span[@class="extended-address"]/text()')
        if extended:
            item['extended_address']=extended.extract()[0]
        else:
            listErrors=listErrors + ['extended_address']

        locality = response.xpath('//span[@class="locality"]/text()')
        if locality:
            item['locality_address']=locality.extract()[0]
        else:
            listErrors=listErrors + ['locality_address']

        score = response.xpath('//div[@class="prw_rup prw_common_bubble_rating bubble_rating"]/span/@alt')
        if score:
            item['score']=score.extract()[0]
        else:
            listErrors=listErrors + ['score']

        has_review = response.xpath('//span[@class="reviews_header_count block_title"]/text()')
        if has_review == '(0)' or has_review == 0:
            item['has_reviews'] = 0
        else:
            item['has_reviews'] = 1

        if len(listErrors)>0:

            #self.send_email(listErrors)
            print(listErrors)
            raise CloseSpider('Error in Parse Hotel')


        return item


    # def send_email(self, listErrors):
    #
    #     global exceptionErrorItem
    #
    #     if exceptionErrorItem == False:
    #         message = 'Al hacer el scrapy de Tripadvisor no existen los campos '
    #
    #         for elementError in listErrors:
    #             message = message + elementError + ', '
    #
    #         message = re.sub(', $', '.' , message)
    #
    #         #Send a email saying if some bug have ocurred
    #         mailer = MailSender(mailfrom="erroresSpider@gmail.com",smtphost="smtp.gmail.com",smtpport=587,smtpuser="erroresSpider@gmail.com",smtppass="errores1234")
    #         mailer.send(to=["erroresSpider@gmail.com"], subject='Errores en el Spider', body=message)
    #         exceptionErrorItem=True
    #
    #         #In this case we delete the extract file until this moment
    #         os.remove('itemslistHotelsTripadvisor.csv')
    #



