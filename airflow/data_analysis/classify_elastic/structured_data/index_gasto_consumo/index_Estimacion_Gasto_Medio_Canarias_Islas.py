# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_gasto_consumo/gasto.xls"
sheet = 0
name_index = "index_estimacion_gasto_por_residencia"
type_index = "structured"

name_items = {
    "type_rows" : "type",
    "subtype_rows" : "place_tourist_residence",
    "type_cols" : "year",
    "subtype_cols" : "place"
}


table_start_and_end = {
    "start_row": 44,
    "start_col": 0,
    "end_row": 53,
    "end_col":35,
    "start_value_row": 46,
    "start_value_col": 1
}
type_value = float

attribute_to_split_remove = [{
    "attributes":["year"],         #Attributes to split
    "attr0":[0],                   #Words by attribute 0
}]

field_region = ["place_tourist_residence"]

fields_to_change = {'TOTAL PAISES' : ['place_tourist_residence','TOTAL']}

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, attribute_to_split_remove = attribute_to_split_remove, field_region = field_region, fields_to_change = fields_to_change)
