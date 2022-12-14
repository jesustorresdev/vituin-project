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
reference = ["id_atraveo",
             "url",
             "price",
             "type_residence",
             "numberReviews",
             "mainBubbles",
             "lat",
             "lng",
             ]

ES = Elasticsearch(
    [
        'elasticsearch:9200/'
    ]
)

FILE_COUNT = 0
ACTIONS = []

EXIST_INDEX = True
FIRST_ITERATION = False
ELASTICSEARCH_INDEX='index_list_homes_atraveo'
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

j = 0
for row in csv.reader(F):
    j +=1
    if(FILE_COUNT!=0):
        item = {}

        try:
            for i in range(len(reference)):
                item[reference[i]] = row[i]
            item['place'] = place

            item['search_date']="08/10/2018"
            item['stay'] = '7 noches'
            res ={}
            try:
                res = ES.search(index=ELASTICSEARCH_INDEX, body={
                    "query": {
                        "match_phrase": {
                            "id_atraveo": item['id_atraveo'] #Use the key to compare
                        }
                    }
                })
            except:
                pass

            if not res or res['hits']['hits'] == []: #If there isn't result

                if not EXIST_INDEX and FIRST_ITERATION is True:
                    NAMES_ITEM_FINAL = utils.get_names_item_final(item)
                    FIRST_ITERATION=False

                item['upload_date']=datetime.datetime.today()

                action = {
                    "_index": "index_list_homes_atraveo",
                    "_type": ELASTICSEARCH_DOC_TYPE,
                    "_id": cont_id,
                    "_source": item
                }

                ACTIONS.append(action)

                cont_id += 1
            else:
                print 'repeat ', FILE_COUNT

        except Exception as error:
            print 'Error', error, ', en', FILE_COUNT
            print '------'
            pass

    FILE_COUNT += 1



if FILE_COUNT > 0:
    if EXIST_INDEX is False:
        es_new = utils.set_properties(NAMES_ITEM_FINAL, ELASTICSEARCH_DOC_TYPE, ELASTICSEARCH_INDEX)
        helpers.bulk(es_new, ACTIONS)
    else:
        helpers.bulk(ES, ACTIONS)
    print "leftovers"
    print "indexed %d" %cont_id

