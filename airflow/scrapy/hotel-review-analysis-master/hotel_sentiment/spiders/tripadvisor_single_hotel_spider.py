import scrapy, datetime, os, re
#from hotel_sentiment.items import HotelSentimentItem
# utilizo la clase del review en vez de la del hotel
from hotel_sentiment.items import TripAdvisorReviewItem
from hotel_sentiment.urls import TripAdvisorHotelsURLs
from scrapy.mail import MailSender
from scrapy.exceptions import CloseSpider
from elasticsearch import Elasticsearch

exceptionErrorItem=False

#TODO use loaders
class TripadvisorSpider(scrapy.Spider):

    name = "tripadvisor_singlehotel"
    #start_urls = TripAdvisorHotelsURLs()
    start_urls = []
    es = Elasticsearch(['elasticsearch:9200'])
    res = es.search(index="index_listhotels_tripadvisor")
    #creamos lista de urls
    for hit in res['hits']['hits']:
            start_urls=start_urls + [hit["_source"]["url"]]


    def parse(self, response):
        listErrors=[]
        es = Elasticsearch(['elasticsearch:9200'])

        for href in response.xpath('//div[starts-with(@class,"quote")]/a/@href'):


            url = response.urljoin(href.extract())

            #se forma el request 
            request = scrapy.Request(url, callback=self.parse_review)

            #la consulta a Elasticsearch ciertos campos por medio de la url
	    res = es.search(index="index_listhotels_tripadvisor", doc_type="hotels_unit",body={
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

	   
            #se almacenan los campos que se van a unir
            request.meta['hotel_name']=hotel
            request.meta['has_review']=has_review

            #Estos campos son opcionales. Pueden estar vacios
            request.meta['hotel_street_address']=street
            request.meta['hotel_extended_address']=extended
            request.meta['hotel_locality_address']=locality
            request.meta['hotel_score']=score


            yield request

        next_page = response.xpath('//div[@class="unified pagination "]/child::*[2][self::a]/@href')
        if next_page:

            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse_hotel)



    #to get the full review content I open its page, because I don't get the full content on the main page
    #there's probably a better way to do it, requires investigation
    def parse_review(self, response):
        item = TripAdvisorReviewItem() #cambio de la clase Hotel Sentiment a la especifica de Tripadvisor
        listErrors=[] #lista de errores si los hubiera

        item['hotel_name']=response.meta['hotel_name'] 
        item['hotel_street_address']=response.meta['hotel_street_address']
        item['hotel_extended_address']=response.meta['hotel_extended_address']
        item['hotel_locality_address']=response.meta['hotel_locality_address']
        item['hotel_score']=response.meta['hotel_score']

        r_d=response.xpath('//span[@class="ratingDate relativeDate"]/@title')
        
        if r_d:
            item['review_date'] = r_d.extract()[0]
        else:
            listErrors=listErrors + ['review_date'] 

        date = datetime.datetime.strptime(item['review_date'] , '%d %B %Y') 
        now = datetime.datetime.combine(datetime.datetime.today(), datetime.time(0, 0))
        item['review_date']= date   


        print(date)
	print('-----------')
        print(now)
	print('-----------')
        print(datetime.datetime.today())
        raise CloseSpider('Error Spider in Parse_Review')

#        if (now - date).days < 7: 
        if (now - date).days < 1000000 and len(listErrors)==0: 

            t = response.xpath('//div[@class="quote isNew"]/a/span/text()') 
            if t: 
                item['title'] = t.extract()[0][1:-1] #strip the quotes (first and last char)
            else:
                listErrors=listErrors + ['title']    

            c = response.xpath('//div[@class="entry"]/p/text()')
            if c:
                item['content'] = c.extract()[0]
            else:
                listErrors=listErrors + ['content']

            r_l = response.xpath('//div[@class="location"]/span/text()')
            if r_l: 
                item['reviewer_location']  = r_l.extract()[0]
        
            else:
                listErrors=listErrors + ['reviewer_location']  

            #si ejecutas como la comentada ves toda la seccion de span y te ayuda a ver los atributos. content tiene la fecha en numerico
            #item['review_date'] = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "relativeDate", " " ))]').extract()[0]

            #item['review_date2'] = response.xpath('//span[@class="ratingDate relativeDate"]/@tittle').extract()

            #item['review_date2'] = response.xpath('//span[@class="ratingDate relativeDate"]/@title').extract()[0]

            #si hay errores al extraer campos

            if len(listErrors)>0:
                #self.send_email(listErrors)
                print(listErrors)
                #si no tiene review no pasa nada por los errores
                if has_review != 1:
                	raise CloseSpider('Error Spider in Parse_Review')


            return item

    def send_email(self, listErrors):

        global exceptionErrorItem

        if exceptionErrorItem == False:
            message = 'Al hacer el scrapy de Tripadvisor no existen los campos '

            for elementError in listErrors:
                message = message + elementError + ', '

            message = re.sub(', $', '.' , message)

            #Mandar un correo informando si hay un error
            mailer = MailSender(mailfrom="erroresSpider@gmail.com",smtphost="smtp.gmail.com",smtpport=587,smtpuser="erroresSpider@gmail.com",smtppass="errores1234")
            mailer.send(to=["erroresSpider@gmail.com"], subject='Errores en el Spider', body=message)
            exceptionErrorItem=True

            #eliminar el archivo extraido hasta entonces
            os.remove('itemsTripadvisor.csv') 




