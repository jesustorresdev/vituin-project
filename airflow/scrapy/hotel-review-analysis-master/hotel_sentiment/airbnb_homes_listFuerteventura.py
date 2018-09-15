# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os
import unicodecsv as csv
from elasticsearch import Elasticsearch
from urls import AirbnbFuerteventuraURLs

driver = webdriver.Chrome()


exceptionErrorItem=False
es = Elasticsearch(
    [
        'elastic:vituinproject@elasticsearch:9200/',
    ]
)


#Fields where data will be write
airbnb_files='airbnb_homes_listFuerteventura.csv'
CSVdir='/usr/local/airflow/scrapy-hotels/hotel-review-analysis-master/classify_elastic'
airbnb_files = os.path.join(CSVdir, airbnb_files)

#Arrays will be save the dada
samples_homes=[]
samples_homes.append(["id_airbnb", "title", "url"])


index_homes=1

contador = 0
number_success = 0

urls = AirbnbFuerteventuraURLs()
for url in urls:
    driver.get(url)
    time.sleep(.5)



    #if size windows is big
    # button = driver.find_element_by_xpath("//button[@id='MapToggleBar']")
    # button.click()
    noLoad = True

    #It could be that no load at first
    while noLoad != False:
        print 'ENTRO'
        noLoad = False
        try:
            next = True
            i=0
            last_page = driver.find_elements_by_xpath("//div[@class='_1bdke5s']")[-1]
            last_page= int(last_page.text) - 1 #It starts in 0
            print 'Last_Page', last_page
            while next == True:
                try:
                    i+=1
                    print '-----Pagina '+str(i)+'------'
                    links = driver.find_elements_by_xpath("//a[contains(@class, '_15ns6vh')]")
                    #print links
                    for link in links:
                        name = link.find_element_by_xpath(".//div[@class='_jnrahhr']").text
                        link=link.get_attribute('href')
                        id_airbnb = link[link.find('rooms')+6:link.find('?')]
                        print 'nombre=',name,', id=', id_airbnb
                        samples_homes.append([id_airbnb, name, link])
                        index_homes+=1


                    new_page = driver.find_elements_by_xpath("//a[@class='_1ip5u88']")#.get_attribute('href')
                    print ''
                    print ''
                    print ''
                    url_new_page = new_page[-1].get_attribute('href')
                    print url_new_page
                    current_page = int(url_new_page[-6+1+url_new_page[-6:].find('='):])

                    print 'Current',current_page, ', last', last_page
                    print 'Current',type(current_page), ', last', type(last_page)
                    if last_page>current_page:
                        driver.get(url_new_page)

                        time.sleep(0.5)
                    else:
                        print 'Fin'
                        next = False

                except Exception as e:
                    print 'Error. Fin'
                    print e

                    next = False
                    break
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

    contador = 0
    number_success+=1
    print 'iteracion--->',number_success

if contador >= 5:
    print "ERROR"
    error = True

driver.close()
#chromedriver dont stop itself
os.system("pkill -f chromedriver")


print('--------------')
print(samples_homes[0])
print('Write ' + str(index_homes-1) + ' airbnb homes')


#It writes the comments and posts files
with open(airbnb_files, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(samples_homes)