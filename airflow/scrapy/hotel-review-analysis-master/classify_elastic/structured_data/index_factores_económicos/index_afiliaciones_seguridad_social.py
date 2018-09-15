# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_factores_económicos/Factores económicos.xlsx"
sheet = 0
name_index = "index_afiliaciones"
type_index = "structured"

name_items = {
    "type_cols" : "attribute_to_split_0",
    "type_rows" : "sector",
}


table_start_and_end = {
    "start_row": 85,
    "start_col": 0,
    "end_row": 98,
    "end_col": 31,
    "start_value_row": 86,
    "start_value_col": 1
}
type_value = int


attribute_to_split = [{
    "attributes":["year","trimester"],  #Attributes to split
    "attr0":[0],                        #Words by attribute 0
    "attr1":[1,2],                      #Words by attribute 1
}]

attributes_to_fixed={
    "place": "Tenerife",
}

lowercase_letters = ["sector"]

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, attributes_to_fixed = attributes_to_fixed, attribute_to_split = attribute_to_split, lowercase_letters = lowercase_letters)


