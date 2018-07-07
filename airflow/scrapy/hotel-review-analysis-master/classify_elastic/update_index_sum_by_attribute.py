# -*- coding: UTF-8 -*-

from elasticsearch import Elasticsearch



#Return all elements of one index
def search_elastic(index,doc_type, field, field_value):
    es = Elasticsearch(
        [
            'elastic:vituinproject@elasticsearch:9200/',
        ]
    )

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

def sum_values(elements, main_field, others_fields, type_operation):
    vs_main_f = main_field['values']
    name_s_main_f = main_field['name_to_search']
    name_c_main_f = main_field['name_to_change']
    name_field_value = main_field['name_value_field']
    result = {}
    for field in vs_main_f:
        result.update({field:[]})

    for element in elements:
    #     #if we want sum the elements with this name
    #     if element['_source'][name_s_main_f] in result:
        for elements_result in result:
            #If now it exist the element in the result (with the same fields) sum value.
            #If it doesn't exist we should to create the field in te result
            exist = False
            #i_exist = 0
            i = 0
            element_to_modified={}

            for element_result in result[elements_result]:
                same = True
                for field in others_fields:
                    if element['_source'][field] != element_result['_source'][field]:
                        same = False
                        break
                if same == True:
                    exist = True
                    #i_exist = i
                    element_to_modified = element_result
                    break

                #i += 1

            #We create the field in result
            if exist == False:
                new_item = element
                new_item['_source'][name_c_main_f] = new_item['_source'][name_s_main_f]

                #If we are working with regions
                if name_s_main_f[-6:] == 'region':
                    new_item['_source'][name_s_main_f] = new_item['_source'][name_s_main_f+'2']
                    new_item['_source'][name_s_main_f+'2'] = ''

                result[elements_result].append(new_item)
            #We going to sum the value at exist field
            else:
                if type_operation == 'sum':
                    element_to_modified['_source'][name_field_value] += element['_source'][name_field_value]

                elif type_operation == 'average':
                    element_to_modified['_source'][name_field_value] = (element_to_modified['_source'][name_field_value] + element['_source'][name_field_value]) / 2

    return result




index = 'index_aeropuertos'
doc_type = 'structured'
field = "place_origin_region"
elements = []
regions = ['europa nórdica','islas británicas']
for region in regions:
    elements.extend(search_elastic(index,doc_type, field, region))

main_field = {
    'name_to_search':'place_origin_region',
    'name_to_change':'place_origin',
    'name_value_field':'value',
    'values':regions
}

type_operation = 'sum'
others_fields = ['airport','year_month']
r = sum_values(elements, main_field, others_fields, type_operation)

print 'r---------->', r