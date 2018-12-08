# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_normalTable

excel = "excels_hoteles/indicedeocupacionporzonas.xls"
sheet = 0
name_index = "index_indice_censal_por_zonas"
type_index = "structured"


table_start_and_end = {
    "start_row": 0,
    "start_col": 0,
    "end_row": 526,
    "end_col": 16,
    "start_value_row": 1,
    "start_value_col": 0
}

type_items = {
    "year" : int,
    "month" : int,
    "type" : str,
    "value" : float
}


pos_value_restrictions = [
    {
        'name':'type',
        'ini':2,
        'end':4
    },
    {
        'name':'type',
        'ini':5,
        'end':7
    },
    {
        'name':'type',
        'ini':8,
        'end':10
    },
    {
        'name':'type',
        'ini':11,
        'end':13
    },
    {
        'name':'type',
        'ini':14,
        'end':16
    }
]

attributes_to_fixed_to_restriction=[
    {"place":"Santa Cruz de Tenerife"},
    {"place":"La Laguna - Tegueste - Tacoronte"},
    {"place":"Puerto de la Cruz - Resto Tenerife"},
    {"place":"Adeje - Arona - Guía Isora - Santiago del Teide - San Miguel - Candelaria - Resto Sur"},
    {"place":"Tenerife"}
]

change_months = 'month'

name_items = ["year","month","hoteliers","non-hoteliers","total","hoteliers","non-hoteliers","total","hoteliers","non-hoteliers","total","hoteliers","non-hoteliers","total","hoteliers","non-hoteliers","total"]

index_excels_normalTable.main(excel, sheet, name_index, type_index, table_start_and_end, type_items, name_items, pos_value_restrictions = pos_value_restrictions, attributes_to_fixed_to_restriction = attributes_to_fixed_to_restriction, change_months=change_months)



