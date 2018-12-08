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

place =  sys.argv[1]

place_names = ["Puerto de la Cruz", "Tenerife","Canarias", "Adeje"]

reference_description = ["id_homeway",
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

reference_homes = [
    "id_homeway",
    "title",
    "url",
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
ELASTICSEARCH_INDEX='index_list_homeway'
ELASTICSEARCH_INDEX_LIST_HOMES='index_list_homes_homeway'
ELASTICSEARCH_INDEX_LIST_DESCRIPTION='index_list_description_homeway'
ELASTICSEARCH_DOC_TYPE='unstructured'
MAIN_FIELD='id_homeway'
NAMES_ITEM_FINAL = []

# #Search the last indexed id
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

number_entries_homes = ES.search(index=ELASTICSEARCH_INDEX_LIST_HOMES, body=doc, size=0)
res_homes = utils.search_elastic(ELASTICSEARCH_INDEX_LIST_HOMES, ELASTICSEARCH_DOC_TYPE)

for row_home in res_homes:

    row_home = row_home['_source']
    item = {}

    for entry in reference_homes:
        item[entry] = row_home[entry]

    #SearchAllEstablishments
    doc = {
        "query": {
            "match_phrase": {
                MAIN_FIELD: item[MAIN_FIELD]
            }
        },
        'sort': [
            {"_id": "asc"}
        ]
    }


    res_description = ES.search(index=ELASTICSEARCH_INDEX_LIST_DESCRIPTION, doc_type="unstructured", body=doc, size=1)

    #if exists row_description
    try:
        row_description = res_description['hits']['hits'][0]['_source']

        for entry in reference_description:
            item[entry] = row_description[entry]
    except:
        for entry in reference_description:
            item[entry] = ''

    if not 'place' in item:
        item['place'] = place_names[int(place)]

    if not EXIST_INDEX and FIRST_ITERATION is True:
        NAMES_ITEM_FINAL = utils.get_names_item_final(item)
        FIRST_ITERATION=False

    item['upload_date']=datetime.datetime.today()

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
    print "indexed %d" %cont_id

