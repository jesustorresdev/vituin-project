# -*- coding: utf-8 -*-
import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers
es = Elasticsearch(
    [
        'elasticsearch:9200/'
    ]
)


def indexed(name_index,type_index, path_to_start, metadata,fields_to_get):

    #Search if there is index
    doc = {
        'query': {
            'match_all' : {}
        }
    }

    try:
        res = es.search(index=name_index, body=doc, size=0)
        exist_index = True
    except:
        exist_index = False

    if exist_index is False:

        elements = get_path(path_to_start,metadata)
        count = 0
        actions = []

        for element in elements:

            item = {}
            item["insert_time"]=datetime.datetime.today()

        if fields_to_get:
            for field in fields_to_get:
                item[field] = element[field]
        #if fields_to_get is empty we're going to get all fields
        else:
            for field in element:
                item[field] = element[field]

            action = {
                "_index": name_index,
                "_type": type_index,
                "_id": int(count),
                "_source": item
            }

            count += 1

        actions.append(action)

        helpers.bulk(es, actions)
        print "leftovers"
        print "indexed %d" %count

    else:

        print "Not indexed"

def get_path(path, metadata):
    start_field = metadata
    for element in path:
        start_field = start_field[element]
    return start_field
