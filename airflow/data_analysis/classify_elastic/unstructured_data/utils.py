# -*- coding: utf-8 -*-
from elasticsearch import Elasticsearch

def set_properties(name_items, type_index, name_index):

    es_new = Elasticsearch(
        [
            'elasticsearch:9200/'
        ]
    )
    indexSettings = {
        "mappings": {
            type_index: {
                "properties":
                    {value:{"type": "keyword"} for value in name_items}
            }
        }
    }
    print 'indexSettings-->', indexSettings
    es_new.indices.create(index=name_index, body=indexSettings)
    return es_new

def get_names_item_final(item):
    name_items = []
    for key in item.keys():
        if key != 'value' and key != 'insert_time':
            name_items.append(key)

    return name_items

#Return all elements of one index
def search_elastic(index,doc_type):
    es = Elasticsearch(
        [
            'elastic:vituinproject@elasticsearch:9200/',
        ]
    )

    #SearchAllEstablishments
    doc = {
        'size' : 10000,
        'query': {
            'match_all' : {}
        },
        'sort': [
            {"_id": "asc"}
        ]
    }


    result = es.search(index=index, doc_type=doc_type, body=doc,scroll='1m',request_timeout=300)
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
                'match_all' : {}
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

def add_restriction(constraints, set_options, fields_restrictions):

    constraints.update(fields_restrictions)
    i=1
    for k, v in fields_restrictions.items():
        set_options.update({
            'restriction'+str(i) : k
        })
        i+=1
    return [constraints, set_options]


#If it should sum fields
def get_sum_field(search,field, **kwords):

    if 'constraints' not in kwords:
        data = {field:[]}
        data[field].append(0)
        for entry in search:
            data[field][0] += entry['_source'][field]

    else:
        data = {}                                                     #We create a variable with values to return
        constraints = kwords['constraints']
        name_options = kwords['name_options']
        restriction = name_options['restriction1']


        for field_res in constraints[restriction]:
            data.update({field_res:[]})                                     #For each restriction we create a group of values results
            data[field_res].append(0)
            for entry in search:
                if entry['_source'][restriction] == field_res:
                    data[field_res][0] += entry['_source'][field]

    return data

def get_count(search,field, **kwords):
    if 'constraints' not in kwords:
        data = {field:[]}
        data[field].append(0)
        for entry in search:
            data[field][0] += entry['_source'][field]

    else:
        data = []                                                     #We create a variable with values to return
        constraints = kwords['constraints']
        name_options = kwords['name_options']
        i = 0
        if 'restriction1' in name_options:
            restriction = name_options['restriction1']
        else:
            restriction = name_options[field]

        for field_res in constraints[restriction]:
            data.append(0)
            for entry in search:
                if 'restriction1' in name_options:
                    if entry['_source'][restriction] == field_res:
                        data[i] += 1
                else:
                    data[i] += 1
            i+=1
    return data


def get_count_and_names(data, field):
    data_result = {field:[]}
    names = []
    for value in data[field]:
        if value not in names:
            names.append(value)
            data_result[field].append(1)
        else:
            pos_value = names.index(value)
            data_result[field][pos_value] += 1

    return [data_result, names]