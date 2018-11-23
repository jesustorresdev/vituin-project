# -*- coding: UTF-8 -*-

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os
import unicodecsv as csv
from elasticsearch import Elasticsearch
from selenium.webdriver.chrome.options import Options
import ast
sys.path.append('../')
from utils import clear_cache

PLACE =  sys.argv[1]

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
rentalia_files='rentalia_homes_description_'+PLACE+'.csv'
CSVdir='/usr/local/airflow/data_analysis/classify_elastic/unstructured_data/data_files'
rentalia_files = os.path.join(CSVdir, rentalia_files)

#Arrays will be save the dada
samples_homes=[]
samples_homes.append(["id_rentalia", "type_residence", "numberReviews", "mainBubbles", "min_stay", "lng", "lat"])


index_homes=1

#SearchAllEstablishments
doc = {
    'size' : 10000,
    "query": {
        "match_phrase": {
            "place": PLACE
        }
    },
    'sort': [
        {"_id": "asc"}
    ]
}


res = es.search(index="index_list_homes_rentalia", doc_type="unstructured", body=doc,scroll='1m')




urls = []
ids = []
#create list of URLs
for hit in res['hits']['hits']:
    urls=urls + [hit["_source"]["url"]]
    ids=ids + [hit["_source"]["id_rentalia"]]
contador = 0
number_success = 0
contador_all = 0

for n in range(0,len(urls)):
    driver.get(urls[n])
    print 'n-->', n
    load_all = False
    #It could be that no load at first
    while load_all is False:
        try:
            print '----Alojamiento numero '+str(number_success)+'----'
            driver.get(urls[n])
            time.sleep(.5)
            load_all = True
            not_page = False
            try:
                not_page = True if driver.find_element_by_xpath("//p[@class='alertText']") else False
            except:
                not_page = False
                pass
            #If home exits
            if not_page is False:
                load = False
                while load is False:
                    try:
                        print urls[n]
                        load = True
                        mainBubbles = driver.find_element_by_xpath("//div[contains(@class,'stars')]/div[@class='percentage']").get_attribute('style')
                        mainBubbles = float(mainBubbles[mainBubbles.find(':')+1:-2]) / (2 * 10)
                        numberReviews = driver.find_elements_by_xpath("//div[contains(@class,'valuations')]/span")[0].text.split()[0]

                        type_residence = driver.find_element_by_xpath("//div[contains(@class,'headercharacteristics')]/div").text.split()[-1]

                        controller =  driver.find_element_by_xpath("//div[@ng-controller='HouseController']").get_attribute('ng-init')
                        pos_longitude = controller.find('"longitude"')
                        controller_coordinates_dict =controller[controller.find('{') : controller[pos_longitude:].find('}')+pos_longitude+1]
                        coor =  controller_coordinates_dict[controller_coordinates_dict.find('"latitude"'):]
                        lat = coor[coor.find(':')+2:coor.find(',')-1]
                        lng = coor[coor.find('"longitude"')+len("longitude")+4:-2]

                        pos_min_stay = controller.rfind('"nights_min":')-1
                        min_stay = controller[pos_min_stay+1:]
                        min_stay = min_stay[min_stay.find(':')+1:min_stay.find(',')]

                        print "url ---->", driver.current_url
                        print 'id ---->',ids[n]
                        print 'latitude-->',lat
                        print 'latitude-->',lat
                        print 'longitude-->',lng
                        print 'rating-->',mainBubbles
                        print "numberReviews ---->", numberReviews
                        print "min_stay ---->", min_stay



                        samples_homes.append([ids[n], type_residence, numberReviews, mainBubbles, min_stay, lng, lat])
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

clear_cache(driver)
driver.close()
#chromedriver dont stop itself
os.system("pkill -f chromedriver")

print('--------------')
print(samples_homes[0])
print('Write ' + str(index_homes-1) + ' rentalia homes description')


#It writes the comments and posts files
with open(rentalia_files, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(samples_homes)