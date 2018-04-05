# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_visitantes/infraestructuras.xlsx"
sheet = "Infraestructuras civiles"
name_index = "index_aeropuertos"
type_index = "structured"

name_items = {
    "type_rows" : "destination",
    "subtype_rows" : "place_origin"
    "type_cols" : "year_month"
}


table_start_and_end = {
    "start_row": 92,
    "start_col": 0,
    "end_row": 125,
    "end_col": 106,
    "start_value_row": 42,
    "start_value_col": 1
}
type_value = int

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value)

