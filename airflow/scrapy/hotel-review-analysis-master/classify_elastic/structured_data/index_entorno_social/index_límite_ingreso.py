# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_entorno_social/Entorno social.xlsx"
sheet = 3
name_index = "index_ingreso_limite"
type_index = "structured"

name_items = {
    "type_rows" : "number people",
    "type_cols" : "euros",
}

table_start_and_end = {
    "start_row": 14,
    "start_col": 0,
    "end_row": 27,
    "end_col": 1,
    "start_value_row": 15,
    "start_value_col": 1
}


type_value = int

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value)

