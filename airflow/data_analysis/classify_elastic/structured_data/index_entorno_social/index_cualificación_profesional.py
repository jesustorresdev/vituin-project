# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_normalTable

excel = "excels_entorno_social/Entorno social.xlsx"
sheet = 4
name_index = "index_cualificacion"
type_index = "structured"


table_start_and_end = {
    "start_row": 1,
    "start_col": 1,
    "end_row": 61,
    "end_col": 9,
    "start_value_row": 2,
    "start_value_col": 1
}

type_items = {
    "certification" : str,
    "specialty" : str,
    "type" : str,
    "place" : str,
}



name_items = ["certification", "specialty", "type", "place"]


index_excels_normalTable.main(excel, sheet, name_index, type_index, table_start_and_end, type_items, name_items)



