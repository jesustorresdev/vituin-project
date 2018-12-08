# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_normalTable

excel = "excels_infraestructuras_generales/infraestructuras.xlsx"
sheet = 4
name_index = "index_cobertura_wifi"
type_index = "structured"


table_start_and_end = {
    "start_row": 4,
    "start_col": 0,
    "end_row": 12,
    "end_col": 1,
    "start_value_row": 5,
    "start_value_col": 0
}

type_items = {
    "point" : str,
    "mbps" : str,
}


coordinates = ['point','place']
name_items = ["point", "mbps"]

attributes_to_fixed={
    "place": "Puerto de la Cruz"
}

index_excels_normalTable.main(excel, sheet, name_index, type_index, table_start_and_end, type_items, name_items, attributes_to_fixed = attributes_to_fixed, coordinates = coordinates)





