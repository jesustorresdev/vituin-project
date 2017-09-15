import scrapy, datetime, os, re
#from hotel_sentiment.items import HotelSentimentItem
# utilizo la clase del review en vez de la del hotel
from hotel_sentiment.items import TripAdvisorReviewItem
from scrapy.mail import MailSender
from scrapy.exceptions import CloseSpider


#TODO use loaders
class TripadvisorSpider(scrapy.Spider):
    name = "tripadvisor"
    start_urls = [
        "https://www.tripadvisor.co.uk/Hotels-g187479-Tenerife_Canary_Islands-Hotels.html"
    ]

    def parse(self, response):
        for href in response.xpath('//div[@class="listing_title"]/a/@href'):
            print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
            url = response.urljoin(href.extract())
#            yield scrapy.Request(url, callback=self.parse_hotel)


#        next_page = response.xpath('//div[@class="unified pagination standard_pagination"]/child::*[2][self::a]/@href')
#        if next_page:
#            url = response.urljoin(next_page[0].extract())
#            yield scrapy.Request(url, self.parse)

    def parse_hotel(self, response):
        for href in response.xpath('//div[starts-with(@class,"quote")]/a/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_review)

        next_page = response.xpath('//div[@class="unified pagination "]/child::*[2][self::a]/@href')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse_hotel)


    #to get the full review content I open its page, because I don't get the full content on the main page
    #there's probably a better way to do it, requires investigation
    def parse_review(self, response):
        item = TripAdvisorReviewItem() #cambio de la clase Hotel Sentiment a la especifica de Tripadvisor
        listErrors=[] #lista de errores si los hubiera

        r_d = response.xpath('//span[@class="ratingDate relativeDate"]/@content')
        if r_d: 
            item['review_date'] = r_d.extract()[0]
        else:
            listErrors=listErrors + ['review_date'] 


        date = datetime.datetime.strptime(item['review_date'], '%Y-%m-%d') 
        now = datetime.datetime.combine(datetime.datetime.today(), datetime.time(0, 0))

	print("EEEEEEEEEEEEEEEEEEEEEEEEEEE")
#        if (now - date).days < 7: 
        if (now - date).days < 1000000: 
            t = response.xpath('//div[@class="quote"]/text()')
            if t: 
                item['title'] = t.extract()[0][1:-1] #strip the quotes (first and last char)
            else:
                listErrors=listErrors + ['title']    

            c = response.xpath('//div[@class="entry"]/p/text()')
            if c:
                item['content'] = c.extract()[0]
            else:
                listErrors=listErrors + ['content']

            r_l = response.xpath('//div[@class="location"]/text()')
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
                raise CloseSpider('Error spider')


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
