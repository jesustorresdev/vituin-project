# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_gasto_consumo/gasto.xls"
sheet = 0
name_index = "index_gasto_por_residencia"
type_index = "structured"

name_items = {
    "type_rows" : "type",
    "subtype_rows" : "place_tourist_residence",
    "type_cols" : "year",
    "subtype_cols" : "place",
}


table_start_and_end = {
    "start_row": 80,
    "start_col": 0,
    "end_row": 87,
    "end_col": 41,
    "start_value_row": 82,
    "start_value_col": 1
}
type_value = float

attribute_to_split_remove = [{
    "attributes":["year"],         #Attributes to split
    "attr0":[0],                   #Words by attribute 0
}]

field_region = ["place_tourist_residence"]


index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, attribute_to_split_remove = attribute_to_split_remove, field_region = field_region)
