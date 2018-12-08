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
    "start_row": 15,
    "start_col": 0,
    "end_row": 20,
    "end_col": 2,
    "start_value_row": 17,
    "start_value_col": 1
}
type_value = float

attributes_to_fixed={
    "type": "agresiones",
}

fields_to_change = {'TOTAL' : ['answer','Total']}

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, attributes_to_fixed = attributes_to_fixed, fields_to_change = fields_to_change)


