# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_factores_económicos/Factores económicos.xlsx"
sheet = 2
name_index = "index_seguridad"
type_index = "structured"

name_items = {
    "type_rows" : "answer",
    "type_cols" : "place",
    "subtype_cols" : "type of measure"
}


table_start_and_end = {
    "start_row": 2,
    "start_col": 0,
    "end_row": 7,
    "end_col": 2,
    "start_value_row": 4,
    "start_value_col": 1
}
type_value = float

attributes_to_fixed={
    "type": "Robos",
}

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, attributes_to_fixed = attributes_to_fixed)


