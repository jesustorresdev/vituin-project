# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_normalTable

excel = "excels_visitantes/turistasalojadospuertodelacruz.xls"
sheet = 0
name_index = "index_turistas_alojados"
type_index = "structured"


table_start_and_end = {
    "start_row": 0,
    "start_col": 0,
    "end_row": 2625,
    "end_col": 8,
    "start_value_row": 1,
    "start_value_col": 0
}

type_items = {
    "year" : str,
    "month" : str,
    "country" : str,
    "type" : str,
    "value" : int
}

attributes_to_fixed={
    "place": "Puerto de la Cruz"
}

pos_value_restrictions = [
     {
        'name':'type',
        'ini':3,
        'end':8
     }
]

name_items = ["year","month","country","4 y 5 stars", "3 stars", "1 y 2 stars", "hoteliers","non-hoteliers","total"]

field_region = ["country"]

index_excels_normalTable.main(excel, sheet, name_index, type_index, table_start_and_end, type_items, name_items, pos_value_restrictions = pos_value_restrictions, attributes_to_fixed =attributes_to_fixed,  field_region = field_region)



