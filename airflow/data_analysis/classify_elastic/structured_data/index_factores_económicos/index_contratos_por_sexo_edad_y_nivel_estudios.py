# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_normalTable

excel = "excels_factores_económicos/Contratos registrados por sexo, edad y nivel de estudios 2016 a 2018.xlsx"
sheet = 0
name_index = "index_contratos_sexo_edad_estudios"
type_index = "structured"


table_start_and_end = {
    "start_row": 0,
    "start_col": 0,
    "end_row": 48962,
    "end_col": 7,
    "start_value_row": 1,
    "start_value_col": 0
}

type_items = {
    "place" : str,
    "gender" : str,
    "education" : str,
    "age" : str,
    "type" : str,
    "year" : str,
    "month" : str,
    "value" : int
}


name_items = ["place", "gender", "education", "age", "type", "year", "month", "value"]

change_months = 'month'

lowercase_letters = ["gender","place"]

fields_to_change = {
    'Gran canaria' : ['place','GRAN CANARIA'],
    'El hierro' : ['place','EL HIERRO'],
    'La gomera' : ['place','LA GOMERA'],
    'La palma' : ['place','LA PALMA'],
    'Tenerife' : ['place','TENERIFE'],
    'Lanzarote' : ['place','LANZAROTE'],
    'Fuerteventura' : ['place','FUERTEVENTURA'],
    'El rosario' : ['place','El Rosario'],
    'El sauzal' : ['place','El Sauzal'],
    'El tanque' : ['place','El Tanque'],
    'Guia de isora' : ['place','Guía de Isora'],
    'Icod de los vinos' : ['place','Icod de los Vinos'],
    'Santa cruz de tenerife' : ['place','Santa Cruz de Tenerife'],
    'Puerto de la cruz' : ['place','Puerto de la Cruz'],
    'La laguna' : ['place','La Laguna'],
    'La guancha' : ['place','La Guancha'],
    'Los realejos' : ['place','Los Realejos'],
    'La matanza' : ['place','La Matanza'],
    'La orotava' : ['place','La Orotava'],
    'La victoria' : ['place','La Victoria'],
    'Santa ursula' : ['place','Santa Úrsula'],
    'Los silos' : ['place','Los Silos'],
    'San miguel de abona' : ['place','San Miguel de Abona'],
    'Santiago del teide' : ['place','Santiago del Teide'],
    'San juan de la rambla' : ['place','San Juan de la Rambla'],
}


attributes_to_fixed={
    "item_creation": "Original",
}


index_excels_normalTable.main(excel, sheet, name_index, type_index, table_start_and_end, type_items, name_items, change_months=change_months, lowercase_letters = lowercase_letters, attributes_to_fixed = attributes_to_fixed, fields_to_change = fields_to_change)







