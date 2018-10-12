# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
import urllib, json

from structured_data import index_json

url = "excels_recursos_naturales/may2018_weather.json"

jsonurl = urllib.urlopen(url)
text = json.loads(jsonurl.read())

name_index = "index_tiempo_dia"
type_index = "structured"
path_to_start = []
#if fields_to_get is empty we're going to get all fields
fields_to_get = ['fecha', 'indicativo', 'nombre', 'provincia', 'type', 'altitud']




attributes_to_fixed={
    "mes": "mayo"
}


names_items_to_fix_in_one = [
    "tmed",
    "prec",
    "tmin",
    "horatmin",
    "tmax",
    "horatmax",
    "dir",
    "velmedia",
    "racha",
    "horaracha",
    "presMax",
    "horaPresMax",
    "presMin",
    "horaPresMin"
]


fix_fields_in_one = [{
    'name':'type',
    'names_items_to_fix_in_one': names_items_to_fix_in_one
}]

attribute_to_split_remove_string = [{
    "attributes":["fecha"],  #Attributes to remove
    "attr0":['start',8],   #String pos to delete
}]

index_json.indexed(name_index,type_index, path_to_start, text, fields_to_get, attributes_to_fixed = attributes_to_fixed, fix_fields_in_one = fix_fields_in_one, attribute_to_split_remove_string = attribute_to_split_remove_string, change_months = change_months)

