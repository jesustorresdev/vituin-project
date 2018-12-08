# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_entorno_social/Entorno social.xlsx"
sheet = 3
name_index = "index_ingresos_sociedad"
type_index = "structured"

name_items = {
    "type_rows" : "place",
    "type_cols" : "type",
}

table_start_and_end = {
    "start_row": 2,
    "start_col": 0,
    "end_row": 10,
    "end_col": 4,
    "start_value_row": 3,
    "start_value_col": 1
}


fields_to_change = {'CANARAS':['place','Canarias']}

type_value = float

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, fields_to_change = fields_to_change)

