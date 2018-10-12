import scrapy, datetime, os, re,time
#from hotel_sentiment.items import HotelSentimentItem
# utilizo la clase del review en vez de la del hotel
from extraction_data.items import ListHomesTripadvisorItem
from extraction_data.urls import TripadvisorFuerteventuraHolidaysRentUrls
from scrapy.mail import MailSender
from scrapy.exceptions import CloseSpider
from elasticsearch import Elasticsearch
from selenium import webdriver

exceptionErrorItem=False
es = Elasticsearch(
   [
     'elastic:vituinproject@elasticsearch:9200/',
   ]
)


n = 0

#TODO use loaders
class TripadvisorSpider(scrapy.Spider):
    name = "tripadvisor_listHolidaysRent"
    #start_urls = [
    #    "https://www.tripadvisor.co.uk/Hotels-g187479-Tenerife_Canary_Islands-Hotels.html"
    #]
    start_urls = TripadvisorFuerteventuraHolidaysRentUrls()

    def parse(self, response):


        parse_is_ok = 0
        listErrors=[]

        for href in response.xpath('//div[@class="property_title"]/a/@href'):

            url = response.urljoin(href.extract())
            request = scrapy.Request(url, callback=self.parse_homes)
            # try:
            #     res = es.search(index="index_listHotlidaysRent_tripadvisor", doc_type="unstructured",body={
            #         "query": {
            #                 "match_phrase": {
            #                         "url": url
            #                         }
            #                 }
            #         })
            #     repeat=''
            #
            #     for hit in res['hits']['hits']:
            #         repeat = hit["_source"]
            # except:
            repeat = ''

            #If the hotel doesnt have in the list, it will extract its data
            if repeat == '':
                yield request
            parse_is_ok = 1
        next_page = response.xpath('//a[@class="ui_button primary nav next"]/@href')

        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)

        if parse_is_ok != 1:

                listErrors=listErrors + ['def parse']
                #self.send_email(listErrors)
                raise CloseSpider('Error scraping')


    def parse_homes(self, response):
        item = ListHomesTripadvisorItem()
        listErrors=[] #Bugs list, if it exists

        cont_bugs = 0
        no_bugs = False
        while cont_bugs < 3 and no_bugs is False:
            name = response.xpath('//h1[contains(@class,"vrPgHdr")]/text()')
            if name:
                item['name'] = name.extract()[0]
                no_bugs=True
            else:
                if cont_bugs == 2:
                    listErrors=listErrors + ['name']

                cont_bugs += 1



        item['url']=response.url

        lo_is_now = False
        cont_bugs = 0
        no_bugs = False
        while cont_bugs < 3 and no_bugs is False:
            lat = response.xpath('//div[@class="mapContainer"]/@data-lat')
            if lat:
                item['lat']= lat.extract()[0]
                no_bugs=True
            else:
                if cont_bugs == 2:
                    no_bugs = False
                    cont_bugs = 0
                    while cont_bugs < 3 and no_bugs is False:
                        #It's possible that it's not disponible. We'll extract a diferent field with selenium
                        driver = webdriver.Chrome()
                        driver.get(item['url'])
                        str_coor = driver.find_element_by_xpath('//span[@class="mapWxH"]/img').get_attribute('src')
                        pos1 = str_coor.find("center")+7
                        pos2 = str_coor.find("maptype")-1
                        coor = str_coor[pos1:pos2]
                        coor = coor.split(',')
                        lat = coor[0]
                        lo = coor[1]
                        driver.close()
                        if lo and lat:
                            item['lat'] = lat
                            item['lo'] = lo
                            no_bugs=True
                            lo_is_now = True
                        else:
                            if cont_bugs == 2:
                                listErrors=listErrors + ['lat']
                                listErrors=listErrors + ['lo']
                                lo_is_now = True

                            cont_bugs += 1


                cont_bugs += 1

        if lo_is_now is False:
            cont_bugs = 0
            no_bugs = False
            while cont_bugs < 3 and no_bugs is False:
                lo = response.xpath('//div[@class="mapContainer"]/@data-lng')
                if lo:
                    item['lo']=lo.extract()[0]
                    no_bugs=True
                else:
                    if cont_bugs == 2:
                        listErrors=listErrors + ['lo']

                    cont_bugs += 1

        cont_bugs = 0
        no_bugs = False
        while cont_bugs < 3 and no_bugs is False:
            driver = webdriver.Chrome()
            driver.get(item['url'])
            price = driver.find_element_by_xpath('//span[@class="NoDatesVariant__basePrice--1uHTH"]')

            if price:
                item['price']=price.text
                no_bugs=True
            else:
                if cont_bugs == 2:
                    listErrors=listErrors + ['price']

                cont_bugs += 1
            driver.close()

        cont_bugs = 0
        no_bugs = False
        while cont_bugs < 3 and no_bugs is False:
            type = response.xpath('//div[@class="propertyType"]/text()')
            if type:
                item['type']=type.extract()[0]
                no_bugs=True
            else:
                if cont_bugs == 2:
                    listErrors=listErrors + ['type']

                cont_bugs += 1

        cont_bugs = 0
        no_bugs = False
        while cont_bugs < 3 and no_bugs is False:
            details = response.xpath('//div[contains(@class,"overflowEllipsis")]/text()')
            if details:
                #it can have a bad composition. We're going to reorganizate
                elements = ''
                for element in details.extract():
                    elements += element

                elements=elements.split(',')
                item['rooms']=elements[0].strip()
                item['bathrooms']=elements[1].strip()
                item['n_people']=elements[2].strip()

                no_bugs=True
            else:
                if cont_bugs == 2:
                    listErrors=listErrors + ['details']

                cont_bugs += 1

        cont_bugs = 0
        no_bugs = False
        while cont_bugs < 3 and no_bugs is False:
            score = response.xpath('//div[@class="photo-viewer-review-summary"]/div/div[@class="rating-summary-bubbles"]/@content')
            if score:
                item['score']=score.extract()[0]
                no_bugs=True
            else:
                cont_bugs += 1

        cont_bugs = 0
        no_bugs = False
        while cont_bugs < 3 and no_bugs is False:
            locality = response.xpath('//div[@class="propertyGeoSpecs"]/text()')
            if locality:
                item['locality']=locality.extract()[0]
                no_bugs=True
            else:
                if cont_bugs == 2:
                    listErrors=listErrors + ['locality']

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
            #chromedriver dont stop itself
            os.system("pkill -f chromedriver")
            raise CloseSpider('Error in Parse Home')


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



