# -*- coding: utf-8 -*-
import datetime
import hashlib
import generals_functions
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import generals_functions
es = Elasticsearch(
    [
        'elasticsearch:9200/'
    ]
)

fs_change = {}
attr_spl_r_s = {}
fix_fields_in_one = {}
attr_fix = {}

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
    first_iteration = True


    attr_fix = {}
    #Are there attributes_to_fixed?
    try:
        if kwords["attributes_to_fixed"]:
            attr_fix = kwords["attributes_to_fixed"]
    except:
        pass
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
    #

    attr_spl_r_s = {}
    #Are there arguments to split and delete substring?
    try:
        if kwords["attribute_to_split_remove_string"]:
            attr_spl_r_s = kwords["attribute_to_split_remove_string"]
    except:
        pass

    fix_fields_in_one = {}
    #Are there arguments with fix fields in only one?
    try:
        if kwords["fix_fields_in_one"]:
            fix_fields_in_one = kwords["fix_fields_in_one"]
    except:
        pass

    #Are name fields to change?
    global fs_change
    fs_change = []
    try:
        if kwords["fields_to_change"]:
            fs_change = kwords["fields_to_change"]
    except:
        pass

    #Are month to change?
    global change_months
    change_months = []
    try:
        if kwords["change_months"]:
            change_months = kwords["change_months"]
    except:
        pass

    elements = get_path(path_to_start,metadata)
    count = 0
    actions = []

    #Fields to get
    if fields_to_get:
        fields = fields_to_get
    #if fields_to_get is empty we're going to get all fields
    else:
        fields = get_all_fields(elements[0])

    elements_to_fix_in_one=[]
    fields_to_fix_elements=[]
    for field in fix_fields_in_one:
        fields_to_fix_elements.append(field['name'])
        elements_to_fix_in_one.append(field['names_items_to_fix_in_one'])
    # if fix_fields_in_one:
    #     elements_to_fix_in_one = fix_fields_in_one['names_items_to_fix_in_one']


    for element in elements:

        item = {}
        str_key = ''
        items_to_fix = []

        for field in fields:
            #Fix all fields_to_fix_elements in onlye one field
            if field in fields_to_fix_elements:
                items_to_fix.extend(generals_functions.fix_fields_in_only_one(field,fields_to_fix_elements,elements_to_fix_in_one,element,fs_change = fs_change))


            #There aren't fields to fix in one
            else:
                if element[field] in fs_change:
                    field_value = generals_functions.change_field_name_json(element[field],fs_change)
                else:
                    field_value = element[field]

                #Save the item
                try:
                    item[field] = str(field_value.decode('UTF-8'))
                except:
                    item[field] = field_value

                item[field] = field_value


        for item_to_fix in items_to_fix:
            tmp_item = {}
            tmp_item.update(item)
            tmp_item.update(item_to_fix)

            # print 'fecha--->', item['fecha']
            #if exist field to remove substring
            if attr_spl_r_s:
                tmp_item = generals_functions.getAttributes_Split_Remove_String(tmp_item,fields, attr_spl_r_s)
            if attr_fix:
                tmp_item=generals_functions.getAttribute_Fixed(tmp_item,attr_fix)

            #If there are fields with months to change
            if change_months:
                tmp_item = generals_functions.change_months(tmp_item, change_months)

            #Generate key
            for field in tmp_item:
                try:
                    str_key += str(tmp_item[field])
                except:
                    str_key += tmp_item[field]


            key =  hashlib.md5(str_key.encode('utf-8')).hexdigest()
            tmp_item["key"] = key



            tmp_item["insert_time"]=datetime.datetime.today()

            if first_iteration:
                global names_item_final
                names_item_final = generals_functions.get_names_item_final(tmp_item)
                first_iteration=False

            action = {
                "_index": name_index,
                "_type": type_index,
                "_id": int(cont_id),
                "_source": tmp_item
            }

            acts = append_Action(index_elastic["exist_index"], key, name_index, action, actions)

            if acts:                       #if actions was append
                actions = acts
                cont_id += 1
                count += 1


    if count > 0:
        if index_elastic['exist_index'] is 0:
            global names_item_final
            es_new = generals_functions.set_properties(names_item_final, type_index, name_index)
            helpers.bulk(es_new, actions)
        else:
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

def get_all_fields(element):
    return [field for field in element]
