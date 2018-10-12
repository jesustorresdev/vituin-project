# -*- coding: utf-8 -*-
import sys,os
sys.path.append('../')


from get_elastic import general_functions

#Fields where data will be write
homeway_file ='homeway.xls'
CSVdir='/usr/local/airflow/data_analysis/get_elastic/excels'
homeway_file = os.path.join(CSVdir, homeway_file)


sheets_and_indexes  = {'0':[ "index_list_description_homeway","index_list_homes_homeway"]}
types_index = {'0':["unstructured", "unstructured"]}

main_field = "id_homeway"
name_items = {"index_list_homes_homeway":["title", "url", "upload_date"], \
              "index_list_description_homeway":["id_homeway","price","capacity", "rooms","bathrooms","m2","min_stay","place"]}

restriction = {'place':'Puerto de la Cruz'}


general_functions.write_excel(sheets_and_indexes, types_index, name_items, homeway_file, main_field=main_field, restriction = restriction)


