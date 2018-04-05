# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_infraestructuras_generales/infraestructuras.xlsx"
sheet = 1
name_index = "index_valoracion_transporte"
type_index = "structured"

name_items = {
    "type_rows" : "type",
    "subtype_rows" : "country",
    "type_cols" : "year_month"
}



table_start_and_end = {
    "start_row": 372,
    "start_col": 0,
    "end_row": 4,
    "end_col": 40,
    "start_value_row": 308,
    "start_value_col": 1
}
type_value = float

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value)


