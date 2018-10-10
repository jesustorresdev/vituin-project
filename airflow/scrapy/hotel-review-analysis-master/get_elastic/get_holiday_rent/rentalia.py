# -*- coding: utf-8 -*-
import sys
sys.path.append('../')


from get_elastic import general_functions

excel = "excels_holiday_rent/rentalia.xls"

sheets_and_indexes  = {'0':["index_list_homes_rentalia","index_list_description_rentalia"]}
types_index = {'0':["unstructured", "unstructured"]}

main_field = "id_rentalia"
name_items = {"index_list_homes_rentalia":["id_rentalia", "title", "url", "price", "rooms","bathrooms", "beds", "capacity", "place", "upload_date"], \
              "index_list_description_rentalia":["type_residence", "numberReviews", "mainBubbles", "capacity", "min_stay", "lng", "lat"]}
name_excel = "rentalia"

restriction = {'place':'Puerto de la Cruz'}


general_functions.write_excel(sheets_and_indexes, types_index, name_items, name_excel, main_field=main_field, restriction = restriction)


