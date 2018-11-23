# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_normalTable

excel = "excels_encuestas/encuesta_normalizado.xlsx"
sheet = 0
name_index = "index_encuestas"
type_index = "structured"


table_start_and_end = {
    "start_row": 0,
    "start_col": 0,
    "end_row": 182,
    "end_col": 3,
    "start_value_row": 1,
    "start_value_col": 0
}

type_items = {
    "respuesta" : str,
    "grupo" : str,
    "indicador" : str,
    "subindicador" : str,
}


name_items = ["respuesta","grupo","indicador","subindicador"]

field_region = ["country"]

index_excels_normalTable.main(excel, sheet, name_index, type_index, table_start_and_end, type_items, name_items)



