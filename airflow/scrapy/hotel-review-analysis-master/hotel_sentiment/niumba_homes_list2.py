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
only_apartments_files='only_apartments_homes_description.csv'
CSVdir='/usr/local/airflow/scrapy-hotels/hotel-review-analysis-master/classify_elastic'
only_apartments_files = os.path.join(CSVdir, only_apartments_files)

#Arrays will be save the dada
samples_homes=[]
samples_homes.append(["id_only_apartments", "title", "numberReviews", "mainBubbles", "bathrooms", "capacity", "beds", "m2", "lng", "lat"])


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


res = es.search(index="index_list_homes_only_apartments", doc_type="unstructured", body=doc,scroll='1m')




urls = []
ids = []
#create list of URLs
for hit in res['hits']['hits']:
    urls=urls + [hit["_source"]["url"]]
    ids=ids + [hit["_source"]["id_only_apartments"]]
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
                    print "url ---->", driver.current_url
                    print 'id ---->',ids[i]


                    numberReviews = driver.find_elements_by_xpath("//div[@class='amenity-title']")[0].text
                    mainBubbles = driver.find_elements_by_xpath("//div[@class='amenity-value']")[0].text




                    attributes_names={
                        "icon-people":'',
                        'as-icon':'',
                        'icon-bedroom':'',
                        'icon-bathroom2':'',

                    }

                    groups_attributes = driver.find_elements_by_xpath("//div[@class='row text-center facilities-icons-list']/div")

                    for group in groups_attributes:
                        attributes = driver.find_elements_by_xpath("//div[@class='row']")
                        attributes_title = attributes[0]
                        attributes_value = attributes[1]

                        for i in range(0,len(attributes_title)):
                            title = attributes_title[i].get_attribute("class") if len(attributes_title[i].get_attribute("class").split()) is 1 \
                                else attributes_title[i].get_attribute("class").split()[1]
                            attributes_names[title] = attributes_value[i].find_element_by_xpath("//span").text


                            # "/div[@class='row']/div[@class='col-xs-3']")
                    bathrooms = attributes["icon-bathroom2"]
                    capacity = attributes["icon-people"]
                    beds = attributes["icon-bedroom"]
                    m2 = attributes["as-icon"]


                    title = driver.find_element_by_xpath("//meta[@itemprop='name']").text
                    coordinates = driver.find_element_by_xpath("//meta[@name='geo.position']").get_attribute('content').split(';')
                    lng = coordinates[0]
                    lat = coordinates[1]
                    print "numberReviews ---->", numberReviews
                    print "mainBubbles ---->", mainBubbles
                    print "m2 ---->", m2
                    print "capacity ---->", capacity
                    print "bathrooms ---->", bathrooms
                    print "beds ---->", beds
                    print 'lng ---->',lng
                    print 'lat ---->',lat

                    arrive = driver.find_element_by_xpath("//input[@placeholder='Llegada']")
                    arrive.click()
                    select_date = False
                    date_arrive = 0
                    while select_date is False:
                        try:
                            date_selected = driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']").find_elements_by_xpath('.//a')
                            date_selected.click()
                            date_arrive = int(date_selected.text)
                            select_date = True
                        except:
                            next_month = driver.find_element_by_xpath("//class[contains(@class='ui-datepicker-header')]").\
                                find_elements_by_xpath(".//a[contains(@class='ui-datepicker-next')]")


                    date_selected = driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']").find_elements_by_xpath('.//a')
                    for date in date_selected:
                        if int(date.text) == (date_arrive + 1):
                            date.click()
                            time.sleep(1)

                    #Price
                    load = False
                    contador_price = 0
                    while load is False:
                        try:
                            load = True
                            price = driver.find_element_by_xpath("//span[@itemprop='price']").text

                        except Exception as error:
                            load = False
                            print 'Error precio. Contador', contador, ', error', error
                            contador_price += 1
                            if contador_price > 5:
                                contador_price = 0
                                load = True
                                price = ''
                            time.sleep(1)
                            pass


                    samples_homes.append([ids[i], title, numberReviews, mainBubbles,bathrooms,capacity, beds, m2, lng, lat])
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
    print('Write ' + str(index_homes-1) + ' only_apartments homes description')


    #It writes the comments and posts files
    with open(only_apartments_files, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(samples_homes)