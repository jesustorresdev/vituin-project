# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_factores_económicos/Factores económicos.xlsx"
sheet = 1
name_index = "index_desarrollo_economico"
type_index = "structured"

name_items = {
    "type_rows" : "place",
    "type_cols" : "type",
    "subtype_rows" : "attribute_to_split_0",
}


table_start_and_end = {
    "start_row": 2,
    "start_col": 0,
    "end_row": 99,
    "end_col": 3,
    "start_value_row": 3,
    "start_value_col": 1
}
type_value = float


attribute_to_split = [{
    "attributes":["year","month"],  #Attributes to split
    "attr0":[0],                        #Words by attribute 0
    "attr1":[1],                      #Words by attribute 1
}]


index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value,  attribute_to_split = attribute_to_split)


