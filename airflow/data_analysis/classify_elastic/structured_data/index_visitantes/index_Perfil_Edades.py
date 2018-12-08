# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_visitantes/visitantes.xlsx"
sheet = 0
name_index = "index_perfil_turistico"
type_index = "structured"

name_items = {
    "type_rows" : "gender",
    "type_cols" : "attribute_to_split_0",
    "subtype_rows" : "place_tourist_residence",
    "subtype_cols" :"age"
}


table_start_and_end = {
    "start_row": 2,
    "start_col": 0,
    "end_row": 16,
    "end_col": 134 ,
    "start_value_row": 4,
    "start_value_col": 1
}

attribute_to_split= [{
    "attributes":["year","trimester"],  #Attributes to split
    "attr0":[0],                        #Words by attribute 0
    "attr1":[1,2],                      #Words by attribute 1
    "exception" : "year",               #If there are fields without two arguments
    "exclude" : ["TOTAL"]               #For each exclude add the attribute. Elements in array should be in order
}]

fields_to_change = {'TOTAL PAÍSES':['place_tourist_residence','TOTAL']}

type_value = int

field_region = ["place_tourist_residence"]

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, field_region = field_region, attribute_to_split=attribute_to_split, fields_to_change = fields_to_change)
