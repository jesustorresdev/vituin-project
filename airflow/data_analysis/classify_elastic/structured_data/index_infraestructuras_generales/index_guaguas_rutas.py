# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_normalTable

excel = "excels_infraestructuras_generales/infraestructuras.xlsx"
sheet = 2
name_index = "index_guaguas_rutas"
type_index = "structured"


table_start_and_end = {
    "start_row": 135,
    "start_col": 0,
    "end_row": 147,
    "end_col": 2,
    "start_value_row": 136,
    "start_value_col": 0
}

type_items = {
    "rute" : str,
    "origin" : str,
    "destiny" : str,
}



name_items = ["rute", "origin", "destiny"]


index_excels_normalTable.main(excel, sheet, name_index, type_index, table_start_and_end, type_items, name_items)



