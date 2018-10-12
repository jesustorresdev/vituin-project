# -*- coding: utf-8 -*-
import sys, os
sys.path.append('../')


from get_elastic import general_functions

#Fields where data will be write
flats9_file ='9flats.xls'
CSVdir='/usr/local/airflow/data_analysis/get_elastic/excels'
flats9_file = os.path.join(CSVdir, flats9_file)


sheets_and_indexes  = {'0':["index_list_homes_9flats"]}
types_index = {'0':["unstructured"]}

main_field = "id_airbnb"
name_items = {"index_list_homes_9flats":["id_9flats", "title", "url","price","type_residence","web","stars", "numberReviews"]}

restriction = {'place':'Puerto de la Cruz'}


general_functions.write_excel(sheets_and_indexes, types_index, name_items, flats9_file, main_field=main_field, restriction = restriction)
