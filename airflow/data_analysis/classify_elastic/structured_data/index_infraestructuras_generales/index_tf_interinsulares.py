# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_infraestructuras_generales/infraestructuras.xlsx"
sheet = 0
name_index = "index_aeropuertos"
type_index = "structured"

name_items = {
    "type_rows" : "place_origin",
    "type_cols" : "attribute_to_split_0"
}



table_start_and_end = {
    "start_row": 236,
    "start_col": 0,
    "end_row": 246,
    "end_col": 106,
    "start_value_row": 237,
    "start_value_col": 1
}
type_value = int

attributes_to_fixed={
    "airport": "Tenerife (ambos)",
    "market" : "Vuelos interinsulares"
}

field_region = ['place_origin']

fields_to_change = {'TOTAL AEROPUERTOS DE ORIGEN' : ['place_origin','Canarias']}


attribute_to_split_remove = [{
    "attributes":["attribute_to_split_0"],         #Attributes to split
    "attr0":[0],                                   #Words by attribute 0
    "condition":["TOTAL"],
    "condition_pos":[1]
}]

attribute_to_split = [{
    "attributes":["year","month"],      #Attributes to split
    "attr0":[0],                        #Words by attribute 0
    "attr1":[1],                        #Words by attribute 1
    "exception" : "year",               #If there are fields without two arguments
    "exclude" : ["Total"]               #For each exclude add the attribute. Elements in array should be in order
}]

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, attributes_to_fixed = attributes_to_fixed, attribute_to_split = attribute_to_split, attribute_to_split_remove = attribute_to_split_remove, field_region = field_region, fields_to_change = fields_to_change)
