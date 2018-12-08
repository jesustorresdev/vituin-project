
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

# filename =  sys.argv[1]

# place_type = ["Puerto de la Cruz", "Tenerife","Canarias", "Adeje"]
# place = place_type[int(sys.argv[2])]

PLACES = ["Puerto de la Cruz", "Tenerife","Canarias"]
FIELDS = ['Total', 'Media por establecimientos']


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
ELASTICSEARCH_INDEX='index_tripadvisor_number_reviews'
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

filter_field = 'has_review'
for field in FIELDS:


    constraints ={
        filter_field : field,
    }

    set_options = {}

    set_options.update({
        'filter-selected' : filter_field,
    })

    res = utils.search_elastic(ELASTICSEARCH_INDEX_SEARCHED, ELASTICSEARCH_DOC_TYPE)

    fields_restrictions = {'place':PLACES}
    fix_restrictions = utils.add_restriction(constraints, set_options, fields_restrictions)
    constraints = fix_restrictions[0]
    set_options = fix_restrictions[1]
    exist_restriction = True
    i = 1
    while exist_restriction:
        if not 'restriction'+str(i) in set_options:
            exist_restriction = False
        else:
            for constraint in constraints[set_options['restriction'+str(i)]]:
                if field == FIELDS[0]:
                    data = utils.get_sum_field(res, filter_field, constraint = constraint, name_options = set_options)
                else:
                    sum = utils.get_sum_field(res, filter_field, constraint = constraint, name_options = set_options)
                    count = utils.get_count(res, filter_field, constraint = constraint, name_options = set_options)
                    if count!=0:
                        data = float(sum) / float(count)
                    else:
                        data = 0


                item = {}
                item['measure'] = field

                item['place'] = constraint
                item['value'] = int(data)

                if not EXIST_INDEX and FIRST_ITERATION is True:
                    NAMES_ITEM_FINAL = utils.get_names_item_final(item)
                    FIRST_ITERATION=False
                print item
                item['upload_date']=datetime.datetime.today()
                action = {
                    "_index": ELASTICSEARCH_INDEX,
                    "_type": ELASTICSEARCH_DOC_TYPE,
                    "_id": cont_id,
                    "_source": item
                }

                ACTIONS.append(action)

                cont_id += 1
            i+=1
    FILE_COUNT +=1


if FILE_COUNT > 0:
    if EXIST_INDEX is False:
        es_new = utils.set_properties(NAMES_ITEM_FINAL, ELASTICSEARCH_DOC_TYPE, ELASTICSEARCH_INDEX)
        helpers.bulk(es_new, ACTIONS)
    else:
        helpers.bulk(ES, ACTIONS)
    print "leftovers"
    print "indexed", str(cont_id), ",", ELASTICSEARCH_DOC_TYPE

