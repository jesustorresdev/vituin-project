# -*- coding: utf-8 -*-
import xlrd
import datetime
import hashlib
from elasticsearch import Elasticsearch
from elasticsearch import helpers


def main(excel, name_index, type_index, name_items, start_row, start_col, type_value):
    # Open a workbook
    wb = xlrd.open_workbook(excel)

    # Get the worksheet
    sheet = wb.sheet_by_index(0)

    # Get type and subtype of the cols
    cols = type_col(sheet)
    n_cols = cols["n_cols"]
    type_cols = cols["array_cols"]
    subtype_cols = subtype_col(sheet,n_cols)

    # Get type and subtype of the rows
    rows = type_row(sheet)
    n_rows = rows["n_rows"]
    type_rows = rows["array_rows"]
    subtype_rows = subtype_row(sheet,n_rows)

    #Upload to elasticsearch
    upload_elastic(sheet, type_cols, subtype_cols, type_rows, subtype_rows, n_cols, n_rows, name_index, type_index, name_items, start_row, start_col, type_value)

def upload_elastic(sheet, type_cols, subtype_cols, type_rows, subtype_rows, n_cols, n_rows, name_index, type_index, name_items, start_row, start_col, type_value):

    es = Elasticsearch(
       [
         'elasticsearch:9200/'
       ]
    )


    count = 0
    actions = []

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

    except:
        #If it's the first gruop of elements indexed
        print("First indexed")
        cont_id = 0
        exist_index = 0

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
                    else:
                        item["value"] = value

                    item["key"] = key

                    action = {
                        "_index": name_index,
                        "_type": type_index,
                        "_id": cont_id,
                        "_source": item
                    }

                    actions.append(action)

                    if exist_index == 1:
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
def type_col(sheet):
    n_cols = 0                      # Number of columns of subtypes for each cloumn of type
    array_cols = []                 # Array with each name of the types

    i=0                             # Number of cells in the table
    all_cols = sheet.row_values(7)  # In ISTAC the table starts at 7 position
    for element in all_cols:
        if element != '':
            array_cols.append(element)
        i=i+1

    n_cols = i / len(array_cols)     # Number of columnss

    cols =  {
      "n_cols" : n_cols,
      "array_cols" : array_cols
    }
    return cols

#Return array with subtypes of columns
def subtype_col(sheet, n_cols):
    array_cols = sheet.row_slice(rowx=8,
                            start_colx=1,
                            end_colx=1+n_cols) #In ISTAC, it will be start in row 8 and col 1

    for i in range(0,len(array_cols)):
        array_cols[i] = array_cols[i].value    #Transform format of row_slice

    return array_cols

#Return array with types of rows
def type_row(sheet):
    n_rows = 0                      # Number of columns of subtypes for each row of type
    array_rows = []                 # Array with each name of the types
    end_row = 9                     # We don't know where the table finish at first. But the start is in pos 9

    all_rows = sheet.col_slice(colx=0,
                            start_rowx=9)

    for element in all_rows:
        if element.value == '':
            break
        end_row = end_row + 1


    array_rows0 = sheet.col_slice(colx=0,
                            start_rowx=9,
                            end_rowx=end_row) # Array with all elements in col 0
    array_rows1 = sheet.col_slice(colx=1,
                            start_rowx=9,
                            end_rowx=end_row) # Array with all elements in col 1
    nElements = len(array_rows0)              # Length of each column in the table

    i=0
    while i < nElements:
        if array_rows1[i].value == '':
            array_rows.append(array_rows0[i].value)
        i = i +1

    n_rows = (i-len(array_rows)) / len(array_rows)

    rows =  {
      "n_rows" : n_rows,
      "array_rows" : array_rows
    }

    return rows

#Return array with subtypes of rows
def subtype_row(sheet, n_rows):
    array_rows = sheet.col_slice(colx=0,
                            start_rowx=10,
                            end_rowx=10+n_rows)

    for i in range(0,len(array_rows)):
        array_rows[i] = array_rows[i].value    #Transform format of col_slice

    return array_rows
