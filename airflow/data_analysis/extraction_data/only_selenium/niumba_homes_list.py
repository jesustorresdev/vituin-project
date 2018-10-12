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
niumba_files='niumba_homes_list.csv'
CSVdir='/usr/local/airflow/data_analysis/classify_elastic/unstructured_data/data_files'
niumba_files = os.path.join(CSVdir, niumba_files)

#Arrays will be save the dada
samples_homes=[]
samples_homes.append(["id_niumba", "title", "url", "price","type_residence", "rooms", "capacity", "min_stay", "place"])


index_homes=1





contador = 0
load_all = False
finish = False
#It could be that no load at first
while load_all is False and contador <= 5:
    load_all = True
    try:
        url = 'https://www.niumba.com/islas-canarias/santa-cruz-de-tenerife/puerto-de-la-cruz/hom_sleeps_max.'
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
                    last_page = driver.find_element_by_xpath("//p[@class='visible-xs-block']").text
                    print 'Page', last_page
                    print '-----Pagina '+str(i)+'------'
                    homes = driver.find_elements_by_xpath("//div[@id='mainSrpResults']/div")
                    #print links
                    samples_homes_tmp = []
                    for home in homes:
                        print 'home-->', home.get_attribute('id')
                        if home.get_attribute('id')[0:4] == 'home':
                            place = home.find_elements_by_xpath(".//div[@class='breadCrumb']/div/a")[2].text
                            print "place-->",place
                            if place != 'Puerto de la Cruz':
                                contador = 6
                                finish = True
                                next = False
                                break
                            id_niumba = home.get_attribute('id')[4:]
                            print 'id_niumba-->',id_niumba
                            title = home.find_element_by_xpath(".//div[@class='column']/h3/a").text
                            url=home.get_attribute('data-rental-unit-url')
                            attributes=home.find_elements_by_xpath(".//ul[@class='accomType mobileHidden']/li")
                            rooms = ''
                            capacity = ''
                            min_stay = ''
                            type_residence = ''
                            for attribute in attributes:
                                print attribute.text
                                if len(attribute.text.split()) > 1:
                                    if attribute.text.split()[1][0] == 'h':
                                        rooms = attribute.text.split()[0]
                                    elif attribute.text.split()[-1][-1] == '.' or attribute.text.split()[0][0] == 'l' :
                                        min_stay = attribute.text.split()[0]
                                        min_stay =  'varía' if min_stay == 'la' else min_stay
                                    else:
                                        try:
                                            if int(attribute.text.split()[1]):
                                                capacity = attribute.text.split()[1]
                                        except:
                                            type_residence = attribute.text
                                else:
                                    type_residence = attribute.text



                            try:
                                price = home.find_element_by_xpath(".//div[@class='column price']/meta").get_attribute("data-tracking-tree")
                            except:
                                try:
                                    price = home.find_element_by_xpath(".//div[@class='column price']/span").get_attribute("data-tracking-tree")
                                except:
                                    price = ''
                            print 'id=',id_niumba,', url=', url,', title=', title, ', rooms=', rooms, ', type_residence=', type_residence, ', capacity=', capacity, ', min_stay=', min_stay, ', price', price, ', place', place
                            samples_homes_tmp.append([id_niumba, title, url, price, type_residence, rooms, capacity, min_stay, place])
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
                    last_page = driver.find_element_by_xpath("//span[@class='hidden-xs']").text
                    next_page = driver.find_element_by_xpath("//a[@class='next hidden-xs']")
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
                    current_page = driver.find_element_by_xpath("//span[@class='hidden-xs']").text
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
print('Write ' + str(index_homes-1) + ' niumba homes')


#It writes the comments and posts files
with open(niumba_files, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(samples_homes)