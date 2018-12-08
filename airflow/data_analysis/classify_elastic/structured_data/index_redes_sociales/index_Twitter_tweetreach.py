# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_normalTable

file =  sys.argv[1]


excel = file
sheet = 0
name_index = "index_twitter_tweetreach"
type_index = "structured"


table_start_and_end = {
    "start_row": 0,
    "start_col": 0,
    "end_row": 2,
    "end_col": 6,
    "start_value_row": 2,
    "start_value_col": 0
}

type_items = {
    "accountsReached" : int,
    "date" : str,
    "impressions" : int,
    "name" : str,
    "platform" : str,
    "source" : str,
    "top_contributors" : int
}



name_items = [
    "accountsReached",
    "date",
    "impressions",
    "name",
    "platform",
    "source",
    "top_contributors"
]

date=['date']


index_excels_normalTable.main(excel, sheet, name_index, type_index, table_start_and_end, type_items, name_items, date=date)



