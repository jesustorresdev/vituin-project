# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_factores_económicos/Factores económicos.xlsx"
sheet = 0
name_index = "index_empleo_turistico"
type_index = "structured"

name_items = {
    "type_rows" : "place",
    "type_cols" : "year",
    "subtype_cols" : "type",
}


table_start_and_end = {
    "start_row": 58,
    "start_col": 0,
    "end_row": 83,
    "end_col": 50,
    "start_value_row": 60,
    "start_value_col": 1
}

type_value = float

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value)


