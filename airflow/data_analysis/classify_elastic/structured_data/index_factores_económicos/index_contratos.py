# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_normalTable

excel = "excels_factores_económicos/Factores económicos.xlsx"
sheet = 0
name_index = "index_contratos"
type_index = "structured"


table_start_and_end = {
    "start_row": 27,
    "start_col": 0,
    "end_row": 40,
    "end_col": 9,
    "start_value_row": 28,
    "start_value_col": 0
}

type_items = {
    "activity" : str,
    "code" : str,
    "island" : str,
    "value" : int
}

pos_value_restrictions = [
    {
        'name':'island',
        'ini':2,
        'end':9
    }
]


name_items = ["activity", "code", "Tenerife", "El Hierro", "Fuerteventura", "Gran Canaria", "La Gomera", "La Palma", "Lanzarote", "Canarias"]


index_excels_normalTable.main(excel, sheet, name_index, type_index, table_start_and_end, type_items, name_items, pos_value_restrictions = pos_value_restrictions)



