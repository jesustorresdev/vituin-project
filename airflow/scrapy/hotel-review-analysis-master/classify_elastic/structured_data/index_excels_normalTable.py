# -*- coding: utf-8 -*-
import xlrd
import datetime
import hashlib
from elasticsearch import Elasticsearch
from elasticsearch import helpers

count = 0
cont_id = 0

def main(excel, n_sheet, name_index, type_index, table_start_and_end, type_items, name_items, pos_value_restrictions, fixed_attributes):
    # Open a workbook
    wb = xlrd.open_workbook(excel)

    # Get the worksheet
    sheet = wb.sheet_by_index(n_sheet)


    t_se = table_start_and_end


    es = Elasticsearch(
       [
         'elasticsearch:9200/'
       ]
    )

    global count
    global cont_id

    actions = []
    index_elastic=call_elastic(name_index,es)
    cont_id = index_elastic["cont_id"]
    init_cont_id = cont_id
    end_cont_id = cont_id

    #Get all values of the sheet
    for i in range(t_se["start_value_row"],t_se["end_row"]):

        row = sheet.row_values(i)

        #Generate key of this value
        item = {}

        restriction = False
        if pos_value_restrictions: restriction = True

        pos_restrictions = []
        name_pos_restrictions = []

        if restriction:

           #It returns arrays with restrictions
           arrays_restrictions = getArraysRestrictions(pos_value_restrictions)

           pos_restrictions = arrays_restrictions['array_pos_restrictions']
           name_pos_restrictions = arrays_restrictions['array_name_pos_restrictions']

           item = getSomeItems(item, pos_restrictions, row, type_items, name_items)


        else:
           item = getAllItems(item,row, type_items, name_items)

        #If there are fixed attributes
        if fixed_attributes:
            for k,v in fixed_attributes.iteritems():
                item[k]=v


        if restriction:
            for restr in name_pos_restrictions:

                for j in restr['pos']:

                    item = item.copy() #It ins't actions point to the same item and modified action append before

                    if(type_items["value"] is str):
                       item["value"] = row[j]                      #If is str it is going to be a unicode type
                    else:
                       item["value"] = type_items["value"](row[j]) #If it is other type, like int or float, it is going to this type


                    item[restr['name']] = type_items[restr['name']](name_items[j]) #It is going to be str ever

                    item["key"]=getKey(item)

                    actions = getActions(actions, es, item, name_index, type_index, index_elastic)

        else:
            item["key"]=getKey(item)
            actions = getActions(actions, es, item, name_index, type_index, index_elastic)


    if count > 0:
        helpers.bulk(es, actions)
        end_cont_id = cont_id
        count_indexed = end_cont_id - init_cont_id
        print "leftovers"
        print "indexed %d" %count_indexed
        print "last id %d" %cont_id
    else:
        print "Not indexed"


def getActions(actions, es, item, name_index, type_index, index_elastic):
        global cont_id
        global count


        item['insert_time']=datetime.datetime.today()

        action = {
                "_index": name_index,
                "_type": type_index,
                "_id": int(cont_id),
                "_source": item
         }


        if index_elastic["exist_index"] == 1:
            exist_element = '0'               #Does it exist element in index?

            #Search if there is same data in the index
            res = es.search(index=name_index, body={
                 "query": {
                            "match_phrase": {
                                           "key": item["key"] #Use the key to compare
                                     }
                           }
                   })

            for hit in res['hits']['hits']:
                exist_element = hit["_source"]

            if exist_element == '0':
                actions.append(action)
                cont_id += 1
                count += 1

        else:
            actions.append(action)
            cont_id += 1
            count += 1

        return actions


def call_elastic(name_index,es):


    #Search the last indexed id
    doc = {
            'size' : 10000,
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

def getKey(item):

    str_key = ''
    for key,value in item.iteritems():
        str_key = str_key + unicode(value)
    key =  hashlib.md5(str_key.encode('utf-8')).hexdigest()

    return key

#It isn't cols that are only one
def getAllItems(item, row, type_items, name_items):

    for j in range(0,len(row)):
        if(type_items[name_items[j]] is str):
            item[name_items[j]] = row[j]                            #If is str it is going to be a unicode type
        else:
            item[name_items[j]] = type_items[name_items[j]](row[j]) #If it is other type, like int or float, it is going to this type 

    return item

#There are cols that are only one
def getSomeItems(item, pos_restrictions, row, type_items, name_items):


    for i in range(0,len(row)):
        if i not in pos_restrictions:
            if(type_items[name_items[i]] is str):
               item[name_items[i]] = unicode(row[i])                   #If is str it is going to be a unicode type
            else:
               item[name_items[i]] = type_items[name_items[i]](row[i]) #If it is other type, like int or float, it is going to this type 
    return item

#return all position with restrictions
def getArraysRestrictions(pos_value_restrictions):
    array_restrictions = {}           #dict to return
    array_pos_restrictions = []       #array with all pos restrictions
    array_name_pos_restrictions = []  #array with name restrictios and its pos


    for element in pos_value_restrictions:
        array_restrictions_for_element = []
        for i in range(element['ini'], element['end']+1):
            array_pos_restrictions.append(i)
            array_restrictions_for_element.append(i)

        array_name_pos_restrictions.append({
                           'name':element['name'],
                           'pos':array_restrictions_for_element
        })

    array_restrictions = {
                      'array_pos_restrictions':array_pos_restrictions,
                      'array_name_pos_restrictions':array_name_pos_restrictions}

    return array_restrictions



