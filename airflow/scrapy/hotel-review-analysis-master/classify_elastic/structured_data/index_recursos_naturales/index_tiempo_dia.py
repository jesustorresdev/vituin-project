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
fields_to_get = []
index_json.indexed(name_index,type_index, path_to_start, text, fields_to_get)

