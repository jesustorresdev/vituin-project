# -*- coding: utf-8 -*-
import xlrd
import datetime
import hashlib
from elasticsearch import Elasticsearch
from elasticsearch import helpers


def main(excel, n_sheet, name_index, type_index, name_items, table_start_and_end, type_value, fixed_attributes):
    # Open a workbook
    wb = xlrd.open_workbook(excel)

    # Get the worksheet
    sheet = wb.sheet_by_index(n_sheet)


    t_se = table_start_and_end

    # Get type and subtype of the cols
    cols = type_col(sheet,t_se)
    n_cols = cols["n_cols"]
    type_cols = cols["array_cols"]
    subtype_cols = subtype_col(sheet,n_cols, t_se)

    # Get type and subtype of the rows
    rows = type_row(sheet,t_se)
    n_rows = rows["n_rows"]
    type_rows = rows["array_rows"]


    if n_rows != 0:
        subtype_rows = subtype_row(sheet,n_rows, t_se)
        #Upload to elasticsearch with subtype_rows
        upload_elastic_with(sheet, type_cols, subtype_cols, type_rows, subtype_rows, n_cols, n_rows, name_index, type_index, name_items, t_se["start_value_row"], t_se["start_value_col"], type_value)
    else:
        #Upload to elasticsearch without subtype_rows
        upload_elastic_without(sheet, type_cols, subtype_cols, type_rows, n_cols, name_index, type_index, name_items, t_se["start_row"], t_se["start_col"], type_value)

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

#upload_elastic with subtype_rows
def upload_elastic_with(sheet, type_cols, subtype_cols, type_rows, subtype_rows, n_cols, n_rows, name_index, type_index, name_items, start_row, start_col, type_value):

    es = Elasticsearch(
       [
         'elasticsearch:9200/'
       ]
    )

    count = 0
    actions = []
    index_elastic=call_elastic(name_index,es)
    cont_id = index_elastic["cont_id"]

    #Get all values of the sheet
    for i in range(0,len(type_rows)):
        for j in range(0,len(subtype_rows)):
            for m in range(0,len(type_cols)):
                for n in range(0,len(subtype_cols)):

                    #Generate key of this value
                    value = sheet.cell_value(rowx=(i*n_rows+i+1+j)+start_row, colx=(m*n_cols+n)+start_col)
                    str_key = str(value) + type_rows[i].strip() + subtype_rows[j].strip() + type_cols[m].strip() + subtype_cols[n].strip()
                    key =  hashlib.md5(str_key.encode('utf-8')).hexdigest()

                    item = {}



                    item['insert_time']=datetime.datetime.today()
                    item[name_items["type_rows"]] = type_rows[i].strip()
                    item[name_items["subtype_rows"]] = subtype_rows[j].strip()
                    item[name_items["type_cols"]] = type_cols[m].strip()
                    item[name_items["subtype_cols"]] = subtype_cols[n].strip()
                    if type_value == int:
                        item["value"] = int(value.replace(".",""))

                    elif type_value == float:
                        item["value"] = value.replace(".","")
                        item["value"] = float(item["value"].replace(",","."))
                    else:
                        item["value"] = value

                    item["key"] = key

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
                                               "key": key #Use the key to compare
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


    if count > 0:
        helpers.bulk(es, actions)
        print "leftovers"
        print "indexed %d" %cont_id
    else:
        print "Not indexed"

#upload_elastic without subtype_rows
def upload_elastic_without(sheet, type_cols, subtype_cols, type_rows, n_cols, name_index, type_index, name_items, start_row, start_col, type_value):
    es = Elasticsearch(
       [
         'elasticsearch:9200/'
       ]
    )

    count = 0
    actions = []
    index_elastic=call_elastic(name_index,es)
    cont_id = index_elastic["cont_id"]

    #Get all values of the sheet
    for i in range(0,len(type_rows)):
        for m in range(0,len(type_cols)):
            for n in range(0,len(subtype_cols)):

                #Generate key of this value
                value = sheet.cell_value(rowx=i+start_row, colx=(m*n_cols+n)+start_col)
                str_key = str(value) + type_rows[i].strip() + type_cols[m].strip() + subtype_cols[n].strip()
                key =  hashlib.md5(str_key.encode('utf-8')).hexdigest()

                item = {}

                item['insert_time']=datetime.datetime.today()
                item[name_items["type_rows"]] = type_rows[i].strip()
                item[name_items["type_cols"]] = type_cols[m].strip()
                item[name_items["subtype_cols"]] = subtype_cols[n].strip()
                if type_value == int:
                    item["value"] = int(value.replace(".",""))
                elif type_value == float:
                    item["value"] = value.replace(".","")
                    item["value"] = float(item["value"].replace(",","."))
                else:
                    item["value"] = value

                item["key"] = key

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
                                           "key": key #Use the key to compare
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


    if count > 0:
        helpers.bulk(es, actions)
        print "leftovers"
        print "indexed %d" %cont_id
    else:
        print "Not indexed"



#Return array with types of columns
def type_col(sheet,t_se):
    n_cols = 0                      # Number of columns of subtypes for each cloumn of type
    array_cols = []                 # Array with each name of the types

    i=0                             # Number of cells in the table
    all_cols = sheet.row_slice(rowx=t_se["start_row"],
                            start_colx=t_se["start_value_col"], # Saving since col values starts, not where it starts table (not col type there)
                            end_colx=t_se["end_col"])

    for element in all_cols:
        if element.value != "":
            array_cols.append(element.value)
        i=i+1

    n_cols = i / len(array_cols)     # Number of columns (its numbers of subtype_cols)

    cols =  {
      "n_cols" : n_cols,
      "array_cols" : array_cols
    }
    return cols

#Return array with subtypes of columns
def subtype_col(sheet, n_cols, t_se):
    array_cols = sheet.row_slice(rowx=t_se["start_row"]+1, #Subtypecol is in the second line
                            start_colx=t_se["start_value_col"], #The line where start cols and values is the same
                            end_colx=t_se["start_value_col"]+n_cols)

    for i in range(0,len(array_cols)):
        array_cols[i] = array_cols[i].value    #Transform format of row_slice


    return array_cols

#Return array with types of rows
def type_row(sheet, t_se):
    n_rows = 0                      # Number of columns of subtypes for each row of type
    array_rows = []                 # Array with each name of the types

    array_rows0 = sheet.col_slice(colx=t_se["start_col"],
                            start_rowx=t_se["start_value_row"],  # Saving since row values starts, not where it starts table (not row type there)
                            end_rowx=t_se["end_row"])

    array_rows1 = sheet.col_slice(colx=t_se["start_col"]+1,      #If there aren't value at right is a type row
                            start_rowx=t_se["start_value_row"],  # Saving since row values starts, not where it starts table (not row type there)
                            end_rowx=t_se["end_row"])

    nElements = len(array_rows0)              # Length of each column in the table

    try:
        for i in range(0,nElements):
            if array_rows1[i].value == '':
                array_rows.append(array_rows0[i].value)

        n_rows = (nElements-len(array_rows)) / len(array_rows)

    except ZeroDivisionError:
        n_rows = 0
        for i in range(0,nElements):
            array_rows.append(array_rows0[i].value)


    rows =  {
      "n_rows" : n_rows,
      "array_rows" : array_rows
    }

    return rows

#Return array with subtypes of rows
def subtype_row(sheet, n_rows, t_se):
    array_rows = sheet.col_slice(colx=t_se["start_col"],
                            start_rowx=t_se["start_value_row"]+1, # First is type and not subtype
                            end_rowx=t_se["start_value_row"]+1+n_rows)

    for i in range(0,len(array_rows)):
        array_rows[i] = array_rows[i].value    #Transform format of col_slice

    return array_rows
