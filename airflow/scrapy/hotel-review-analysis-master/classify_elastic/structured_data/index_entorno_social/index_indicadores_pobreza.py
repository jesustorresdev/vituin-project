# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_entorno_social/Entorno social.xlsx"
sheet = 3
name_index = "index_pobreza"
type_index = "structured"

name_items = {
    "type_rows" : "type",
    "type_cols" : "val",
}

table_start_and_end = {
    "start_row": 32,
    "start_col": 0,
    "end_row": 36,
    "end_col": 1,
    "start_value_row": 33,
    "start_value_col": 1
}


type_value = float

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value)

