# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os
import unicodecsv as csv
from elasticsearch import Elasticsearch

#NO ACABADO
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
driver = webdriver.Chrome()


exceptionErrorItem=False
es = Elasticsearch(
    [
        'elastic:vituinproject@elasticsearch:9200/',
    ]
)


#Fields where data will be write
flats9_files='9flats_homes_description.csv'
CSVdir='/usr/local/airflow/data_analysis/classify_elastic/unstructured_data/data_files'
flats9_files = os.path.join(CSVdir, flats9_files)

#Arrays will be save the dada
samples_homes=[]
samples_homes.append(["id_9flats", "type_residence", "price", "numberReviews", "mainBubbles", "capacity", "rooms", "bathrooms", "m2","min_stay"])


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


res = es.search(index="index_list_homes_9flats", doc_type="unstructured", body=doc,scroll='1m')




urls = []
ids = []
#create list of URLs
for hit in res['hits']['hits']:
    urls=urls + [hit["_source"]["url"]]
    ids=ids + [hit["_source"]["id_9flats"]]
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
            element_error = driver.find_element_by_xpath("//div[@class='error-container']")
        except:
            not_page = True
            pass
    #If home exits
        if not_page is not True:
            try:
                print "url ---->", driver.current_url
                print 'id ---->',ids[i]
                type_residence = driver.find_elements_by_xpath("//div[@class='amenity-title']")[0].text
                m2 = driver.find_elements_by_xpath("//div[@class='amenity-value']")[0].text
                capacity = driver.find_elements_by_xpath("//div[@class='amenity-value']")[1].text
                rooms = driver.find_elements_by_xpath("//div[@class='amenity-value']")[2].text
                bathrooms = driver.find_elements_by_xpath("//div[@class='amenity-value']")[3].text
                min_stay = driver.find_elements_by_xpath("//div[@class='amenity-value']")[4].text
                price = driver.find_elements_by_xpath("//div[@class='price-range-container']/div/div[@class='price-large']")[0].text
                mainBubbles = driver.find_elements_by_xpath("//div[@class='large-superlative-summary']/div/span")[1].text
                mainBubbles = mainBubbles[:mainBubbles.find('/')]
                numberReviews = driver.find_element_by_xpath("//div[@class='large-superlative-summary']/div/span[@class='review-count']").text
                numberReviews = numberReviews[:numberReviews.find('c')].strip()

                print "Tipo de residencia ---->",type_residence
                print "m2 ---->",m2
                print "capacity ---->",capacity
                print "rooms ---->",rooms
                print "bathrooms ---->",bathrooms
                print "min_stay ---->",min_stay
                print "numberReviews ---->", numberReviews
                print "mainBubbles ---->", mainBubbles
                print "Precio ---->", price


                samples_homes.append([ids[i], type_residence, price, numberReviews, mainBubbles, capacity, rooms, bathrooms, m2, min_stay])
                index_homes+=1
                contador = 0
                number_success+=1
                print 'iteracion--->',number_success
            except:
                print 'No Load'
                time.sleep(1)
                contador += 1
                print "contador sube", contador
                print 'eee'
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
    print('Write ' + str(index_homes-1) + ' 9flats homes description')


    #It writes the comments and posts files
    with open(flats9_files, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(samples_homes)