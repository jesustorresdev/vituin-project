# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_hoteles/hoteles.xls"
sheet = 0
name_index = "index_plazas_ofertadas"
type_index = "structured"

name_items = {
    "type_rows" : "type",
    "subtype_rows" :"year",
    "type_cols" : "place"
}


table_start_and_end = {
    "start_row": 18,
    "start_col": 0,
    "end_row": 26,
    "end_col": 24,
    "start_value_row": 19,
    "start_value_col": 1
}


type_value = int

fixed_attributes={}

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, fixed_attributes)
