# -*- coding: utf-8 -*-
import xlrd
import datetime
import hashlib
from elasticsearch import Elasticsearch
from elasticsearch import helpers

count = 0
cont_id = 0

def main(excel, n_sheet, name_index, type_index, table_start_and_end, type_items, name_items, name_extraItem, pos_value, fixed_attributes):
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


    #Get all values of the sheet
    for i in range(t_se["start_value_row"],t_se["end_row"]):

        row = sheet.row_values(i)

        #Generate key of this value
        item = {}

        restriction = False
        if pos_value: restriction = True

        if restriction:
           item = getSomeItems(item, pos_value, row, type_items, name_items)
        else:
           item = getAllItems(item,row, type_items, name_items)

        #If there are fixed attributes
        if fixed_attributes:
            for k,v in fixed_attributes.iteritems():
                item[k]=v

        if restriction:

            for j in range(pos_value[0], pos_value[1]):

                if(type_items["value"] is str):
                   item["value"] = row[j]                      #If is str it is going to be a unicode type
                   print "eee"
                else:
                   item["value"] = type_items["value"](row[j]) #If it is other type, like int or float, it is going to this type


                item[name_extraItem] = type_items[name_extraItem](name_items[j]) #It is going to be str ever

                item["key"]=getKey(item)
                actions = getActions(actions, es, item, name_index, type_index,  index_elastic)

        else:

            item["key"]=getKey(item)
            actions = getActions(actions, es, item, name_index, type_index, index_elastic)

    if count > 0:
        helpers.bulk(es, actions)
        print "leftovers"
        print "indexed %d" %cont_id
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


        actions.append(action)

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
    for element in item:
        if type(element) is not unicode:
                str_key = str_key + str(element) #If is unicode it is going to be unicode for the sum, if not it is going to be str type
        else:
            str_key += element

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
def getSomeItems(item, pos_value, row, type_items, name_items):


    for i in range(0,len(row)):
        if i < pos_value[0] or i > pos_value[1]:
            if(type_items[name_items[i]] is str):
               item[name_items[i]] = row[i]                            #If is str it is going to be a unicode type
            else:
               item[name_items[i]] = type_items[name_items[i]](row[i]) #If it is other type, like int or float, it is going to this type 

    return item

