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
flats9_files='9flats_homes_list.csv'
CSVdir='/usr/local/airflow/scrapy-hotels/hotel-review-analysis-master/classify_elastic/unstructured_data'
flats9_files = os.path.join(CSVdir, flats9_files)

#Arrays will be save the data
samples_homes=[]
samples_homes.append(["id_flat9", "title", "url","price", "type_residence", "web", "stars", "numberReviews"])


index_homes=1





contador = 0
load_all = False
finish = False
#It could be that no load at first
while load_all is False and contador <= 5:
    load_all = True
    try:
        url = 'https://www.9flats.com/es/searches?utf8=%E2%9C%93&mode=list&search%5Bplace_type%5D=&search%5Bprice_min%5D=&search%5Bprice_max%5D=&search%5Bcurrency%5D=EUR&search%5Bsort_by%5D=top_ranking&search%5Bview_index%5D=0&search%5Bnumber_of_bathrooms%5D=0&search%5Bnumber_of_bedrooms%5D=0&search%5Bradius%5D=25&search%5Bamenities%5D=&search%5Bwoeid%5D=770966&search%5Bbb_sw%5D=&search%5Bbb_ne%5D=&search%5Blat%5D=28.4142&search%5Blng%5D=-16.5474&search%5Biso%5D=&search%5Bis_country%5D=&search%5Bcategory%5D=&search%5Bgeo_search%5D=&search%5Bgeo_region%5D=false&search%5Bpoint_of_interest%5D=false&search%5Bprice_range%5D=&search%5Bancestries%5D=&search%5Bcontinuous_update%5D=&search%5Bbooking_type%5D=&search%5Bpayment_type%5D=&search%5Bstart_date_alt%5D=&search%5Bend_date_alt%5D=&search%5Bquery%5D=Puerto+de+la+Cruz%2C+Pto+de+la+Cruz'
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
                    last_page = driver.find_element_by_xpath("//span[@class='search__pagination__info']").text
                    print 'Page', last_page
                    print '-----Pagina '+str(i)+'------'
                    homes = driver.find_elements_by_xpath("//div[@class = 'search__results__i row']/div")
                    #print links
                    samples_homes_tmp = []
                    for home in homes:
                        print 'home-->', home.get_attribute('id')
                        if home.get_attribute('id')[0:5] == 'place':
                            # place = home.find_elements_by_xpath(".//div[@class='breadCrumb']/div/a")[2].text
                            # print "place-->",place
                            # if place != 'Puerto de la Cruz':
                            #     contador = 6
                            #     finish = True
                            #     next = False
                            #     break
                            id_flat9 = home.get_attribute('id')[6:]
                            print 'id_flat9-->',id_flat9
                            title = home.find_element_by_xpath(".//h5[@class = 'card-title']").text
                            url=home.find_elements_by_xpath(".//a")[0].get_attribute('href')
                            # attributes=home.find_elements_by_xpath(".//ul[@class='accomType mobileHidden']/li")
                            type_residence= home.find_element_by_xpath(".//h6[@class = 'card-text']").text
                            try:
                                type_residence = type_residence[:type_residence.find('Puerto')].strip()
                            except:
                                pass
                            try:
                                web = home.find_element_by_xpath(".//div[@class = 'provider mt-2']").text
                            except:
                                web = ''
                            try:
                                stars = home.find_element_by_xpath(".//span[contains(@class , 'search__place__content__stars')]").text
                            except:
                                stars = ''
                            try:
                                numberReviews = home.find_element_by_xpath(".//span[@class = 'search__place__content__reviews']").text
                            except:
                                numberReviews = ''
                            price = home.find_element_by_xpath(".//span[@class = 'money']").text[1:]

                            print 'id=',id_flat9,', url=', url,', title=', title, ', type_residence=', type_residence, ', price', price, ', web', web, ', stars', stars, ', numberReviews', numberReviews,
                            samples_homes_tmp.append([id_flat9, title, url, price, type_residence, web, stars, numberReviews])
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
                        finish = True
                        contador = 0
                        next = False
                    time.sleep(1)
                    pass
            load = False
            while load is False and finish is False:
                try:
                    load = True
                    next_page = driver.find_element_by_xpath("//a[contains(@class,'pagination__item__link_next')]").get_attribute('href')
                    next_page_url = 'https://www.9flats.com'+next_page
                    print next_page
                    driver.get(next_page)
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
                    current_page = driver.find_element_by_xpath("//span[@class='search__pagination__info']").text
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



print('--------------')
print(samples_homes[0])
print('Write ' + str(index_homes-1) + ' flat9 homes')


#It writes the comments and posts files
with open(flats9_files, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(samples_homes)