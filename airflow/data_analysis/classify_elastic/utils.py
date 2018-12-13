from elasticsearch import Elasticsearch
from elasticsearch import helpers

ES = Elasticsearch(
    [
        'elastic:vituinproject@elasticsearch:9200/',
    ]
)

def size_index(index):
    doc = {
        'query': {
            'match_all' : {}
        }
    }

    return ES.search(index=index, body=doc, size=0)


#Return all elements of one index
def search_elastic(index,doc_type):

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


    result = ES.search(index=index, doc_type=doc_type, body=doc,scroll='1m',request_timeout=300)
    numberElements = ES.search(index=index, doc_type=doc_type, body=doc,size=0)['hits']['total']    #The number of Elements searched

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

        result = ES.search(index=index, doc_type=doc_type, body=doc)

        numberElements -= count
        count = 0
        for hit in result['hits']['hits']:        #Append the elements in the array
            elements.append(hit)
            count += 1

        pos += count                              #Last pos append


    elements=sorted(elements, key=lambda k: int(k['_id']))

    return elements

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

def get_names_item(item):
    name_items = []
    for key in item.keys():
        if key != 'value' and key != 'insert_time':
            name_items.append(key)

    return name_items

def update_elastic(name_index, doc_type, actions, count_id, count_update, exist_index, names_item):
    if exist_index is False:
        es_new = set_properties(names_item, doc_type, name_index)
        helpers.bulk(es_new, actions)
    else:
        helpers.bulk(ES, actions)
    print "indexed", str(count_update), "elements"
    print "total", str(count_id), ",", name_index
