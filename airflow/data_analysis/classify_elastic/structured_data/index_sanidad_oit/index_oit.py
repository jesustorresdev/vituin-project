# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_normalTable

excel = "excels_sanidad_oit/sanidad_oit.xlsx"
sheet = 0
name_index = "index_oficinas_turismo"
type_index = "structured"


table_start_and_end = {
    "start_row": 1,
    "start_col": 0,
    "end_row": 3,
    "end_col":6,
    "start_value_row": 2,
    "start_value_col": 0
}

type_items = {
    "name" : str,
    "adress" : str,
    "lat" : str,
    "lng" : str,
    "phone" : str,
    "email" : str,
    "schedule" : str,
}


name_items = ["name", "adress","lat","lng","phone","email","schedule"]

attributes_to_fixed={
    "place": "Puerto de la Cruz"
}

index_excels_normalTable.main(excel, sheet, name_index, type_index, table_start_and_end, type_items, name_items, attributes_to_fixed = attributes_to_fixed)





