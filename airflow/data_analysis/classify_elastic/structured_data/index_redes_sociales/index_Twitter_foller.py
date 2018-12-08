# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_normalTable

file =  sys.argv[1]


excel = file
sheet = 0
name_index = "index_twitter_foller"
type_index = "structured"


table_start_and_end = {
    "start_row": 0,
    "start_col": 0,
    "end_row": 2,
    "end_col": 22,
    "start_value_row": 2,
    "start_value_col": 0
}

type_items = {
    "date" : str,
    "followers" : int,
    "followers_ratio" : float,
    "following" : int,
    "hashtags" : str,
    "hashtags_for_xtweets" : int,
    "linked_domains_for_xtweets" : str,
    "links_for_xtweets" : int,
    "media_for_xtweets" : int,
    "mentions_for_xtweets" : int,
    "name" : str,
    "platform" : str,
    "replies_for_xtweets" : int,
    "retweets_for_xtweets" : int,
    "source" : str,
    "topics" : str,
    "tweetingSchedule" : str,
    "tweets" : int,
    "twitter_clients_for_xtweets" : str,
    "xtweets" : int,
}



name_items = [
    "date",
    "followers",
    "followers_ratio",
    "following",
    "hashtags",
    "hashtags_for_xtweets",
    "linked_domains_for_xtweets",
    "links_for_xtweets",
    "media_for_xtweets",
    "mentions_for_xtweets",
    "name",
    "platform",
    "replies_for_xtweets",
    "retweets_for_xtweets",
    "source",
    "topics",
    "tweetingSchedule",
    "tweets",
    "twitter_clients_for_xtweets",
    "xtweets",
]

date=['date']


index_excels_normalTable.main(excel, sheet, name_index, type_index, table_start_and_end, type_items, name_items, date=date)



