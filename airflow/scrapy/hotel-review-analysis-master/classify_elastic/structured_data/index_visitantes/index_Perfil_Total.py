# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_visitantes/visitantes.xlsx"
sheet = 0
name_index = "index_perfil_turistico"
type_index = "structured"

name_items = {
    "type_rows" : "place_tourist_residence",
    "type_cols" : "year",
}

table_start_and_end = {
    "start_row": 19,
    "start_col": 0,
    "end_row": 30,
    "end_col": 7,
    "start_value_row": 20,
    "start_value_col": 1
}

fixed_attributes={
    "gender": "AMBOS SEXOS",
    "age" : "Cualquiera"
}

type_value = int

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, fixed_attributes)

