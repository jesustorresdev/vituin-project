import scrapy, datetime, re, os
from scrapy.loader import ItemLoader
from extraction_data.items import BookingReviewItem
from extraction_data.urls import BookingURLs
from scrapy.mail import MailSender
from scrapy.exceptions import CloseSpider
from elasticsearch import Elasticsearch
from datetime import timedelta
#crawl up to 6 pages of review per hotel
#max_pages_per_hotel = 6
exceptionErrorItem=False


class BookingSpider(scrapy.Spider):
    name = "booking_reviews"

    #When we want to get it a specific URLs
    #start_urls = BookingURLs()
    start_urls = []
    es = Elasticsearch(
       [
         'elastic:vituinproject@elasticsearch:9200/',
       ]
    )

    doc = {
        'size' : 10000,
        "query": {
            "bool": {
                "filter": {
                    "term" : { "place" : "Puerto de la Cruz" },
                }
            }
        }
    }
    res = []
    try:
        res = es.search(index='index_list_homes_booking', body=doc, scroll='1m')
    except:
        pass


    #create list of URLs
    if res:
        for hit in res['hits']['hits']:
            start_urls=start_urls + [hit["_source"]["url"]]


    #pageNumber = 1

    def parse(self, response):
        listErrors=[]
        #Make a query to Elasticsearch using the URL
        es = Elasticsearch(
           [
             'elastic:vituinproject@elasticsearch:9200/',
           ]
        )

        try:
            url = response.xpath('//a[starts-with(@class,"show_all_reviews_btn")]/@href')[0].extract()
            url_reviews = 'https://www.booking.com'+url
            print('url',url_reviews)
        except:
            url = None
        #if there are comment

        if url:

            request_en = scrapy.Request(url_reviews, callback=self.parse_review)
            request = scrapy.Request(url_reviews.replace('en-gb.',''), callback=self.parse_language)

            res = es.search(index="index_list_homes_booking", doc_type="unstructured",body={
                "query": {
                    "bool": {
                        "filter": {
                            "term" : { "url": response.url },
                        }
                    }
                }
            })

            hotel =  ''
            address =  ''

            for hit in res['hits']['hits']:

                    hotel = hit["_source"]["name"]
                    address = hit["_source"]["address"]
                    # score = hit["_source"]["score"]
                    # phone = hit["_source"]["phone"]


            #save some fields that we will send
            request.meta['hotel_name']=hotel
            request.meta['hotel_address']=address
            request_en.meta['hotel_name']=hotel
            request_en.meta['hotel_address']=address


            yield request_en
            yield request

    def parse_language(self, response):
        try:
            url_fr = response.xpath('//link[@hreflang="fr"]/@href')[0].extract()
        except:
            url_fr = None
            pass
        try:
            url_de = response.xpath('//link[@hreflang="de"]/@href')[0].extract()
        except:
            url_de = None
            pass
        try:
            url_es = response.xpath('//link[@hreflang="es"]/@href')[0].extract()
        except:
            url_es = None
            pass
        print ''
        print ''
        print 'url_fr',url_fr
        print 'url_es',url_es
        print 'url_de',url_de
        print ''
        print ''

        if url_fr:
            request_fr = scrapy.Request(url_fr, callback=self.parse_review)
            request_fr.meta['hotel_name']=response.meta['hotel_name']
            request_fr.meta['hotel_address']=response.meta['hotel_address']
        else:
            request_fr = None
        if url_es:
            request_es = scrapy.Request(url_es, callback=self.parse_review)
            request_es.meta['hotel_name']=response.meta['hotel_name']
            request_es.meta['hotel_address']=response.meta['hotel_address']
        else:
            request_es = None
        if url_de:
            request_de = scrapy.Request(url_de, callback=self.parse_review)
            request_de.meta['hotel_name']=response.meta['hotel_name']
            request_de.meta['hotel_address']=response.meta['hotel_address']
        else:
            request_de = None


        #self.pageNumber = 1
        #if there are comment
        if request_fr:
            yield request_fr
        if request_es:
            yield request_es
        if request_de:
            yield request_de

    #Parse the reviews
    def parse_review(self, response):

        now = datetime.datetime.combine(datetime.datetime.today(), datetime.time(0, 0))
        listErrors=[]

        #if self.pageNumber > max_pages_per_hotel:
        #    return
        is_end = False

        for rev in response.xpath('//li[starts-with(@class,"review_item")]'):


            item = BookingReviewItem()
            #sometimes the title is empty because of some reason, not sure when it happens but this works
            item['url']=response.url
            item['hotel_name']=response.meta['hotel_name']
            item['hotel_address']=response.meta['hotel_address']
            # item['hotel_score']=response.meta['hotel_score']

            review_date = rev.xpath('.//meta[@itemprop="datePublished"]/@content')
            if review_date:
                item['review_date'] = review_date[0].extract()
                date = datetime.datetime.strptime(item['review_date'], '%Y-%m-%d')

                item['review_date']= date
                #if (now - date).days < 7:
                if (now - date).days < 15:

                    title = rev.xpath('.//div[@class="review_item_review_header"]//span[@itemprop="name"]/text()')
                    if title:
                        item['title'] = title[0].extract()
                    else:
                        listErrors=listErrors + ['title']


                    print response.url
                    print response.url
                    print response.url
                    print''
                    print''
                    print''
                    print''
                    print''
                    print''
                    print''
                    content_pos = rev.xpath('.//div[@class="review_item_review_content"]/p[starts-with(@class,"review_pos")]/span/text()')
                    if content_pos:
                        item['positive_content'] = content_pos[0].extract()

                    content_neg = rev.xpath('.//div[@class="review_item_review_content"]/p[starts-with(@class,"review_neg")]/span/text()')
                    if content_neg:
                        item['negative_content'] = content_neg[0].extract()

                    score=rev.xpath('.//span[@itemprop="reviewRating"]/meta[@itemprop="ratingValue"]/@content')
                    if score:
                        item['score'] = score[0].extract()
                    else:
                        listErrors=listErrors + ['score']

                    # reviewer_location = rev.xpath('.//span[@class="reviewer_country"]/span[@itemprop="nationality"]/span[@itemprop="name"]/text()')
                    # if reviewer_location:
                    #     item['reviewer_location'] = reviewer_location.extract()

                    print ''
                    print ''
                    print ''
                    print ''
                    print ''
                    if len(listErrors)>0:
                        #self.send_email(listErrors)
                        print('-----------')
                        print('-----------')
                        print('-----------')
                        print('-----------')
                        print(listErrors)
                        raise CloseSpider('Error spider')


                    yield item

                else:
                    is_end = True
                    break
            else:
                is_photo = ''
                is_photo = rev.xpath('//li[@class="review_item_photo review_item_photo-p"]').extract()
                #if rev is a review item photo
                if is_photo == '':
                    listErrors=listErrors + ['review_date']
                    #self.send_email(listErrors)
                    raise CloseSpider('Error spider DATE')


        if is_end is False:
            next_page = response.xpath('//link[@rel="next"]/@href')
            if next_page:
                #self.pageNumber += 1
                url = next_page[0].extract()
                request = scrapy.Request(url, self.parse_review)
                #We send the meta data to the request of the next pages
                request.meta['hotel_name']=response.meta['hotel_name']
                request.meta['hotel_address']=response.meta['hotel_address']
                # request.meta['hotel_score']=response.meta['hotel_score']
                yield request


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
    #         #mailer.send(to=["erroresSpider@gmail.com"], subject='Errores en el Spider', body=message)
    #         exceptionErrorItem=True
    #
    #         #In this case we delete the extract file until this moment
    #         os.remove('itemsBooking.csv')

