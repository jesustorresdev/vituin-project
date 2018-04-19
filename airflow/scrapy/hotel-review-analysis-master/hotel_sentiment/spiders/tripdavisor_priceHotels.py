import scrapy, datetime, os, re
#from hotel_sentiment.items import HotelSentimentItem
# utilizo la clase del review en vez de la del hotel
from scrapy.mail import MailSender
from scrapy.exceptions import CloseSpider
from hotel_sentiment.items import ListPriceHotelsItem
from elasticsearch import Elasticsearch
from selenium import webdriver
from datetime import datetime
import time
from dateutil.relativedelta import relativedelta

exceptionErrorItem=False
es = Elasticsearch(
    [
        'elastic:vituinproject@elasticsearch:9200/',
    ]
)



#TODO use loaders
class TripadvisorSpider(scrapy.Spider):
    name = "tripadvisor_priceHotels"

    start_urls = []
    es = Elasticsearch(
        [
            'elastic:vituinproject@elasticsearch:9200/',
        ]
    )
    #SearchAllEstablishments
    res = es.search(index="index_tripadvisor_hotels_establishments", doc_type="hotels",body={
        "query": {
            "match_phrase": {
                "island": "Fuerteventura"
            }
        }
    },scroll='1m')
    #creamos lista de urls
    for hit in res['hits']['hits']:
        start_urls=start_urls + [hit["_source"]["url"]]

    def parse(self, response):


        print response.xpath('//div[@class="ui_overlay ui_popover arrow_top light no_x small"]')

        raise CloseSpider('eeh')
        # listErrors=[]
        # #Create the request
        # request = scrapy.Request(response.url, callback=self.parse_hotel)
        # es = Elasticsearch(
        #     [
        #         'elastic:vituinproject@elasticsearch:9200/',
        #     ]
        # )
        #
        # #Make a query to Elasticsearch using the URL
        # res = es.search(index="index_tripadvisor_hotels_establishments", doc_type="hotels",body={
        #     "query": {
        #         "match_phrase": {
        #             "url": response.url
        #         }
        #     }
        # })
        #
        #
        # hotel =  ''
        #
        # for hit in res['hits']['hits']:
        #     hotel = hit["_source"]["name"]
        #
        #
        # #save some fields that we will send
        # request.meta['hotel_name']=hotel
        #
        # yield request

    #
    # def parse_hotel(self, response):
    #     driver = webdriver.Chrome()
    #     driver.get(response.url)
    #
    #     num = 0
    #     month=[0,0,1,3]
    #     day=[0,14,0,0]
    #     time_borrow = ['today', 'in two weeks', 'in a month', 'in three month']
    #     while num < 4:
    #         d1 = datetime.now()
    #         driver.find_element_by_xpath("//span[@data-datetype='CHECKIN']").click()
    #         if driver.find_element_by_xpath("//span[@class='rsdc-month-title']").text[:3] != d1.strftime("%b"):
    #             print 'NOOOOOOOOO'
    #             while driver.find_element_by_xpath("//span[@class='rsdc-month-title']").text[:3] != d1.strftime("%b"):
    #                 print 'cambiando'
    #                 print driver.find_element_by_xpath("//span[@class='rsdc-month-title']").text[:3]
    #                 driver.find_element_by_xpath("//div[contains(@class,'rsdc-prev')]").click()
    #
    #         d1 = d1 + relativedelta(days=day[num]) + relativedelta(months=month[num])
    #         d2 = d1 + relativedelta(days=1)
    #         num += 1
    #
    #         checkIn = str(d1.year)+'-'+str(d1.month - 1)+ '-' + str(d1.day)
    #         checkOut = str(d2.year)+'-'+str(d2.month - 1)+ '-' + str(d2.day)
    #         #
    #
    #         time.sleep(0.1)
    #         finish = False
    #         checkInError = False
    #         contador = 0
    #         print checkIn, checkOut
    #
    #         while finish == False:
    #             try:
    #                 driver.find_element_by_xpath("//span[@data-date='"+checkIn+"']").click()
    #                 time.sleep(0.1)
    #                 print 'fecha'
    #                 finish = True
    #
    #                 # yield request
    #
    #             except Exception as e:
    #                 try:
    #                     i -= 1
    #                     res1 = driver.find_element_by_xpath("//div[@class = 'no_cpu offer textLink ']//div["+str(i)+"]//span[1]")
    #                     res2 = driver.find_element_by_xpath("//div[@class = 'no_cpu offer textLink ']//div["+str(i)+"]//span[2]")
    #                     i += 1
    #                     print res1.get_attribute('title'), res2.get_attribute('title')
    #                     print '---------'
    #                     print '---------'
    #                     print '---------'
    #                     print ', i= ',  i,', periodo= ', time_borrow[num], '-------> ', response.meta['hotel_name']
    #                     print res1, res2
    #                     print '---------'
    #                     item = ListPriceHotelsItem() #Class with Tripadvisor fields
    #
    #                     item['name']=response.meta['hotel_name']
    #                     item['url']=response.url
    #                     item['company']=res1
    #                     item['price']= res2
    #                     item["time_borrow"]=time_borrow[num]
    #                     yield item
    #                 except Exception as e2:
    #                     print 'except'
    #                     print 'except'
    #                     print '1---------> ', e
    #                     print '2---------> ', e2
    #                     print response.meta['hotel_name'], time_borrow[num]
    #                     print response
    #                     print 'except'
    #                     print 'except'
    #                     print 'except'
    #                     elements = False
    #
    #     driver.close()
    #
    #     # #geckdriver dont stop itself
    #     # os.system("pkill -f chromedriver")
    # #     # os.system("pkill -f chrome")
    # #
    #
    #             except:
    #                 print driver.find_element_by_xpath("//span[@class='rsdc-month-title']").text
    #                 driver.find_element_by_xpath("//div[contains(@class,'rsdc-next')]").click()
    #                 print 'next'
    #                 time.sleep(0.1)
    #                 contador += 1
    #                 print contador
    #                 if contador == 14:
    #                     finish = True
    #                     checkInError = True
    #
    #         if checkInError == True:
    #             import sys
    #             sys.exit('ERROR')
    #
    #
    #         driver.find_element_by_xpath("//span[@data-date='"+checkOut+"']").click()
    #         time.sleep(1)
    #
    # #
    #         # if checkInError == True:
    #         #     import sys
    #         #     sys.exit('ERROR')
    #
    #         elements = True
    #         i = 1
    #         while elements == True:
    #             try:
    #                 res1 = driver.find_element_by_xpath("//div[@class = 'prw_rup prw_meta_view_all_text_links']//div["+str(i)+"]//span[1]").get_attribute('title')
    #                 res2 = driver.find_element_by_xpath("//div[@class = 'prw_rup prw_meta_view_all_text_links']//div["+str(i)+"]//span[2]").get_attribute('title')
    #                 # request = scrapy.Request(response.url, callback=self.parse_hotel)
    #                 # request.meta['i']=i
    #                 i += 1
    #                 #
    #                 #
    #                 # request.meta['hotel_name']=response.meta['hotel_name']
    #                 # request.meta['res1']=res1
    #                 # request.meta['res2']=res2
    #                 # request.meta['num']=num
    #                 print '---------'
    #                 print '---------'
    #                 print '---------'
    #                 print ', i= ',  i,', periodo= ', time_borrow[num], '-------> ', response.meta['hotel_name']
    #                 print res1, res2
    #                 print '---------'
    #                 item = ListPriceHotelsItem() #Class with Tripadvisor fields
    #
    #                 item['name']=response.meta['hotel_name']
    #                 item['url']=response.url
    #                 item['company']=res1
    #                 item['price']= res2
    #                 item["time_borrow"]=time_borrow[num]
    #                 yield item
    #
    #
    #                 # yield request
    #
    #             except Exception as e:
    #                 try:
    #                     i -= 1
    #                     res1 = driver.find_element_by_xpath("//div[@class = 'no_cpu offer textLink ']//div["+str(i)+"]//span[1]")
    #                     res2 = driver.find_element_by_xpath("//div[@class = 'no_cpu offer textLink ']//div["+str(i)+"]//span[2]")
    #                     i += 1
    #                     print res1.get_attribute('title'), res2.get_attribute('title')
    #                     print '---------'
    #                     print '---------'
    #                     print '---------'
    #                     print ', i= ',  i,', periodo= ', time_borrow[num], '-------> ', response.meta['hotel_name']
    #                     print res1, res2
    #                     print '---------'
    #                     item = ListPriceHotelsItem() #Class with Tripadvisor fields
    #
    #                     item['name']=response.meta['hotel_name']
    #                     item['url']=response.url
    #                     item['company']=res1
    #                     item['price']= res2
    #                     item["time_borrow"]=time_borrow[num]
    #                     yield item
    #                 except Exception as e2:
    #                     print 'except'
    #                     print 'except'
    #                     print '1---------> ', e
    #                     print '2---------> ', e2
    #                     print response.meta['hotel_name'], time_borrow[num]
    #                     print response
    #                     print 'except'
    #                     print 'except'
    #                     print 'except'
    #                     elements = False
    #
    #     driver.close()
    #
    #     # #geckdriver dont stop itself
    #     # os.system("pkill -f chromedriver")
    #     # os.system("pkill -f chrome")




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

