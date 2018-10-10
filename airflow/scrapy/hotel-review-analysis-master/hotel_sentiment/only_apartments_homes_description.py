# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time, os, sys
import unicodecsv as csv
from elasticsearch import Elasticsearch
from datetime import datetime

driver = webdriver.Chrome()
driver.set_window_size(1700,1000)

months = {'enero':'1','febrero':'2','marzo':'3','abril':'4','mayo':'5','junio':'6','julio':'7','agosto':'8','septiembre':'9','octubre':'10','noviembre':'11','diciembre':'12'}


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
samples_homes.append(["id_only_apartments", "title", "price", "numberReviews", "mainBubbles", "bathrooms", "capacity", "beds", "m2", "day_price", "stay", "lng", "lat"])


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
    i += 1
    print ''
    print ''
    print ''
    print '-----Pagina '+str(i)+'------'



    #if size windows is big
    # button = driver.find_element_by_xpath("//button[@id='MapToggleBar']")
    # button.click()
    time.sleep(.5)
    load_all = False
    #It could be that no load at first
    while load_all is False:
        print 'ENTRO'
        load_all = True
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
                    load = True
                    print "url ---->", driver.current_url
                    print 'id ---->',ids[i]

                    numberReviews = ''
                    mainBubbles = ''
                    #Only-apartments reviews and ratings
                    try:
                        reviews_rating = driver.find_element_by_xpath("//div[contains(@class,'comments-eval')]")
                        mainBubbles = reviews_rating.find_element_by_xpath(".//div[@class='total-rating']./span[@class='value']").text
                        numberReviews = reviews_rating.find_element_by_xpath("//div[contains(@class,'comments')]./h5/strong").text.split()[2]
                    #Tripadvisor reviews and ratings
                    except:
                        try:
                            reviews_rating = driver.find_element_by_xpath("//div[@class='tripadvisor-rating']")
                            mainBubbles = reviews_rating.find_element_by_xpath(".//div[@class='trip-image']/img").get_attribute('src')
                            pos_start_mainBubbles = mainBubbles.find('traveler') + mainBubbles[mainBubbles.find('traveler'):].find('/') + 1
                            mainBubbles = mainBubbles[pos_start_mainBubbles:mainBubbles[pos_start_mainBubbles:].find('-')]
                            numberReviews = reviews_rating.find_element_by_xpath("//div[@class,'trip-based-on']/span").text.split()[0]
                        except:
                            pass

                    attributes_names={
                        "icon-people":'',
                        'as-icon':'',
                        'icon-bed':'',
                        'icon-bathroom2':'',

                    }

                    groups_attributes = driver.find_elements_by_xpath("//div[@class='row text-center facilities-icons-list']/div")

                    attributes_title = []
                    attributes_value = []
                    for group in groups_attributes:
                        attributes_title_sel = []
                        attributes_value_sel = []
                        attributes = group.find_elements_by_xpath(".//div[@class='row']")
                        attributes_title_sel.append(attributes[0])
                        attributes_value_sel.append(attributes[1])

                        for attribute in attributes_title_sel:
                            attributes_title.extend(attribute.find_elements_by_xpath(".//div"))

                        for attribute in attributes_value_sel:
                            attributes_value.extend(attribute.find_elements_by_xpath(".//span"))

                        for i in range(0,len(attributes_title)):
                            try:
                                attribute_title = attributes_title[i].find_element_by_xpath(".//*")
                            except:
                                break


                            title = attribute_title.get_attribute("class") if len(attribute_title.get_attribute("class").split()) is 1 \
                                else attribute_title.get_attribute("class").split()[1]
                            # print 'title-->',title
                            # print 'attributes_value[i].text-->',attributes_value[i].text
                            if title in attributes_names:
                                attributes_names[title] = attributes_value[i].text


                    # print 'attributes_names-->',attributes_names
                    bathrooms = attributes_names["icon-bathroom2"][1:]
                    capacity = attributes_names["icon-people"][1:]
                    beds = attributes_names["icon-bed"][1:]
                    m2 = attributes_names["as-icon"]


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
                    # n_data = 0
                    # n_data_out = 0
                    # get_price = False
                    # while get_price is False:
                    #     get_price = True
                    #     datepicker = driver.find_elements_by_xpath("//button[@class='ui-datepicker-trigger']")
                    #     arrive = datepicker[0]
                    #     driver.execute_script("return arguments[0].scrollIntoView();", arrive)
                    #     arrive.click()
                    #
                    #     select_date = False
                    #     day_in = 0
                    #     while select_date is False:
                    #         n_in = n_data
                    #         try:
                    #             print 'entro'
                    #             date_selected = driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']").find_elements_by_xpath('.//a')
                    #             month_in = str(driver.find_element_by_xpath("//span[@class='ui-datepicker-month']").text).lower()
                    #             year_in = str(driver.find_element_by_xpath("//span[@class='ui-datepicker-year']").text)
                    #             day_in = str(date_selected[0].text)
                    #             driver.execute_script("return arguments[0].scrollIntoView();", date_selected[0])
                    #             print 'pinche'
                    #             select_date = True
                    #         except Exception as error:
                    #             print 'No pincho por', error
                    #             next_month = driver.find_element_by_xpath("//div[contains(@class,'ui-datepicker-header')]"). \
                    #                 find_elements_by_xpath(".//a[contains(@class,'ui-datepicker-next')]")
                    #             next_month[0].click()
                    #             n_in = 0
                    #

                    #     time.sleep(1)
                    #     select_date = False
                    #     n_out = 0
                    #     contador_out = 0
                    #     datepicker = driver.find_elements_by_xpath("//button[@class='ui-datepicker-trigger']")
                    #     print 'len datapicker-->', len(datepicker)
                    #     driver.execute_script("return arguments[0].scrollIntoView();", datepicker[1])
                    #     go_out = datepicker[1]
                    #     go_out.click()
                    #     while select_date is False:
                    #         n_out = n_data + 1 + n_data_out
                    #         try:
                    #             date_selected = driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']").find_elements_by_xpath('.//a')
                    #             day_out = str(date_selected[n_out].text)
                    #             print 'n_out-->',n_out
                    #             print 'len date_selected-->',len(date_selected)
                    #             print 'str(date_selected[0].text)-->',str(date_selected[0].text)
                    #             month_out = str(driver.find_element_by_xpath("//span[@class='ui-datepicker-month']").text).lower()
                    #             year_out = str(driver.find_element_by_xpath("//span[@class='ui-datepicker-year']").text)
                    #             select_date = True
                    #             date_selected[n_out].click()
                    #         except Exception as error:
                    #             print 'No pincho en out por',error
                    #             print 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno)
                    #             time.sleep(1)
                    #             contador_out += 1
                    #             print contador
                    #             if contador_out > 5:
                    #                 next_month = driver.find_element_by_xpath("//div[contains(@class,'ui-datepicker-header')]"). \
                    #                     find_elements_by_xpath(".//a[contains(@class,'ui-datepicker-next')]")
                    #                 next_month[0].click()
                    #                 n_out = 0
                    #                 break
                    #
                    #
                    #     print 'day_in-->', day_in
                    #     print 'day_out-->', day_out
                    #
                    #     date_in = year_in+'-'+str(months[month_in])+'-'+day_in
                    #     date_out= year_out+'-'+str(months[month_out])+'-'+day_out
                    #     print 'date_in-->', date_in
                    #     print 'date_out-->', date_out
                    #     date_in_datetime = datetime.strptime(date_in,"%Y-%m-%d")
                    #     date_out_datetime = datetime.strptime(date_out,"%Y-%m-%d")
                    #
                    #     print 'date_in_datetime-->',date_in_datetime
                    #     print 'date_out_datetime-->', date_out_datetime
                    #     stay = (date_out_datetime - date_in_datetime).days
                    #     print 'min_stay-->',stay
                    #
                    #     url_add = '?daterange.start_date='+date_in+'&daterange.end_date='+date_out+'&paxes=ADULT:2&page=1'
                    #     price_url = driver.current_url + url_add
                    #     print 'new_url-->', price_url
                    #     driver.get(price_url)
                    #     time.sleep(1)
                    #     #Price
                    #     load_price = False
                    #     contador_price = 0
                    #     price = ''
                    #     while load_price is False:
                    #         try:
                    #             load_price = True
                    #             try:
                    #                 price = driver.find_element_by_xpath("//span[@itemprop='price']").text
                    #                 print 'price normal-->', price
                    #             except:
                    #                 price = driver.find_element_by_xpath("//div[@id='total_price_head_container']").find_element_by_xpath(".//div[contains(@class,'brand-primary')]").text.split()[0]
                    #                 print 'price hotel-->', price
                    #
                    #         except Exception as error:
                    #             load_price = False
                    #             contador_price += 1
                    #             print 'Error precio. Contador', contador, ', error', error
                    #             no_allow = ''
                    #             try:
                    #                 no_allow = driver.find_element_by_xpath("//span[@class='message message-no-available']").text
                    #             except Exception as  error:
                    #                 print 'No había mensaje', error
                    #                 pass
                    #
                    #             print 'no_allow-->',no_allow
                    #
                    #             if no_allow:
                    #                 print no_allow.split()[0]
                    #                 if no_allow[0].split() == 'No':
                    #                     print 'suma de día. Muy pronto reserva'
                    #                     get_price = False
                    #                     n_data += 1
                    #                     break
                    #                 elif no_allow.split()[0] == 'La':
                    #                     print 'Suma día salida. Más estancia minima'
                    #                     get_price =  False
                    #                     n_data_out += 1
                    #                     break
                    #
                    #             if contador_price > 5:
                    #                 contador_price = True
                    #                 price = ''
                    #                 min_stay = ''
                    #             time.sleep(1)
                    #             pass


                    samples_homes.append([ids[i], title, '', numberReviews, mainBubbles,bathrooms,capacity, beds, m2, '', '', lng, lat])
                    index_homes+=1
                    contador = 0
                    number_success+=1
                    print 'iteracion--->',number_success
                except Exception as error:
                    print 'No Load', error
                    print 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno)

                    time.sleep(1)
                    contador += 1
                    print "contador sube", contador
                    if contador >= 5:
                        load = True
                        print "BREAK"
                        break
                    else:
                        print 'pass'
                        load = False
                        pass
        else:
            print ids[i], 'eliminada. No existe oferta actualmente.'
    if contador >= 5:
        load_all = True
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