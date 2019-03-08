# # -*- coding: UTF-8 -*-
#
# import sys
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time, os
# import unicodecsv as csv
# import datetime
# from elasticsearch import Elasticsearch
# sys.path.append('../')
# from utils import clear_cache, get_reactions
#
# driver = webdriver.Chrome()
#
#
# es = Elasticsearch(
#     [
#         'elastic:vituinproject@elasticsearch:9200/',
#     ]
# )
#
# #Fields where data will be write
# facebook_post_files='facebook_selenium_description_VisitPuertodelaCruz.csv'
# CSVdir='/usr/local/airflow/data_analysis/classify_elastic/unstructured_data/data_files'
# facebook_post_files = os.path.join(CSVdir, facebook_post_files)
#
# facebook_comments_files='facebook_selenium_description_VisitPuertodelaCruz.csv'
# CSVdir='/usr/local/airflow/data_analysis/classify_elastic/unstructured_data/data_files'
# facebook_comments_files = os.path.join(CSVdir, facebook_comments_files)
#
# #Arrays will be save the dada
# samples_posts=[]
# samples_comments=[]
#
# samples_posts.append(["id","message", "comments", "shares","reproductions","likes","loves","wows","enjoyes","sads","angries", "key", "extraction_time"])
# samples_comments.append(["id", "message","likes","loves","wows","hahas","sads","angries","thankfuls","prides", "key", "creation_time", "extraction_time", "parent", "exist_now"])
#
# index_homes=1
#
# #SearchAll
# doc = {
#     'size' : 10000,
#     'query': {
#         'match_all' : {}
#     }
# }
#
#
# res = es.search(index="index_list_selenium_facebook", doc_type="unstructured", body=doc,scroll='1m')
#
#
# urls = []
# #create list of URLs
# for hit in res['hits']['hits']:
#     urls=urls + [hit["_source"]["url"]]
# contador = 0
# number_success = 0
#
# for i in range(0,len(urls)):
#     driver.get(urls[i])
#
#
#     # driver = (driver.find_elements_by_xpath("//div[@class='_4-u2 _4-u8']"))[0]
#     # SEE ALL TITLE
#     load = False
#     contador = 0
#     while load is False and contador < 5:
#         try:
#             see_more = driver.find_element_by_xpath(".//a[@class='see_more_link']")
#             print "see_more-->",see_more.text
#             see_more.click()
#         except Exception as error:
#             print 'Error',contador,'en see more', error
#             contador += 1
#             pass
#
#     # TITLE
#     load = False
#     contador = 0
#     title = None
#     while load is False and contador < 5:
#         try:
#             title = driver.find_elements_by_xpath("//div[contains(@class, 'userContent')]/p")
#             print "title-->",title
#             load = True
#         except Exception as error:
#             print 'Error',contador,'en title', error
#             contador += 1
#             pass
#
#     message = ''
#     if title:
#         n_paragraph=0
#         for paragraph in title:
#             print "Parrafo", n_paragraph, ", texto-->", paragraph.text
#             message += paragraph.text
#             n_paragraph += 1
#         print ''
#         print 'se acabo titulo'
#
#     #REACTIONS CLICK BUTTON
#     load = False
#     contador = 0
#     post_click = False
#     while load is False and contador < 5:
#         print 'click reactions'
#         try:
#             driver.find_element_by_xpath("//span[@class='_3t54']").click()
#             load = True
#             post_click = True
#         except Exception as error:
#             print 'Error',contador,'en click reactions post', error
#             contador += 1
#             pass
#
#
#     if post_click is True:
#         load = False
#         contador = 0
#         while load is False and contador < 5:
#             try:
#                 body=driver.find_element_by_tag_name("body")
#                 print 'body-->', body
#                 load = True
#             except Exception as error:
#                 print 'Error',contador,'get body', error
#                 time.sleep(3)
#                 contador += 1
#                 pass
#
#     #REACTIONS
#     load = False
#     contador = 0
#     reactions = None
#     while load is False and contador < 5:
#         try:
#
#             print 'Estoy cogiendo REACTIONS'
#             reactions = body.find_elements_by_xpath(".//li[contains(@class, '_ds-') and contains(@class, ' _45hc')]")
#             print "reactions-->",reactions
#             load = True
#         except Exception as error:
#             print 'Error',contador,'en reactions del post', error
#             contador += 1
#             pass
#             #Could be not load
#         if not reactions and load:
#             print 'No ha cargado. Se repite'
#             load = False
#             time.sleep(3)
#         if contador >= 5:
#             load = True
#             print 'Se sigue. No se cargó'
#
#
#     if reactions:
#         print 'Estoy en REACTIONS'
#
#         name = 'posts'
#
#         reactions_values=get_reactions(reactions, name, driver)
#         print 'reactions_values-->', reactions_values
#         likes = reactions_values['likes']
#         loves = reactions_values['loves']
#         wows = reactions_values['wows']
#         enjoyes = reactions_values['enjoyes']
#         sads = reactions_values['sads']
#         angries = reactions_values['angries']
#
#     # CLOSE REACTIONS SQUARE
#     load = False
#     contador = 0
#     while load is False and contador < 5:
#         try:
#             body.find_element_by_xpath("//a[@title='Cerrar']").click()
#             load = True
#         except Exception as error:
#             print 'Error',contador,'en cerrar cuadro reactions del post', error
#             contador += 1
#             pass
#
#
#
#     # NUMBER REVIEWS AND SHARE
#     load = False
#     contador = 0
#     while load is False and contador < 5:
#         print 'Estoy en NUMERO DE COMENTARIOS y SHARES'
#         try:
#             # number_rev_and_sh = driver.find_elements_by_xpath(".//div[contains(@class,'_ipo')]/div")
#             number_rev_and_sh = driver.find_elements_by_xpath(".//div[contains(@class,'_ipo')]/div")
#             load = True
#             print 'number_rev_and_sh-->',number_rev_and_sh
#         except Exception as error:
#             print 'Error',contador,'en number_rev_and_sh', error
#             contador += 1
#             pass
#
#     if number_rev_and_sh:
#         for element in number_rev_and_sh:
#             try:
#                 attribute = element.find_element_by_xpath(".//a").get_attribute('href')
#                 number_interaction =  element.find_element_by_xpath(".//a").text
#                 print 'attribute-->',attribute
#                 print 'el atributo cortado-->',attribute[25:25+6]
#                 print 'number_interaction-->',number_interaction
#                 if attribute[25:25+6] == 'shares':
#                     shares_all = number_interaction.split()
#                     print 'shares_all-->', shares_all
#
#                     if len(shares_all) > 1:
#                         if shares_all[1] == 'mil':
#                             shares = shares_all[0] * 1000
#                         else:
#                             shares = shares_all[0]
#                     print 'shares-->', shares
#                 else:
#                     comments_all = number_interaction.split()
#                     print 'comments_all-->', comments_all
#
#                     if len(comments_all) > 1:
#                         if comments_all[1] == 'mil':
#                             comments = comments_all[0] * 1000
#                         else:
#                             comments = comments_all[0]
#                         print 'comments-->', comments
#
#             except Exception as error:
#                 print 'Error',error
#                 #if it doesn't have href the element is reproductions
#                 reproductions_all = element.text[:element.text.find('r')].strip()
#                 if len(reproductions_all) > 1:
#                     if reproductions_all[1] == 'mil':
#                         reproductions = reproductions_all[0] * 1000
#                     else:
#                         reproductions = reproductions_all[0]
#                 print 'reproductions-->', reproductions
#
#
#     # SEE ALL REVIEWS
#     load = False
#     contador = 0
#     while load is False and contador < 5:
#         try:
#             see_more_reviews = driver.find_element_by_xpath(".//div[contains(@class,'UFILastCommentComponent')]/div/div/a[@class='UFIPagerLink']")
#             print "see_more_reviews-->",see_more_reviews.text
#             see_more_reviews.click()
#             load = True
#         except Exception as error:
#             print 'Error',contador,'en see more views', error
#             contador += 1
#             pass
#
#     #driver.execute_script("window.scrollTo(900, Y)")
#     # REVIEWS
#     print 'REVIEWS'
#     load = False
#     contador = 0
#     while load is False and contador < 5:
#         try:
#             reviews = driver.find_elements_by_xpath(".//div[@aria-label='Comentario']")
#             #reviews = driver.find_elements_by_xpath(".//div[contains(@class,'UFIRow') and contains(@class,'UFIComment')]")
#
#             print 'reviews-->', reviews
#             load = True
#         except Exception as error:
#             print 'Error',contador,'en reviews', error
#             contador += 1
#             pass
#
#     #reviews.location_once_scrolled_into_view
#     time.sleep(1)
#     m = 0
#     if reviews:
#         for review in reviews:
#
#             print 'Comentario numero', m
#
#             print 'aria label de la review-->',review.get_attribute('aria-label')
#             if review.get_attribute('aria-label') == 'Comentario':
#                 print 'Es comentario con identificador--> ', review.get_attribute('data-ft')
#             elif review.get_attribute('aria-label') == 'Respuesta a un comentario':
#                 print 'Es una respuesta al comentario--> ', review.get_attribute('data-ft')
#
#             # CREATE TIME
#             load = False
#             contador = 0
#             while load is False and contador < 5:
#                 try:
#                     creation_time = review.find_elements_by_xpath(".//abbr")
#                     creation_time = creation_time[0].get_attribute('title')
#                     print 'creation_time-->',creation_time
#                     load = True
#                 except Exception as error:
#                     print 'Error',contador,'en creation_time', error
#                     contador += 1
#                     pass
#
#             load = False
#             contador = 0
#             while load is False and contador < 5:
#                 try:
#                     #review_text = review.find_element_by_xpath(".//span[@class='UFICommentBody']/span")
#                     review_text = review.find_element_by_xpath(".//span[@class='UFICommentBody']")
#
#                     print 'review'+str(m)+'-->',review_text.text
#                     load = True
#                 except Exception as error:
#                     print 'Error',contador,'en review', error
#                     contador += 1
#                     pass
#
#
#
#             #REACTIONS REVIEW CLICK BUTTON
#             review_click = False
#             load = False
#             contador = 0
#             while load is False and contador < 5:
#                 try:
#                     review.find_element_by_xpath("//span[@class='_3t54']").click()
#                     load = True
#                     review_click = True
#                 except Exception as error:
#                     print 'Error',contador,'en click reactions comentario', error
#                     contador += 1
#                     pass
#             if review_click is True:
#                 #review.find_element_by_xpath(".//div[contains(@class,'UFICommentReactionsBling')]").click()
#                 load = False
#                 contador = 0
#                 try:
#                     body=driver.find_element_by_tag_name("body")
#                     print 'body-->', body
#                     load = True
#                 except Exception as error:
#                     print 'Error',contador,'get body', error
#                     time.sleep(3)
#                     contador += 1
#                     pass
#
#
#                 #REACTIONS REVIEWS
#                 load = False
#                 contador = 0
#                 reactions_reviews = None
#                 while load is False and contador < 5:
#                     try:
#                         print 'Estoy cogiendo REACTIONS REVIEW'
#                         reactions_reviews = body.find_elements_by_xpath(".//li[contains(@class, '_ds-') and contains(@class, ' _45hc')]")
#                         print "reactions_reviews-->",reactions_reviews
#                         load = True
#                     except Exception as error:
#                         print 'Error',contador,'en reactions reviews', error
#                         contador += 1
#                         pass
#                     #Could be not load
#                     if not reactions_reviews and load:
#                         print 'No ha cargado. Se repite'
#                         load = False
#                         time.sleep(3)
#                     if contador >= 5:
#                         load = True
#                         print 'Se sigue. No se cargó'
#
#
#
#                 if reactions_reviews:
#                     print 'Estoy en REACTIONS REVIEW'
#                     name = 'comentarios'
#                     get_reactions(reactions_reviews, name,driver)
#
#                 # CLOSE REACTIONS REVIEWS SQUARE
#                 load = False
#                 contador = 0
#                 while load is False and contador < 5:
#                     try:
#                         body.find_element_by_xpath(".//a[@title='Cerrar']").click()
#                         load = True
#                     except Exception as error:
#                         print 'Error',contador,'en cerrar cuadro reactions comentario', error
#                         contador += 1
#                         pass
#
#             extraction_time_comment = datetime.datetime.today()
#             samples_comments.append([id_comment, message_comment, likes_comment, loves_comment, wows_comment, hahas_comment, sads_comment, angries_comment, thankfuls_comment,prides_comment, creation_time_comment, extraction_time_comment, parent_comment])
#
#
#             m += 1
#
#
#     # SEE ALL REVIEWS OF REVIEWS
#     load = False
#     contador = 0
#     while load is False and contador < 5:
#         try:
#             see_more_reviews_of_reviews = driver.find_element_by_xpath(".//div[@class=' UFIReplyList']")
#             print "see_more_reviews_of_reviews-->",see_more_reviews_of_reviews.text
#             see_more_reviews_of_reviews.click()
#             load = True
#         except Exception as error:
#             print 'Error',contador,'en see_more_reviews_of_reviews', error
#             contador += 1
#             pass
#
#     load = False
#     contador = 0
#     while load is False and contador < 5:
#         try:
#             reviews_reviews = driver.find_elements_by_xpath(".//div[@class=' UFIReplyList']/div[contains(@class,'UFIRow') and contains(@class,'UFIComment')]")
#             print 'reviews_reviews-->', reviews_reviews
#             load = True
#         except Exception as error:
#             print 'Error',contador,'en reviews_reviews', error
#             contador += 1
#             pass
#
#     m += 0
#     if reviews_reviews:
#         for review_reviews in reviews_reviews:
#             print 'Comentario de comentario numero', m
#             print 'aria label de la review-->',review_reviews.get_attribute('aria-label')
#             if review_reviews.get_attribute('aria-label') == 'Comentario':
#                 print 'Es comentario con identificador--> ', review_reviews.get_attribute('data-ft')
#             elif review_reviews.get_attribute('aria-label') == 'Respuesta a un comentario':
#                 print 'Es una respuesta al comentario--> ', review_reviews.get_attribute('data-ft')
#
#                 # CREATE TIME
#             load = False
#             contador = 0
#             while load is False and contador < 5:
#                 try:
#                     creation_time = review_reviews.find_elements_by_xpath(".//abbr")
#                     creation_time = creation_time[0].get_attribute('title')
#                     print 'creation_time-->',creation_time
#                     load = True
#                 except Exception as error:
#                     print 'Error',contador,'en creation_time', error
#                     contador += 1
#                     pass
#
#             load = False
#             contador = 0
#             while load is False and contador < 5:
#                 try:
#                     #review_text = review.find_element_by_xpath(".//span[@class='UFICommentBody']/span")
#                     review_reviews_text = review_reviews.find_element_by_xpath(".//span[@class='UFICommentBody']")
#
#                     print 'review'+str(m)+'-->',review_reviews_text.text
#                     load = True
#                 except Exception as error:
#                     print 'Error',contador,'en review_reviews', error
#                     contador += 1
#                     pass
#
#             #REACTIONS REVIEW_REVIEWS CLICK BUTTON
#             load = False
#             contador = 0
#             review_reviews_click = False
#             while load is False and contador < 5:
#                 try:
#                     review_reviews.find_element_by_xpath("//span[@class='_3t54']").click()
#                     load = True
#                     review_reviews_click = True
#
#                 except Exception as error:
#                     print 'Error',contador,'en click reactions comentario de comentario', error
#                     contador += 1
#                     pass
#             if review_click is True:
#                 #review_reviews.find_element_by_xpath(".//div[contains(@class,'UFICommentReactionsBling')]").click()
#                 load = False
#                 contador = 0
#                 try:
#                     body=driver.find_element_by_tag_name("body")
#                     print 'body-->', body
#                     load = True
#                 except Exception as error:
#                     print 'Error',contador,'get body', error
#                     time.sleep(3)
#                     contador += 1
#                     pass
#
#
#                 #REACTIONS REVIEW_REVIEWS
#                 load = False
#                 contador = 0
#                 reactions_review_reviews = None
#                 while load is False and contador < 5:
#                     try:
#                         print 'Estoy cogiendo REACTIONS REVIEW_REVIEWS'
#                         reactions_review_reviews = body.find_elements_by_xpath(".//li[contains(@class, '_ds-') and contains(@class, ' _45hc')]")
#                         print "reactions_review_reviews-->",reactions_review_reviews
#                         load = True
#                     except Exception as error:
#                         print 'Error',contador,'en reactions review_reviews', error
#                         contador += 1
#                         pass
#                     #Could be not load
#                     if not reactions_review_reviews and load:
#                         print 'No ha cargado. Se repite'
#                         load = False
#                         time.sleep(3)
#                     if contador >= 5:
#                         load = True
#                         print 'Se sigue. No se cargó'
#
#
#                 if reactions_review_reviews:
#                     print 'Estoy en REACTIONS REVIEW REVIEW'
#                     name = 'comentarios de un comentario'
#                     get_reactions(reactions_review_reviews, name, driver)
#
#                 # CLOSE REACTIONS REVIEW_REVIEWS SQUARE
#                 load = False
#                 contador = 0
#                 while load is False and contador < 5:
#                     try:
#                         body.find_element_by_xpath(".//a[@title='Cerrar']").click()
#                         load = True
#                     except Exception as error:
#                         print 'Error',contador,'en cerrar cuadro reactions comentario de comentario', error
#                         contador += 1
#                         pass
#             m += 1
#
#             extraction_time_comment = datetime.datetime.today()
#             samples_comments.append([id_comment, message_comment, likes_comment, loves_comment, wows_comment, hahas_comment, sads_comment, angries_comment, thankfuls_comment,prides_comment, creation_time_comment, extraction_time_comment, parent_comment])
#
#
#     creation_time = datetime.datetime.strptime(creation_time, '%d/%m/%Y %H:%M')
#     samples_posts.append([id, message, comments, shares,reproductions,likes,loves,wows,enjoyes,sads,angries,creation_time])
#
