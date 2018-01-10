# -*- coding: utf-8 -*-
import scrapy, datetime, os, re, time
#from hotel_sentiment.items import HotelSentimentItem
# utilizo la clase del review en vez de la del hotel
from hotel_sentiment.items import ListRestaurantsTripadvisorItem
#from hotel_sentiment.urls import TripAdvisorPtoCruzRestaurantsURLs
#from scrapy.mail import MailSender
from scrapy.exceptions import CloseSpider
from elasticsearch import Elasticsearch
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

exceptionErrorItem=False
es = Elasticsearch(
   [
     'elastic:vituinproject@elasticsearch:9200/',
   ]
)


#TODO use loaders
class TripadvisorSpider(scrapy.Spider):
    name = "tripadvisor_listRestaurants"
    #start_urls = [
    #    "https://www.tripadvisor.co.uk/Hotels-g187479-Tenerife_Canary_Islands-Hotels.html"
    #]
#    start_urls = TripAdvisorPtoCruzRestaurantsURLs()
    start_urls = [
         #"https://www.tripadvisor.co.uk/Restaurants-g187481-Puerto_de_la_Cruz_Tenerife_Canary_Islands.html"
         #"https://www.tripadvisor.co.uk/Restaurants-g187479-Tenerife_Canary_Islands.html"
         "https://www.tripadvisor.co.uk/Restaurants-g187475-La_Palma_Canary_Islands.html"
         #"https://www.tripadvisor.co.uk/Restaurants-g187473-El_Hierro_Canary_Islands.html"
         #"https://www.tripadvisor.co.uk/Restaurants-g187469-La_Gomera_Canary_Islands.html"
         #"https://www.tripadvisor.co.uk/Restaurants-g187471-Gran_Canaria_Canary_Islands.html"
         #"https://www.tripadvisor.co.uk/Restaurants-g187477-Lanzarote_Canary_Islands.html"
         #"https://www.tripadvisor.co.uk/Restaurants-g187467-Fuerteventura_Canary_Islands.html"

    ]


    def parse(self, response):
        parse_is_ok = 0
        listErrors=[]
        n = 0
        end = 0
        print("**************************")
        print("**************************")
        print("**************************")
        print("**************************")
        print("**************************")
        print("**************************")
        print("**************************")
        print("**************************")
        print("**************************")
        print("**************************")
        print("**************************")
        print("**************************")
        
        #Use selenium for extract to next page
        #open webdriver
             
        driver = webdriver.Firefox()
        driver.get(response.url)
        url=driver.current_url
        time.sleep(2)   

        while end != 1:
            try:
                n=n+1
                #Make click in the buttom
                print("----")
                print("----")
                print('n= ' + str(n))
                print(url)
                print(response)                
                response.replace(url=url)
                print("paso")
                print(response)
                print("----")
                print("----")                
                
                '''
                for href in response.xpath('//div[@class="ui_column is-9 shortSellDetails"]/div[@class="title"]/a/@href'): 
                    url_restaurant = response.urljoin(href.extract())
                    request = scrapy.Request(url_restaurant, callback=self.parse_restaurant)
                    request.meta['n']=n
                    print('++++')
                    print('VA A RESTAURANT ' + str(n))
                    print(url_restaurant)
                    print(url)
                    print('++++')

                    yield request
                '''
   
                iteracion = 1
                while iteracion > -1:
                    try:
                        href=driver.find_element_by_xpath('//div[contains(@class, "listing rebrand listingIndex-' + str(iteracion) + '")]/div[@class="ui_columns is-mobile"]/div[@class="ui_column is-9 shortSellDetails"]/div[@class="title"]/a')                  
                        print("**********")
                        print("**********")
                        print("**********")
                        print("**********")

                        #print(href.get_attribute('href'))
                        print(iteracion)
                        url_restaurant = href.get_attribute('href')
                        print(url_restaurant)
                        print("**********")

                        request = scrapy.Request(url_restaurant, callback=self.parse_restaurant)
                        request.meta['n']=n
                        print('++++')
                        print('VA A RESTAURANT ' + str(iteracion) + ' y la n es ' + str(n))
                        print(url_restaurant)
                        print('++++')    
                        iteracion=iteracion+1

                        yield request
                    except:
                        iteracion = -1

                        pass 
                #request = scrapy.Request(url, self.parse)
                #We send the meta data to the request of the next pages
                #yield request

                driver.find_element_by_xpath('//a[@class="nav next rndBtn ui_button primary taLnk"]').click() 
                url = driver.current_url #Get the new url
                #driver.close()               
                #geckdriver dont stop itself
                #os.system("pkill -f geckodriver")
                time.sleep(1)   

            
            except:
                
                print("----")
                print("----")
                print("----")
                print("----")
                print('noooo')
                print("----")
                print("----")
                print("----")
                print("----")

                end=1
                try:
                    print('-')
                    #If is the last page (or there is some problem)
                    driver.close()
                    #geckdriver dont stop itself
                    os.system("pkill -f geckodriver")

                except:
                    pass
                
                '''
                if n != 18:
                    print("----")
                    print("----")
                    print("----")
                    print("----")
                    print('ERROR')
                    print('n= ' + str(n))
                    print("----")
                    print("----")
                    print("----")                 
                    raise CloseSpider('Error en Selenium')
                '''
#        if parse_is_ok != 1:

#                listErrors=listErrors + ['def parse']
                #self.send_email(listErrors)
#                raise CloseSpider('Error scraping')


    def parse_restaurant(self, response):
        print("----")
        print("----")
        print("----")  
        print("DENTRO " + str(response.meta['n']))
        print("----")
        print("----")
        print("----")    
        item = ListRestaurantsTripadvisorItem()
      
        listErrors=[] #Bugs list, if it exists
        name = response.xpath('//div[@id="taplc_location_detail_header_restaurants_0"]/h1/text()')
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
        #else:
        #        listErrors=listErrors + ['extended_address']

        locality = response.xpath('//span[@class="locality"]/text()')
        if locality:
                item['locality_address']=locality.extract()[0]
        else:
                listErrors=listErrors + ['locality_address']

        score = response.xpath('//div[@class="prw_rup prw_common_bubble_rating bubble_rating"]/span/@content')
        if score:
                item['score']=score.extract()[0]
        else:
                listErrors=listErrors + ['score']

        price = response.xpath('//span[@class="ui_column is-6 price"]/span/text()')
        if price:
            if price.extract()[0].find('-') == -1:
                if(len(price.extract()[0]) == 1):
                    item['price']='Cheap Eats' #There is one $
                else:
                    item['price']='Fine Dining' #There are four $
            else:
                item['price']='Mid Range' #if price is between two ranges($$-$$$)

        else:
                listErrors=listErrors + ['price']

        ratingExcellent = response.xpath('//ul[@class="ratings_chart"]/li[@data-idx="5"]/span[@class="row_count row_cell"]/text()')
        if ratingExcellent:
            item['ratingExcellent'] = ratingExcellent.extract()[0].replace("%","") #to eliminate the %
        else:
            listErrors=listErrors + ['ratingExcellent']

        ratingVeryGood = response.xpath('//ul[@class="ratings_chart"]/li[@data-idx="4"]/span[@class="row_count row_cell"]/text()')
        if ratingVeryGood:
            item['ratingVeryGood'] = ratingVeryGood.extract()[0].replace("%","") #to eliminate the %
        else:
            listErrors=listErrors + ['ratingVeryGood']

        ratingAverage = response.xpath('//ul[@class="ratings_chart"]/li[@data-idx="3"]/span[@class="row_count row_cell"]/text()')
        if ratingAverage:
            item['ratingAverage'] = ratingAverage.extract()[0].replace("%","") #to eliminate the %
        else:
            listErrors=listErrors + ['ratingAverage']

        ratingPoor = response.xpath('//ul[@class="ratings_chart"]/li[@data-idx="2"]/span[@class="row_count row_cell"]/text()')
        if ratingPoor:
            item['ratingPoor'] = ratingPoor.extract()[0].replace("%","") #to eliminate the %
        else:
            listErrors=listErrors + ['ratingPoor']

        ratingTerrible = response.xpath('//ul[@class="ratings_chart"]/li[@data-idx="1"]/span[@class="row_count row_cell"]/text()')
        if ratingTerrible:
            item['ratingTerrible'] = ratingTerrible.extract()[0].replace("%","") #to eliminate the %
        else:
            listErrors=listErrors + ['ratingTerrible']

        has_review = response.xpath('//div[@class="rating"]/a/text()')
        if has_review:
            #print("----")
            #print(has_review)
            #print("----") 
            item['has_reviews'] = has_review.extract()[0].split(' ')[0]
            try:
                item['has_reviews'] = item['has_reviews'].replace(",","") #If it's a number of four (or more) digits we have to eliminate the coma
            except:
                pass 
        else:
            item['has_reviews'] = 0


        #ratings for elements: food, service, value, atmosphere
        ratings = response.xpath('//div[@class="ui_columns is-multiline questionRatings"]/div[@class="ui_column is-6"]')
        if ratings:
            n=0
            while n < len(ratings.extract()):
                try:
                    #we extract the name of the item
                    variable = ratings.xpath('.//span[@class="text"]/text()').extract()[n].lower()
                    #Extract the 2 last elements. It's are the bubbles
                    value = (ratings.xpath('.//span/@class').extract()[n*2])[-2:]
                    value = value[:1] + '.' + value[1:]
                    item[variable]=value
                    n=n+1
                except:
                    listErrors=listErrors + ['ratingsBucle']
                    break
        else:
            listErrors=listErrors + ['ratings']

        if len(listErrors)>0:

                #self.send_email(listErrors)
                print(listErrors)
       #         raise CloseSpider('Error in Parse Restaurant')




        return item

