# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_recursos_naturales/recursos.xlsx"
sheet = 0
name_index = "index_tiempo_atmosferico_anyo"
type_index = "structured"

name_items = {
    "type_rows" : "type",
    "type_cols" : "month"
}


table_start_and_end = {
    "start_row": 20,
    "start_col": 1,
    "end_row": 46,
    "end_col": 13,
    "start_value_row": 21,
    "start_value_col": 2
}
type_value = float

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value)


