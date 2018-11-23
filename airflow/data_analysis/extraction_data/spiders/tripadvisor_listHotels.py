import scrapy, datetime, os, re
#from extraction_data.items import HotelSentimentItem
# utilizo la clase del review en vez de la del hotel
from extraction_data.items import ListHotelsTripadvisorItem
from extraction_data.urls import TripAdvisorZonePuertoDeLaCruzURLs
from extraction_data.urls import TripAdvisorZoneFuerteventuraURLs
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
    # start_urls = TripAdvisorZonePuertoDeLaCruzURLs()
    start_urls = TripAdvisorZoneFuerteventuraURLs()

    def parse(self, response):
        parse_is_ok = 0
        listErrors=[]
        print 'INICIO'
        print ''
        print ''
        print ''
        print ''
        print ''
        print ''
        print '-----------'
        print '-----------'
        for href in response.xpath('//div[@class="listing_title"]/a/@href'):

            url = response.urljoin(href.extract())
            request = scrapy.Request(url, callback=self.parse_hotel)
            # res = es.search(index="index_listhotels_tripadvisor", doc_type="unstructured",body={
            #     "query": {
            #             "match_phrase": {
            #                     "url": url
            #                     }
            #             }
            #     })
            repeat=''

            # for hit in res['hits']['hits']:
            #     repeat = hit["_source"]

            #If the hotel doesnt have in the list, it will extract its data
            if repeat == '':
                yield request
            parse_is_ok = 1


        next_page = response.xpath('//a[@class="nav next taLnk ui_button primary"]/@href')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)

        if parse_is_ok != 1:

                listErrors=listErrors + ['def parse']
                #self.send_email(listErrors)
                print ''
                print ''
                print listErrors
                raise CloseSpider('Error scraping')


    def parse_hotel(self, response):
        item = ListHotelsTripadvisorItem()
        listErrors=[] #Bugs list, if it exists

        cont_bugs = 0
        no_bugs = False
        while cont_bugs < 3 and no_bugs is False:
            name = response.xpath('//h1[@class="ui_header h1"]/text()')
            if name:
                item['name'] = name.extract()[0]
            else:
                if cont_bugs == 2:
                    listErrors=listErrors + ['name']
            cont_bugs += 1

        item['url']=response.url

        cont_bugs = 0
        no_bugs = False
        while cont_bugs < 3 and no_bugs is False:
            street = response.xpath('//span[@class="street-address"]/text()')
            if street:
                item['street_address']= street.extract()[0]
            else:
                if cont_bugs == 2:
                    listErrors=listErrors + ['street_address']
            cont_bugs += 1

        cont_bugs = 0
        no_bugs = False
        while cont_bugs < 3 and no_bugs is False:
            extended = response.xpath('//span[@class="extended-address"]/text()')
            if extended:
                item['extended_address']=extended.extract()[0]

            cont_bugs += 1

        cont_bugs = 0
        no_bugs = False
        while cont_bugs < 3 and no_bugs is False:
            locality = response.xpath('//span[@class="locality"]/text()')
            if locality:
                item['locality_address']=locality.extract()[0]
            else:
                if cont_bugs == 2:
                    listErrors=listErrors + ['locality_address']
            cont_bugs += 1

        cont_bugs = 0
        no_bugs = False
        while cont_bugs < 3 and no_bugs is False:
            score = response.xpath('//span[@class="overallRating"]/text()')
            if score:
                item['score']=score.extract()[0]
            else:
                if cont_bugs == 2:
                    listErrors=listErrors + ['score']
            cont_bugs += 1


        cont_bugs = 0
        no_bugs = False
        while cont_bugs < 3 and no_bugs is False:
            score_per = response.xpath('//span[@class="row_count row_cell"]/text()')
            if score_per:
                item['excelent']=score_per.extract()[0]
                item['very_good']=score_per.extract()[1]
                item['average']=score_per.extract()[2]
                item['poor']=score_per.extract()[3]
                item['terrible']=score_per.extract()[4]

            else:
                if cont_bugs == 2:
                    listErrors=listErrors + ['score_per']
            cont_bugs += 1

        has_review = response.xpath('//span[@class="reviews_header_count block_title"]/text()')
        if has_review == '(0)' or has_review == 0:
            item['has_reviews'] = 0
        else:
            item['has_reviews'] = 1

        if len(listErrors)>0:

            #self.send_email(listErrors)
            print '--------'
            print 'ERRORS---->', listErrors
            print 'url----->', item['url']
            print '--------'
            print ''
            print ''
            # raise CloseSpider('Error in Parse Hotel')


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



