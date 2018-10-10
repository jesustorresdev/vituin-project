# -*- coding: utf-8 -*-
import sys
sys.path.append('../')


from get_elastic import general_functions

excel = "excels_holiday_rent/niumba.xls"

sheets_and_indexes  = {'0':["index_list_homes_niumba"]}
types_index = {'0':["unstructured"]}

main_field = "id_airbnb"
name_items = {"index_list_homes_niumba":["id_niumba", "title", "url","price","type_residence","rooms","capacity", "min_stay", "place", "upload_date"]}
name_excel = "niumba"

restriction = {'place':'Puerto de la Cruz'}


general_functions.write_excel(sheets_and_indexes, types_index, name_items, name_excel, main_field=main_field, restriction = restriction)
