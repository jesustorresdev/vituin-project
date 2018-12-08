
# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_gasto_consumo/gasto.xls"
sheet = 0
name_index = "index_gasto_por_residencia"
type_index = "structured"

name_items = {
    "type_rows" : "type",
    "subtype_rows" : "place",
    "type_cols" : "attribute_to_split_0",
    "subtype_cols" :"place_tourist_residence"
}


table_start_and_end = {
    "start_row": 310,
    "start_col": 0,
    "end_row": 334,
    "end_col": 201,
    "start_value_row": 312,
    "start_value_col": 1
}
type_value = float

attribute_to_split_remove = [{
    "attributes":["attribute_to_split_0"],         #Attributes to split
    "attr0":[0],                                   #Words by attribute 0
    "condition":["ESTIMACIÓN" ,"ANUAL"],
    "condition_pos":[1,2]
}]

attribute_to_split = [{
    "attributes":["year","trimester"],  #Attributes to split
    "attr0":[0],                        #Words by attribute 0
    "attr1":[1,2],                      #Words by attribute 1
    "exception" : "year",               #If there are fields without two arguments
    "exclude" : ["TOTAL"]               #For each exclude add the attribute. Elements in array should be in order
}]



attributes_to_fixed={
    "shop place": "En Canarias",
    "period":"TOTAL"
}

fields_to_change = {'TOTAL PAISES' : ['place_tourist_residence','TOTAL']}

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, attributes_to_fixed = attributes_to_fixed, attribute_to_split_remove = attribute_to_split_remove, attribute_to_split = attribute_to_split, fields_to_change = fields_to_change)


