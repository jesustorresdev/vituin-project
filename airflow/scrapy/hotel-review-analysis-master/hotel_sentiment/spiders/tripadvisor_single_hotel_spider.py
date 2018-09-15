import scrapy, datetime, os, re
#from hotel_sentiment.items import HotelSentimentItem
# utilizo la clase del review en vez de la del hotel
from hotel_sentiment.items import TripAdvisorReviewItem
from hotel_sentiment.urls import TripAdvisorHotelsURLs
from scrapy.mail import MailSender
from scrapy.exceptions import CloseSpider
from elasticsearch import Elasticsearch
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


exceptionErrorItem=False

#TODO use loaders
class TripadvisorSpider(scrapy.Spider):

    name = "tripadvisor_singlehotel"
    #start_urls = TripAdvisorHotelsURLs()
    start_urls = []
    es = Elasticsearch(
       [
          'elastic:vituinproject@elasticsearch:9200/',
       ]
    )
    #SearchAllEstablishments
    doc = {
            'size' : 10000,
            'query': {
                 'match_all' : {}
             }
          }
    res = es.search(index='index_tripadvisor_hotels_establishments', doc_type='hotels', body=doc,scroll='1m')

    #creamos lista de urls
    for hit in res['hits']['hits']:
            start_urls=start_urls + [hit["_source"]["url"]]


    start_urls = [
        # "https://www.tripadvisor.co.uk/Hotel_Review-g187481-d10437912-Reviews-Hotel_Weare_La_Paz-Puerto_de_la_Cruz_Tenerife_Canary_Islands.html",
       "https://www.tripadvisor.co.uk/Hotel_Review-g187481-d567656-Reviews-Hotel_Tosca-Puerto_de_la_Cruz_Tenerife_Canary_Islands.html"
    ]


    def parse(self, response):


        listErrors=[]
        #Create the request
        request = scrapy.Request(response.url, callback=self.parse_review)
        es = Elasticsearch(
            [
               'elastic:vituinproject@elasticsearch:9200/',
            ]
        )

        #Make a query to Elasticsearch using the URL
        res = es.search(index="index_tripadvisor_hotels_establishments", doc_type="hotels",body={
        	"query": {
                	"match_phrase": {
                        	"url": response.url
                        	}
                	}
       		})


        hotel =  ''
        has_review =  ''
        street =  ''
        extended =  ''
        locality =  ''
        score = ''
        phone = ''

        for hit in res['hits']['hits']:

            hotel = hit["_source"]["name"]
            has_review = hit["_source"]["has_reviews"]
            street = hit["_source"]["name"]
            extended = hit["_source"]["extended_address"]
            locality = hit["_source"]["locality_address"]
            score = hit["_source"]["score"]


        #save some fields that we will send
        request.meta['hotel_name']=hotel
        #this fields are optionals
        request.meta['hotel_street_address']=street
        request.meta['hotel_extended_address']=extended
        request.meta['hotel_locality_address']=locality
        request.meta['hotel_score']=score
        #if there are comment. If there isnt, it doesnt pass
        if has_review:
                yield request


    #to get the full review content I open its page, because I don't get the full content on the main page
    #there's probably a better way to do it, requires investigation
    def parse_review(self, response):
        listErrors=[] #if there is bugs

        for rev in response.xpath('//div[starts-with(@class,"review-container")]'):
            item = TripAdvisorReviewItem() #Class with Tripadvisor fields

            item['hotel_name']=response.meta['hotel_name']
            item['hotel_street_address']=response.meta['hotel_street_address']
            item['hotel_extended_address']=response.meta['hotel_extended_address']
            item['hotel_locality_address']=response.meta['hotel_locality_address']
            item['hotel_score']=response.meta['hotel_score']

            r_d=rev.xpath('.//span[@class="ratingDate"]/@title')
            if r_d:
                item['review_date'] = r_d.extract()[0]

                date = datetime.datetime.strptime(item['review_date'] , '%d %B %Y')
                now = datetime.datetime.combine(datetime.datetime.today(), datetime.time(0, 0))
                item['review_date']= date

#                if (now - date).days < 7:
                if (now - date).days < 1000000:

#                    t = response.xpath('//div[@class="quote isNew"]/a/span/text()')
                    t = rev.xpath('.//div[starts-with(@class,"quote")]/a/span/text()')
                    if t:
                         item['title'] = t[0].extract()
                    else:
                         listErrors=listErrors + ['title']

                    c = rev.xpath('.//div[@class="entry"]/p/text()')
                    if c:
                         item['content'] = c.extract()
                    else:
                         listErrors=listErrors + ['content']
                    print '++++++++++++++++++++++'
                    print '++++++++++++++++++++++'
                    print '++++++++++++++++++++++'
                    print '++++++++++++++++++++++'
                    print t, c
                    print '++++++++++++++++++++++'
                    print '++++++++++++++++++++++'
                    print '++++++++++++++++++++++'
                    print '++++++++++++++++++++++'

                    r_l = rev.xpath('.//div[@class="location"]/span/text()')
                    if r_l:
                        item['reviewer_location']  = r_l[0].extract()

                    #if there is bugs to extract fields
                    if len(listErrors)>0:
                        #self.send_email(listErrors)
                        print '-----------------------'
                        print '-----------------------'
                        print '-----------------------'
                        print '-----------------------'
                        print '-----------------------'
                        print '-----------------------'
                        print '-----------------------'
                        print '-----------------------'
                        print '-----------------------'
                        print '-----------------------'
                        print '-----------------------'
                        print '-----------------------'
                        print '-----------------------'
                        print '-----------------------'
                        print '-----------------------'
                        print '-----------------------'
                        print '-----------------------'
                        print '-----------------------'
                        print '-----------------------'
                        print '-----------------------'
                        print '-----------------------'
                        print '-----------------------'
                        print '-----------------------'
                        # print listErrors
                        # print 'response --> ', response
                        # print 'title ', item['title']
                        # print 'entry ---> ', rev.xpath('.//div[@class="entry"]')
                        # print 'entry/p ---> ', rev.xpath('.//div[@class="entry"]/p/text()')
                        # print 'partial entry ---> ', rev.xpath('.//p[@class="partial_entry"]')
                        # raise CloseSpider('Error Spider in Parse_Review general')
                        # break

                    yield item

                else:
                    break

            else:
                listErrors=listErrors + ['review_date']
                print listErrors
                print 'HOOOOOOOOOOOOOOOOOOOOOOOOOOLA'
                print 'HOOOOOOOOOOOOOOOOOOOOOOOOOOLA'
                print 'HOOOOOOOOOOOOOOOOOOOOOOOOOOLA'
                print 'HOOOOOOOOOOOOOOOOOOOOOOOOOOLA'
                print 'HOOOOOOOOOOOOOOOOOOOOOOOOOOLA'
                print response
                print 'HOOOOOOOOOOOOOOOOOOOOOOOOOOLA'
                print 'HOOOOOOOOOOOOOOOOOOOOOOOOOOLA'
                print 'HOOOOOOOOOOOOOOOOOOOOOOOOOOLA'
                print 'HOOOOOOOOOOOOOOOOOOOOOOOOOOLA'
                print 'HOOOOOOOOOOOOOOOOOOOOOOOOOOLA'
                print 'HOOOOOOOOOOOOOOOOOOOOOOOOOOLA'
                print 'HOOOOOOOOOOOOOOOOOOOOOOOOOOLA'
                print 'HOOOOOOOOOOOOOOOOOOOOOOOOOOLA'
                #self.send_email(listErrors)
                raise CloseSpider('Error Spider in Parse_Review date')


        #Use selenium for extract to next page
        #open webdriver
        driver = webdriver.Chrome()
        driver.get(response.url)

        try:
            #Make click in the buttom
            driver.find_element_by_xpath("//div[@class='listContainer']/div[@class='prw_rup prw_common_north_star_pagination']/div/span[contains(@class, 'nav next taLnk')]").click()
            url = driver.current_url #Get the new url
            driver.close()

            #geckdriver dont stop itself
            os.system("pkill -f geckodriver")

            request = scrapy.Request(url, self.parse_review)
            #We send the meta data to the request of the next pages
            request.meta['hotel_name']=response.meta['hotel_name']
            request.meta['hotel_score']=response.meta['hotel_score']
            request.meta['hotel_street_address']=response.meta['hotel_street_address']
            request.meta['hotel_extended_address']=response.meta['hotel_extended_address']
            request.meta['hotel_locality_address']=response.meta['hotel_locality_address']
            yield request

        except:
            #If is the last page (or there is some problem)
            driver.close()

            #geckdriver dont stop itself
            os.system("pkill -f geckodriver")





    #
    #
    # def send_email(self, listErrors):
    #
    #     global exceptionErrorItem
    #
    #     if exceptionErrorItem == False:
    #         message = 'Al hacer el scrapy de Tripadvisor, no existen los campos '
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
    #         os.remove('itemsTripadvisor.csv')
