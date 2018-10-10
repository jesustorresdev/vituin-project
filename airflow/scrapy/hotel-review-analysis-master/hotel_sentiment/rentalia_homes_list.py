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
rentalia_files='rentalia_homes_list.csv'
CSVdir='/usr/local/airflow/scrapy-hotels/hotel-review-analysis-master/classify_elastic/unstructured_data'
rentalia_files = os.path.join(CSVdir, rentalia_files)

#Arrays will be save the dada
samples_homes=[]
samples_homes.append(["id_rentalia", "title", "url", "price", "rooms","bathrooms", "beds", "capacity", "place"])


index_homes=1





contador = 0
load_all = False
finish = False
#It could be that no load at first
while load_all is False and contador <= 5:
    load_all = True
    try:
        url = 'https://es.rentalia.com/alquiler-vacaciones-puerto-de-la-cruz/'
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
                    last_page = driver.find_element_by_xpath("//li[@class='active waves-effect']/a").text
                    print 'Page', last_page
                    print '-----Pagina '+str(i)+'------'
                    homes = driver.find_elements_by_xpath("//div[contains(@class,'itemList')]")
                    #print links
                    samples_homes_tmp = []
                    for home in homes:
                        print 'home-->', home.get_attribute('id')

                        title = home.find_element_by_xpath(".//div[contains(@class,'title')]/h3").text
                        place = home.find_element_by_xpath(".//div[contains(@class,'title')]/h4").text
                        if len(place.split(',')) is 3:
                            place = place.split(',')[1].strip()
                        elif len(place.split(',')) is 2:
                            place = place.split(',')[0].strip()
                        else:
                            place = place.strip()
                        if place != 'Puerto de la Cruz':
                            contador = 6
                            finish = True
                            next = False
                            break
                        id_rentalia = home.get_attribute('id')
                        url='https://es.rentalia.com/'+home.get_attribute('id')
                        attributes=home.find_element_by_xpath(".//p[contains(@class,'capacityInfo')]").text.split('·'.decode('UTF-8'))
                        attributes_names={
                            'personas':'',
                            'habitaciones':'',
                            'baños'.decode('UTF-8'):'',
                            'camas':'',
                        }
                        for attribute in attributes:
                            attributes_names[attribute.split()[1].strip()] = attribute.split()[0].strip()

                        bathrooms = attributes_names['baños'.decode('UTF-8')]
                        rooms = attributes_names['habitaciones']
                        beds = attributes_names['camas']
                        capacity = attributes_names['personas']



                        price = home.find_element_by_xpath(".//div[@class='price']/span").text.split()[0]
                        print 'id=',id_rentalia,', url=', url,', title=', title, ', rooms=', rooms, ', bathrooms=', bathrooms, ', capacity=', capacity, ', beds=', beds, ', price', price, ', place', place
                        samples_homes_tmp.append([id_rentalia, title, url, price, rooms, bathrooms, beds, capacity, place])
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
                    pagination_elements = driver.find_elements_by_xpath("//ul[@class='pagination']/li/a")

                    if pagination_elements[-1].text.split()[0] == 'Siguiente':
                        next_page = pagination_elements[-1]
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
                    current_page = driver.find_element_by_xpath("//li[@class='active waves-effect']/a").text
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
print('Write ' + str(index_homes-1) + ' rentalia homes')


#It writes the comments and posts files
with open(rentalia_files, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(samples_homes)
     #

     #
     # {"street_type":null,
     #  "street_type_str":null,
     #  "street_name":"Calle la Hoya, 23, 38400 Puerto de la Cruz, Santa Cruz de Tenerife, Spain",
     #  "street_num":null,
     #  "misc":null,
     #  "address":"Calle la Hoya, 23, 38400 Puerto de la Cruz, Santa Cruz de Tenerife, Spain 38400 ",
     #  "city":"Puerto de la Cruz",
     #  "municipality":"Puerto de la Cruz",
     #  "postcode":"38400",
     #  "country":"Espa\u00f1a",
     #  "country_code":"ES",
     #  "zone_id":null,
     #  "zone":"",
     #  "levels":{"6":62395,"5":2139,"4":74,"3":7,"2":1},
     #  "levels_urls":
     #      {
     #          "6":"\/alquiler-vacaciones-puerto-de-la-cruz-id62395\/",
     #          "5":"\/alquiler-vacaciones-puerto-de-la-cruz\/",
     #          "4":"\/alquiler-vacaciones-tenerife\/",
     #          "3":"\/alquiler-vacaciones-canarias\/",
     #          "2":"\/alquiler-vacaciones-espana\/"
     #      },
     #  "complete_addr":true,
     #  "neighborhood":null,
     #  "region":"Tenerife",
     #  "ccaa":"Canarias",
     #  "location":"Puerto de la Cruz (Tenerife)",
     #  "locationm":
     #      {
     #          "es":"Puerto de la Cruz (Tenerife)",
     #          "en":"Puerto de la Cruz (Tenerife)",
     #          "de":"Puerto de la Cruz (Teneriffa)",
     #          "fr":"Puerto de la Cruz (T\u00e9n\u00e9riffe)",
     #          "pt":"Puerto de la Cruz (Tenerife)",
     #          "it":"Puerto de la Cruz (Tenerife)",
     #          "nl":"Puerto de la Cruz (Tenerife)"
     #      },
     #  "show_exact_address":true,
     #  "latitude_geo":28.4168643,
     #  "longitude_geo":-16.5460865,
     #  "latitude":"28.416850199999995",
     #  "longitude":"-16.54654279999999"
     #  }, '', 'Borrar selección', 745871, 63, 0, 'es', 'ES',
    # [
#      {
#         "txt":"Espa\u00f1a",
#         "url":"\/alquiler-vacaciones-espana\/"
#      },{
#          "txt":"Canarias",
#          "url":"\/alquiler-vacaciones-canarias\/"
#      },{"txt":"Tenerife","url":"\/alquiler-vacaciones-tenerife\/"},
#     {"txt":"Puerto de la Cruz","url":"\/alquiler-vacaciones-puerto-de-la-cruz\/"},
# {"txt":"Ref. 745871","url":"http:\/\/es.rentalia.com\/745871"}]
# , 745871, '960525', 'reserva',\
#   [{"capacity_min":6,"capacity_max":6,"idprice":459047418,"price_night":"62.42","price_week":"436.94",
#     "price_fortnight":"873.88","price_month":"1810.18","price_night_weekend":"62.42",
#     "price_additional_guest":null,"nights_min":4,"date_init":null,"date_end":null,"name":null,
#     "force_weekend":false,"checkin_day":null,"checkout_day":null,"date":{"period":"rest","text":"Precio b\u00e1sico"}},
# {"capacity_min":6,"capacity_max":6,"idprice":459047416,
#  "price_night":"62.42","price_week":"436.94",
#  "price_fortnight":"873.88","price_month":"1810.18","price_night_weekend":"62.42",
#  "price_additional_guest":null,"nights_min":5,"date_init":"2018-08-04",
#  "date_end":"2020-01-31","name":null,"force_weekend":false,"checkin_day":null,"checkout_day":null,
#  "date":{"init":"04\/08\/2018","end":"31\/01\/2020","iniday":"4","inimonth":"08","iniyear":"2018",
#          "inimonth_text":"agosto","endday":"31","endmonth":"01","endyear":"2020","endmonth_text":"enero",
#          "text":"04\/08\/2018 a 31\/01\/2020"}},
# {"capacity_min":6,"capacity_max":6,"idprice":459047417,"price_night":"62.42",
#  "price_week":"436.94","price_fortnight":"873.88","price_month":"1810.18","price_night_weekend":"62.42",
#  "price_additional_guest":null,"nights_min":5,"date_init":"2020-02-01","date_end":"2020-05-01","name":null,
#  "force_weekend":false,"checkin_day":null,
#  "checkout_day":null,"date":
#      {"init":"01\/02\/2020","end":"01\/05\/2020","iniday":"1","inimonth":"02","iniyear":"2020",
#       "inimonth_text":"febrero","endday":"1","endmonth":"05","endyear":"2020","endmonth_text":"mayo",
#       "text":"01\/02\/2020 a 01\/05\/2020"}}]