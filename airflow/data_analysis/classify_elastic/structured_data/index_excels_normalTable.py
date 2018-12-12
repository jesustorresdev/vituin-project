# -*- coding: utf-8 -*-
import xlrd
import datetime
import hashlib
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import utils
import countries_region

count = 0
cont_id = 0

def main(excel, n_sheet, name_index, type_index, table_start_and_end, type_items, name_items, **kwords):
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

    global first_iteration
    first_iteration = True
    global count
    global cont_id

    actions = []
    index_elastic=call_elastic(name_index,es)
    cont_id = index_elastic["cont_id"]
    init_cont_id = cont_id


    if 'attributes_to_fixed' in kwords:                           #If it exits, we're going to add a extra field
        attributes_to_fixed = kwords['attributes_to_fixed']
    else:
        attributes_to_fixed = {}                                  #If it exists, we're going to join some fields in only one
    if 'pos_value_restrictions' in kwords:
        pos_value_restrictions = kwords['pos_value_restrictions']
    else:
        pos_value_restrictions = []
    if 'attributes_to_fixed_to_restriction' in kwords:                           #If it exits, we're going to add a extra field
        attributes_to_fixed_to_restriction = kwords['attributes_to_fixed_to_restriction']
    else:
        attributes_to_fixed_to_restriction = {}                                  #If it exists, we're going to join some fields in only one
    if 'coordinates' in kwords:                                    #If it exists, we're going to search and fix the coordinates
        coordinates = kwords['coordinates']
    else:
        coordinates = []
    #Are there arguments with region?
    if 'field_region' in kwords:
        field_region = kwords["field_region"]
    else:
        field_region = []

    if 'lowercase_letters' in kwords:
        lowercase_letters = kwords["lowercase_letters"]
    else:
        lowercase_letters = []

    if 'change_months' in kwords:
        change_months = kwords["change_months"]
    else:
        change_months = []

    if 'fields_to_change' in kwords:
        change_fields = kwords["fields_to_change"]
    else:
        change_fields = []

    if 'date' in kwords:
        date = kwords["date"]
    else:
        date = []



    #Get all values of the sheet
    for i in range(t_se["start_value_row"],t_se["end_row"]+1):

        row = sheet.row_slice(rowx=i,
                        start_colx=t_se["start_value_col"], # Saving since col values starts, not where it starts table (not col type there)
                        end_colx=t_se["end_col"]+1)         # row_slice uses end col - 1 by defect. For this it's necessary sum 1
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
        if attributes_to_fixed:
            item = utils.getAttribute_Fixed(item, attributes_to_fixed)

        if coordinates:
            coor=utils.getCoordinates(coordinates, item)
            item['lat']=coor['lat']
            item['lng']=coor['lng']

        if lowercase_letters:
            item = utils.getLowercaseWord(item, lowercase_letters)

        if restriction:
            n=0
            for restr in name_pos_restrictions:
                for j in restr['pos']:

                    item_tmp = item.copy() #It ins't actions point to the same item and modified action append before

                    if(type_items["value"] is str):
                        item_tmp["value"] = row[j].value                      #If is str it is going to be a unicode type
                    else:
                        try:
                            item_tmp["value"] = type_items["value"](row[j].value) #If it is other type, like int or float, it is going to this type
                        except:
                            item_tmp["value"] = 0

                    item_tmp[restr['name']] = type_items[restr['name']](name_items[j]) #It is going to be str ever

                    if field_region:
                        item_tmp = loopRegion(item_tmp, field_region)

                    if change_months:
                        item_tmp = utils.change_months(item_tmp, change_months)

                    if attributes_to_fixed_to_restriction:
                        item_tmp = utils.getRestrictionAttribute_Fixed(item_tmp, attributes_to_fixed_to_restriction, n)

                    if change_fields:
                        item_tmp = utils.change_field_name(item_tmp,change_fields)

                    if date:
                        item_tmp = utils.set_date(item_tmp,date)

                    item_tmp["key"]=getKey(item_tmp)
                    actions = getActions(actions, es, item_tmp, name_index, type_index, index_elastic)

                n+=1

        else:
            if field_region:
                item = loopRegion(item, field_region)

            if change_months:
                item = utils.change_months(item, change_months)

            if change_fields:
                item = utils.change_field_name(item,change_fields)

            if date:
                item = utils.set_date(item,date)

            item["key"]=getKey(item)
            actions = getActions(actions, es, item, name_index, type_index, index_elastic)

    if count > 0:

        if index_elastic['exist_index'] is 0:
            global names_item_final
            es_new = utils.set_properties(names_item_final, type_index, name_index)
            helpers.bulk(es_new, actions)
        else:
            helpers.bulk(es, actions)
        end_cont_id = cont_id
        count_indexed = end_cont_id - init_cont_id
        print "leftovers"
        print "indexed", str(count), ",", name_index
        print "last id %d" %cont_id
    else:
        print "Not indexed"


def getActions(actions, es, item, name_index, type_index, index_elastic):
        global cont_id
        global count
        global first_iteration
        if first_iteration:
            global names_item_final
            names_item_final = utils.get_names_item_final(item)
            first_iteration=False

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
        try:
            str_key = str_key + value.decode('UTF-8')
        except:
            str_key = str_key + unicode(value) #when the numeric value founded

    key =  hashlib.md5(str_key.encode('utf-8')).hexdigest()

    return key

#There aren't cols that are only one
def getAllItems(item, row, type_items, name_items):

    for j in range(0,len(row)):
        if(type_items[name_items[j]] is str):
            try:
                item[name_items[j]] = row[j].value.decode("utf-8")
            except:
                item[name_items[j]] = row[j].value                            #If is str it is going to be a unicode type

        else:
            if row[j].value == '' or row[j].value == '.' or row[j].value == '..' :
                item[name_items[j]] = 0
            else:
                item[name_items[j]] = type_items[name_items[j]](row[j].value) #If it is other type, like int or float, it is going to this type
    return item

#There are cols that are only one
def getSomeItems(item, pos_restrictions, row, type_items, name_items):


    for i in range(0,len(row)):
        if i not in pos_restrictions:
            if(type_items[name_items[i]] is str):                      #If it is str it is going to be a unicode type
               if type(row[i]) is float:                                            #If it was a number before, like years
                   if int(row[i]) == row[i]:                                               #If it was a int
                       item[name_items[i]] =unicode(int(row[i].value))
                   else:
                       item[name_items[i]] = unicode(row[i].value)
               else:                                                                #If it has ever been a str or it was a float
                   item[name_items[i]] = unicode(row[i].value)[:-2] if unicode(row[i].value)[-2:] == '.0' else unicode(row[i].value)
            else:
               item[name_items[i]] = type_items[name_items[i]](row[i].value) #If it is other type, like int or float, it is going to this type
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

#return item with region
def loopRegion(item, field_region):
    tem_attr_fix = {}
    if field_region:
        for field in item:
            for element in field_region:
                if element == field:
                    regions = countries_region.get_region(item[field], field = field)
                    tem_attr_fix = {}
                    tem_attr_fix.update(regions)

    #if there are attributes_to_fixed
    if tem_attr_fix:
        item=utils.getAttribute_Fixed(item, tem_attr_fix)
    return item

