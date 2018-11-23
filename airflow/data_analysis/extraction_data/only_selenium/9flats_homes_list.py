# -*- coding: UTF-8 -*-

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os
import unicodecsv as csv
from elasticsearch import Elasticsearch
sys.path.append('../')
from urls import Flats9URLs
from utils import clear_cache

PLACE =  sys.argv[1]

driver = webdriver.Chrome()


exceptionErrorItem=False
es = Elasticsearch(
    [
        'elastic:vituinproject@elasticsearch:9200/',
    ]
)

#Fields where data will be write
flats9_files='9flats_homes_list_'+PLACE+'.csv'
CSVdir='/usr/local/airflow/data_analysis/classify_elastic/unstructured_data/data_files'
flats9_files = os.path.join(CSVdir, flats9_files)

#Arrays will be save the data
samples_homes=[]
samples_homes.append(["id_flat9", "title", "url","price", "type_residence", "web", "stars", "numberReviews"])


index_homes=1





contador = 0
load_all = False
finish = False
urls = Flats9URLs(PLACE)
n_url = 0
for url in urls:
    #It could be that no load at first
    while load_all is False and contador <= 5:
        load_all = True
        try:
            time.sleep(1)
            driver.get(url)
            next = True
            i=0
            while next == True:
                i += 1
                load = False
                while load is False and finish is False:
                    load = True
                    try:
                        last_page = driver.find_element_by_xpath("//span[@class='search__pagination__info']").text
                        print 'Page', last_page
                        print '-----Pagina '+str(i)+'------'
                        homes = driver.find_elements_by_xpath("//div[@class = 'search__results__i row']/div")
                        #print links
                        samples_homes_tmp = []
                        for home in homes:
                            print 'home-->', home.get_attribute('id')
                            if home.get_attribute('id')[0:5] == 'place':
                                # place = home.find_elements_by_xpath(".//div[@class='breadCrumb']/div/a")[2].text
                                # print "place-->",place
                                # if place != PLACE:
                                #     contador = 6
                                #     finish = True
                                #     next = False
                                #     break
                                id_flat9 = home.get_attribute('id')[6:]
                                print 'id_flat9-->',id_flat9
                                title = home.find_element_by_xpath(".//h5[@class = 'card-title']").text
                                url=home.find_elements_by_xpath(".//a")[0].get_attribute('href')
                                # attributes=home.find_elements_by_xpath(".//ul[@class='accomType mobileHidden']/li")
                                type_residence= home.find_element_by_xpath(".//h6[@class = 'card-text']").text
                                try:
                                    type_residence = type_residence[:type_residence.find('Puerto')].strip()
                                except:
                                    pass
                                try:
                                    web = home.find_element_by_xpath(".//div[@class = 'provider mt-2']").text
                                except:
                                    web = ''
                                try:
                                    stars = home.find_element_by_xpath(".//span[contains(@class , 'search__place__content__stars')]").text
                                except:
                                    stars = ''
                                try:
                                    numberReviews = home.find_element_by_xpath(".//span[@class = 'search__place__content__reviews']").text
                                except:
                                    numberReviews = ''
                                price = home.find_element_by_xpath(".//span[@class = 'money']").text[1:]

                                print 'id=',id_flat9,', url=', url,', title=', title, ', type_residence=', type_residence, ', price', price, ', web', web, ', stars', stars, ', numberReviews', numberReviews,
                                samples_homes_tmp.append([id_flat9, title, url, price, type_residence, web, stars, numberReviews])
                                index_homes+=1
                        print '-----Fin página '+str(i)+'------'
                        contador = 0
                        samples_homes.extend(samples_homes_tmp)
                    except Exception as error:
                        load = False
                        print 'Error elementos de la pagina. Contador', contador, ', error', error
                        contador += 1
                        if contador > 5:
                            load = True
                            finish = True
                            contador = 0
                            next = False
                        time.sleep(1)
                        pass
                load = False
                while load is False and finish is False:
                    try:
                        load = True
                        next_page = driver.find_element_by_xpath("//a[contains(@class,'pagination__item__link_next')]").get_attribute('href')
                        next_page_url = 'https://www.9flats.com'+next_page
                        print next_page
                        driver.get(next_page)
                        time.sleep(1)

                    except Exception as error:
                        load = False
                        print 'Error cargar siguiente. Contador', contador, ', error', error
                        contador += 1
                        if contador > 5:
                            contador = 0
                            load = True
                            finish = True
                            next = False
                        time.sleep(1)
                        pass
                load = False
                while load is False and finish is False:
                    try:
                        load = True
                        current_page = driver.find_element_by_xpath("//span[@class='search__pagination__info']").text
                        print 'Current',current_page, ', last', last_page
                        contador = 0
                        if last_page!=current_page:
                            pass
                        else:
                            print 'Fin'
                            next = False

                    except Exception as error:
                        load = False
                        print 'Error ver pagina actual. Contador', contador, ', error', error
                        contador += 1
                        if contador > 5:
                            load = True
                            finish = True
                            next = False
                            contador = 0
                        time.sleep(1)
                        pass

        except Exception as error:
            print 'No Load', contador, ', error', error
            load_all = False
            contador += 1

            pass
        if contador > 5:
            load_all = True
        contador = 0

    if n_url < len(urls):
        print 'Siguiente url'
        n_url += 1
        contador = 0
        load_all = False
        finish = False

print('--------------')
print(samples_homes[0])
print('Write ' + str(index_homes-1) + ' flat9 homes')


#It writes the comments and posts files
with open(flats9_files, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(samples_homes)