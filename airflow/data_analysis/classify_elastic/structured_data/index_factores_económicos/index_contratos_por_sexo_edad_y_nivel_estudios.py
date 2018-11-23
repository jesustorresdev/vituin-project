# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_normalTable

excel = "excels_factores_económicos/Contratos registrados por sexo, edad y nivel de estudios 2016 a 2018.xlsx"
sheet = 0
name_index = "index_contratos_sexo_edad_estudios"
type_index = "structured"


table_start_and_end = {
    "start_row": 0,
    "start_col": 0,
    "end_row": 48962,
    "end_col": 7,
    "start_value_row": 1,
    "start_value_col": 0
}

type_items = {
    "place" : str,
    "gender" : str,
    "education" : str,
    "age" : str,
    "type" : str,
    "year" : str,
    "month" : str,
    "value" : int
}


name_items = ["place", "gender", "education", "age", "type", "year", "month", "value"]

change_months = 'month'

index_excels_normalTable.main(excel, sheet, name_index, type_index, table_start_and_end, type_items, name_items, change_months=change_months)





