# -*- coding: utf-8 -*-
import index_excels_normalTable

excel = "excels_visitantes/turistasalojadospuertodelacruz.xls"
sheet = 0
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
    "type" : str,
    "value" : int
}

fixed_attributes={
    "place": "Puerto de la Cruz"
}

pos_value = [3,8]

name_items = ["year","month","country","4 y 5 stars", "3 stars", "1 y 2 stars", "hoteliers","non-hoteliers","total"]
name_extraItem = "type"
index_excels_normalTable.main(excel, sheet, name_index, type_index, table_start_and_end, type_items, name_items, name_extraItem, pos_value, fixed_attributes)



