# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_recursos_naturales/recursos.xlsx"
sheet = 0
name_index = "index_tiempo_atmosferico_anyo"
type_index = "structured"

name_items = {
    "type_rows" : "type",
    "type_cols" : "month"
}


table_start_and_end = {
    "start_row": 20,
    "start_col": 1,
    "end_row": 46,
    "end_col": 13,
    "start_value_row": 21,
    "start_value_col": 2
}
type_value = float


attributes_to_fixed={
    "place": "Puerto de la Cruz"
}



names_items_to_fix_in_one = [
    "p_max",
    "hr",
    "q_max",
    "nw_55",
    "q_mar",
    "q_med",
    "tm_min",
    "ta_max",
    "ts_min",
    "nt_30",
    "w_racha",
    "np_100",
    "nw_91",
    "np_001",
    "ta_min",
    "w_rec",
    "e",
    "np_300",
    "p_mes",
    "w_med",
    "nt_00",
    "ti_max",
    "tm_mes",
    "tm_max",
    "q_min",
    "np_010"
]


fix_fields_in_one = [
    {
        'name':'type',
        'names_items_to_fix_in_one': names_items_to_fix_in_one
    }
]

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, attributes_to_fixed = attributes_to_fixed, fix_fields_in_one = fix_fields_in_one)


