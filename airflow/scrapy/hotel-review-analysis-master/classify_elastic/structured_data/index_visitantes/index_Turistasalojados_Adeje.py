# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
import index_excels_normalTable

excel = "excels_visitantes/turistasalojadosadeje.xls"
name_index = "index_turistas_alojados"
type_index = "structured"


table_start_and_end = {
    "start_row": 0,
    "start_col": 0,
    "end_row": 2458,
    "end_col": 9,
    "start_value_row": 1,
    "start_value_col": 0
}

type_items = {
    "year" : int,
    "month" : int,
    "country" : str,
    "4 y 5 stars" : int,
    "3 stars" : int,
    "1 y 2 stars" : int,
    "hoteliers" : int,
    "non-hoteliers" : int,
    "total": int
}

fixed_attributes={
    "place": "Adeje"
}
name_items = ["year","month","country","4 y 5 stars", "3 stars", "1 y 2 stars", "hoteliers","non-hoteliers","total"]

index_excels_normalTable.main(excel, name_index, type_index, table_start_and_end, type_items, name_items, fixed_attributes)















