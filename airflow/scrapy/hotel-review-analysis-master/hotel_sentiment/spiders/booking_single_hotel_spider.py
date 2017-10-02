import scrapy, datetime, os, re
from scrapy.loader import ItemLoader
from hotel_sentiment.items import BookingReviewItem
from hotel_sentiment.urls import BookingHotelsURLs
from scrapy.mail import MailSender
from scrapy.exceptions import CloseSpider
from elasticsearch import Elasticsearch
from datetime import timedelta
#crawl up to 6 pages of review per hotel
max_pages_per_hotel = 6
exceptionErrorItem=False

class BookingSpider(scrapy.Spider):
    name = "booking_singlehotel"
    
    #En caso de que obtengamos la lista de urls que nosotros le pasamos
    #start_urls = BookingHotelsURLs()
    start_urls = []
    es = Elasticsearch(['elasticsearch:9200'])
    res = es.search(index="index_listhotels_booking")
    #creamos lista de urls
    for hit in res['hits']['hits']:
            start_urls=start_urls + [hit["_source"]["url"]]


    def parse(self, response):
        #parse_is_ok = 0
        listErrors=[]
        es = Elasticsearch(['elasticsearch:9200'])

        #la consulta a Elasticsearch se hace por medio de la url
        request = scrapy.Request(response.url, callback=self.parse_review)
        res = es.search(index="index_listhotels_booking", doc_type="hotels_unit",body={
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


        #se almacenan una serie de campos que se van a enviar
        request.meta['hotel_name']=hotel
        request.meta['has_review']=has_review
        #Estos campos son opcionales. Pueden estar vacios
        request.meta['hotel_address']=address
        request.meta['hotel_score']=score

        yield request

        #parse_is_ok = 1


    #Parse the reviews
    def parse_review(self, response):

        now = datetime.datetime.combine(datetime.datetime.today(), datetime.time(0, 0))
        listErrors=[]


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

                    #tags are separated by ;
                    # comento las tags. No la usamos en el proyecto
                    #item['tags'] = ";".join(rev.xpath('.//li[@class="review_info_tag"]/text()').extract())
                    # anado codigo para sar la fecha de la revision y la localizacion del revisor

                    item['reviewer_location'] = rev.xpath('.//span[@class="reviewer_country"]/span[@itemprop="nationality"]/span[@itemprop="name"]/text()')[0].extract()

                    yield item

                else:
                    break
            else:
                listErrors=listErrors + ['review_date']

        if len(listErrors)>0:

          #self.send_email(listErrors)
          raise CloseSpider('Error spider')


        next_page = response.xpath('//a[@id="review_next_page_link"]/@href')
        if next_page:
            self.pageNumber += 1
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse_reviews)


    def send_email(self, listErrors):

        global exceptionErrorItem

        if exceptionErrorItem == False:
            message = 'Al hacer el scrapy de Tripadvisor no existen los campos '

            for elementError in listErrors:
                message = message + elementError + ', '

            message = re.sub(', $', '.' , message)

            #Mandar un correo informando si hay un error
            mailer = MailSender(mailfrom="erroresSpider@gmail.com",smtphost="smtp.gmail.com",smtpport=587,smtpuser="erroresSpider@gmail.com",smtppass="errores1234")
            #mailer.send(to=["erroresSpider@gmail.com"], subject='Errores en el Spider', body=message)
            exceptionErrorItem=True

            #eliminar el archivo extraido hasta entonces
            os.remove('itemsBooking.csv')

