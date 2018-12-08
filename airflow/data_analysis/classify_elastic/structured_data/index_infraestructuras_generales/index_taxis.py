# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_visitantes/infraestructuras.xlsx"
sheet = "Público"
name_index = "index_transporte_taxis"
type_index = "structured"

name_items = {
    "type_rows" : "name",
    "type_cols" : "type"
}


table_start_and_end = {
    "start_row": 1,
    "start_col": 0,
    "end_row": 4,
    "end_col": 4,
    "start_value_row": 2,
    "start_value_col": 1
}
type_value = int

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value)


