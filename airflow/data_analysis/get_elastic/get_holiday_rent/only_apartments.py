# -*- coding: utf-8 -*-
import sys,os
sys.path.append('../')


from get_elastic import general_functions

#Fields where data will be write
only_apartments_file ='only_apartments.xls'
CSVdir='/usr/local/airflow/data_analysis/get_elastic/excels'
only_apartments_file = os.path.join(CSVdir, only_apartments_file)


sheets_and_indexes  = {'0':[ "index_list_homes_only_apartments","index_list_description_only_apartments"]}
types_index = {'0':["unstructured", "unstructured"]}



main_field = "id_only_apartments"
name_items = {"index_list_homes_only_apartments":["id_only_apartments", "url", "type_residence", "place", "upload_date"], \
              "index_list_description_only_apartments":[ "title", "price", "numberReviews", "mainBubbles", "bathrooms", "capacity", "beds", "m2", "day_price", "stay", "lng", "lat"]}

restriction = {'place':'Puerto de la Cruz'}


general_functions.write_excel(sheets_and_indexes, types_index, name_items, only_apartments_file, main_field=main_field, restriction = restriction)


