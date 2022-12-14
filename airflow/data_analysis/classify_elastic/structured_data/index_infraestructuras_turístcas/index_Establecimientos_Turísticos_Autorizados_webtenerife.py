# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_visitantes/tcpuerto201810.xlsx"
sheet = 67
name_index = "index_establecimientos_turisticos_autorizados_webtenerife"
type_index = "structured"

name_items = {
    "type_rows" : "year",
    "type_cols" : "accomodation",
    "subtype_cols" : "accomodation"
}


table_start_and_end = {
    "start_row": 4,
    "start_col": 1,
    "end_row": 26,
    "end_col": 27,
    "start_value_row": 6,
    "start_value_col": 2
}

attributes_to_fixed={
    "place": "Puerto de la Cruz"
}

lowercase_letters = ["month"]

type_value = int

fields_to_change = {
    'Total establecimientos' : ['accomodation','TOTAL ESTABLECIMIENTOS'],
    'Total establecimientos hoteles Hoteles' : ['accomodation','TOTAL HOTELES'],
    'Total establecimientos apartamentos Apartamentos' : ['accomodation','TOTAL APARTAMENTOS'],
    'Total establecimientos hoteles rurales Hoteles Rurales' : ['accomodation','TOTAL HOTELES RURALES'],
    'Total establecimientos Casas Rurales' : ['accomodation','TOTAL CASAS RURALES'],

}

establishments = True

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, attributes_to_fixed = attributes_to_fixed, fields_to_change = fields_to_change, establishments = establishments)
