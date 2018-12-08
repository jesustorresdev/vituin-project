# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_entorno_social/Entorno social.xlsx"
sheet = 0
name_index = "index_valoraciones_sociedad"
type_index = "structured"

name_items = {
    "type_rows" : "type",
    "subtype_rows" : "place_origin",
    "type_cols" : "attribute_to_split_0",
}

table_start_and_end = {
    "start_row": 11,
    "start_col": 0,
    "end_row": 35,
    "end_col": 40,
    "start_value_row": 12,
    "start_value_col": 1
}

attributes_to_fixed={
    "place": "Tenerife",
}

attribute_to_split= [{
    "attributes":["year","trimester"],  #Attributes to split
    "attr0":[0],                        #Words by attribute 0
    "attr1":[1,2],                      #Words by attribute 1
    "exception" : "year",               #If there are fields without two arguments
    "exclude" : ["TOTAL"]               #For each exclude add the attribute. Elements in array should be in order
}]

fields_to_change = {'TOTAL PAÍSES' : ['place_origin','TOTAL']}

type_value = float

field_region = ["place_origin"]

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, attributes_to_fixed=attributes_to_fixed, attribute_to_split=attribute_to_split, field_region = field_region, fields_to_change = fields_to_change)
