import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_visitantes/visitantes.xlsx"
sheet = 0
name_index = "index_poblacion_turistica"
type_index = "structured"

name_items = {
    "type_rows" : "place",
    "type_cols" : "year",
}

table_start_and_end = {
    "start_row": 34,
    "start_col": 0,
    "end_row": 45,
    "end_col": 6,
    "start_value_row": 35,
    "start_value_col": 1
}


type_value = int


index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value)

