# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_infraestructuras_turísticas/Infraestructuras turísticas.xlsx"
sheet = 0
name_index = "index_hoteles_istac"
type_index = "structured"

name_items = {
    "type_rows" : "type",
    "subtype_rows" : "stars",
    "type_cols" : "place",
    "subtype_cols" : "attribute_to_split_0"
}


table_start_and_end = {
    "start_row": 1,
    "start_col": 0,
    "end_row": 14,
    "end_col": 106,
    "start_value_row": 3,
    "start_value_col": 1
}
type_value = int

attribute_to_split = [{
    "attributes":["year","month"],      #Attributes to split
    "attr0":[0],                        #Words by attribute 0
    "attr1":[1],                        #Words by attribute 1
    "exception" : "year",               #If there are fields without two arguments
    "exclude" : ["Total"]               #For each exclude add the attribute. Elements in array should be in order
}]

fields_to_change = {'TOTAL CATEGORÍAS' : ['stars','TOTAL']}


index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, attribute_to_split = attribute_to_split,fields_to_change = fields_to_change)
