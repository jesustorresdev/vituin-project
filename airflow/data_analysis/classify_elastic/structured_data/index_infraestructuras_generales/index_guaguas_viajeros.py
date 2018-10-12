# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_infraestructuras_generales/infraestructuras.xlsx"
sheet = 2
name_index = "index_guagua_viajeros"
type_index = "structured"

name_items = {
    "type_rows" : "attribute_to_split_0",
    "type_cols" : "type",
}


table_start_and_end = {
    "start_row": 21,
    "start_col": 0,
    "end_row": 118,
    "end_col": 3,
    "start_value_row": 22,
    "start_value_col": 1
}
type_value = int

attribute_to_split = [{
    "attributes":["year","month"],      #Attributes to split
    "attr0":[0],                        #Words by attribute 0
    "attr1":[1],                        #Words by attribute 1
}]

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, attribute_to_split = attribute_to_split)


