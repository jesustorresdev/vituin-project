# -*- coding: utf-8 -*-

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


FIELDS = ['Total', 'Media por post']

ES = Elasticsearch(
    [
        'elasticsearch:9200/'
    ]
)

FILE_COUNT = 0
ACTIONS = []

EXIST_INDEX = True
FIRST_ITERATION = False
ELASTICSEARCH_INDEX_SEARCHED='index_comments_facebook_selenium'
ELASTICSEARCH_INDEX='index_comments_stats_by_date'
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

for field in FIELDS:
    dates = []
    res = utils.search_elastic(ELASTICSEARCH_INDEX_SEARCHED, ELASTICSEARCH_DOC_TYPE)
    field = 'Media por post'
    for entry in res:
        date = entry['_source']['creation_time']
        date = date[:10]
        if date not in dates:
            dates.append(date)
            for filter_field in ["likes", "loves", \
                         "wows", "hahas", "sads", "angries",]:
                constraints ={
                    filter_field : field,
                }

                set_options = {}

                set_options.update({
                    'filter-selected' : filter_field,
                })

                res = utils.search_elastic(ELASTICSEARCH_INDEX_SEARCHED, ELASTICSEARCH_DOC_TYPE)

                fields_restrictions = {'creation_time':date}
                fix_restrictions = utils.add_restriction(constraints, set_options, fields_restrictions)
                constraints = {'creation_time':[date]}
                set_options = fix_restrictions[1]
                if field == FIELDS[0]:
                    data = utils.get_sum_field(res, filter_field, constraints = constraints, name_options = set_options, date = 31)
                else:
                    sum = utils.get_sum_field(res, filter_field, constraints = constraints, name_options = set_options, date = 31)
                    count = utils.get_count(res, filter_field, constraints = constraints, name_options = set_options, date = 31)
                    data = float(sum) / float(count)

                # exit()
                item = {}
                item['measure'] = field

                item['type'] = filter_field
                item['value'] = float(data)
                item['period'] = 'Por día'.decode('UTF-8')
                item['date'] = date

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
                FILE_COUNT +=1


if FILE_COUNT > 0:
    if EXIST_INDEX is False:
        es_new = utils.set_properties(NAMES_ITEM_FINAL, ELASTICSEARCH_DOC_TYPE, ELASTICSEARCH_INDEX)
        helpers.bulk(es_new, ACTIONS)
    else:
        helpers.bulk(ES, ACTIONS)
    print "leftovers"
    print "indexed %d" %cont_id

