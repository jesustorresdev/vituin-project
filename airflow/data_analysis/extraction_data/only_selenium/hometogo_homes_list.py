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
airbnb_files='homeway_homes_list.csv'
CSVdir='/usr/local/airflow/data_analysis/classify_elastic/unstructured_data/data_files'
airbnb_files = os.path.join(CSVdir, airbnb_files)

#Arrays will be save the dada
samples_homes=[]
samples_homes.append(["url_web", "url_details", "price", "web"])


index_homes=1


url = "https://www.hometogo.es/search/5460aedcd4609?bedrooms=1&bounds=28.42563%2C-16.56022%3B28.39316%2C-16.53416&lastZoom=15&mapZoom=15&persons=2&pricetype=perNight"
driver.get(url)



time.sleep(1)
noLoad = True

#It could be that no load at first
while noLoad != False:
    noLoad = False
    try:
        next = True
        i=0
        list_homes = driver.find_elements_by_xpath("//div[@id='offers-list']")
        while next == True:
            try:
                i+=1
                print '-----Pagina '+str(i)+'------'
                #print links
                for home in list_homes:
                    name = home.text
                    link_web=home.find_element_by_xpath('.//a[contains(@class, "ghost-cta-button")]').get_attribute('href')
                    link_details=home.find_element_by_xpath('.//a[contains(@class, "trs-all") and contains(@class, "c-gray-dark")]').get_attribute('href')
                    price=home.find_elements_by_xpath('.//div[@class="df aife"]/div[contains(@class, "fwb"]').text
                    web=home.find_elements_by_xpath('.//div[@class="text-overflow pr2"]').text
                    web = web[web.find(':'):].strip()
                    print 'link_web=',link_web,', id=', link_details
                    samples_homes.append([link_web,link_details, price, web])
                    index_homes+=1


                try:
                    more = driver.find_element_by_xpath("//div[@role='filter-pager']/button")
                    more.click()
                    list_homes_tmp = driver.find_elements_by_xpath("//div[@id='offers-list']")
                    list_homes = []
                    #It shoudn't repeat
                    for home in list_homes:
                        if home.get_attribute('data-position') >= index_homes:
                            list_homes.append(home)

                except Exception as error:
                    print 'Fin, por', error
                    next = False

            except Exception as e:
                print 'Error. Fin'
                print e

                next = False
    except:
        print 'No Load'
        noLoad = True
        pass



driver.close()
#chromedriver dont stop itself
os.system("pkill -f chromedriver")


print('--------------')
print(samples_homes[0])
print('Write ' + str(index_homes-1) + ' homeway homes')


#It writes the comments and posts files
with open(airbnb_files, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(samples_homes)