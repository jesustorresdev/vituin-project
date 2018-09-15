# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_entorno_social/Entorno social.xlsx"
sheet = 2
name_index = "index_idiomas_sector"
type_index = "structured"

name_items = {
    "type_rows" : "sector",
    "type_cols" : "language",
}

table_start_and_end = {
    "start_row": 18,
    "start_col": 0,
    "end_row": 30,
    "end_col": 9,
    "start_value_row": 19,
    "start_value_col": 1
}


fields_to_change = {'TOTAL' : 'España'}

type_value = int

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, fields_to_change = fields_to_change)

