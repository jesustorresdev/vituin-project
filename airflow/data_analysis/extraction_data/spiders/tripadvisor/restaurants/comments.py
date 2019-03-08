# # -*- coding: UTF-8 -*-
#
# import scrapy, datetime, os, re
# from extraction_data.items import TripAdvisorReviewRestaurantsItem
# from scrapy.mail import MailSender
# from scrapy.exceptions import CloseSpider
# from elasticsearch import Elasticsearch
#
# exceptionErrorItem=False
#
# MONTHS_SPANISH = {
#     'enero':"1",
#     'febrero':"2",
#     'marzo':"3",
#     'abril':"4",
#     'mayo':"5",
#     'junio':"6",
#     'julio':"7",
#     'agosto':"8",
#     'septiembre':"9",
#     'octubre':"10",
#     'noviembre':"11",
#     'diciembre':"12"
# }
#
# MONTHS_GERMAN = {
#     'Januar':"1",
#     'Februar':"2",
#     'März'.decode('UTF-8'):"3",
#     'April':"4",
#     'Mai':"5",
#     'Juni':"6",
#     'Juli':"7",
#     'August':"8",
#     'September':"9",
#     'Oktober':"10",
#     'November':"11",
#     'Dezember':"12"
# }
#
#
# MONTHS_FRENCH = {
#     'janvier':"1",
#     'février'.decode('UTF-8'):"2",
#     'marche':"3",
#     'avril':"4",
#     'mai':"5",
#     'juin':"6",
#     'juillet':"7",
#     'août'.decode('UTF-8'):"8",
#     'septembre':"9",
#     'octobre':"10",
#     'novembre':"11",
#     'décembre'.decode('UTF-8'):"12"
# }
#
# #TODO use loaders
# class TripadvisorSpider(scrapy.Spider):
#
#     name = "tripadvisor_restaurantes_reviews"
#     start_urls = []
#     es = Elasticsearch(
#        [
#           'elastic:vituinproject@elasticsearch:9200/',
#        ]
#     )
#     #SearchAllEstablishments
#     doc = {
#         'size' : 10000,
#         "query": {
#             "bool": {
#                 "filter": {
#                     "term" : { "place" : "Puerto de la Cruz" },
#                 }
#             }
#         }
#     }
#     res = es.search(index='index_tripadvisor_restaurantes', doc_type='unstructured', body=doc,scroll='1m')
#
#     #creamos lista de urls
#     for hit in res['hits']['hits']:
#             start_urls=start_urls + [hit["_source"]["url"]]
#
#     print('start_urls--->',len(start_urls))
#     print ''
#     print ''
#     print ''
#     print ''
#
#     new_urls = []
#     for url in start_urls:
#         new_urls.append(url.replace('co.uk','es'))
#         new_urls.append(url.replace('co.uk','de'))
#         new_urls.append(url.replace('co.uk','fr'))
#
#
#     start_urls.extend(new_urls)
#
#     def parse(self, response):
#
#
#         listErrors=[]
#         #Create the request
#         request = scrapy.Request(response.url, callback=self.parse_review)
#         es = Elasticsearch(
#             [
#                'elastic:vituinproject@elasticsearch:9200/',
#             ]
#         )
#
#         domain = response.url[24:response.url[24:].find('/')+24]
#         url = response.url if domain == 'co.uk' else response.url.replace('.'+domain,'.co.uk')
#         print('')
#         print('')
#         print('domain',domain)
#         print('url',url)
#         print('response.url',response.url)
#         print('')
#         print('')
#         print('')
#         #Make a query to Elasticsearch using the URL
#         res = es.search(index="index_tripadvisor_restaurantes", doc_type="unstructured",body={
#         	"query": {
#                 	"match_phrase": {
#                         	"url": url
#                         	}
#                 	}
#        		})
#
#
#         restaurant =  ''
#         has_review =  ''
#
#
#         for hit in res['hits']['hits']:
#
#             restaurant = hit["_source"]["name"]
#             has_review = hit["_source"]["has_review"]
#
#
#         request.meta['domain']=domain
#         #save some fields that we will send
#         request.meta['restaurant_name']=restaurant
#         #if there are comment. If there isnt, it doesnt pass
#         if has_review:
#                 yield request
#
#
#     #to get the full review content I open its page, because I don't get the full content on the main page
#     #there's probably a better way to do it, requires investigation
#     def parse_review(self, response):
#         listErrors=[] #if there is bugs
#         is_end = False
#         for rev in response.xpath('//div[starts-with(@class,"review-container")]'):
#             item = TripAdvisorReviewRestaurantsItem() #Class with Tripadvisor fields
#             item['id'] = rev.xpath('.//@data-reviewid')[0].extract()
#             item['url'] = response.url
#             item['restaurant_name']=response.meta['restaurant_name']
#
#
#             r_d=rev.xpath('.//span[starts-with(@class,"ratingDate")]/@title')
#             if r_d:
#                 item['review_date'] = r_d.extract()[0]
#                 if response.meta['domain'] == 'co.uk':
#                     date = datetime.datetime.strptime(item['review_date'], '%d %B %Y')
#                 elif response.meta['domain'] == 'es':
#                     date_str = item['review_date'].split()
#                     item['review_date'] = item['review_date'].replace(str(date_str[2]),MONTHS_SPANISH[date_str[2]])
#                     date = datetime.datetime.strptime(item['review_date'], '%d de %m de %Y')
#                 elif response.meta['domain'] == 'de':
#                     date_str = item['review_date'].split()
#                     item['review_date'] = item['review_date'].replace(date_str[1],MONTHS_GERMAN[date_str[1]])
#                     date = datetime.datetime.strptime(item['review_date'], '%d. %m %Y')
#                 elif response.meta['domain'] == 'fr':
#                     date_str = item['review_date'].split()
#                     item['review_date'] = item['review_date'].replace(date_str[1],MONTHS_FRENCH[date_str[1]])
#                     date = datetime.datetime.strptime(item['review_date'], '%d %m %Y')
#
#                 now = datetime.datetime.combine(datetime.datetime.today(), datetime.time(0, 0))
#                 item['review_date'] = date
#
# #                if (now - date).days < 100000:
#                 if (now - date).days < 15:
#                     print ''
#                     print ''
#                     print ''
#                     print ''
#                     print ''
#                     print '(now - date).days',(now - date).days
#                     print '(now - date).days',(now - date).days
#                     print '(now - date).days',(now - date).days
#                     print '(now - date).days',(now - date).days
#                     print '(now - date).days',(now - date).days
#                     print ''
#                     print ''
#                     print ''
#                     print ''
#                     print ''
# #                    t = response.xpath('//div[@class="quote isNew"]/a/span/text()')
#                     t = rev.xpath('.//div[starts-with(@class,"quote")]/a/span/text()')
#                     if t:
#                          item['title'] = t[0].extract()
#                     else:
#                          listErrors=listErrors + ['title']
#
#                     c = rev.xpath('.//div[@class="entry"]/p/text()')
#                     if c:
#                          item['content'] = c.extract()
#                     else:
#                          listErrors=listErrors + ['content']
#                     print '++++++++++++++++++++++'
#                     print '++++++++++++++++++++++'
#                     print '++++++++++++++++++++++'
#                     print '++++++++++++++++++++++'
#                     print t, c
#                     print '++++++++++++++++++++++'
#                     print '++++++++++++++++++++++'
#                     print '++++++++++++++++++++++'
#                     print '++++++++++++++++++++++'
#
#                     # r_l = rev.xpath('.//div[@class="location"]/span/text()')
#                     # if r_l:
#                     #     item['reviewer_location']  = r_l[0].extract()
#
#                     #if there is bugs to extract fields
#                     if len(listErrors)>0:
#                         #self.send_email(listErrors)
#                         print '-----------------------'
#                         print '-----------------------'
#                         print '-----------------------'
#                         print '-----------------------'
#                         print '-----------------------'
#                         print '-----------------------'
#                         print '-----------------------'
#                         print '-----------------------'
#                         print '-----------------------'
#                         print '-----------------------'
#                         print '-----------------------'
#                         print '-----------------------'
#                         print '-----------------------'
#                         print '-----------------------'
#                         print '-----------------------'
#                         print '-----------------------'
#                         print '-----------------------'
#                         print '-----------------------'
#                         print '-----------------------'
#                         print '-----------------------'
#                         print '-----------------------'
#                         print '-----------------------'
#                         print '-----------------------'
#                         print listErrors
#                         # print 'response --> ', response
#                         # print 'title ', item['title']
#                         # print 'entry ---> ', rev.xpath('.//div[@class="entry"]')
#                         # print 'entry/p ---> ', rev.xpath('.//div[@class="entry"]/p/text()')
#                         # print 'partial entry ---> ', rev.xpath('.//p[@class="partial_entry"]')
#                         # raise CloseSpider('Error Spider in Parse_Review general')
#                         # break
#
#                     yield item
#
#                 else:
#                     is_end = True
#                     break
#
#             else:
#                 listErrors=listErrors + ['review_date']
#                 print listErrors
#                 print 'HOOOOOOOOOOOOOOOOOOOOOOOOOOLA'
#                 print 'HOOOOOOOOOOOOOOOOOOOOOOOOOOLA'
#                 print 'HOOOOOOOOOOOOOOOOOOOOOOOOOOLA'
#                 print 'HOOOOOOOOOOOOOOOOOOOOOOOOOOLA'
#                 print 'HOOOOOOOOOOOOOOOOOOOOOOOOOOLA'
#                 print response
#                 print 'HOOOOOOOOOOOOOOOOOOOOOOOOOOLA'
#                 print 'HOOOOOOOOOOOOOOOOOOOOOOOOOOLA'
#                 print 'HOOOOOOOOOOOOOOOOOOOOOOOOOOLA'
#                 print 'HOOOOOOOOOOOOOOOOOOOOOOOOOOLA'
#                 print 'HOOOOOOOOOOOOOOOOOOOOOOOOOOLA'
#                 print 'HOOOOOOOOOOOOOOOOOOOOOOOOOOLA'
#                 print 'HOOOOOOOOOOOOOOOOOOOOOOOOOOLA'
#                 print 'HOOOOOOOOOOOOOOOOOOOOOOOOOOLA'
#                 #self.send_email(listErrors)
#                 raise CloseSpider('Error Spider in Parse_Review date')
#
#         if is_end is False:
#             try:
#                 url = response.xpath('.//div[@class="unified ui_pagination "]/a[contains(@class,"next")]/@href')[0].extract()
#                 print('URL-->', url)
#                 response.urljoin(url)
#                 url = 'https://www.tripadvisor.'+response.meta['domain']+url
#                 print('22222222',url)
#                 print('22222222',url)
#                 print('22222222',url)
#                 print('22222222',url)
#                 request = scrapy.Request(url, self.parse_review)
#                 #We send the meta data to the request of the next pages
#                 request.meta['restaurant_name']=response.meta['restaurant_name']
#                 request.meta['domain']=response.meta['domain']
#                 print('TODO BIEN')
#                 print('TODO BIEN')
#                 print('TODO BIEN')
#                 print('TODO BIEN')
#                 print('TODO BIEN')
#                 print('TODO BIEN')
#                 print('TODO BIEN')
#                 yield request
#             except:
#                 print('SE ACABO',response.url)
#                 print('SE ACABO',response.url)
#                 print('SE ACABO',response.url)
#                 print('SE ACABO',response.url)
#                 print('SE ACABO',response.url)
#         else:
#                 print('SE ACABO',response.url)
#                 print('SE ACABO',response.url)
#                 print('SE ACABO',response.url)
#                 print('SE ACABO',response.url)
#                 print('SE ACABO',response.url)
#
#
#
#     #
#     #
#     # def send_email(self, listErrors):
#     #
#     #     global exceptionErrorItem
#     #
#     #     if exceptionErrorItem == False:
#     #         message = 'Al hacer el scrapy de Tripadvisor, no existen los campos '
#     #
#     #         for elementError in listErrors:
#     #             message = message + elementError + ', '
#     #
#     #         message = re.sub(', $', '.' , message)
#     #
#     #         #Send a email saying if some bug have ocurred
#     #         mailer = MailSender(mailfrom="erroresSpider@gmail.com",smtphost="smtp.gmail.com",smtpport=587,smtpuser="erroresSpider@gmail.com",smtppass="errores1234")
#     #         mailer.send(to=["erroresSpider@gmail.com"], subject='Errores en el Spider', body=message)
#     #         exceptionErrorItem=True
#     #
#     #         #In this case we delete the extract file until this moment
#     #         os.remove('itemsTripadvisor.csv')
