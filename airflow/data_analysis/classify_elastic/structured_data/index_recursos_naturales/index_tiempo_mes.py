# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
import urllib, json

from structured_data import index_json

url = "excels_recursos_naturales/2018_weather.json"

jsonurl = urllib.urlopen(url)
text = json.loads(jsonurl.read())

name_index = "index_tiempo_mes"
type_index = "structured"

path_to_start = []
#if fields_to_get is empty we're going to get all fields
fields_to_get = ['fecha', 'indicativo', 'type']
fields_to_change = {'2018-13' : ['fecha','TOTAL']}



attributes_to_fixed={
    "place": "Puerto de la Cruz"
}


names_items_to_fix_in_one = [
    "p_max",
    "hr",
    "q_max",
    "nw_55",
    "q_mar",
    "q_med",
    "tm_min",
    "ta_max",
    "ts_min",
    "nt_30",
    "w_racha",
    "np_100",
    "nw_91",
    "np_001",
    "ta_min",
    "w_rec",
    "e",
    "np_300",
    "p_mes",
    "w_med",
    "nt_00",
    "ti_max",
    "tm_mes",
    "tm_max",
    "q_min",
    "np_010"
]


fix_fields_in_one = [{
        'name':'type',
        'names_items_to_fix_in_one': names_items_to_fix_in_one
    }]

attribute_to_split_remove_string = [{
    "attributes":["fecha"],  #Attributes to remove
    "attr0":['start',5],   #String pos to delete
}]

change_months = ['fecha']


index_json.indexed(name_index,type_index, path_to_start, text, fields_to_get, fields_to_change = fields_to_change, attributes_to_fixed = attributes_to_fixed, fix_fields_in_one = fix_fields_in_one, attribute_to_split_remove_string = attribute_to_split_remove_string, change_months = change_months)



