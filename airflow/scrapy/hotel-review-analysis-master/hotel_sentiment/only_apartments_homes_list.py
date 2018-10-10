# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os
import unicodecsv as csv
from elasticsearch import Elasticsearch


driver = webdriver.Chrome()


exceptionErrorItem=False
es = Elasticsearch(
    [
        'elastic:vituinproject@elasticsearch:9200/',
    ]
)


#Fields where data will be write
only_apartments_files='only_apartments_homes_list.csv'
CSVdir='/usr/local/airflow/scrapy-hotels/hotel-review-analysis-master/classify_elastic/unstructured_data'
only_apartments_files = os.path.join(CSVdir, only_apartments_files)

#Arrays will be save the dada
samples_homes=[]
samples_homes.append(["id_only_apartments", "url", "type_residence", "place"])


index_homes=1





contador = 0
load_all = False
finish = False
#It could be that no load at first
while load_all is False and contador <= 5:
    load_all = True
    try:
        url = 'https://www.only-apartments.es/apartamentos-en-puerto-de-la-cruz.html'
        time.sleep(1)
        driver.get(url)
        next = True
        i=0
        while next == True:
            i += 1
            load = False
            print '-----Pagina '+str(i)+'------'
            while load is False and finish is False:
                load = True
                try:
                    last_page = driver.find_element_by_xpath("//ul[contains(@class,'pagination')]/li[@class='active']").text
                    print 'Page', last_page
                    homes = driver.find_elements_by_xpath("//div[contains(@class, 'row-full')]")
                    #print links
                    samples_homes_tmp = []
                    for home in homes:
                        print home.get_attribute('data-id')
                        attributes =home.find_element_by_xpath(".//a[contains(@itemprop, 'url')]")
                        url=attributes.get_attribute('href')
                        name = attributes.find_element_by_xpath(".//strong").text
                        id_only_apartments = home.get_attribute('data-id')
                        place_and_type = home.find_elements_by_xpath(".//h6[@class='location ellipsis']/span")
                        type_residence = place_and_type[0].text
                        place = place_and_type[1].text
                        print 'id=',id_only_apartments,', url=', url,', type_residence=', type_residence, ', place', place
                        samples_homes_tmp.append([id_only_apartments, url, type_residence, place])
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
                        finish = False
                        contador = 0
                        next = False
                    time.sleep(1)
                    pass
            load = False
            while load is False and finish is False:
                try:
                    load = True
                    next_page = driver.find_elements_by_xpath("//ul[contains(@class,'pagination')]/li")[-1].find_element_by_xpath('.//button').get_attribute('data-href')
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
                    current_page = driver.find_element_by_xpath("//ul[contains(@class,'pagination')]/li[@class='active']").text
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




driver.close()
#chromedriver dont stop itself
os.system("pkill -f chromedriver")


print('--------------')
print(samples_homes[0])
print('Write ' + str(index_homes-1) + ' only_apartments homes')


#It writes the comments and posts files
with open(only_apartments_files, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(samples_homes)