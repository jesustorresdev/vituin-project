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
filename_con =  sys.argv[2]


F = open(filename)
f_con = open(filename_con)
reference = ["id_homeway",
             "type_residence",
             "price",
             "numberReviews",
             "mainBubbles",
             "capacity",
             "rooms",
             "bathrooms",
             "m2",
             "min_stay",
             "lng",
             "lat",
             "place"
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
ELASTICSEARCH_INDEX='index_tripadvisor_hoteles'
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
    res = ES.search(index='index_list_description_homeway', body=doc, size=0)
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
            tmp_row = None
            for row_con in csv.reader(f_con):
                print row[0], ',', row_con[0]
                if row[0] == row_con[0]:
                    tmp_row = row_con[0]
                    break
            print 'tmp_row-->', tmp_row
            if tmp_row is None:
                break

            for i in range(len(reference)):
                if reference[i] == 'lat':
                    item['lat'] = tmp_row['lat']
                elif reference[i] == 'lng':
                    item['lng'] = tmp_row['lng']
                else:
                    item[reference[i]] = row[i]

            item['upload_date']=datetime.datetime.today()
            print 'item-->', item
            import sys
            sys.exit()
            res ={}
            try:
                res = ES.search(index="index_list_description_homeway", body={
                    "query": {
                        "match_phrase": {
                            "id_homeway": item['id_homeway'] #Use the key to compare
                        }
                    }
                })
            except:
                pass

            if not res or res['hits']['hits'] == []: #If there isn't result

                if not EXIST_INDEX and FIRST_ITERATION is True:
            NAMES_ITEM_FINAL = utils.get_names_item_final(item)
            FIRST_ITERATION=False

        action = {
                    "_index": "index_list_description_homeway",
                    "_type": ELASTICSEARCH_DOC_TYPE,
                    "_id": cont_id,
                    "_source": item
                }

                ACTIONS.append(action)

                cont_id += 1
            else:
                print 'repeat ', count
                for element in res['hits']['hits']['_source']:
                    if item[element] == res['hits']['hits']['_source'][element]:
                        same = False

                if same is False:

                    if not EXIST_INDEX and FIRST_ITERATION is True:
            NAMES_ITEM_FINAL = utils.get_names_item_final(item)
            FIRST_ITERATION=False

        action = {
                        "_index": "index_list_description_homeway",
                        "_type": ELASTICSEARCH_DOC_TYPE,
                        "_id": cont_id,
                        "_source": item
                    }

                    ACTIONS.append(action)

                    cont_id += 1

        except Exception as error:
            print 'Error', error, ', en', count
            print '------'
            pass

    FILE_COUNT += 1



# if FILE_COUNT > 0:
    if EXIST_INDEX is False:
        es_new = utils.set_properties(NAMES_ITEM_FINAL, ELASTICSEARCH_DOC_TYPE, ELASTICSEARCH_INDEX)
        helpers.bulk(es_new, ACTIONS)
    else:
        helpers.bulk(ES, ACTIONS)#     helpers.bulk(ES, ACTIONS)
#     print "leftovers"
#     print "indexed %d" %cont_id

