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
airbnb_files='airbnb_homes_list.csv'
CSVdir='/usr/local/airflow/scrapy-hotels/hotel-review-analysis-master/classify_elastic'
airbnb_files = os.path.join(CSVdir, airbnb_files)

#Arrays will be save the dada
samples_homes=[]
samples_homes.append(["id_airbnb", "title", "url"])


index_homes=1


url = 'https://www.airbnb.es/s/Puerto-de-la-Cruz--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJBxuTnlXVQQwRQWOmKGEY6s0&query=Puerto%20de%20la%20Cruz%2C%20Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&s_tag=o78DH6Gz'
driver.get(url)



#if size windows is big
# button = driver.find_element_by_xpath("//button[@id='MapToggleBar']")
# button.click()
time.sleep(1)
noLoad = True

#It could be that no load at first
while noLoad != False:
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
    except:
        print 'No Load'
        noLoad = True
        pass



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