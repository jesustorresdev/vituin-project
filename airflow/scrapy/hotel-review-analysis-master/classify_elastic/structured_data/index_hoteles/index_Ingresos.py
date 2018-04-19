# -*- coding: utf-8 -*-
print 'cacddasa'
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_hoteles/ingresos.xls"
sheet = 0
name_index = "index_ingresos"
type_index = "structured"

name_items = {
    "type_rows" : "type",
    "type_cols" : "place",
    "subtype_cols" :"year"
}


table_start_and_end = {
    "start_row": 7,
    "start_col": 0,
    "end_row": 11,
    "end_col": 80,
    "start_value_row": 9,
    "start_value_col": 1
}


type_value = float

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value)
