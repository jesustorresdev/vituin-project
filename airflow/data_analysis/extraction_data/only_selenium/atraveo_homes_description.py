# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os
import unicodecsv as csv
from elasticsearch import Elasticsearch
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--window-size=1400,1000")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.set_window_size(1400,1000)

exceptionErrorItem=False
es = Elasticsearch(
    [
        'elastic:vituinproject@elasticsearch:9200/',
    ]
)



#Fields where data will be write
atraveo_files='atraveo_homes_description.csv'
CSVdir='/usr/local/airflow/data_analysis/classify_elastic/unstructured_data/data_files'
atraveo_files = os.path.join(CSVdir, atraveo_files)

#Arrays will be save the dada
samples_homes=[]
samples_homes.append(["id_atraveo", "description", "capacity", "rooms", "bathrooms", "m2","min_stay"])


index_homes=1

#SearchAllEstablishments
doc = {
    'size' : 10000,
    "query": {
        "match_phrase": {
            "place": "Puerto de la Cruz"
        }
    },
    'sort': [
        {"_id": "asc"}
    ]
}


res = es.search(index="index_list_homes_atraveo", doc_type="unstructured", body=doc,scroll='1m')



urls = []
ids = []
#create list of URLs
for hit in res['hits']['hits']:
    urls=urls + [hit["_source"]["url"]]
    ids=ids + [hit["_source"]["id_atraveo"]]
contador = 0
contador_all = 0
number_success = 0


for n in range(0,len(urls)):
    print 'n-->', n
    load_all = False
    #It could be that no load at first
    while load_all is False:
        try:
            print '----Alojamiento numero '+str(number_success)+'----'
            print urls[n]
            driver.get(urls[n])
            time.sleep(.5)
            load_all = True
            not_page = False
            try:
                try:
                    #if error
                    not_page = True if driver.find_element_by_xpath("//div[@class='pimcore_area_headline pimcore_area_content']/h1") == 'Alojamiento descatalogado'  else False
                except:
                    not_page = False

            except:
                not_page = False
                pass
            #If home exits
            if not_page is False:
                load = False
                while load is False:
                    try:
                        load = True

                        description = driver.find_element_by_xpath("//meta[@name='description']").get_attribute('content')
                        attributes = driver.find_element_by_xpath("//div[@class='featuresText']").text.split()

                        print "attributes-->", attributes
                        m2 = attributes[1]
                        rooms = attributes[3]
                        bathrooms = attributes[5]

                        try:
                            capacity = driver.find_elements_by_xpath("//div[@class='smalllabel']")[0].text.split()
                            if capacity[0] == 'máximo'.decode('UTF-8'):
                                capacity = capacity[1]
                            else:
                                capacity = ''
                        except:
                            capacity = ''
                        try:
                            min_stay = driver.find_element_by_xpath("//div[@class='minStayLegend']").text
                            print 'min_stay  texto-->',min_stay[:min_stay.find(',')]
                            print 'min_stay  texto-->',min_stay
                            if min_stay[:min_stay.find(',')] !='Por favor':
                                min_stay = min_stay[min_stay.find(':')+1:].strip()
                            else:
                                min_stay = ''
                        except:
                            print 'except min_stay  texto-->',min_stay
                            min_stay = ''

                        print "url ---->", driver.current_url
                        print 'id ---->',ids[n]
                        try:
                            print "m2 ---->",m2.split()[0]
                            m2 = m2.split()[0]
                        except:
                            print "m2 ---->",m2


                        print "description ---->",description
                        print "capacity ---->",capacity
                        print "rooms ---->",rooms
                        print "bathrooms ---->",bathrooms
                        print "min_stay ---->",min_stay
                        samples_homes.append([ids[n], description, capacity, rooms, bathrooms, m2, min_stay])
                        index_homes+=1
                        contador = 0
                        number_success+=1
                        print 'iteracion--->',number_success
                    except Exception as error:
                        print 'No Load,', error, "contador--->", contador
                        contador += 1
                        load = False
                        if contador >= 5:
                            load = True
                            print "BREAK"
                            pass
                        else:
                            driver.set_window_size(1400,1000)
                            time.sleep(1)
                            print 'pass'
                            load = False
                            pass
            else:
                print ids[n], 'eliminada. No existe oferta actualmente.'

        except Exception as error:
            print 'Error en general, ', error
            load_all = False
            contador += 1
            pass
        if contador >= 5:
            print "url ---->", driver.current_url
            print 'CONTADOR-->', contador
            load_all = True

    if contador >= 5:
        print "ERROR"
        break

driver.close()
#chromedriver dont stop itself
os.system("pkill -f chromedriver")

print('--------------')
print(samples_homes[0])
print('Write ' + str(index_homes-1) + ' atraveo homes description')


#It writes the comments and posts files
with open(atraveo_files, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(samples_homes)