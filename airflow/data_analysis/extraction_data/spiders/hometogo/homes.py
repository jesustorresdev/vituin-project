# # -*- coding: UTF-8 -*-
#
# """Extracción de viviendas en Airbnb
# """
#
# __authors__ = 'Sergio Díaz, Jesús Torres'
# __organization__ = 'Universidad de La Laguna'
# __licensed__ = 'UNLICENSED'
# __contact__ = "jmtorres@ull.edu.es, sdiazgon@ull.edu.es"
# # __copyright__ = f"Copyright 2017-2018 {__organization__}"
#
# from extraction_data.items import List
# # from scrapy.mail import MailSender
# from scrapy.exceptions import CloseSpider
# # from elasticsearch import Elasticsearch
# import scrapy
# import sys
# import time, os
# import unicodecsv as csv
# # from elasticsearch import Elasticsearch
# from extraction_data.urls import AirbnbURLs
# # from extraction_data.utils import clear_cache
# from extraction_data.selenium_spider import SeleniumSpider
# from extraction_data.utils import get_coordinates
#
#
# def get_attribute(element):
#     type = ['capacity','rooms','bathrooms','beds']
#     attribute = {
#         'huesped':type[0],
#         'huéspedes'.decode('UTF-8'):type[0],
#         'dormitorio':type[1],
#         'dormitorios':type[1],
#         'baño'.decode('UTF-8'):type[2],
#         'baños'.decode('UTF-8'):type[2],
#         'cama':type[3],
#         'camas':type[3],
#     }
#     return attribute[element]
#
#
#
# #TODO use loaders
# class AibrnbSpider(SeleniumSpider):
#     name = "airbnb_listHomes"
#     place = "Puerto de la Cruz"
#     #start_urls = [
#     #    "https://www.tripadvisor.co.uk/Hotels-g187479-Tenerife_Canary_Islands-Hotels.html"
#     #]
#     # start_urls = TripAdvisorZonePuertoDeLaCruzURLs()
#     start_urls = AirbnbURLs(place)
#     # start_urls = [
#     #     'https://www.airbnb.es/rooms/31411560?location=Puerto%20de%20la%20Cruz%2C%20Santa%20Cruz%20de%20Tenerife'
#     #     'https://www.airbnb.es/rooms/23499128?location=Puerto%20de%20la%20Cruz%2C%20Santa%20Cruz%20de%20Tenerife',
#     #     'https://www.airbnb.es/rooms/19048187?location=Puerto%20de%20la%20Cruz%2C%20Santa%20Cruz%20de%20Tenerife',
#     #     'https://www.airbnb.es/rooms/23739662?location=Puerto%20de%20la%20Cruz%2C%20Santa%20Cruz%20de%20Tenerife',
#     #
#     # ]
#     # start_urls = ['https://www.airbnb.es/rooms/31411560?location=Puerto%20de%20la%20Cruz%2C%20Santa%20Cruz%20de%20Tenerife']
#     print 'INICIO'
#
#     def parse(self, response):
#         print 'INICIO'
#         print response.url
#         selenium = SeleniumSpider(self)
#         selenium.create_sesion()
#         selenium.set_url(response.url)
#         n = 0
#         i = 0
#         pages = True
#         while pages:
#             i += 1
#             last_page = selenium.get_page("//div[@class='_1bdke5s']", last = True)
#             print 'Last_Page', last_page
#             links = selenium.find_element_by_xpath("//a[contains(@class, '_1ol0z3h')]",multiple=True, stop_if_error=True)
#             print links
#             for link in links:
#                 link = selenium.get_attribute(link,'href')
#                 id_airbnb = link[link.find('rooms')+6:link.find('?')]
#                 n+=1
#                 url = response.urljoin(link)
#                 print ''
#                 print(n, ' id=', id_airbnb, ', url=', url)
#                 print ''
#                 request = scrapy.Request(url, callback=self.parse_home)
#                 repeat=''
#                 # request.meta['id_airbnb']=id_airbnb
#                 # for hit in res['hits']['hits']:
#                 #     repeat = hit["_source"]
#
#                 request.meta['id_airbnb']=id_airbnb
#
#                 #If the hotel doesnt have in the list, it will extract its data
#                 if repeat == '':
#                     yield request
#
#
#             url_new_page = selenium.get_page("//a[@class='_1ip5u88']", url = True)
#             print url_new_page
#             last_page = selenium.get_page("//div[@class='_1bdke5s']")
#             current_page = selenium.get_page("//div[@class='_e602arm']")
#
#             print 'Current',current_page, ', last', last_page
#             print 'Current',type(current_page), ', last', type(last_page)
#             if last_page>current_page:
#                 selenium.set_url(url_new_page)
#             else:
#                 pages = False
#                 print 'Fin'
#
#
#             print '-----Fin página '+str(i)+' ------'
#             print '-----Fin página '+str(i)+' ------'
#             print '-----Fin página '+str(i)+' ------'
#         selenium.close_browser()
#         selenium.kill_chromedriver()
#
#
#
#
#
#
#     def parse_home(self, response):
#         item = List
#         name = response.xpath("//meta[@property='og:title']/@content")[0].extract()
#         description = response.xpath("//meta[@name='description']/@content")[0].extract()
#
#
#         selenium = SeleniumSpider(self)
#         selenium.create_sesion(width=330,height=350)
#         selenium.set_url(response.url)
#         url_coordinates = selenium.find_element_by_xpath("//div[@class='_59m2yxn']/img", get_attr='src')
#         (lat, lng) = get_coordinates(url_coordinates)
#         attributes = selenium.find_element_by_xpath("//div[@class='_2h22gn']/div[@class='_iq8x9is']", multiple=True)
#
#         list_attributes = {}
#         repeat_attributes = True
#
#         while repeat_attributes is True:
#             repeat_attributes = False
#             attributes = selenium.find_element_by_xpath("//div[@class='_2h22gn']/div[@class='_iq8x9is']/div/span[@class='_1p3joamp']", multiple=True)
#
#             if not attributes:
#                 attributes = selenium.find_element_by_xpath("//div[@class='_2h22gn']/div[@class='_iq8x9is']/div/div[@class='_qtix31']", multiple=True)
#                 if attributes:
#                     print('')
#                     print('SEGUNDO TIPO')
#                     print('')
#                     print(attributes)
#                 else:
#
#                     print('')
#                     print('TERCER TIPO')
#                     print('')
#                     print(attributes)
#                     selenium.close_browser()
#                     selenium = SeleniumSpider(self)
#                     selenium.create_sesion(width=330,height=350)
#                     selenium.set_url(response.url)
#                     repeat_attributes = True
#             else:
#                 print('')
#                 print('PRIMER TIPO')
#                 print('')
#                 print(attributes)
#
#         for element in attributes:
#             # print('')
#             # print('eeh, elementos-->', len(element.text.split(' ')))
#             # print(element.text.split(' '))
#             elements = element.text.split(' ')
#             list_attributes.update({get_attribute(elements[1]):elements[0][elements[0].find('\n')+1:]})
#             # print(element.text.split(' '))
#             # for el in element.text.split(' '):
#             #     print el[el.find('\n')+1:]
#
#
#         item['name'] = name
#         item['id_airbnb'] = response.meta['id_airbnb']
#         item['description'] = description
#         item['lat'] = lat
#         item['lng'] = lng
#         item['capacity'] = list_attributes['capacity']
#         item['rooms'] = list_attributes['rooms']
#         item['bathrooms'] = list_attributes['bathrooms']
#         item['beds'] = list_attributes['beds']
#         # item['min_stay'] = min_stay
#         # item['price'] = price
#
#
#
#         selenium.close_browser()
#         # selenium.kill_chromedriver()
#         # selenium.kill_chrome()
#
#         return item
