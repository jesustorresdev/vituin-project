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
atraveo_files='atraveo_homes_list.csv'
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
while load_all is False and contador <= 5:
    load_all = True
    try:
        url = 'https://www.atraveo.es/puerto_de_la_cruz#eyJkYXRhIjp7ImNvdW50cnlJZCI6IkVTIiwicmVnaW9uSWQiOjE3NSwic3ViUmVnaW9uSWQiOjg4MywiY2l0eUlkIjo5ODI3LCJhcnJpdmFsRGF0ZSI6MTUzODk5NjQwMCwiZHVyYXRpb24iOjcsIm1pblBlcnNvbnMiOjJ9LCJjb25maWciOnt9fQ=='
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
                    last_page = driver.find_element_by_xpath("//li[@class ='number current']").text
                    print 'Page', last_page
                    print '-----Pagina '+str(i)+'------'
                    homes = driver.find_elements_by_xpath("//ul[@class='resultlist arrivaldate']/li")
                    #print links
                    samples_homes_tmp = []
                    for home in homes:
                        print 'id-->', home.get_attribute('data-accommodation-id')
                        lng = home.get_attribute('data-lng')
                        lat = home.get_attribute('data-lat')
                        id_atraveo = home.get_attribute('data-accommodation-id')
                        name = home.find_element_by_xpath(".//h3[@class='resulthead']").text
                        url = home.find_element_by_xpath(".//div[@class='resultlinks']/a").get_attribute('href')
                        type_residence =  name[:name.find('para')]
                        price = home.find_element_by_xpath(".//div[@class='price']").text.split()[1]
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
                    next_page = driver.find_element_by_xpath("//a[@class='forward']")
                    next_page.click()
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




driver.close()
#chromedriver dont stop itself
os.system("pkill -f chromedriver")


print('--------------')
print(samples_homes[0])
print('Write ' + str(index_homes-1) + ' atraveo homes')


#It writes the comments and posts files
with open(atraveo_files, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(samples_homes)