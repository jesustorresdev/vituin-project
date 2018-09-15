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
airbnb_files='airbnb_homes_descriptionFuereventura.csv'
CSVdir='/usr/local/airflow/scrapy-hotels/hotel-review-analysis-master/classify_elastic'
airbnb_files = os.path.join(CSVdir, airbnb_files)

#Arrays will be save the dada
samples_homes=[]
samples_homes.append(["id_airbnb", "type_residence", "price", "details_str", "numberReviews", "mainBubbles", "accuracy", "communication", "cleanliness", "location", "check_in", "value", "min_stay"])


index_homes=1

#SearchAllEstablishments
doc = {
    'size' : 10000,
    "query": {
        "match_phrase": {
            "place": "Fuerteventura"
        }
    },
    'sort': [
        {"_id": "asc"}
    ]
}


res = es.search(index="index_list_homes_airbnb", doc_type="unstructured", body=doc,scroll='1m')




urls = []
ids = []
#create list of URLs
for hit in res['hits']['hits']:
    urls=urls + [hit["_source"]["url"]]
    ids=ids + [hit["_source"]["id_airbnb"]]
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

        #If home exits
        if driver.current_url != 'https://www.airbnb.es/':
            try:
                print "url ---->", driver.current_url
                print 'id ---->',ids[i]
                type_residence = driver.find_element_by_xpath("//span[@class='_1hh2h7tb']/span").text
                details = driver.find_elements_by_xpath("//div[@class='_qtix31']/div[@class='_1thk0tsb']/span[@class='_fgdupie']")  #More than one
                price = driver.find_element_by_xpath("//span[@class='_doc79r']").text
                print "Tipo de residencia ---->",type_residence
                print "Precio ---->", price
                j=0
                details_str = ''
                for detail in details:
                    j+=1
                    details_str = details_str + detail.text + ', '
                    print "Detalle", j, "---->", detail.text
                details_str = details_str[:-2]
                print "Detalles todos:",details_str

                try:
                    numberReviews = driver.find_element_by_xpath("//span[@class='_492uxj4']/h2/span").text
                    mainBubbles = driver.find_element_by_xpath("//div[@itemprop='ratingValue']").get_attribute('content')
                    print "Numero de reviews ---->",numberReviews
                    print "Puntuación media ---->",mainBubbles
                    secundaryBubbles = driver.find_elements_by_xpath("//div[@class='_2h22gn']/div[@class='_en5l15m']")

                    valuations = []
                    names = []
                    for column in secundaryBubbles:
                        element = column.find_elements_by_xpath(".//div/div")
                        bubblesNames = column.find_elements_by_xpath(".//span[@class='_fgdupie']")
                        bubblesNumber = column.find_elements_by_xpath(".//div[@class='_1iu38l3']/span")
                        #Type of bubble
                        for name in bubblesNames:
                            names.append(name.text)


                        for valuation in bubblesNumber:
                            valuations.append(valuation.get_attribute('aria-label'))
                    m = 0
                    for valuation in valuations:
                        print names[m], ' tiene', valuation
                        m += 1

                    accuracy = valuations[0]
                    communication = valuations[1]
                    cleanliness = valuations[2]
                    location = valuations[3]
                    check_in = valuations[4]
                    value = valuations[5]

                except:

                    numberReviews = ''
                    mainBubbles = ''
                    accuracy = ''
                    cleanliness = ''
                    communication = ''
                    location = ''
                    check_in = ''
                    value = ''

                # No funciona
                # cancelations = driver.find_element_by_xpath("//div[@class='_ncwphzu']/span").text
                #
                # print 'cancelaciones---> ',cancelations

                # time.sleep(.1)
                min_stay = driver.find_elements_by_xpath("//div[@class='_q401y8m']/span")[0]
                min_stay = min_stay.find_element_by_xpath(".//span/strong").text
                print 'estancia minima---> ',min_stay
                #
                # driver.find_elements_by_xpath("//div[@class='_1n57hdr7']/button")[1].click()
                # time.sleep(.1)
                # headServices = driver.find_elements_by_xpath("//div[@class='_wpwi48']/section/div")
                # services = ''
                #
                # for service in headServices:
                #
                #     servicesName = service.find_element_by_xpath(".//h2[@class='_tpbrp']/div").text
                #     print 'Group name--', servicesName
                #     services = services + servicesName.upper() + ': '
                #     servicesList = service.find_elements_by_xpath(".//div[@class='_2930ex']")
                #     for serv in servicesList:
                #         if servicesName.text != "No incluidos":
                #             sName = serv.find_element_by_xpath(".//div[@class='_ncwphzu']").text
                #             print 'Elemento--', sName
                #             services = services + sName
                #             try:
                #                 sDetails = serv.find_element_by_xpath(".//div[@class='_1nhodd4u']").text
                #                 print 'Detalles del elemento--',sDetails
                #                 services = services + ' (' + sDetails + ')'
                #             except:
                #                 pass
                #             services = services +', '
                #             print'---'
                #         services = services[:-1]
                #         services = services + '. '


                samples_homes.append([ids[i], type_residence, price, details_str, numberReviews, mainBubbles, accuracy, communication, cleanliness, location, check_in, value, min_stay])
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
    print('Write ' + str(index_homes-1) + ' airbnb homes description')


    #It writes the comments and posts files
    with open(airbnb_files, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(samples_homes)