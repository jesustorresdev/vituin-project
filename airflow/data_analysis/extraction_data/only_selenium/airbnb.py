# # -*- coding: UTF-8 -*-
#
# from extraction_data.spiders.prueba_selenium_price import webdriver
# import time, os
# driver = webdriver.Chrome()
#
# #----------------------1-------------------------------
# # driver.get("https://www.airbnb.es/s/Puerto-de-la-Cruz--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJBxuTnlXVQQwRQWOmKGEY6s0&query=Puerto%20de%20la%20Cruz%2C%20Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&s_tag=o78DH6Gz")
# # time.sleep(1)
# # driver.maximize_window()
# # print driver.get_window_size()
# #driver.find_element_by_class_name("ui_close_x")
#
# #if size windows is big
# # button = driver.find_element_by_xpath("//button[@id='MapToggleBar']")
# # button.click()
# # time.sleep(1)
#
# # next = True
# # i=0
# # last_page = driver.find_elements_by_xpath("//div[@class='_1bdke5s']")[-1]
# # last_page= int(last_page.text) - 1 #It starts in 0
# # print 'Last_Page', last_page
# # while next == True:
# #     try:
# #         i+=1
# #         print '-----Pagina '+str(i)+'------'
# #         links = driver.find_elements_by_xpath("//a[contains(@class, '_15ns6vh')]")
# #         #print links
# #         for link in links:
# #             print link.get_attribute('href')
# #         new_page = driver.find_elements_by_xpath("//a[@class='_1ip5u88']")#.get_attribute('href')
# #         print ''
# #         print ''
# #         print ''
# #         url_new_page = new_page[-1].get_attribute('href')
# #         print url_new_page
# #         current_page = int(url_new_page[-6+1+url_new_page[-6:].find('='):])
# #
# #         print 'Current',current_page, ', last', last_page
# #         print 'Current',type(current_page), ', last', type(last_page)
# #         if last_page>current_page:
# #             driver.get(url_new_page)
# #
# #             time.sleep(0.1)
# #         else:
# #             print 'Fin'
# #             next = False
# #
# #     except:
# #         print 'Error. Fin'
# #         next = False
# #
#
# #----------------------FIN DE 1-------------------------------
# # #----------------------2-------------------------------
# # #**********PARTE 1: Datos generales***********
# #
# # driver.set_window_size(330,350)
# driver.get("https://www.airbnb.es/rooms/6213016?location=Puerto%20de%20la%20Cruz%2C%20Santa%20Cruz%20de%20Tenerife&s=o78DH6Gz")
# # print "url", driver.current_url
# # time.sleep(1)
# # tittle = driver.find_element_by_xpath("//h1[@class='_1xu9tpch']")
# # type_residence = driver.find_element_by_xpath("//span[@class='_1hh2h7tb']/span")
# # details = driver.find_elements_by_xpath("//div[@class='_qtix31']/div[@class='_1thk0tsb']/span[@class='_fgdupie']")  #More than one
# # price = driver.find_element_by_xpath("//span[@class='_doc79r']")
# # print "Titulo ---->",tittle.text
# # print "Tipo de residencia ---->",type_residence.text
# # print "Precio ---->", price.text
# # i=0
# # for detail in details:
# #     i+=1
# #     print "Detalle", i, "---->", detail.text
# #
# # numberReviews = driver.find_element_by_xpath("//span[@class='_492uxj4']/span")
# # mainBubbles = driver.find_element_by_xpath("//div[@itemprop='ratingValue']")
# # print "Numero de reviews ---->",numberReviews.text
# # print "Puntuación media ---->",mainBubbles.get_attribute('content')
# # secundaryBubbles = driver.find_elements_by_xpath("//div[@class='_2h22gn']/div[@class='_en5l15m']")
# #
# # for column in secundaryBubbles:
# #     element = column.find_elements_by_xpath(".//div/div")
# #     bubblesNames = column.find_elements_by_xpath(".//span[@class='_fgdupie']")
# #     bubblesNumber = column.find_elements_by_xpath(".//div[@class='_1iu38l3']/span")
# #     names = []
# #     valuations = []
# #     #Type of bubble
# #     for name in bubblesNames:
# #         names.append(name.text)
# #
# #
# #     for valuation in bubblesNumber:
# #         valuations.append(valuation.get_attribute('aria-label'))
# #     for i in range(0,len(names)):
# #         print names[i], ' tiene', valuations[i]
# #
# # cancelations = driver.find_element_by_xpath("//div[@class='_ncwphzu']/span")
# #
# # print 'cancelaciones',cancelations.text
# #
# # estancia_minima = driver.find_element_by_xpath("//div[@class='_q401y8m']//span[@class='_fgdupie']/span/strong")
# #
# # print 'estancia minima',estancia_minima.text
# # #**********FIN PARTE 1***********
# # #**********PARTE 2: Ubicacion***********
# time.sleep(1)
# coordenates = driver.find_element_by_xpath("//div[@class='_59m2yxn']/img").get_attribute('src')
# print "Coordenadas ------>", coordenates
# str_coor = str(coordenates)
# pos1 = str_coor.find("center")+7
# pos2 = str_coor.find("scale")-1
# #print pos1, pos2
# coor = str_coor[pos1:pos2]
# coor = coor.split(',')
# lat = coor[0]
# lo=coor[1]
# print 'separados----->',lat, lo
# # #**********FIN PARTE 2***********
# # #**********PARTE 3. Servicios***********
# # time.sleep(1)
# # driver.set_window_size(2560, 1440)
# # driver.find_elements_by_xpath("//div[@class='_1n57hdr7']/button")[1].click()
# #
# # headServices = driver.find_elements_by_xpath("//div[@class='_wpwi48']/section/div")
# # print ''
# # print ''
# # print ''
# #
# #
# # for service in headServices:
# #
# #     #print 'Service text--->', service.text
# #     servicesName = service.find_element_by_xpath(".//h2[@class='_tpbrp']/div")
# #     print 'Group name--', servicesName.text
# #     servicesList = service.find_elements_by_xpath(".//div[@class='_2930ex']")
# #     for serv in servicesList:
# #         if servicesName.text != "No incluidos":
# #             sName = serv.find_element_by_xpath(".//div[@class='_ncwphzu']")
# #             print 'Elemento--', sName.text
# #             try:
# #                 sDetails = serv.find_element_by_xpath(".//div[@class='_1nhodd4u']")
# #                 print 'Detalles del elemento--',sDetails.text
# #             except:
# #                 pass
# #             print'---'
# #
# #     print ''
# #     print ''
# #     print ''
# #     print ''
# #
# # #**********FIN PARTE 3***********
#
#
# driver.close()
# #chromedriver dont stop itself
# os.system("pkill -f chromedriver")
