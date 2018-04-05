# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_visitantes/infraestructuras.xlsx"
sheet = "Infraestructuras civiles"
name_index = "index_puertos"
type_index = "structured"


name_items = {
    "type_rows" : "port",
    "subtype_rows" : "type"
    "type_cols" : "year_month"
}


table_start_and_end = {
    "start_row": 343,
    "start_col": 0,
    "end_row": 351,
    "end_col": 105,
    "start_value_row": 344,
    "start_value_col": 1
}
type_value = int

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value)


