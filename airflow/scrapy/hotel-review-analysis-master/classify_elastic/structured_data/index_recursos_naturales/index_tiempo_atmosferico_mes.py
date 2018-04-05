import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_visitantes/recursos.xlsx"
sheet = "Tiempo atmosférico"
name_index = "index_tiempo_atmosferico_mes"
type_index = "structured"

name_items = {
    "type_rows" : "type",
    "type_cols" : "day"
}


table_start_and_end = {
    "start_row": 3,
    "start_col": 1,
    "end_row": 17,
    "end_col": 30,
    "start_value_row": 4,
    "start_value_col": 2
}
type_value = float

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value)


