# -*- coding: utf-8 -*-
import sys,os
sys.path.append('../')


from get_elastic import general_functions

#Fields where data will be write
niumba_file ='niumba.xls'
CSVdir='/usr/local/airflow/data_analysis/get_elastic/excels'
niumba_file = os.path.join(CSVdir, niumba_file)


sheets_and_indexes  = {'0':["index_list_homes_niumba"]}
types_index = {'0':["unstructured"]}

main_field = "id_airbnb"
name_items = {"index_list_homes_niumba":["id_niumba", "title", "url","price","type_residence","rooms","capacity", "min_stay", "place", "upload_date"]}

restriction = {'place':'Puerto de la Cruz'}


general_functions.write_excel(sheets_and_indexes, types_index, name_items, niumba_file, main_field=main_field, restriction = restriction)
