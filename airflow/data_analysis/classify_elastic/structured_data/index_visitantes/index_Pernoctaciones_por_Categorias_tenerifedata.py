# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_normalTable

excel = "excels_visitantes/pernoctacionesporcategorias.xls"
sheet = 0
name_index = "index_pernoctaciones_por_categorias"
type_index = "structured"


table_start_and_end = {
    "start_row": 0,
    "start_col": 0,
    "end_row": 529,
    "end_col": 9,
    "start_value_row": 1,
    "start_value_col": 0
}

type_items = {
    "year" : int,
    "month" : int,
    "type" : str,
    "value" : int
}

attributes_to_fixed={
    "place": "Tenerife"
}

pos_value_restrictions = [
     {
        'name':'type',
        'ini':2,
        'end':9
     }
]

change_months = 'month'

name_items = ["year","month","1 stars", "2 stars", "3 stars", "4 stars", "5 stars", "hoteliers","non-hoteliers","total"]

index_excels_normalTable.main(excel, sheet, name_index, type_index, table_start_and_end, type_items, name_items, pos_value_restrictions = pos_value_restrictions, attributes_to_fixed =attributes_to_fixed, change_months=change_months)



