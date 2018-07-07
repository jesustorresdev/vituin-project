# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_normalTable

excel = "excels_recursos_naturales/recursos.xlsx"
sheet = 1
name_index = "index_playas"
type_index = "structured"

table_start_and_end = {
    "start_row": 1,
    "start_col": 0,
    "end_row": 4,
    "end_col": 4,
    "start_value_row": 2,
    "start_value_col": 1
}

type_items = {
    "beach" : str,
    "season" : str,
    "blue flag" : str,
    "condition" : str,
    "water classification" : str
}

attributes_to_fixed={
    "place": "Puerto de la Cruz"
}

coordinates = ['beach','place']
name_items = ["beach", "season", "blue flag", "condition", "water classification"]
index_excels_normalTable.main(excel, sheet, name_index, type_index, table_start_and_end, type_items, name_items, attributes_to_fixed = attributes_to_fixed, coordinates = coordinates)




