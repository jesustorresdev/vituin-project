import index_excels

excel = "indice_Censal.xls"
name_index = "index_indice_censal"
type_index = "structured"

name_items = {
    "type_rows" : "type",
    "type_cols" : "place",
    "subtype_cols" :"year"
}

start_row = 9
start_col = 1

type_value = float

index_excels.main(excel, name_index, type_index, name_items, start_row, start_col, type_value)
