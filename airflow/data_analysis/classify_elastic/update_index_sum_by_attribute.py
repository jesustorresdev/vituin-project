# -*- coding: UTF-8 -*-

from elasticsearch import Elasticsearch
from elasticsearch import helpers
import copy
import datetime
import hashlib

global es
es = Elasticsearch(
    [
        'elastic:vituinproject@elasticsearch:9200/',
    ]
)

#Return all elements of one index
def search_elastic(index,doc_type, field, field_value):

    #Elasticsearch
    global es

    #SearchAllEstablishments
    doc = {
        'size' : 10000,
        'query': {
            # 'match_all' : {}
            # "term" : { 'place_origin_region': '"islas británicas"'}
            "match_phrase" : {
                field: field_value
            }
        },
        'sort': [
            {"_id": "asc"}
        ]
    }


    result = es.search(index=index, doc_type=doc_type, body=doc,scroll='1m')

    numberElements = es.search(index=index, doc_type=doc_type, body=doc,size=0)['hits']['total']    #The number of Elements searched

    elements = []
    count = 0

    for hit in result['hits']['hits']:            #Append the elements in the array
        elements.append(hit)
        count += 1

    pos = count - 1                               #Last pos appended
    numberElements -= count

    #Elastic only allow search 10000 elements in a called. If the table contains more element \
    # its necessary to do a recursive called
    while numberElements > 0:


        doc = {
            'size':10000,
            'query': {
                # 'match_all' : {}
                # "term" : { field: field_value}
                "match_phrase" : {
                    field: field_value
                }
            },
            "search_after": [elements[pos]['_id']],  #It allows to search since a determinate position
            "sort": [
                {"_id": "asc"}
            ]
        }

        result = es.search(index=index, doc_type=doc_type, body=doc)

        numberElements -= count
        count = 0
        for hit in result['hits']['hits']:        #Append the elements in the array
            elements.append(hit)
            count += 1

        pos += count                              #Last pos append


    elements=sorted(elements, key=lambda k: int(k['_id']))

    return elements

#Return cont_id
def last_id_index(name_index):

    #Elasticsearch
    global es

    #Search the last indexed id
    doc = {
        'query': {
            'match_all' : {}
        }
    }


    res = es.search(index=name_index, body=doc, size=0)
    #The next element indexed going to be the next id doesn't used
    cont_id = int(res['hits']['total'])

    return cont_id




def sum_values(elements, fields_to_change, other_fields, type_operation):
    vs_main_f = fields_to_change['values']
    name_s_main_f = fields_to_change['name_to_search']        #name_to_search
    name_c_main_f = fields_to_change['name_to_change']        #name_to_change
    name_field_value = fields_to_change['name_value_field']
    result = {}
    for field in vs_main_f:
        result.update({field:[]})

    for element in elements:
    #     #if we want sum the elements with this name
    #     if element['_source'][name_s_main_f] in result:
        for elements_result in result:
            #If now it exist the element in the result (with the same fields) sum value.

            #i_exist = 0
            i = 0
            element_to_modified={}
            # print '++++++++++++'
            # print '++++++++++++'
            # print '++++++++++++'
            # print '++++++++++++'
            # print 'element original', element
            # print 'result--->',result
            # print 'elements_result--->',elements_result.decode('UTF-8')
            # print 'element[_source][fields_to_change[name_to_search]]---->',element['_source'][fields_to_change['name_to_search']], type(element['_source'][fields_to_change['name_to_search']])
            # print 'result [elements_result]--->', result[elements_result]


            #If element field to search is one element to change
            if elements_result.decode('UTF-8') == element['_source'][fields_to_change['name_to_search']]:
                # print ''
                # print ''
                # print 'ENTRO'
                #If it doesn't exist we should to create the field in te result
                exist = False

                for element_result in result[elements_result]:
                    same = True
                    # print ''
                    # print ''
                    # print ''
                    # print 'DENTRO'
                    # print 'element[_source]--->',element['_source']
                    # print 'element_result[_source]--->',element_result['_source']


                    for field in other_fields:
                        if element['_source'][field] != element_result['_source'][field]:
                            same = False
                            break
                    if same == True:
                        # print ''
                        # print ''
                        # print ''
                        # print 'SIIIIIIIIIIIIIII'

                        exist = True
                        element_to_modified = element_result
                        break


                #We create the field in result
                if exist == False:
                    new_item = copy.deepcopy(element)
                    new_item['_source'][name_c_main_f] = new_item['_source'][name_s_main_f]
                    # print 'name_s_main_f--->', name_s_main_f
                    # print 'new_item[_source][name_s_main_f]---->', new_item['_source'][name_s_main_f]


                    #If we are working with regions
                    if name_s_main_f[-6:] == 'region':
                        new_item['_source'][name_s_main_f] = new_item['_source'][name_s_main_f+'2']
                        new_item['_source'][name_s_main_f+'2'] = ''

                    # print 'new_item--->', new_item
                    # print'-------'
                    # print'-------'
                    # action = generate_Action(item, main_fields, other_fields)

                    result[elements_result].append(new_item)
                #We going to sum the value at exist field
                else:
                    if type_operation == 'sum':
                        # print 'SUUUUUUUUUUUMA'
                        # print 'antes',element_to_modified['_source'][name_field_value]
                        element_to_modified['_source'][name_field_value] += element['_source'][name_field_value]
                        # print 'ahora',element_to_modified['_source'][name_field_value]
                        # print result[elements_result][0]
                    elif type_operation == 'average':
                        element_to_modified['_source'][name_field_value] = (element_to_modified['_source'][name_field_value] + element['_source'][name_field_value]) / 2



    return result

def generate_Actions(elements, main_fields, other_fields, key_fields, name_index, type_index, cont_id):

    count = 0
    actions = []

    for element in elements:
        for row in elements[element]:

            item = {}
            item['insert_time']=datetime.datetime.today()

            source = row['_source']
            for field in main_fields:
                item[field] = source[field]
            for field in other_fields:
                item[field] = source[field]

            item['value'] = source['value']
            str_key = ""
            for field in key_fields:
                try:
                    str_key += str(source[field])
                except:
                    str_key += source[field]

            key =  hashlib.md5(str_key.encode('utf-8')).hexdigest()
            item["key"] = key

            action = {
                "_index": name_index,
                "_type": type_index,
                "_id": int(cont_id),
                "_source": item
            }

            acts = append_Action(key, name_index, action, actions)

            if acts:                       #if actions was append
                actions = acts
                cont_id += 1
                count += 1

    return {'actions' : actions, 'count':count}

def append_Action(key, name_index, action, actions):

    #Elasticsearch
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



name_index = 'index_aeropuertos'
type_index = 'structured'
field = "place_origin_region"
elements = []
regions = ['Europa Nórdica','Islas Británicas']
for region in regions:
    elements.extend(search_elastic(name_index,type_index, field, region))


cont_id = int(last_id_index(name_index))

fields_to_change = {
    'name_to_search':'place_origin_region',
    'name_to_change':'place_origin',
    'name_value_field':'value',
    'values':regions
}

type_operation = 'sum'
main_fields = ['place_origin','place_origin_region','place_origin_region2']
other_fields = ['airport','month', 'year', 'market']
key_fields = ['place_origin','month','year','airport']
data = sum_values(elements, fields_to_change, other_fields, type_operation)

result = generate_Actions(data, main_fields, other_fields, key_fields, name_index, type_index, cont_id)

count = result['count']
actions = result['actions']

print count
if count > 0:
    helpers.bulk(es, actions)
    print "leftovers"
    print "indexed", str(count), ",", name_index
else:
    print "Not indexed"
