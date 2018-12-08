# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_visitantes/visitantes.xlsx"
sheet = 0
name_index = "index_turistas_motivos_por_tipo_alojamiento"
type_index = "structured"

name_items = {
    "type_rows" : "reason",
    "subtype_rows" : "place",
    "type_cols" : "year",
    "subtype_cols" :"accommodation"
}


table_start_and_end = {
    "start_row": 125,
    "start_col": 0,
    "end_row": 150,
    "end_col": 15,
    "start_value_row": 127,
    "start_value_col": 1
}
type_value = int

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value)

