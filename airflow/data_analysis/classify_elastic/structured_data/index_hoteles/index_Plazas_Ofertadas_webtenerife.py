# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_visitantes/tcpuerto201810.xlsx"
sheet = 57
name_index = "index_plazas_ofertadas_webtenerife"
type_index = "structured"


name_items = {
    "type_rows" : "year",
    "subtype_rows" : "semester",
    "type_cols" : "place",
    "subtype_cols" :"accomodation"
}


table_start_and_end = {
    "start_row": 4,
    "start_col": 1,
    "end_row": 88,
    "end_col": 47,
    "start_value_row": 7,
    "start_value_col": 3
}
type_value = int



add_column_value_to_previous_item = [{
    "type_item":"subtype_cols",
    "name_item":"interanual variation",
    "name":"variación interanual"
}]


fields_to_change = {'Total' : ['accomodation','TOTAL TURISTAS'], 'extrahotelero' : ['accomodation','Extrahotelero'], 'Tenerife':['place', 'TENERIFE']}

involved_elements = [{"name":"Santa Cruz","number":4,"type":"less", "subtype_cols":["TOTAL TURISTAS"]}]
irregular_table = [{"type":"sum", "name_item":"subtype_cols", "number":4, "involved_elements": involved_elements}]
third_col = True
two_rows = True
index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, \
                        irregular_table = irregular_table,  add_column_value_to_previous_item = add_column_value_to_previous_item, \
                        fields_to_change =  fields_to_change, third_col = third_col, two_rows = two_rows)


