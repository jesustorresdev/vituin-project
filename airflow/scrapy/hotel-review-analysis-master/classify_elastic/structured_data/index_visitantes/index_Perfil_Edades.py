# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_visitantes/visitantes.xlsx"
sheet = 0
name_index = "index_perfil_turistico"
type_index = "structured"

name_items = {
    "type_rows" : "gender",
    "type_cols" : "year",
    "subtype_rows" : "place_tourist_residence",
    "subtype_cols" :"age"
}


table_start_and_end = {
    "start_row": 2,
    "start_col": 0,
    "end_row": 15,
    "end_col": 21,
    "start_value_row": 4,
    "start_value_col": 1
}
type_value = int

field_region = ["place_tourist_residence"]

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, field_region = field_region)
