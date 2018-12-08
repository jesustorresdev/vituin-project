# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_normalTable

excel = "excels_eventos_museos/eventos_museos.xlsx"
sheet = 0
name_index = "index_museos"
type_index = "structured"


table_start_and_end = {
    "start_row": 0,
    "start_col": 0,
    "end_row": 6,
    "end_col": 2,
    "start_value_row": 1,
    "start_value_col": 0
}

type_items = {
    "name" : str,
    "address" : str,
    "place" : str,
}


coordinates = ['address','place']
name_items = ["name", "address", "place"]


index_excels_normalTable.main(excel, sheet, name_index, type_index, table_start_and_end, type_items, name_items, coordinates = coordinates)





