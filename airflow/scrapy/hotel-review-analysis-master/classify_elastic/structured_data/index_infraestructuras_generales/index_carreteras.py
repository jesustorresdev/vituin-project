# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_normalTable

excel = "excels_infraestructuras_generales/infraestructuras.xlsx"
sheet = 0
name_index = "index_carreteras"
type_index = "structured"


table_start_and_end = {
    "start_row": 4,
    "start_col": 8,
    "end_row": 34,
    "end_col": 17,
    "start_value_row": 5,
    "start_value_col": 8
}

type_items = {
    "road" : str,
    "kilometre" : float,
    "access" : str,
    "estation" : str,
    "character" : str,
    "asc" : int,
    "dec" : int,
    "average speed" : float,
    "vehicles total" : int,
    "vehicles heavy" : int
}



name_items = ["road","kilometre","access", "estation", "character", "asc", "dec", "average speed", "vehicles total", "vehicles heavy"]


index_excels_normalTable.main(excel, sheet, name_index, type_index, table_start_and_end, type_items, name_items)



