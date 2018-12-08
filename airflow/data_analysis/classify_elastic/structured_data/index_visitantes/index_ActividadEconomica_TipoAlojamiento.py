# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_visitantes/actividadEco_tipoAlojamiento.xls"
sheet = 0
name_index = "index_actividad_economica_por_tipo_alojamiento"
type_index = "structured"

name_items = {
    "type_rows" : "activity",
    "type_cols" : "attribute_to_split_0",
    "subtype_rows" : "accommodation",
}


table_start_and_end = {
    "start_row": 7,
    "start_col": 0,
    "end_row": 103,
    "end_col": 40 ,
    "start_value_row": 8,
    "start_value_col": 1
}

attribute_to_split= [{
    "attributes":["year","trimester"],  #Attributes to split
    "attr0":[0],                        #Words by attribute 0
    "attr1":[1,2],                      #Words by attribute 1
    "exception" : "year",               #If there are fields without two arguments
    "exclude" : ["TOTAL"]               #For each exclude add the attribute. Elements in array should be in order
}]

fields_to_change = {'TOTAL ALOJAMIENTOS':['accommodation','TOTAL'],'TOTAL ACTIVIDAD ECONÓMICA':['activity','TOTAL']}

type_value = int

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, attribute_to_split=attribute_to_split, fields_to_change = fields_to_change)
