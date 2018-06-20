# -*- coding: utf-8 -*-
import datetime
import hashlib
import generals_functions
from elasticsearch import Elasticsearch
from elasticsearch import helpers
es = Elasticsearch(
    [
        'elasticsearch:9200/'
    ]
)

fs_change = {}

def call_elastic(name_index,es):


    #Search the last indexed id
    doc = {
        'query': {
            'match_all' : {}
        }
    }

    exist_index = 1
    try:
        res = es.search(index=name_index, body=doc, size=0)
        #The next element indexed going to be the next id doesn't used
        cont_id = int(res['hits']['total'])
        index_elastic = {
            'cont_id' : cont_id,
            'exist_index' : 1,
        }
    except:
        #If it's the first gruop of elements indexed
        print("First indexed")
        cont_id = 0
        index_elastic = {
            'cont_id' : cont_id,
            'exist_index' : 0,
        }

    return index_elastic

def indexed(name_index,type_index, path_to_start, metadata,fields_to_get, **kwords):

    index_elastic=call_elastic(name_index,es)
    cont_id = index_elastic["cont_id"]

    # #Are there attributes_to_fixed?
    # try:
    #     if kwords["attributes_to_fixed"]:
    #         global attr_fix
    #         attr_fix = kwords["attributes_to_fixed"]
    # except:
    #     pass
    #
    # #Are there arguments to split?
    # try:
    #     if kwords["attribute_to_split"]:
    #         global attr_spl
    #         attr_spl = kwords["attribute_to_split"]
    # except:
    #     pass
    #
    # #Are there arguments to split?
    # try:
    #     if kwords["field_region"]:
    #         global field_region
    #         field_region = kwords["field_region"]
    # except:
    #     pass

    #Are name fields to change?
    global fs_change
    try:
        if kwords["fields_to_change"]:
            fs_change = kwords["fields_to_change"]
    except:
        pass

    elements = get_path(path_to_start,metadata)
    count = 0
    actions = []


    for element in elements:

        item = {}
        str_key = ''
        item["insert_time"]=datetime.datetime.today()

        if fields_to_get:
            for field in fields_to_get:
                #if exist field to change
                if element[field] in fs_change:
                    value = generals_functions.change_field_name_json(element[field],fs_change)
                else:
                    value = element[field]

                item[field] = value
                str_key += item[field]

        #if fields_to_get is empty we're going to get all fields
        else:
            for field in element:
                #if exist field to change
                if element[field] in fs_change:
                    value = generals_functions.change_field_name_json(element[field],fs_change)
                else:
                    value = element[field]

                item[field] = value
                str_key += item[field]

        key =  hashlib.md5(str_key.encode('utf-8')).hexdigest()
        item["key"] = key
        # print item

        action = {
            "_index": name_index,
            "_type": type_index,
            "_id": int(cont_id),
            "_source": item
        }

        acts = append_Action(index_elastic["exist_index"], key, name_index, action, actions)

        if acts:                       #if actions was append
            actions = acts
            cont_id += 1
            count += 1


    if count > 0:
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

def append_Action(exist_index, key, name_index, action, actions):
    if exist_index == 1:
        # exist_element = '0'               #Does it exist element in index?
        global es

        #Search if there is same data in the index
        res = es.search(index=name_index, body={
            "query": {
                "match_phrase": {
                    "key": key #Use the key to compare
                }
            }
        })

        if res['hits']['hits'] == []: #If there isn't result
            actions.append(action)
            return actions
    else:
        actions.append(action)
        return actions