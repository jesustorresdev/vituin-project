# -*- coding: UTF-8 -*-

"""Extracción de viviendas en Only Apartments
"""

__authors__ = 'Sergio Díaz, Jesús Torres'
__organization__ = 'Universidad de La Laguna'
__licensed__ = 'UNLICENSED'
__contact__ = "jmtorres@ull.edu.es, sdiazgon@ull.edu.es"
# __copyright__ = f"Copyright 2017-2018 {__organization__}"

from scrapy import Request
from extraction_data.urls import OnlyApartmentsURLs
from extraction_data.items import ListOnlyApartmentsHomeItem
from extraction_data.required_fields import ListOnlyApartmentsHomeRequiredFields
from extraction_data.scrapy_spider import ScrapySpider
from extraction_data.utils import type_try

ELASTICSEARCH_INDEX = 'only_apartments_homes'
ELASTICSEARCH_DOC_TYPE = 'unstructured'

#TODO use loaders
class OnlyApartmentsSpider(ScrapySpider):
    name = "only_apartments_listHomes"

    def __init__(self, place=''):
        self.place = place
        self.start_urls = OnlyApartmentsURLs(place)
        self.first_searched = self.get_if_first_searched(ELASTICSEARCH_INDEX, ELASTICSEARCH_DOC_TYPE)

    def parse(self, response):
        current_page = self.xpath(response,"//ul[contains(@class,'pagination')]/li[@class='active']/button", type='text')
        homes = self.xpath(response,"//div[@class='wrapper container']/../..", type='object')
        print('')
        print('')
        print(len(homes))
        print(homes[0])
        print('')
        print('')
        # for home in homes:
        #     url=self.xpath(home, './', type='attribute', attribute='href')
        #     id=self.xpath(home, './', type='attribute', attribute='data-id')
        #     place_and_type = self.xpath(home, ".//h6[@class='location ellipsis']/span",type='object')
        #     if place_and_type:
        #         type_residence = self.xpath(place_and_type[0],'./', type='text')
        #         place = self.xpath(place_and_type[1], './', type='text')
        #     else:
        #         type_residence = ''
        #         place = ''
        #     print('url--->',url)
        #     print('id--->',url)
        #     request = Request(url, callback=self.parse_home)
        #     request.meta['id'] = id
        #     request.meta['type_residence'] = type_residence
        #     request.meta['place'] = place
        #     # request.meta['type_residence'] = type_residence
        #     # if place.find(self.place) != -1:
        #     #     yield request
        #     if self.first_searched:
        #         yield request
        #     elif not self.exist_item(ELASTICSEARCH_INDEX, url):
        #         yield request

        total_of_apartments = self.xpath(response,"//b[@id='header_total_ads']", type='text')
        current_page = type_try(current_page, int) if current_page is not '' else 100
        total_of_apartments = type_try(total_of_apartments, float) if total_of_apartments is not '' else 1

        print('')
        print('')
        print('')
        print 'Current',current_page, ', last', total_of_apartments
        print 'Current',type(current_page), ', last', type(total_of_apartments)
        print('')
        print('')
        print('')

        if current_page < total_of_apartments / 15:
            next_page_url= self.xpath(response, "//ul[contains(@class,'pagination')]/li[last()]/button", type='attribute', attribute='data-href')
            yield Request(
                next_page_url, callback=self.parse
            )


    def parse_home(self, response):
        item = ListOnlyApartmentsHomeItem()

        title= self.xpath(response, "//meta[@property='og:title']", type='attribute', attribute='content')
        title = title[:title.find('|')-1]
        description= self.xpath(response, "//meta[@itemprop='description']", type='attribute', attribute='content')
        street= self.xpath(response, "//meta[@name='geo.placename']", type='attribute', attribute='content')
        (lat,lng)= self.xpath(response, "//meta[@name='geo.position']", type='attribute', attribute='content').split(';')      #####  <--------- OJO SPLIT!!!!!!!!!!! SI NO EXISTE ELEMENTO DA ERROR



        mainBubbles = self.xpath(response,"//span[@class='rating-number']/strong", type='text')
        numberReviews = self.xpath(response,"//strong[@class ='review-count']", type='text')

        #Only-apartments reviews and ratings
        tripadvisor_rating = self.xpath(response, "//div[@class='tripadvisor-rating']",type='object')
        mainBubblesTripadvisor = self.xpath(tripadvisor_rating,".//span[@itemprop='ratingCount']", type='text')
        numberReviewsTripadvisor = self.xpath(tripadvisor_rating,".//span[@itemprop='ratingValue']", type='text')

        item['id'] = response.meta['id']
        item['url'] = response.url
        item['title'] = title
        item['description'] = description
        item['type_residence'] = response.meta['type_residence']
        item['place'] = response.meta['place']
        item['street'] = street
        item['lat'] = lat
        item['lng'] = lng
        item['number_reviews'] = numberReviews
        item['main_bubbles'] = mainBubbles
        item['number_reviews_tripadvisor'] = numberReviewsTripadvisor
        item['main_bubbles_tripadvisor'] = mainBubblesTripadvisor
        item['place_searched'] = self.place

        self.check_item(item, ListOnlyApartmentsHomeRequiredFields())
        self.update_database(item, ELASTICSEARCH_INDEX, ELASTICSEARCH_DOC_TYPE, self.first_searched)
        if self.first_searched:
            self.first_searched = False

        return item



#EN SU MOMENTO INTENTE SIMULAR EL PRECIO Y LA ESTANCIA MINIMA        # n_data = 0
        # n_data_out = 0
        # get_price = False
        # while get_price is False:
        #     get_price = True
        #     datepicker = driver.find_elements_by_xpath("//button[@class='ui-datepicker-trigger']")
        #     arrive = datepicker[0]
        #     driver.execute_script("return arguments[0].scrollIntoView();", arrive)
        #     arrive.click()
        #
        #     select_date = False
        #     day_in = 0
        #     while select_date is False:
        #         n_in = n_data
        #         try:
        #             print 'entro'
        #             date_selected = driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']").find_elements_by_xpath('.//a')
        #             month_in = str(driver.find_element_by_xpath("//span[@class='ui-datepicker-month']").text).lower()
        #             year_in = str(driver.find_element_by_xpath("//span[@class='ui-datepicker-year']").text)
        #             day_in = str(date_selected[0].text)
        #             driver.execute_script("return arguments[0].scrollIntoView();", date_selected[0])
        #             print 'pinche'
        #             select_date = True
        #         except Exception as error:
        #             print 'No pincho por', error
        #             next_month = driver.find_element_by_xpath("//div[contains(@class,'ui-datepicker-header')]"). \
        #                 find_elements_by_xpath(".//a[contains(@class,'ui-datepicker-next')]")
        #             next_month[0].click()
        #             n_in = 0
        #

        #     time.sleep(1)
        #     select_date = False
        #     n_out = 0
        #     contador_out = 0
        #     datepicker = driver.find_elements_by_xpath("//button[@class='ui-datepicker-trigger']")
        #     print 'len datapicker-->', len(datepicker)
        #     driver.execute_script("return arguments[0].scrollIntoView();", datepicker[1])
        #     go_out = datepicker[1]
        #     go_out.click()
        #     while select_date is False:
        #         n_out = n_data + 1 + n_data_out
        #         try:
        #             date_selected = driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']").find_elements_by_xpath('.//a')
        #             day_out = str(date_selected[n_out].text)
        #             print 'n_out-->',n_out
        #             print 'len date_selected-->',len(date_selected)
        #             print 'str(date_selected[0].text)-->',str(date_selected[0].text)
        #             month_out = str(driver.find_element_by_xpath("//span[@class='ui-datepicker-month']").text).lower()
        #             year_out = str(driver.find_element_by_xpath("//span[@class='ui-datepicker-year']").text)
        #             select_date = True
        #             date_selected[n_out].click()
        #         except Exception as error:
        #             print 'No pincho en out por',error
        #             print 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno)
        #             time.sleep(1)
        #             contador_out += 1
        #             print contador
        #             if contador_out > 5:
        #                 next_month = driver.find_element_by_xpath("//div[contains(@class,'ui-datepicker-header')]"). \
        #                     find_elements_by_xpath(".//a[contains(@class,'ui-datepicker-next')]")
        #                 next_month[0].click()
        #                 n_out = 0
        #                 break
        #
        #
        #     print 'day_in-->', day_in
        #     print 'day_out-->', day_out
        #
        #     date_in = year_in+'-'+str(months[month_in])+'-'+day_in
        #     date_out= year_out+'-'+str(months[month_out])+'-'+day_out
        #     print 'date_in-->', date_in
        #     print 'date_out-->', date_out
        #     date_in_datetime = datetime.strptime(date_in,"%Y-%m-%d")
        #     date_out_datetime = datetime.strptime(date_out,"%Y-%m-%d")
        #
        #     print 'date_in_datetime-->',date_in_datetime
        #     print 'date_out_datetime-->', date_out_datetime
        #     stay = (date_out_datetime - date_in_datetime).days
        #     print 'min_stay-->',stay
        #
        #     url_add = '?daterange.start_date='+date_in+'&daterange.end_date='+date_out+'&paxes=ADULT:2&page=1'
        #     price_url = driver.current_url + url_add
        #     print 'new_url-->', price_url
        #     driver.get(price_url)
        #     time.sleep(1)
        #     #Price
        #     load_price = False
        #     contador_price = 0
        #     price = ''
        #     while load_price is False:
        #         try:
        #             load_price = True
        #             try:
        #                 price = driver.find_element_by_xpath("//span[@itemprop='price']").text
        #                 print 'price normal-->', price
        #             except:
        #                 price = driver.find_element_by_xpath("//div[@id='total_price_head_container']").find_element_by_xpath(".//div[contains(@class,'brand-primary')]").text.split()[0]
        #                 print 'price hotel-->', price
        #
        #         except Exception as error:
        #             load_price = False
        #             contador_price += 1
        #             print 'Error precio. Contador', contador, ', error', error
        #             no_allow = ''
        #             try:
        #                 no_allow = driver.find_element_by_xpath("//span[@class='message message-no-available']").text
        #             except Exception as  error:
        #                 print 'No había mensaje', error
        #                 pass
        #
        #             print 'no_allow-->',no_allow
        #
        #             if no_allow:
        #                 print no_allow.split()[0]
        #                 if no_allow[0].split() == 'No':
        #                     print 'suma de día. Muy pronto reserva'
        #                     get_price = False
        #                     n_data += 1
        #                     break
        #                 elif no_allow.split()[0] == 'La':
        #                     print 'Suma día salida. Más estancia minima'
        #                     get_price =  False
        #                     n_data_out += 1
        #                     break
        #
        #             if contador_price > 5:
        #                 contador_price = True
        #                 price = ''
        #                 min_stay = ''
        #             time.sleep(1)
        #             pass