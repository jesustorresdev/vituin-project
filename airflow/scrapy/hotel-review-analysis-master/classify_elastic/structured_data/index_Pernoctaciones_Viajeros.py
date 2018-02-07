import index_excels

excel = "Pernoctaciones_Viajeros.xls"
name_index = "index_pernoctaciones_viajeros""
type_index = "structured"

name_items = {
    "type_rows" : "type",
    "subtype_rows" : "place_tourist_residence",
    "type_cols" : "place",
    "subtype_cols" :"year"
}

start_row = 9
start_col = 1

type_value = int

index_excels.main(excel, name_index, type_index, name_items, start_row, start_col, type_value)
