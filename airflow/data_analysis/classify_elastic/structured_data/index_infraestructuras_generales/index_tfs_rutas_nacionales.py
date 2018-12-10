# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_normalTable

excel = "excels_infraestructuras_generales/AenaTenerifeSur.xlsx"
sheet = 1
name_index = "index_rutas_aereas"
type_index = "structured"


table_start_and_end = {
    "start_row": 0,
    "start_col": 0,
    "end_row": 25,
    "end_col": 2,
    "start_value_row": 1,
    "start_value_col": 0
}

type_items = {
    "airport" : str,
    "city" : str,
    "company" : str,
}


coordinates = ['airport','destiny']
name_items = ["airport", "city", "company"]

attributes_to_fixed={
    "destiny": "España".decode('UTF-8'),
    "origin": "Tenerife Sur"
}

index_excels_normalTable.main(excel, sheet, name_index, type_index, table_start_and_end, type_items, name_items, attributes_to_fixed = attributes_to_fixed, coordinates = coordinates)





