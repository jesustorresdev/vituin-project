# -*- coding: utf-8 -*-
import sys
sys.path.append('../')


from get_elastic import general_functions

excel = "excels_holiday_rent/atraveo.xls"

sheets_and_indexes  = {'0':["index_list_homes_atraveo", "index_list_description_atraveo"]}
types_index = {'0':["unstructured", "unstructured"]}

main_field = "id_atraveo"
name_items = {"index_list_homes_atraveo":["id_atraveo", "price","type_residence","numberReviews", "mainBubbles", "lat", "lng","url","upload_date","place","stay","search_date"], \
              "index_list_description_atraveo":["description", "capacity", "rooms", "bathrooms", "m2","min_stay"]}
name_excel = "atraveo"

restriction = {'place':'Puerto de la Cruz'}


general_functions.write_excel(sheets_and_indexes, types_index, name_items, name_excel, main_field=main_field, restriction = restriction)


