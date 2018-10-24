# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_infraestructuras_generales/infraestructuras.xlsx"
sheet = 2
name_index = "index_transporte_guagua"
type_index = "structured"

name_items = {
    "type_rows" : "year_month",
    "type_cols" : "type"
}


table_start_and_end = {
    "start_row": 21,
    "start_col": 0,
    "end_row": 118,
    "end_col": 4,
    "start_value_row": 22,
    "start_value_col": 1
}
type_value = int

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value)


