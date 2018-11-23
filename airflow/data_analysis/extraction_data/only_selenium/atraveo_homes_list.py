# -*- coding: UTF-8 -*-

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os
import unicodecsv as csv
from elasticsearch import Elasticsearch

sys.path.append('../')
from urls import AtraveoURLs
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
atraveo_files='atraveo_homes_list_'+PLACE+'.csv'
CSVdir='/usr/local/airflow/data_analysis/classify_elastic/unstructured_data/data_files'
atraveo_files = os.path.join(CSVdir, atraveo_files)

#Arrays will be save the dada
samples_homes=[]
samples_homes.append(["id_atraveo", "url","price", "type_residence","numberReviews", "mainBubbles", "lat", "lng"])


index_homes=1





contador = 0
load_all = False
finish = False
#It could be that no load at first

urls = AtraveoURLs(PLACE)
n_url = 1
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
                load = False
                while load is False and finish is False:
                    load = True
                    try:
                        try:
                            last_page = driver.find_element_by_xpath("//li[@class ='number current']").text
                        except:
                            last_page = 1
                        print 'Page', last_page
                        print '-----Pagina '+str(i)+'------'
                        homes = driver.find_elements_by_xpath("//div[@id='searchResults']/ul/li")
                        samples_homes_tmp = []
                        for home in homes:
                            print 'id-->', home.get_attribute('data-accommodation-id')
                            lng = home.get_attribute('data-lng')
                            lat = home.get_attribute('data-lat')
                            id_atraveo = home.get_attribute('data-accommodation-id')
                            name = home.find_element_by_xpath(".//h3[@class='resulthead']").text
                            url = home.find_element_by_xpath(".//div[@class='resultlinks']/a").get_attribute('href')
                            type_residence =  name[:name.find('para')]
                            try:
                                price = home.find_element_by_xpath(".//div[@class='price']/span").text.split()[1]
                            except:
                                price = ''
                            try:
                                summary = home.find_element_by_xpath(".//span[@class='summary']").text
                                print 'sumary-->', summary
                                numberReviews = summary.split()[0]
                                mainBubbles = summary.split()[3]
                            except:
                                numberReviews = ''
                                mainBubbles = ''
                            print 'id=',id_atraveo,', url=', url,', name=', name, ', price=', price, 'type_residence=', type_residence,', numberReviews=', numberReviews,', mainBubbles=', mainBubbles, ', lat=', lat, ', lng=', lng
                            samples_homes_tmp.append([id_atraveo, url, price, type_residence, numberReviews, mainBubbles, lat, lng])
                            index_homes+=1
                        print '-----Fin página '+str(i)+'------'
                        contador = 0
                        samples_homes.extend(samples_homes_tmp)
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
                    try:
                        load = True
                        next_page = driver.find_element_by_xpath("//a[@class='forward']")
                        next_page.click()
                        time.sleep(1)

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
                load = False
                while load is False and finish is False:
                    try:
                        load = True
                        current_page = driver.find_element_by_xpath("//li[@class ='number current']").text
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

clear_cache(driver)
driver.close()
#chromedriver dont stop itself
os.system("pkill -f chromedriver")


print('--------------')
print(samples_homes[0])
print('Write ' + str(index_homes-1) + ' atraveo homes' + PLACE)


#It writes the comments and posts files
with open(atraveo_files, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(samples_homes)