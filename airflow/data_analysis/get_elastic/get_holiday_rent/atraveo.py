# -*- coding: utf-8 -*-
import sys,os
sys.path.append('../')


from get_elastic import general_functions

#Fields where data will be write
atraveo_file ='atraveo.xls'
CSVdir='/usr/local/airflow/data_analysis/get_elastic/excels'
atraveo_file = os.path.join(CSVdir, atraveo_file)


sheets_and_indexes  = {'0':["index_list_homes_atraveo", "index_list_description_atraveo"]}
types_index = {'0':["unstructured", "unstructured"]}

main_field = "id_atraveo"
name_items = {"index_list_homes_atraveo":["id_atraveo", "price","type_residence","numberReviews", "mainBubbles", "lat", "lng","url","upload_date","place","stay","search_date"], \
              "index_list_description_atraveo":["description", "capacity", "rooms", "bathrooms", "m2","min_stay"]}

restriction = {'place':'Puerto de la Cruz'}


general_functions.write_excel(sheets_and_indexes, types_index, name_items, atraveo_file, main_field=main_field, restriction = restriction)


