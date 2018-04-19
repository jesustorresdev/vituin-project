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
    "type_cols" : "attribute_to_split_0",
    "subtype_cols" :"place_tourist_residence"
}


table_start_and_end = {
    "start_row": 171,
    "start_col": 0,
    "end_row": 181,
    "end_col": 80,
    "start_value_row": 173,
    "start_value_col": 1
}
type_value = float

extra_arguments={
    "attribute_to_split": [{
        "attributes":["year","trimester"],  #Attributes to split
        "attr0":[0],                        #Words by attribute 0
        "attr1":[1,2]                       #Words by attribute 1
    }]
}

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, extra_arguments)
