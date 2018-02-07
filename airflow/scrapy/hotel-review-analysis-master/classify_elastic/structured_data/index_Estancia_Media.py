import index_excels

excel = "estancia_Media.xls"
name_index = "index_estancia_media"
type_index = "structured"

name_items = {
    "type_rows" : "place_tourist_residence",
    "type_cols" : "place",
    "subtype_cols" :"year"
}

start_row = 9
start_col = 1

type_value = float

index_excels.main(excel, name_index, type_index, name_items, start_row, start_col, type_value)
