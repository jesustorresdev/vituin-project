# -*- coding: utf-8 -*-
import xlrd
import xlwt
from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch(
    [
        'elasticsearch:9200/'
    ]
)

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


    print 'index---->', index
    result = es.search(index=index, doc_type=doc_type, body=doc,scroll='1m',request_timeout=300)
    print 'bien'
    print ''
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

def get_values(elements,constraints, assigned_options):
    values = {}
    namespie = []

    # print constraints
    # print '----'
    if type(constraints[assigned_options['checklist1']]) is list:
        for element in constraints[assigned_options['checklist1']]:
            values.update({element:[]})
    #If it isn't list
    else:
        values.update({constraints[assigned_options['checklist1']]:[]})


    for i in range(0,len(elements)):
        valid = True
        # print ''
        # print ''
        # print ''
        # print elements[i]['_source'], ', tipo = ', type(elements[i]['_source'])
        # print constraints
        #Comprobate restrictions
        for key, value in constraints.iteritems():
            # print 'BUUUUUUUUCLE | ', key, ' : ', value
            # if key == 'age':
            #      print '---------------------------ENTRO ---> ', key, ' : ', value, ', tipo = ', type(value)
            #if value is a list with some values
            if type(value) is list and value:
                any_concidence = 0

                for val in value:
                    if elements[i]['_source'][key] == val:
                        any_concidence = 1
                        # print 'BREAK 1'
                        # print elements[i]['_source']
                        # print val
                        break

                if any_concidence == 0:
                    valid = False
            else:
                if elements[i]['_source'][key] != value:
                    # print 'NO ENTRO ---> ',  elements[i]['_source'][key]
                    valid = False
                    # print 'BREAK 2'
                    # print elements[i]['_source']
                    # print 'value = ', value, ', key = ', key, ', elements[i][_source][key] = ' , elements[i]['_source'][key]
                    break


        #If is valid value
        if valid == True:
            values[elements[i]['_source'][assigned_options['checklist1']]].append(elements[i]['_source']['value'])

            #If is a piechart
            if type(constraints[assigned_options['checklist1']]) is not list:
                namespie.append(elements[i]['_source'][assigned_options['checklist2']])


    if type(constraints[assigned_options['checklist1']]) is list:
        return values
    else:
        val_with_names=[values,namespie]
        return val_with_names

def write_excel(sheets_and_indexes, types_index, name_items, name_excel,**kwords):
    workbook = xlwt.Workbook()
    data_all = {}
    for sheet_name in sheets_and_indexes:
        sheet = workbook.add_sheet(sheet_name)
        i = 0
        indexes = sheets_and_indexes[sheet_name]
        type_index = types_index[sheet_name]
        for index in indexes:
            data_all.update({index:[]})


        print "data_all---> ", data_all
        main_field_value = ''
        for n in range(0,len(indexes)):

            print "index---> ", indexes[n]
            print "type_index---> ", type_index[n]
            data_all[indexes[n]] = search_elastic(indexes[n], type_index[n])
            print 'data--> ',data_all[indexes[n]][0]


        sheet = write_column_names(sheet,indexes,name_items)
        row = 1
        for element in data_all[indexes[0]]:

            #If there is some condition
            if kwords['restriction']:
                condition = True
                for field, value in kwords['restriction'].iteritems():
                    if element['_source'][field] != value:
                        condition = False
                        break
                if condition == True:

                    sheet = write_fields(sheet,name_items[indexes[0]], element['_source'], row,0)

                    #If there are data from more than 1 index
                    if len(indexes) > 1:
                        n = 1
                        column=0
                        while n < len(indexes):
                            value_main_field = element['_source'][kwords["main_field"]]
                            element_other = search_element_by_field(data_all[indexes[n]],kwords["main_field"],value_main_field)
                            if element_other is not None:
                                #The column is the sum with the  column and
                                column =+ len(name_items[indexes[n-1]])
                                sheet = write_fields(sheet,name_items[indexes[n]], element_other['_source'], row, column)
                            n+=1
                    row+=1





        #     n = 1
    #     if len(indexes) > 1:
    #        while n < len(indexes):
    #            for element in data[n]:
    #                print indexes[n]
    #                print type_index[n]
    #                n += 1
    # #
    #     data = [0,3,4,1]
    #     sheet = workbook.add_sheet(sheet_name)
    #     sheet = write_column_names(sheet,name_items)
    #
    #     row = 0
    #     for element in data:
    #         for column, value in enumerate(element):
    #             sheet.write(row, column, value)
    #             row+=1
    #
    workbook.save(name_excel+'.xls')

#First row. Only write the name
def write_column_names(sheet,indexes,items):
    column = 0
    for n in range(0,len(indexes)):
        for name in items[indexes[n]]:
            print 'name wrote---> ', name
            sheet.write(0, column, name)
            column+=1
    return sheet

#Write the data in fields
def write_fields(sheet, items, element,row,column):
    print 'items---> ', items
    for name in items:
        print name, column
        sheet.write(row, column, element[name])
        column+=1
    return sheet

#Search element by a field
def search_element_by_field(data,main_field,value_main_field):
    for element in data:
        if element['_source'][main_field] == value_main_field:
            return element

