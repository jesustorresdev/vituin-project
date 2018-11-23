import scrapy, datetime, re, os
from scrapy.loader import ItemLoader
from extraction_data.items import BookingReviewItem
from extraction_data.urls import BookingHotelsURLs
from scrapy.mail import MailSender
from scrapy.exceptions import CloseSpider
from elasticsearch import Elasticsearch
from datetime import timedelta
#crawl up to 6 pages of review per hotel
#max_pages_per_hotel = 6
exceptionErrorItem=False


class BookingSpider(scrapy.Spider):
    name = "booking_singlehotel"

    #When we want to get it a specific URLs
    #start_urls = BookingHotelsURLs()
    start_urls = []
    es = Elasticsearch(
       [
         'elastic:vituinproject@elasticsearch:9200/',
       ]
    )

    doc = {
        'size' : 10000,
        'query': {
            'match_all' : {}
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

    print 'start_urls--->',len(start_urls)
    print ''
    print ''
    print ''
    print ''
    #pageNumber = 1

    def parse(self, response):
        listErrors=[]
        #Make a query to Elasticsearch using the URL
        es = Elasticsearch(
           [
             'elastic:vituinproject@elasticsearch:9200/',
           ]
        )
        request = scrapy.Request(response.url, callback=self.parse_review)

        res = es.search(index="index_list_homes_booking", doc_type="unstructured",body={
            "query": {
                    "match_phrase": {
                            "url": response.url
                            }
                    }
             })


        hotel =  ''
        has_review =  ''
        address =  ''
        score = ''
        phone = ''

        for hit in res['hits']['hits']:

                hotel = hit["_source"]["name"]
                has_review = hit["_source"]["has_reviews"]
                address = hit["_source"]["address"]
                score = hit["_source"]["score"]
                phone = hit["_source"]["phone"]


        #save some fields that we will send
        request.meta['hotel_name']=hotel
        #this fields are optionals
        request.meta['hotel_address']=address
        request.meta['hotel_score']=score

        #self.pageNumber = 1

        #if there are comment
        if has_review:
            yield request


    #Parse the reviews
    def parse_review(self, response):
        now = datetime.datetime.combine(datetime.datetime.today(), datetime.time(0, 0))
        listErrors=[]

        #if self.pageNumber > max_pages_per_hotel:
        #    return


        for rev in response.xpath('//li[starts-with(@class,"review_item")]'):


            item = BookingReviewItem()
            #sometimes the title is empty because of some reason, not sure when it happens but this works
            item['hotel_name']=response.meta['hotel_name']
            item['hotel_address']=response.meta['hotel_address']
            item['hotel_score']=response.meta['hotel_score']

            review_date = rev.xpath('.//meta[@itemprop="datePublished"]/@content')
            if review_date:
                item['review_date'] = review_date [0].extract()
                date = datetime.datetime.strptime(item['review_date'], '%Y-%m-%d')

                item['review_date']= date
                #if (now - date).days < 7:
                if (now - date).days < 1000000:

                    title = rev.xpath('.//a[@class="review_item_header_content"]/span[@itemprop="name"]/text()')
                    if title:
                        item['title'] = title[0].extract()
                    else:
                        listErrors=listErrors + ['title']

                    positive_content = rev.xpath('.//p[@class="review_pos"]//span/text()')
                    if positive_content:
                        item['positive_content'] = positive_content[0].extract()
                    negative_content = rev.xpath('.//p[@class="review_neg"]//span/text()')
                    if negative_content:
                        item['negative_content'] = negative_content[0].extract()

                    score=rev.xpath('.//span[@itemprop="reviewRating"]/meta[@itemprop="ratingValue"]/@content')
                    if score:
                        item['score'] = score[0].extract()
                    else:
                        listErrors=listErrors + ['score']

                    reviewer_location = rev.xpath('.//span[@class="reviewer_country"]/span[@itemprop="nationality"]/span[@itemprop="name"]/text()')
                    if reviewer_location:
                        item['reviewer_location'] = reviewer_location.extract()

                    print ''
                    print ''
                    print ''
                    print ''
                    print 'item-->', item
                    print ''
                    print ''
                    print ''
                    print ''
                    if len(listErrors)>0:
                        #self.send_email(listErrors)
                        raise CloseSpider('Error spider')


                    yield item

                else:
                    break
            else:
                is_photo = ''
                is_photo = rev.xpath('//li[@class="review_item_photo review_item_photo-p"]').extract()
                #if rev is a review item photo
                if is_photo == '':
                    listErrors=listErrors + ['review_date']
                    #self.send_email(listErrors)
                    raise CloseSpider('Error spider')



        next_page = response.xpath('//a[@id="review_next_page_link"]/@href')
        if next_page:
            #self.pageNumber += 1
            url = response.urljoin(next_page[0].extract())
            request = scrapy.Request(url, self.parse_review)
            #We send the meta data to the request of the next pages
            request.meta['hotel_name']=response.meta['hotel_name']
            request.meta['hotel_address']=response.meta['hotel_address']
            request.meta['hotel_score']=response.meta['hotel_score']
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

