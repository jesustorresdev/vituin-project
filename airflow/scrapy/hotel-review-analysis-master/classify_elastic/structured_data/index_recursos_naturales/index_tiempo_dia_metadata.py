# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
import urllib, json

from structured_data import index_json_metadata

url = "excels_recursos_naturales/month_weather_metadata.json"

jsonurl = urllib.urlopen(url)
text = json.loads(jsonurl.read())

name_index = "index_tiempo_dia_metadata"
type_index = "structured"
path_to_start = ['campos']
fields_to_get = ['id', 'descripcion']
index_json_metadata.indexed(name_index,type_index, path_to_start, text, fields_to_get)

