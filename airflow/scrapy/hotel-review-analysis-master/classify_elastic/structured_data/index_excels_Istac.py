# -*- coding: utf-8 -*-
import xlrd
import datetime
import hashlib
import generals_functions
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from countries_region import get_region
es = Elasticsearch(
       [
         'elasticsearch:9200/'
       ]
    )

field_region = []
attr_fix = {}
attr_spl = {}
fs_change = {}
attr_spl_r = {}
low_let = []
attr_spl_s = {}
attr_spl_r_s = {}

names_item_final = []

def main(excel, n_sheet, name_index, type_index, name_items, table_start_and_end, type_value, **kwords):
    # Open a workbook
    wb = xlrd.open_workbook(excel)

    # Get the worksheet
    sheet = wb.sheet_by_index(n_sheet)

    t_se = table_start_and_end

    # Get type and subtype of the cols
    try:
        if name_items["subtype_cols"]:
            cols = type_col(sheet,t_se, 1)
    except:
        cols = type_col(sheet,t_se, 0)

    n_cols = cols["n_cols"]
    type_cols = cols["array_cols"]

    # Get type and subtype of the rows
    rows = type_row(sheet,t_se)
    n_rows = rows["n_rows"]
    type_rows = rows["array_rows"]

    #Are there attributes_to_fixed?
    try:
        if kwords["attributes_to_fixed"]:
            global attr_fix
            attr_fix = kwords["attributes_to_fixed"]
    except:
        pass

    #Are there arguments to split?
    try:
        if kwords["attribute_to_split"]:
            global attr_spl
            attr_spl = kwords["attribute_to_split"]
    except:
        pass

    #Are there arguments to split and delete element?
    try:
        if kwords["attribute_to_split_remove"]:
            global attr_spl_r
            attr_spl_r = kwords["attribute_to_split_remove"]
    except:
        pass

    #Are there arguments to split?
    try:
        if kwords["field_region"]:
            global field_region
            field_region = kwords["field_region"]
    except:
        pass

    #Are name fields to change?
    try:
        if kwords["fields_to_change"]:
            global fs_change
            fs_change = kwords["fields_to_change"]
    except:
        pass

    try:
        if kwords["lowercase_letters"]:
            global low_let
            low_let = kwords["lowercase_letters"]
    except:
        pass

    try:
        if kwords["attribute_to_split_string"]:
            global attr_spl_s
            attr_spl_s = kwords["attribute_to_split_string"]
    except:
        pass

    #Are there arguments to split and delete substring?
    try:
        if kwords["attribute_to_split_remove_string"]:
            global attr_spl_r_s
            attr_spl_r_s = kwords["attribute_to_split_remove_string"]
    except:
        pass

    if  n_cols != 0 and n_rows != 0:
        subtype_cols = subtype_col(sheet,n_cols, t_se)
        subtype_rows = subtype_row(sheet,n_rows, t_se)
        #Upload to elasticsearch with all parameters
        sub_c = ['subtype_cols', subtype_cols]
        sub_r = ['subtype_rows', subtype_rows]
        update_elastic(sheet, n_cols, n_rows, name_index, type_index, name_items, t_se["start_value_row"], t_se["start_value_col"], type_value, type_cols, type_rows, sub_c, sub_r)
    elif n_cols != 0:
        subtype_cols = subtype_col(sheet,n_cols, t_se)
        sub_c = ['subtype_cols', subtype_cols]
        #Upload to elasticsearch with subtype_cols
        update_elastic(sheet, n_cols, 0, name_index, type_index, name_items, t_se["start_value_row"], t_se["start_value_col"], type_value, type_cols, type_rows, sub_c)
    elif n_rows != 0:
        subtype_rows = subtype_row(sheet,n_rows, t_se)
        sub_r = ['subtype_rows', subtype_rows]
        #Upload to elasticsearch with subtype_rows
        update_elastic(sheet, 0, n_rows, name_index, type_index, name_items, t_se["start_value_row"], t_se["start_value_col"], type_value, type_cols, type_rows, sub_r)
    else:
        #Upload to elasticsearch without subtypes
        update_elastic(sheet, 0, 0, name_index, type_index, name_items, t_se["start_value_row"], t_se["start_value_col"], type_value, type_cols, type_rows)


#upload_elastic
def update_elastic(sheet, n_cols, n_rows, name_index, type_index, name_items, start_row, start_col, type_value, type_cols, type_rows, *subtypes):

    subtype_rows=[]
    subtype_cols=[]
    for element in subtypes:
        if element[0] == 'subtype_cols':
            subtype_cols = element[1]
        if element[0] == 'subtype_rows':
            subtype_rows = element[1]


    index_elastic=call_elastic(name_index,es)
    cont_id = index_elastic["cont_id"]


    #Get all values of the sheet
    if subtype_rows and subtype_cols:
        dic_loop = loop_all_parameters(type_rows, type_cols, subtype_rows, subtype_cols, n_rows, n_cols, start_row ,start_col, type_value, name_index, type_index, name_items, cont_id, sheet, index_elastic)
    elif subtype_cols:
        dic_loop = loop_sub_c(type_rows, type_cols, subtype_cols, n_cols, start_row ,start_col, type_value, name_index, type_index, name_items, cont_id, sheet, index_elastic)
    elif subtype_rows:
        dic_loop = loop_sub_r(type_rows, type_cols, subtype_rows, n_rows, start_row ,start_col, type_value, name_index, type_index, name_items, cont_id, sheet, index_elastic)
    else:
        dic_loop = loop_without_subtypes(type_rows, type_cols, start_row ,start_col, type_value, name_index, type_index, name_items, cont_id, sheet, index_elastic)



    count = dic_loop['count']
    actions = dic_loop['actions']

    print count
    if count > 0:
        if index_elastic['exist_index'] is 0:
            global names_item_final
            es_new = set_properties(names_item_final, type_index, name_index)
            helpers.bulk(es_new, actions)
        else:
            helpers.bulk(es, actions)
        print "leftovers"
        print "indexed", str(count), ",", name_index
    else:
        print "Not indexed"


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


def loop_all_parameters(type_rows, type_cols, subtype_rows, subtype_cols, n_rows, n_cols, start_row ,start_col, type_value, name_index, type_index, name_items, cont_id, sheet, index_elastic):

    count = 0
    actions = []
    first_iteration = True

    for i in range(0,len(type_rows)):
        for j in range(0,len(subtype_rows)):
            for m in range(0,len(type_cols)):
                for n in range(0,len(subtype_cols)):

                    value = sheet.cell_value(rowx=(i*n_rows+i+1+j)+start_row, colx=(m*n_cols+n)+start_col)

                    item = {}

                    item["insert_time"]=datetime.datetime.today()
                    #If the type is str, it has attribute "strip()" (can be a blank space)
                    #if the type isn't str, it should transform to str
                    try:
                        item[name_items["type_rows"]] = type_rows[i].strip()
                    except:
                        item[name_items["type_rows"]] = str(type_rows[i])

                    try:
                        item[name_items["subtype_rows"]] = subtype_rows[j].strip()
                    except:
                        item[name_items["subtype_rows"]] = str(subtype_rows[j])

                    try:
                        item[name_items["type_cols"]] = type_cols[m].strip()
                    except:
                        item[name_items["type_cols"]] = str(type_cols[m])

                    try:
                        item[name_items["subtype_cols"]] = subtype_cols[n].strip()
                    except:
                        item[name_items["subtype_cols"]] = str(subtype_cols[n])


                    global fs_change
                    #if exist field to change
                    if fs_change:
                        item = generals_functions.change_field_name(item,fs_change)

                    global attr_spl_r_s
                    #if exist field to change
                    if attr_spl_r_s:
                        item = generals_functions.getAttributes_Split_Remove_String(item,name_items, attr_spl_r_s)

                    #Generate key of this value
                    if type_value != str:
                        str_key = str(value) + item[name_items["type_rows"]] + item[name_items["type_cols"]] + item[name_items["subtype_rows"]] + item[name_items["subtype_cols"]]
                    else:
                        str_key = value + item[name_items["type_rows"]] + item[name_items["type_cols"]] + item[name_items["subtype_rows"]] + item[name_items["subtype_cols"]]

                    '''
                    print '-----------------------------------'
                    print 'rowx = ', (i*n_rows+i+1+j)+start_row
                    print 'colx = ', (m*n_cols+n)+start_col
                    print 'value = ', value
                    print 'all'
                    '''

                    global attr_fix
                    #if it's place, country or city
                    global field_region
                    tem_attr_fix = {}
                    if field_region:
                        for name in name_items:
                            for element in field_region:
                                if element == name_items[name]:
                                    regions = get_region(item[name_items[name]], field = name_items[name])
                                    tem_attr_fix = {}              #Temp for the variables in this iteration that they will be fixed
                                    tem_attr_fix.update(attr_fix)
                                    tem_attr_fix.update(regions)
                    else:
                        tem_attr_fix = attr_fix

                    #if there are attributes_to_fixed
                    if tem_attr_fix:
                        item=generals_functions.getAttribute_Fixed(item,tem_attr_fix)
                        for element in tem_attr_fix:
                            str_key += tem_attr_fix[element]

                    global attr_spl_r
                    if attr_spl_r:
                        item=generals_functions.getAttributes_Split_Remove(item,name_items, attr_spl_r)

                    global attr_spl_s
                    if attr_spl_s:
                        item=generals_functions.getAttributes_Split_String(item,name_items, attr_spl_s)


                    global attr_spl
                    if attr_spl:
                        item=generals_functions.getAttributes_Split(item,name_items, attr_spl)

                    global low_let
                    if low_let:
                        item = generals_functions.getLowercaseWord(item, low_let)

                    if value == '.' or value == '..':               #if there isn't value
                        continue

                    item["value"] = generals_functions.getValue_with_type(type_value, value)

                    key =  hashlib.md5(str_key.encode('utf-8')).hexdigest()
                    item["key"] = key

                    if first_iteration:
                        global names_item_final
                        names_item_final = get_names_item_final(item)
                        first_iteration=False

                    action = {
                        "_index": name_index,
                        "_type": type_index,
                        "_id": int(cont_id),
                        "_source": item
                    }


                    acts = append_Action(index_elastic["exist_index"], key, name_index, action, actions)

                    if acts:                       #if actions was append
                        actions = acts
                        cont_id += 1
                        count += 1

    return {'actions' : actions, 'count':count}

def loop_sub_c(type_rows, type_cols, subtype_cols, n_cols, start_row ,start_col, type_value, name_index, type_index, name_items, cont_id, sheet, index_elastic):

    count = 0
    actions = []
    first_iteration = True

    #Get all values of the sheet
    for i in range(0,len(type_rows)):
        for m in range(0,len(type_cols)):
            for n in range(0,len(subtype_cols)):

                value = sheet.cell_value(rowx=i+start_row, colx=(m*n_cols+n)+start_col)

                item = {}

                item['insert_time']=datetime.datetime.today()
                #If the type is str, it has attribute "strip()" (can be a blank space)
                #if the type isn't str, it should transform to str
                try:
                    item[name_items["type_rows"]] = type_rows[i].strip()
                except:
                    item[name_items["type_rows"]] = str(type_rows[i])

                try:
                    item[name_items["type_cols"]] = type_cols[m].strip()
                except:
                    item[name_items["type_cols"]] = str(type_cols[m])

                try:
                    item[name_items["subtype_cols"]] = subtype_cols[n].strip()
                except:
                    item[name_items["subtype_cols"]] = str(subtype_cols[n])

                global fs_change
                #if exist field to change
                if fs_change:
                    item = generals_functions.change_field_name(item,fs_change)

                global attr_spl_r_s
                #if exist field to change
                if attr_spl_r_s:
                    item = generals_functions.getAttributes_Split_Remove_String(item,name_items, attr_spl_r_s)

                #Generate key of this value
                if type_value != str:
                    str_key = str(value) + item[name_items["type_rows"]] + item[name_items["type_cols"]] + item[name_items["subtype_cols"]]
                else:
                    str_key = value + item[name_items["type_rows"]] + item[name_items["type_cols"]] + item[name_items["subtype_cols"]]

                '''
                print '-----------------------------------'
                print 'rowx = ', i+start_row
                print 'colx = ', (m*n_cols+n)+start_col
                print 'value = ', value
                print 'sub_c'
                '''

                global attr_fix
                #if it's place, country or city
                global field_region
                tem_attr_fix = {}
                if field_region:
                    for name in name_items:
                        for element in field_region:
                            if element == name_items[name]:
                                regions = get_region(item[name_items[name]], field = name_items[name])
                                tem_attr_fix = {}              #Temp for the variables in this iteration that they will be fixed
                                tem_attr_fix.update(attr_fix)
                                tem_attr_fix.update(regions)
                else:
                    tem_attr_fix = attr_fix

                #if there are attributes_to_fixed
                if tem_attr_fix:
                    item=generals_functions.getAttribute_Fixed(item,tem_attr_fix)
                    for element in tem_attr_fix:
                        str_key += tem_attr_fix[element]

                global attr_spl_r
                if attr_spl_r:
                    item=generals_functions.getAttributes_Split_Remove(item,name_items, attr_spl_r)

                global attr_spl_s
                if attr_spl_s:
                    item=generals_functions.getAttributes_Split_String(item,name_items, attr_spl_s)

                global attr_spl
                if attr_spl:
                    item=generals_functions.getAttributes_Split(item,name_items, attr_spl)

                global low_let
                if low_let:
                    item = generals_functions.getLowercaseWord(item, low_let)

                if value == '.' or value == '..':               #if there isn't value
                    continue

                item["value"] = generals_functions.getValue_with_type(type_value, value)

                key =  hashlib.md5(str_key.encode('utf-8')).hexdigest()
                item["key"] = key

                if first_iteration:
                    global names_item_final
                    names_item_final = get_names_item_final(item)
                    first_iteration=False

                action = {
                  "_index": name_index,
                  "_type": type_index,
                  "_id": int(cont_id),
                  "_source": item
                }


                acts = append_Action(index_elastic["exist_index"], key, name_index, action, actions)

                if acts:                       #if actions was append
                    actions = acts
                    cont_id += 1
                    count += 1

    return {'actions' : actions, 'count':count}

def loop_sub_r(type_rows, type_cols, subtype_rows, n_rows, start_row ,start_col, type_value, name_index, type_index, name_items, cont_id, sheet, index_elastic):

    count = 0
    actions = []
    first_iteration = True

    for i in range(0,len(type_rows)):
        for j in range(0,len(subtype_rows)):
            for m in range(0,len(type_cols)):

                value = sheet.cell_value(rowx=(i*n_rows+i+1+j)+start_row, colx=m+start_col)

                item = {}

                item['insert_time']=datetime.datetime.today()
                #If the type is str, it has attribute "strip()" (can be a blank space)
                #if the type isn't str, it should transform to str
                try:
                    item[name_items["type_rows"]] = type_rows[i].strip()
                except:
                    item[name_items["type_rows"]] = str(type_rows[i])

                try:
                    item[name_items["type_cols"]] = type_cols[m].strip()
                except:
                    item[name_items["type_cols"]] = str(type_cols[m])

                try:
                    item[name_items["subtype_rows"]] = subtype_rows[j].strip()
                except:
                    item[name_items["subtype_rows"]] = str(subtype_rows[j])

                global fs_change
                #if exist field to change
                if fs_change:
                    item = generals_functions.change_field_name(item,fs_change)

                global attr_spl_r_s
                #if exist field to change
                if attr_spl_r_s:
                    item = generals_functions.getAttributes_Split_Remove_String(item,name_items, attr_spl_r_s)

                #Generate key of this value
                if type_value != str:
                    str_key = str(value) + item[name_items["type_rows"]] + item[name_items["type_cols"]] + item[name_items["subtype_rows"]]
                else:
                    str_key = value + item[name_items["type_rows"]] + item[name_items["type_cols"]] + item[name_items["subtype_rows"]]


                '''
                print '-----------------------------------'
                print 'rowx = ', (i*n_rows+i+1+j)+start_row
                print 'colx = ', m+start_col
                print 'value = ', value
                print 'sub_r'
                print type(value)
                '''

                global attr_fix
                #if it's place, country or city
                tem_attr_fix = {}
                global field_region
                if field_region:
                    for name in name_items:
                        for element in field_region:
                            if element == name_items[name]:
                                regions = get_region(item[name_items[name]], field = name_items[name])
                                tem_attr_fix = {}              #Temp for the variables in this iteration that they will be fixed
                                tem_attr_fix.update(attr_fix)
                                tem_attr_fix.update(regions)
                else:
                    tem_attr_fix = attr_fix
                #if there are attributes_to_fixed
                if tem_attr_fix:
                    item=generals_functions.getAttribute_Fixed(item,tem_attr_fix)
                    for element in tem_attr_fix:
                        str_key += tem_attr_fix[element]

                global attr_spl_r
                if attr_spl_r:
                    item=generals_functions.getAttributes_Split_Remove(item,name_items, attr_spl_r)

                global attr_spl_s
                if attr_spl_s:
                    item=generals_functions.getAttributes_Split_String(item,name_items, attr_spl_s)

                global attr_spl
                if attr_spl:
                    item=generals_functions.getAttributes_Split(item,name_items, attr_spl)

                global low_let
                if low_let:
                    item = generals_functions.getLowercaseWord(item, low_let)

                if value == '.' or value == '..':               #if there isn't value
                     continue

                item["value"] = generals_functions.getValue_with_type(type_value, value)

                key =  hashlib.md5(str_key.encode('utf-8')).hexdigest()
                item["key"] = key

                if first_iteration:
                    global names_item_final
                    names_item_final = get_names_item_final(item)
                    first_iteration=False

                action = {
                    "_index": name_index,
                    "_type": type_index,
                    "_id": int(cont_id),
                    "_source": item
                }


                acts = append_Action(index_elastic["exist_index"], key, name_index, action, actions)

                if acts:                       #if actions was append
                    actions = acts
                    cont_id += 1
                    count += 1

    return {'actions' : actions, 'count':count}

def loop_without_subtypes(type_rows, type_cols, start_row ,start_col, type_value, name_index, type_index, name_items, cont_id, sheet, index_elastic):

    count = 0
    actions = []
    first_iteration = True

    for i in range(0,len(type_rows)):
        for m in range(0,len(type_cols)):

            value = sheet.cell_value(rowx=i+start_row, colx=m+start_col)

            item = {}

            item['insert_time']=datetime.datetime.today()
            #If the type is str, it has attribute "strip()" (can be a blank space)
            #if the type isn't str, it should transform to str
            try:
                item[name_items["type_rows"]] = type_rows[i].strip()
            except:
                item[name_items["type_rows"]] = str(type_rows[i])
            try:
                item[name_items["type_cols"]] = type_cols[m].strip()
            except:
                item[name_items["type_cols"]] = str(int(type_cols[m]))

            global fs_change
            #if exist field to change
            if fs_change:
                item = generals_functions.change_field_name(item,fs_change)

            global attr_spl_r_s
            #if exist field to change
            if attr_spl_r_s:
                item = generals_functions.getAttributes_Split_Remove_String(item,name_items, attr_spl_r_s)

            #Generate key of this value
            if type_value != str:
                str_key = str(value) + item[name_items["type_rows"]] + item[name_items["type_cols"]]
            else:
                str_key = value + item[name_items["type_rows"]] + item[name_items["type_cols"]]

            '''
            print '-----------------------------------'
            print 'rowx = ', i+start_row
            print 'colx = ', m+start_col
            print 'value = ', value
            print 'nothing'
            print type(value)
            '''

            global attr_fix
            #if it's place, country or city
            global field_region
            tem_attr_fix = {}
            if field_region:
                for name in name_items:
                    for element in field_region:
                        if element == name_items[name]:
                            regions = get_region(item[name_items[name]], field = name_items[name])
                            tem_attr_fix = {}              #Temp for the variables in this iteration that they will be fixed
                            tem_attr_fix.update(attr_fix)
                            tem_attr_fix.update(regions)

            else:
                tem_attr_fix = attr_fix
            #if there are attributes_to_fixed
            if tem_attr_fix:
                item=generals_functions.getAttribute_Fixed(item,tem_attr_fix)
                for element in tem_attr_fix:
                    str_key += tem_attr_fix[element]

            global attr_spl_r
            if attr_spl_r:
                item=generals_functions.getAttributes_Split_Remove(item,name_items, attr_spl_r)

            global attr_spl_s
            if attr_spl_s:
                item=generals_functions.getAttributes_Split_String(item,name_items, attr_spl_s)

            global attr_spl
            if attr_spl:
                item=generals_functions.getAttributes_Split(item,name_items, attr_spl)

            global low_let
            if low_let:
                item = generals_functions.getLowercaseWord(item, low_let)

            if value == '.' or value == '..':               #if there isn't value
                 continue

            item["value"] = generals_functions.getValue_with_type(type_value, value)

            key =  hashlib.md5(str_key.encode('utf-8')).hexdigest()
            item["key"] = key

            if first_iteration:
                global names_item_final
                names_item_final = get_names_item_final(item)
                first_iteration=False

            action = {
                "_index": name_index,
                "_type": type_index,
                "_id": int(cont_id),
                "_source": item
            }


            acts = append_Action(index_elastic["exist_index"], key, name_index, action, actions)

            if acts:                       #if actions was append
                actions = acts
                cont_id += 1
                count += 1

    return {'actions' : actions, 'count':count}

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


#Return array with types of columns
def type_col(sheet,t_se, subtype_col):
    n_cols = 0                      # Number of columns of subtypes for each cloumn of type
    array_cols = []                 # Array with each name of the types

    i=0                             # Number of cells in the table
    all_cols = sheet.row_slice(rowx=t_se["start_row"],
                            start_colx=t_se["start_value_col"], # Saving since col values starts, not where it starts table (not col type there)
                            end_colx=t_se["end_col"]+1)         # row_slice uses end col - 1 by defect. For this it's necessary sum 1

    for element in all_cols:
        if element.value != "":
            array_cols.append(element.value)
        i=i+1

    if subtype_col:                      #If there is subtype_col
        n_cols = i / len(array_cols)     # Number of columns (its numbers of subtype_cols)
    else:
        n_cols = 0

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
                            end_rowx=t_se["end_row"]+1)          # col_slice uses end row - 1 by defect. For this it's necessary sum 1


    array_rows1 = sheet.col_slice(colx=t_se["start_col"]+1,      #If there aren't value at right is a type row
                            start_rowx=t_se["start_value_row"],  # Saving since row values starts, not where it starts table (not row type there)
                            end_rowx=t_se["end_row"]+1)          # col_slice uses end row - 1 by defect. For this it's necessary sum 1


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