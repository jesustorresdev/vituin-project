import sys
import unicodecsv as csv
import json
import datetime

from elasticsearch import Elasticsearch
from elasticsearch import helpers
import utils
#takes two arguments:
#   the name of the file to index
#   the starting index for the id
#       the ids shouldn't overlap or you will replace existing opinion units
#IMPORTANT: before indexing opinion units you must index the parent reviews

filename =  sys.argv[1]

place_type = ["Puerto de la Cruz", "Tenerife","Canarias", "Adeje"]
place = place_type[int(sys.argv[2])]

F = open(filename)

ES = Elasticsearch(
   [
     'elasticsearch:9200/'
   ]
)

FILE_COUNT = 0
ACTIONS = []

EXIST_INDEX = True
FIRST_ITERATION = False
ELASTICSEARCH_INDEX='index_tripadvisor_restaurantes'
ELASTICSEARCH_DOC_TYPE='unstructured'
NAMES_ITEM_FINAL = []
#Search the last indexed id
doc = {
        'size' : 10000,
        'query': {
             'match_all' : {}
         }
       }
try:
    res = ES.search(index=ELASTICSEARCH_INDEX, body=doc, size=0)
    #The next element indexed going to be the next id doesn't used
    cont_id = int(res['hits']['total'])

except:
    #If it's the first gruop of elements indexed
    print("First indexed")
    cont_id = 0
    EXIST_INDEX = False
    FIRST_ITERATION = True
    EXIST_INDEX = False
    FIRST_ITERATION = True
for row in csv.reader(F):

    if(FILE_COUNT!=0):
        item={}

        try:
            item['service']=float(row[0])#service
        except:
            item['service']=float(-1)
        try:
            item['atmosphere']=float(row[1])#atmosphere
        except:
            item['atmosphere']=float(-1)
        item['name']=row[2]#name
        item['extended']=row[3]#extended
        try:
            item['food']=float(row[4])#food
        except:
            item['food']=float(-1)
        item['has_review']=int(row[5])#has_review
        item['locality']=row[6]#locality
        item['url']=row[7]#url
        item['ratingExcellent']=int(row[8])#ratingExcelent
        try:
            item['value']=float(row[9])#value
        except:
            item['value']=float(-1)
        item['phone']=row[10]#phone
        item['ratingVeryGood']=int(row[11])#ratingVeryGood
        item['score']=float(row[12])#score
        item['ratingAverage']=int(row[13])#ratingAverage
        item['ratingTerrible']=int(row[14])#ratingTerrible
        if row[15] == "":
            row[15]="None"
        item['price']=row[15]#price
        item['street_address']=row[16]#street_address
        item['ratingpoor']=int(row[17])#ratingpoor
        item['lat']=row[18]#lon
        item['lng']=row[19]#lng
        # item['key']=str(row[20])#key
        item['place'] = place

        if not EXIST_INDEX and FIRST_ITERATION is True:
            NAMES_ITEM_FINAL = utils.get_names_item_final(item)
            FIRST_ITERATION=False

        item['upload_time']=datetime.datetime.today()

        action = {
            "_index": ELASTICSEARCH_INDEX,
            "_type": ELASTICSEARCH_DOC_TYPE,
            "_id": cont_id,
            "_source": item
                }

        ACTIONS.append(action)
        cont_id += 1

    FILE_COUNT += 1

if FILE_COUNT > 0:
    if EXIST_INDEX is False:
        es_new = utils.set_properties(NAMES_ITEM_FINAL, ELASTICSEARCH_DOC_TYPE, ELASTICSEARCH_INDEX)
        helpers.bulk(es_new, ACTIONS)
    else:
        helpers.bulk(ES, ACTIONS)
    print "leftovers"
    print 'indexed %d' % cont_id


