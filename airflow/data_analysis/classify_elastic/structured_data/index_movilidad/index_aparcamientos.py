# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_normalTable

excel = "excels_movilidad/aparcamientos.xlsx"
sheet = 0
name_index = "index_alquiler_vacacional_reglado"
type_index = "structured"


table_start_and_end = {
    "start_row": 0,
    "start_col": 0,
    "end_row": 2471,
    "end_col": 2,
    "start_value_row": 2,
    "start_value_col": 1
}

type_items = {
    "name" : str,
    "city" : str,
    "place" : str,
}



name_items = ["name", "city", "place"]


index_excels_normalTable.main(excel, sheet, name_index, type_index, table_start_and_end, type_items, name_items)



