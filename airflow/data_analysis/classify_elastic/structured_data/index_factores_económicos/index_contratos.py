# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_normalTable

excel = "excels_factores_económicos/contratos 2016 a 2018.xlsx"
sheet = 0
name_index = "index_contratos"
type_index = "structured"


table_start_and_end = {
    "start_row": 0,
    "start_col": 0,
    "end_row": 2462,
    "end_col": 5,
    "start_value_row": 1,
    "start_value_col": 0
}

type_items = {
    "activity" : str,
    "code" : str,
    "place" : str,
    "month" : str,
    "year" : str,
    "value" : int
}


name_items = ["year", "month", "place", "activity", "code", "value"]

change_months = 'month'

index_excels_normalTable.main(excel, sheet, name_index, type_index, table_start_and_end, type_items, name_items, change_months=change_months)



