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
hometogo_files='hometogo_homes_description.csv'
CSVdir='/usr/local/airflow/scrapy-hotels/hotel-review-analysis-master/classify_elastic'
hometogo_files = os.path.join(CSVdir, hometogo_files)

#Arrays will be save the dada
samples_homes=[]
samples_homes.append(["id_hometogo", "type_residence", "numberReviews", "mainBubbles"])


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


res = es.search(index="index_list_homes_hometogo", doc_type="unstructured", body=doc,scroll='1m')




urls = []
ids = []
#create list of URLs
for hit in res['hits']['hits']:
    urls=urls + [hit["_source"]["url_details"]]
    ids=ids + [hit["_id"]]
contador = 0
number_success = 0

for i in range(0,len(urls)):
    driver.get(urls[i])



    #if size windows is big
    # button = driver.find_element_by_xpath("//button[@id='MapToggleBar']")
    # button.click()
    time.sleep(.5)
    noLoad = True
    #It could be that no load at first
    while noLoad != False and contador <= 5:
        print 'ENTRO'
        noLoad = False
        not_page = False
        try:
            #if error
            element_error = driver.find_element_by_xpath("//header").text
        except:
            not_page = True
            pass
    #If home exits
        if not_page is not True and element_error is not '404':
            try:
                details = driver.find_elements_by_xpath("//div[@class='rental-sticky-sidebar']")[1]

                print "url ---->", driver.current_url
                id = details.find_element_by_xpath("//span[@class='fwb fz11 c-gray-dark fxg1']").text
                type_residence = details.find_element_by_xpath("//div[@class='fwb fz16 mb4']").text
                type_residence = type_residence.split()[0]
                capacity = details.find_elements_by_xpath("//div[@class='amenity-value']")[1].text
                mainBubbles = details.find_element_by_xpath("//div[@class='df wsnw h20 aic']/span").text
                numberReviews = driver.find_element_by_xpath("//span[@class='c-gray-dark wsnw']").text
                numberReviews = numberReviews.split()[0]

                print "id ---->",id
                print "Tipo de residencia ---->",type_residence
                print "capacity ---->",capacity
                print "numberReviews ---->", numberReviews
                print "mainBubbles ---->", mainBubbles


                samples_homes.append([id, type_residence, numberReviews, mainBubbles, capacity])
                index_homes+=1
                contador = 0
                number_success+=1
                print 'iteracion--->',number_success
            except:
                print 'No Load'
                time.sleep(1)
                contador += 1
                print "contador sube", contador
                if contador >= 5:
                    noLoad = False
                    print "BREAK"
                    break
                else:
                    print 'pass'
                    noLoad = True
                    pass
        else:
            print ids[i], 'eliminada. No existe oferta actualmente.'
    if contador >= 5:
        noLoad = False
        print "BREAK"
        break

error = False
if contador >= 5:
    print "ERROR"
    error = True

driver.close()
#chromedriver dont stop itself
os.system("pkill -f chromedriver")

if error == False or number_success > 10:
    print('--------------')
    print(samples_homes[0])
    print('Write ' + str(index_homes-1) + ' hometogo homes description')


    #It writes the comments and posts files
    with open(hometogo_files, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(samples_homes)