# -*- coding: UTF-8 -*-

"""Interfaz con bases de datos.
"""

__authors__ = 'Jesús Torres, Sergio Díaz'
__organization__ = 'Universidad de La Laguna'
__licensed__ = 'UNLICENSED'
__contact__ = "jmtorres@ull.edu.es, sdiazgon@ull.edu.es"
# __copyright__ = f"Copyright 2017-2018 {__organization__}"

import elasticsearch
import elasticsearch_dsl

from default_settings import Config

_HELPERS = elasticsearch.helpers
_ELASTICSEARCH = elasticsearch.Elasticsearch

_ES = elasticsearch.Elasticsearch(
    [
        'elasticsearch:9200/'
    ],
    timeout = Config.ELASTICSEARCH_TIMEOUT
)

# _ES_CLIENT = elasticsearch.Elasticsearch(
#     hosts = Config.ELASTICSEARCH_HOSTS,
#     timeout = Config.ELASTICSEARCH_TIMEOUT
# )
#
#
# _ES_DSL_SEARCH = elasticsearch_dsl.Search(using=_ES_CLIENT)
#
#
# def get_es_search():
#     """Obtener una instancia de Search para hacer consultas a Elasticsearch
#     """
#     return _ES_DSL_SEARCH
