# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_entorno_natural/Entorno natural.xlsx"
sheet = 1
name_index = "index_residuos_per_capita"
type_index = "structured"

name_items = {
    "type_rows" : "type",
    "type_cols" : "year",
}

table_start_and_end = {
    "start_row": 2,
    "start_col": 0,
    "end_row": 7,
    "end_col": 6,
    "start_value_row": 3,
    "start_value_col": 1
}

attributes_to_fixed={
    "place": "Canarias",
}


type_value = float

lowercase_letters = ["type"]

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, attributes_to_fixed=attributes_to_fixed, lowercase_letters = lowercase_letters)