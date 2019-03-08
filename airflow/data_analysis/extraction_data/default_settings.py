# -*- coding: UTF-8 -*-

"""Configuraciones por defecto de la aplicación.
"""

__authors__ = 'Sergio Díaz, Jesús Torres'
__organization__ = 'Universidad de La Laguna'
__licensed__ = 'UNLICENSED'
__contact__ = "jmtorres@ull.edu.es, sdiazgon@ull.edu.es"
# __copyright__ = f"Copyright 2017-2018 {__organization__}"


class Config:
    ELASTICSEARCH_HOSTS = None
    ELASTICSEARCH_TIMEOUT = 300


class DevelopmentConfig(Config):
    ENV = 'development'
    GOOGLEMAP_ACCESS_TOKEN = 'AIzaSyD2owaTzJTWi9m1f2QqAlJ1S0hfFT3nT0w'