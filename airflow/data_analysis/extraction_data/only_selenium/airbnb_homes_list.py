# -*- coding: UTF-8 -*-

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os
import unicodecsv as csv
from elasticsearch import Elasticsearch
sys.path.append('../')
from urls import AirbnbURLs
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
airbnb_files='airbnb_homes_list_'+PLACE+'1.csv'
CSVdir='/usr/local/airflow/data_analysis/classify_elastic/unstructured_data/data_files'
airbnb_files = os.path.join(CSVdir, airbnb_files)

#Arrays will be save the dada
samples_homes=[]
samples_homes.append(["id_airbnb", "title", "url"])


index_homes=1

contador = 0
load_all = False
finish = False

#It could be that no load at first
urls = AirbnbURLs(PLACE)
n_url = 0
for url in urls:
    while load_all is False and contador <= 5:
        load_all = True
        try:
            driver.get(url)
            time.sleep(1)
            next = True
            i=0
            while next == True:
                i += 1
                print 'next-->', i
                load = False
                while load is False and finish is False:
                    load = True
                    try:
                        try:
                            last_page = driver.find_elements_by_xpath("//div[@class='_1bdke5s']")[-1]
                            last_page= int(last_page.text) - 1 #It starts in 0
                        except:
                            last_page = 1
                            pass
                        print 'Last_Page', last_page
                        print '-----Pagina '+str(i)+'------'
                        links = driver.find_elements_by_xpath("//a[contains(@class, '_1ol0z3h')]")
                        print links
                        for link in links:
                            # name = link.find_element_by_xpath(".//div[@class='_1pkilk3o']/div").text
                            name=''
                            link=link.get_attribute('href')
                            id_airbnb = link[link.find('rooms')+6:link.find('?')]
                            print 'nombre=',name,', id=', id_airbnb
                            samples_homes.append([id_airbnb, link])
                            index_homes+=1
                        print '-----Fin página '+str(i)+'------'
                    except Exception as error:
                        load = False
                        print 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno)
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
                    load = True
                    try:
                        new_page = driver.find_elements_by_xpath("//a[@class='_1ip5u88']")#.get_attribute('href')
                        url_new_page = new_page[-1].get_attribute('href')
                        print url_new_page
                        current_page = int(driver.find_element_by_xpath("//div[@class='_e602arm']").text) -1

                        print 'Current',current_page, ', last', last_page
                        print 'Current',type(current_page), ', last', type(last_page)
                        if last_page>current_page:
                            driver.get(url_new_page)

                            time.sleep(0.5)
                        else:
                            print 'Fin'
                            next = False

                    except Exception as error:
                        load = False
                        print 'Error cargar siguiente. Contador', contador, ', error', error
                        print 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno)
                        contador += 1
                        if contador > 5:
                            contador = 0
                            load = True
                            finish = True
                            next = False
                        time.sleep(1)
                        pass


        except Exception as error:
            print 'No Load', contador, ', error', error
            load_all = False
            contador += 1

    if n_url < len(urls):
        print 'Siguiente url'
        n_url += 1
        contador = 0
        load_all = False
        finish = False

clear_cache(driver)
driver.close()
#chromedriver dont stop itself
os.system("pkill -f chromedriver")


print('--------------')
print(samples_homes[0])
print('Write ' + str(index_homes-1) + ' airbnb homes')


#It writes the comments and posts files
with open(airbnb_files, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(samples_homes)