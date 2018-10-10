# -*- coding: utf-8 -*-
import sys
sys.path.append('../')


from get_elastic import general_functions

excel = "excels_holiday_rent/homeway.xls"

sheets_and_indexes  = {'0':[ "index_list_description_homeway","index_list_homes_homeway"]}
types_index = {'0':["unstructured", "unstructured"]}

main_field = "id_homeway"
name_items = {"index_list_homes_homeway":["title", "url", "upload_date"], \
              "index_list_description_homeway":["id_homeway","price","capacity", "rooms","bathrooms","m2","min_stay","place"]}
name_excel = "homeway"

restriction = {'place':'Puerto de la Cruz'}


general_functions.write_excel(sheets_and_indexes, types_index, name_items, name_excel, main_field=main_field, restriction = restriction)


