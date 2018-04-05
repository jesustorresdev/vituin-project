# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_normalTable

excel = "excels_recursos_naturales/recursos.xlsx"
sheet = 4
name_index = "index_especies_amenazadas"
type_index = "structured"

table_start_and_end = {
    "start_row": 3,
    "start_col": 0,
    "end_row": 21,
    "end_col": 4,
    "start_value_row": 4,
    "start_value_col": 0
}

type_items = {
    "scientific name" : str,
    "common name" : str,
    "endemic" : str,
    "island" : str,
    "category" : str
}

pos_value_restrictions = []
fixed_attributes={}
name_items = ["scientific name", "common name", "endemic", "island", "category"]
index_excels_normalTable.main(excel, sheet, name_index, type_index, table_start_and_end, type_items, name_items, pos_value_restrictions, fixed_attributes)




