# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_recursos_naturales/valoraciones.xlsx"
sheet = 0
name_index = "index_valoraciones_bano_clima"
type_index = "structured"

name_items = {
    "type_rows" : "type",
    "subtype_rows" : "place_origin",
    "type_cols" : "attribute_to_split_0",
}

table_start_and_end = {
    "start_row": 0,
    "start_col": 0,
    "end_row": 16,
    "end_col": 40,
    "start_value_row": 1,
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
        "exclude" : ["Total"]               #For each exclude add the attribute. Elements in array should be in order
    }]


type_value = int

field_region = ["place_origin"]

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, attributes_to_fixed=attributes_to_fixed, attribute_to_split=attribute_to_split, field_region = field_region)

