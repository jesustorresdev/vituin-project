# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_gasto_consumo/gasto.xls"
sheet = 0
name_index = "index_variacion_interanual"
type_index = "structured"

name_items = {
    "type_rows" : "type",
    "subtype_rows" : "place_tourist_residence",
    "type_cols" : "year",
    "subtype_cols" : "place",
}


table_start_and_end = {
    "start_row": 11,
    "start_col": 0,
    "end_row": 120,
    "end_col": 87,
    "start_value_row": 113,
    "start_value_col": 1
}
type_value = float


field_region = ["place_tourist_residence"]


index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, field_region = field_region)
