# -*- coding: utf-8 -*-
from googlemaps import Client as GoogleMaps
from elasticsearch import Elasticsearch
import datetime

def change_field_name_json(field, fs_change):
    return fs_change[field].decode('UTF-8')

def getAttribute_Fixed(item, attr_fix):

    for k,v in attr_fix.items():
        item[k]=v.decode('UTF-8')

    return item

def getRestrictionAttribute_Fixed(item, attr_rest_fix, n):

    for k,v in attr_rest_fix[n].items():
        item[k]=v.decode('UTF-8')

    return item

def getAttributes_Split(item, name_items, attr_spl):
    for k,v in name_items.items():
        if v[:-2]=="attribute_to_split":                                #if is a attr_split type
            for i in range(0,len(attr_spl)):                           #See how many attr_spl there are. For each one, we'll save new item
                attribute = attr_spl[i]
                value_item = item["attribute_to_split_"+str(i)].split() #It's a array with all words for the name of the first item (without split)

                #If not an exception. It can be a field without second value
                if len(value_item) != 1:
                    for j in range(0,len(attribute["attributes"])):         #Number of new items than we are going to create
                        key_item = attribute["attributes"][j]
                        item[key_item] = ''

                        for number in attribute["attr"+str(j)]:
                            item[key_item] += value_item[number]            #Set new items
                            item[key_item] += ' '
                        item[key_item] = item[key_item][:-1]                #Eliminate last space
                    del item["attribute_to_split_"+str(i)]                  #Delete to the old item
                else:
                    key_item = attribute["exception"]
                    item[key_item] = value_item[0]
                    del item["attribute_to_split_"+str(i)]                  #Delete to the old item

                    temp_attr = attribute["attributes"][:]                  #copy the list
                    temp_attr.remove(attribute["exception"])
                    #For each exclude add value
                    for j in range(0,len(temp_attr)):
                        key_item = temp_attr[j]
                        item[key_item] = attribute["exclude"][j]


    return item

def getAttributes_Split_String(item, name_items, attr_spl_s):
    for k,v in name_items.items():
        if v[:-2]=="attribute_to_split_string_":                         #if is a attr_split type
            for i in range(0,len(attr_spl_s)):                           #See how many attr_spl there are. For each one, we'll save new item
                attribute = attr_spl_s[i]
                value_item = item["attribute_to_split_string_"+str(i)]   #It's a array with all words for the name of the first item (without split)

                #If not an exception. It can be a field without second value
                if not "exception" in attribute:
                    for j in range(0,len(attribute["attributes"])):         #Number of new items than we are going to create
                        key_item = attribute["attributes"][j]
                        item[key_item] = ''

                        # for attribute, we get the substring indicate:
                        attr_n = attribute["attr"+str(j)]
                        item[key_item] = value_item[attr_n[0]:attr_n[1]]    #Set new items

                    del item["attribute_to_split_string_"+str(i)]           #Delete to the old item
                else:
                    key_item = attribute["exception"]
                    attr_exception = attribute["attr_exception"]
                    item[key_item] = value_item[attr_exception[0]:attr_exception[1]]
                    del item["attribute_to_split_string_"+str(i)]           #Delete to the old item

                    temp_attr = attribute["attributes"][:]                  #copy the list
                    temp_attr.remove(attribute["exception"])
                    #For each exclude add value
                    for j in range(0,len(temp_attr)):
                        key_item = temp_attr[j]
                        item[key_item] = attribute["exclude"][j]


    return item

def getAttributes_Split_Remove(item, name_items, attr_spl_r):

    for element in attr_spl_r:
        for i in range(0,len(element["attributes"])):                                  #All elements to split
            for k,v in name_items.items():
                if v == element["attributes"][i]:                                      #if is the element
                    split_item = item[v].split()
                    condition = False
                    #There are condition in this split. It means that exits value that should change but others not should change
                    if "condition" in element:
                        condition = True
                        for j in range(0,len(element["condition"])):
                            try:
                                if element["condition"][j].decode('UTF-8') != split_item[element["condition_pos"][j]]:
                                    condition = False
                                    break
                            except:
                                condition =  False
                    else:
                        condition = True

                    if condition == True:
                        item[v] = ''
                        for attribute in element["attr"+str(i)]:
                            item[v] += split_item[attribute] + ' '
                        item[v] = item[v][:-1]                                              #Eliminate last space
    return item

def getAttributes_Split_Remove_String(item, name_items, attr_spl_r_s):

    list_items = []
    if isinstance(name_items,list) is False:
        for k,v in name_items.items():
            list_items.append(v)
    else:
        list_items = name_items
    list_items = ['dia','mes']
    for element in attr_spl_r_s:
        for i in range(0,len(element["attributes"])):                                  #All elements to split
            for v in list_items:
                if v == element["attributes"][i]:                                      #if is the element

                    old_string = item['fecha']
                    pos_start = True if element["attr"+str(i)][0] is 'start' else False
                    pos_final = True if element["attr"+str(i)][1] is 'final' else False


                    if not pos_start:
                        new_string_0 = old_string[:element["attr"+str(i)][0]]
                    else:
                        new_string_0 = ''

                    if not pos_final:
                        new_string_1 = old_string[element["attr"+str(i)][1]:]
                    else:
                        new_string_1 = ''

                    if not pos_final and not pos_start:
                        new_string=old_string[element["attr"+str(i)][0]:element["attr"+str(i)][1]]
                    else:
                        new_string = new_string_0 + new_string_1
                    item[v] = new_string

    return item


def change_field_name(item, fs_change):

    for element in fs_change:
        #if the name of item is a field that should to change
        field = fs_change[element][0]
        try:
            if item[field].encode('UTF-8') == element:
                item[field] = fs_change[element][1].decode('UTF-8')
        except:
            if item[field] == element:
                item[field] = fs_change[element][1].decode('UTF-8')
    return item

def getValue_with_type(type_value, value):
    if type_value == int:
        try:
            value_type = int(value.replace(".",""))
        except:
            value_type = int(value)

    elif type_value == float:
        try:
            value_type = float(value.replace(",","."))
        except:
            try:
                value_type = value.replace(".","")
                value_type = float(value_type.replace(",","."))
            except:
                value_type = float(value)
    else:
        value_type = value

    return value_type

def getCoordinates(coordinates,item):

    result_coordinates = {'lat':'','lng':''}

    place = ''
    for field in coordinates:
        if field in item:
            place += str(item[field].encode('UTF-8'))                   #The place searched is the composed to the fields to get the coordinates
            place += ' '
    print place
    api_key = 'AIzaSyD2owaTzJTWi9m1f2QqAlJ1S0hfFT3nT0w'
    gmaps = GoogleMaps(api_key)
    location = gmaps.geocode(place)
    ok = False
    while ok is False:
        try:
            if 'location' in location[0]['geometry']:
                lat=location[0]['geometry']['location']['lat']
                lng=location[0]['geometry']['location']['lng']
            else:  #if it's a aproximation
                lat = location[0]['geometry']['bounds']['northeast']['lat'] + location[0]['geometry']['bounds']['southwest']['lat']
                lng = location[0]['geometry']['bounds']['northeast']['lng'] + location[0]['geometry']['bounds']['southwest']['lng']
            ok = True
        except Exception as error:
            print 'algo va mal', error
            print 'location-->', location
            ok = True
            lat = ''
            lng = ''
            print place.find('Ed')
            if place.find('Ed') != -1: #In structured comercio tenerife cases
                place = str(item[coordinates[0]][:item[coordinates[0]].find('Ed')].encode('UTF-8'))
                for i in range(1,len(coordinates)):
                    field = coordinates[i]
                    if field in item:
                        place += str(item[field].encode('UTF-8'))                   #The place searched is the composed to the fields to get the coordinates
                        place += ' '
                ok = False
                location = gmaps.geocode(place)
                print 'place->',place
            print 'ok->',ok
            pass

    result_coordinates['lat']=lat
    result_coordinates['lng']=lng
    return result_coordinates


def getLowercaseWord(item, fields):

    for field in fields:
        item[field] = item[field].upper()[0] + item[field].lower()[1:]
    return item


def fix_fields_in_only_one(field,fields_to_fix_elements,elements_to_fix_in_one,element, **kwords):
    fs_change = {}
    if 'fs_change' in kwords:
        fs_change = kwords['fs_change']

    items_to_fix = []
    for element_to_fix in elements_to_fix_in_one[fields_to_fix_elements.index(field)]:
        # print 'element_to_fix-->', element_to_fix
        tmp_item = {}
        #If field to change in value o field
        try:
            if element[element_to_fix] in fs_change:
                value = change_field_name_json(element[field],fs_change)
            else:
                value = element[element_to_fix]
        except:
            value = ''

        if element_to_fix in fs_change:
            element_to_fix = change_field_name_json(field,fs_change)

        #Save the item: first field and after the value
        try:
            tmp_item[field] = str(element_to_fix.decode('UTF-8'))
        except:
            tmp_item[field] = element_to_fix

        tmp_item['value'] = value
        #Save the item
        try:
            tmp_item['value'] = str(value.decode('UTF-8'))
        except:
            tmp_item['value'] = value

        items_to_fix.append(tmp_item)

    return items_to_fix

def set_date(item,fields_date):
    for field_date in fields_date:
        item[field_date] = datetime.datetime.strptime(item[field_date], '%Y-%m-%d %H:%M:%S.%f')
    return item


def change_months(item, field_month):
    months_str = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', \
             'Septiembre', 'Octubre', 'Noviembre', 'Diciembre', 'Total']
    try:
        month = months_str[int(item[field_month])-1]
        item[field_month] = month
    except:
        pass

    return item

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
        if key != 'value' and key != 'insert_time' and key != 'date':
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