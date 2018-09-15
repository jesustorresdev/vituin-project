# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_factores_económicos/Factores económicos.xlsx"
sheet = 3
name_index = "index_precio_hotelero"
type_index = "structured"

name_items = {
    "type_rows" : "place",
    "type_cols" : "type",
    "subtype_rows" : "attribute_to_split_string_0"
}


table_start_and_end = {
    "start_row": 2,
    "start_col": 0,
    "end_row": 101,
    "end_col": 2,
    "start_value_row": 3,
    "start_value_col": 1
}
type_value = float

attribute_to_split_string = [{
    "attributes":["year","month"],  #Attributes to split
    "attr0":[0,4],                      #Attribute 0 pos
    "attr1":[5,7],                      #Attribute 1 pos
}]

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, attribute_to_split_string = attribute_to_split_string)

