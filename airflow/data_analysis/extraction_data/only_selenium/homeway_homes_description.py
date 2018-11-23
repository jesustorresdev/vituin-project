# -*- coding: UTF-8 -*-

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os
import unicodecsv as csv
from elasticsearch import Elasticsearch
from selenium.webdriver.chrome.options import Options
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
homeway_files='homeway_homes_description_'+PLACE+'.csv'
CSVdir='/usr/local/airflow/data_analysis/classify_elastic/unstructured_data/data_files'
homeway_files = os.path.join(CSVdir, homeway_files)

#Arrays will be save the dada
samples_homes=[]
samples_homes.append(["id_homeway", "type_residence", "price", "numberReviews", "mainBubbles", "capacity", "rooms", "bathrooms", "m2","min_stay", "lng", "lat"])


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


res = es.search(index="index_list_homes_homeway", doc_type="unstructured", body=doc,scroll='1m')



urls = []
ids = []
#create list of URLs
for hit in res['hits']['hits']:
    urls=urls + [hit["_source"]["url"]]
    ids=ids + [hit["_source"]["id_homeway"]]
contador = 0
contador_all = 0
number_success = 429


for n in range(0,len(urls)):
    if n > 428:
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
                        not_page = True if driver.find_element_by_xpath("//div[@class='error-container']") else False
                    except:
                        not_page = True if driver.find_element_by_xpath("//div[@class='error-container']")\
                                                    .find_element_by_xpath(".//h2") == \
                                                'La página que usted busca ya no existe.' else False

                except:
                    not_page = False
                    pass
                #If home exits
                if not_page is False:
                    load = False
                    while load is False:
                        try:
                            load = True
                            try:
                                price = driver.find_element_by_xpath("//meta[@property='og:price:amount']").get_attribute('content')
                            except Exception as error:
                                print 'Error, no pagina-->', error
                                print 'continue'
                                not_page = True
                                index_homes+=1
                                contador = 0
                                number_success+=1
                                break
                            mainBubbles = driver.find_element_by_xpath("//meta[@property='og:rating']").get_attribute('content')
                            try:
                                script_coordinates = driver.find_element_by_xpath("//a[@title ='Informar a Google acerca de errores en las imágenes o en el mapa de carreteras']").get_attribute('href')
                                coordinates_string = script_coordinates[script_coordinates.find('@')+1:]
                                lat = coordinates_string.split(',')[0]
                                lng = coordinates_string.split(',')[1]
                                # lat=driver.find_element_by_xpath("//meta[@property='homeaway:location:latitude']").get_attribute('content')
                                # lng=driver.find_element_by_xpath("//meta[@property='homeaway:location:longitude']").get_attribute('content')
                            except Exception as error:
                                lng = ''
                                lat = ''
                                print 'Error coordenadas,', error

                            # type_search_attributes = False
                            # try:
                            #     type_residence = driver.find_elements_by_xpath("//div[@class='amenity-tittle']")
                            #     print type_residence
                            #     type_residence = type_residence[0].text
                            #     type_search_attributes = 0
                            #
                            # except Exception as error:
                            #     try:
                            #         print 'error0', error
                            #         print 'Se prueba la otra forma1'
                            #         type_residence = driver.find_elements_by_xpath("//li[@class='listing-highlights__list-item']")
                            #         type_residence = type_residence[0].find_element_by_xpath(".//span[contains(@class,'small')]").text
                            #         type_search_attributes = 1
                            #
                            #     except Exception as error:
                            #
                            #         print 'error1', error
                            #         print 'Se prueba la otra forma2'
                            #         types = driver.find_elements_by_xpath("//table[contains(@class,'amenity-table')]/tbody/tr")
                            #         for posibility in types:
                            #             print 'posibilidad-->', posibility.find_elements_by_xpath(".//td")
                            #             print 'posibilidad-->', posibility.text
                            #             print 'posibilidad-->', posibility.text
                            #
                            #             if posibility[0].text.strip() == 'Tipo de propiedad':
                            #                 type_residence = posibility.find_elements_by_xpath(".//td")[1].text
                            #                 break
                            #         type_search_attributes = 2

                            # type_residence = type_residence[0].text
                            try:
                                place = driver.find_elements_by_xpath("//a[@class='js-breadcrumbLink']")[1].text
                            except Exception as error:
                                print 'fallo en place,', error
                                try:
                                    place = driver.find_elements_by_xpath("//div[contains(@class,'location-pin__text')]")[0].text
                                    place = place.split(',')[0]
                                except:
                                    try:
                                        place = driver.find_element_by_xpath("//li[@class='last']/a").text
                                    except:
                                        place = ''
                            # print 'type_residence-->',type_residence
                            # attributes_names={
                            #     type_residence:'',
                            #     'Capacidad':'',
                            #     'Habitaciones':'',
                            #     'Baños'.decode('UTF-8'):'',
                            #     'Mín. Estancia'.decode('UTF-8'):'',
                            #     'Tipo de propiedad':''
                            # }

                            attributes_title = []
                            attributes_value = []
                            # print 'Tipo de busqueda = ', type_search_attributes
                            # if type_search_attributes is 0:
                            #     attributes_title = driver.find_elements_by_xpath("//div[@class='amenity-title']")
                            #     attributes_value = driver.find_elements_by_xpath("//div[@class='amenity-value']")
                            #     print 'Funciono forma0'
                            #
                            # elif type_search_attributes is 1:
                            #
                            #     all_attributes = driver.find_elements_by_xpath("//li[@class='listing-highlights__list-item']")
                            #     for attribute in all_attributes:
                            #         print attribute.find_element_by_xpath(".//span[contains(@class,'small')]")
                            #         attributes_title.append(attribute.find_element_by_xpath(".//span[contains(@class,'small')]"))
                            #         attributes_value.append(attribute.find_element_by_xpath(".//span[@class='listing-highlights__value']"))
                            #     print 'Funciono forma1'
                            #
                            # elif type_search_attributes is 2:
                            #     both = driver.find_elements_by_xpath("//table[@class='amenity-table']/tbody/tr")
                            #     attributes_title = both.find_elements_by_xpath(".//td")[0]
                            #     attributes_value = both.find_elements_by_xpath(".//td")[1]
                            #     print 'Funciono forma2'
                            # else:
                            #     print 'Error'
                            #     contador = 5
                            #
                            #
                            #
                            # for i in range(0,len(attributes_title)):
                            #     attributes_names[attributes_title[i].text.strip()] = attributes_value[i].text.strip()
                            #
                            # m2 = attributes_names[type_residence]
                            # capacity = attributes_names['Capacidad']
                            # rooms = attributes_names['Habitaciones']
                            # bathrooms = attributes_names['Baños'.decode('UTF-8')]
                            # if attributes_names['Mín. Estancia'.decode('UTF-8')] is not '':
                            #     min_stay = attributes_names['Mín. Estancia'.decode('UTF-8')]
                            # else:
                            #     min_stay = attributes_names['Estancia Mín.'.decode('UTF-8')]

                            numberReviews = ''
                            try:
                                numberReviews = driver.find_element_by_xpath("//strong[@class='large-superlative-summary']/div/span[@class='review-count']").text
                                numberReviews = numberReviews[1:numberReviews.find('c')].strip()

                            except Exception as error:
                                try:
                                    print 'No hay comentarios. Error0', error
                                    numberReviews = driver.find_element_by_xpath("//strong[@class='reviews-summary__num-reviews']").text.split()[0]
                                except:
                                    print 'No hay comentarios. Error1', error
                                    pass

                            print "url ---->", driver.current_url
                            print 'id ---->',ids[n]
                            print 'latitude-->',lng
                            print 'longitude-->',lat
                            # print "Tipo de residencia ---->",type_residence
                            print 'price-->', price
                            print 'og:rating-->',mainBubbles
                            print "numberReviews ---->", numberReviews
                            print "place ---->",place
                            # try:
                            #     print "m2 ---->",m2.split()[0]
                            #     m2 = m2.split()[0]
                            # except:
                            #     print "m2 ---->",m2


                            # print "capacity ---->",capacity
                            # print "rooms ---->",rooms
                            # print "bathrooms ---->",bathrooms
                            # print "min_stay ---->",min_stay
                            # samples_homes.append([ids[n], type_residence, price, numberReviews, mainBubbles, capacity, rooms, bathrooms, m2, min_stay, lng, lat, place])
                            samples_homes.append([ids[n], '', price, numberReviews, mainBubbles, '', '', '', '', '', lng, lat, place])
                            index_homes+=1
                            contador = 0
                            number_success+=1
                            print 'iteracion--->',number_success
                        except Exception as error:
                            print 'No carga,', error, "contador--->", contador
                            print 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno)
                            driver.get(urls[n])
                            time.sleep(1)
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
                print 'CONTADOR-->', contador
                load_all = True

        if contador >= 5:
            print "ERROR"
            break

try:
    clear_cache(driver)
except:
    pass
try:
    driver.close()
except:
    pass
#chromedriver dont stop itself
os.system("pkill -f chromedriver")

print('--------------')
print(samples_homes[0])
print(len(samples_homes))
print('Write ' + str(index_homes-1) + ' homeway homes description')


#It writes the comments and posts files
with open(homeway_files, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(samples_homes)