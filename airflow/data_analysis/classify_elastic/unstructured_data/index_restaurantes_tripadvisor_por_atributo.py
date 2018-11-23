# -*- coding: UTF-8 -*-

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


PLACES = ["Puerto de la Cruz", "Tenerife", "Canarias"]


ES = Elasticsearch(
    [
        'elasticsearch:9200/'
    ]
)

FILE_COUNT = 0
ACTIONS = []

EXIST_INDEX = True
FIRST_ITERATION = False
ELASTICSEARCH_INDEX_SEARCHED='index_tripadvisor_restaurantes'
ELASTICSEARCH_INDEX='index_restaurantes_tripadvisor_numeros_por_atributo'
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

filters_fields = ['price', 'score']

for filter_field in filters_fields:
    for place in PLACES:

        constraints ={
            filter_field : place,
        }

        set_options = {}

        set_options.update({
            'filter-selected' : filter_field,
        })

        res = utils.search_elastic(ELASTICSEARCH_INDEX_SEARCHED, ELASTICSEARCH_DOC_TYPE)
        fields_restrictions = {'place':place}
        fix_restrictions = utils.add_restriction(constraints, set_options, fields_restrictions)
        constraints = fix_restrictions[0]
        set_options = fix_restrictions[1]
        data = {}
        data.update({constraints[set_options['restriction1']]:[]})                                                     #For each value in radioItem we create a group of values results
        for entry in res:
            if entry['_source'][set_options['restriction1']] == constraints[set_options['restriction1']]:            #If the restriction is satisfied
                data[constraints[set_options['restriction1']]].append(entry['_source'][set_options['filter-selected']])
        data = utils.get_count_and_names(data, constraints[set_options['restriction1']])


        for i in range(0,len(data[0][place])):
            item = {}
            item['measure'] = filter_field
            item['place'] = place
            item['value'] = int(data[0][place][i])
            item['type'] = data[1][i] if data[1][i] != -1 else 'No se puntuó'.decode('UTF-8')
            if not EXIST_INDEX and FIRST_ITERATION is True:
                NAMES_ITEM_FINAL = utils.get_names_item_final(item)
                FIRST_ITERATION=False

            item['upload_date']=datetime.datetime.today()
            print item
            action = {
                "_index": ELASTICSEARCH_INDEX,
                "_type": ELASTICSEARCH_DOC_TYPE,
                "_id": cont_id,
                "_source": item
            }

            ACTIONS.append(action)

            cont_id += 1
            FILE_COUNT +=1
        print('fin')


if FILE_COUNT > 0:
    if EXIST_INDEX is False:
        es_new = utils.set_properties(NAMES_ITEM_FINAL, ELASTICSEARCH_DOC_TYPE, ELASTICSEARCH_INDEX)
        helpers.bulk(es_new, ACTIONS)
    else:
        helpers.bulk(ES, ACTIONS)
    print "leftovers"
    print "indexed %d" %cont_id

