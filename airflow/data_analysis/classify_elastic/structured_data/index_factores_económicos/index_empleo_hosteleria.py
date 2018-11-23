# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_factores_económicos/empleoHosteleria.xls"
sheet = 0
name_index = "index_empleo_hosteleria"
type_index = "structured"

name_items = {
    "type_rows" : "sector",
    "type_cols" : "place",
    "subtype_cols" : "attribute_to_split_0",
}

table_start_and_end = {
    "start_row": 7,
    "start_col": 0,
    "end_row": 11,
    "end_col": 78,
    "start_value_row": 9,
    "start_value_col": 1
}

type_value = int


attribute_to_split = [{
    "attributes":["year","trimester"],  #Attributes to split
    "attr0":[0],                        #Words by attribute 0
    "attr1":[1,2],                      #Words by attribute 1
}]

lowercase_letters = ["sector"]

fields_to_change = {'Tenerife - Valle de la Orotava':['place','Valle de la Orotava']}

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value,   attribute_to_split = attribute_to_split, lowercase_letters = lowercase_letters, fields_to_change = fields_to_change)


