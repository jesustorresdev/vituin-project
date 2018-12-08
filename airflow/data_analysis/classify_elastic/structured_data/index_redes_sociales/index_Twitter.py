from elasticsearch import Elasticsearch
from elasticsearch import helpers
import datetime
from datetime import timedelta

import sys
sys.path.append('../')
from structured_data import utils
#takes two arguments:
#   the name of the file to index
#   the starting index for the id
#       the ids shouldn't overlap or you will replace existing opinion units
#IMPORTANT: before indexing opinion units you must index the parent reviews

reference_foller = [
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

reference_tweetearch = [
    "accountsReached",
    "date",
    "impressions",
    "name",
    "platform",
    "source",
    "top_contributors"
]

ES = Elasticsearch(
    [
        'elasticsearch:9200/'
    ]
)

FILE_COUNT = 0
ACTIONS = []

EXIST_INDEX = True
FIRST_ITERATION = False
ELASTICSEARCH_INDEX='index_twitter'
ELASTICSEARCH_INDEX_TWEETSEARCH='index_twitter_tweetreach'
ELASTICSEARCH_INDEX_FOLLER='index_twitter_foller'
ELASTICSEARCH_DOC_TYPE='structured'
MAIN_FIELD='name'
DATE_FIELD='date'
NAMES_ITEM_FINAL = []

# #Search the last indexed id
doc = {
    'size' : 10000,
    'query': {
        'match_all' : {}
    }
}
try:
    res = ES.search(index=ELASTICSEARCH_INDEX, body=doc, size=0)
    #The next element indexed going to be the next id doesn't used
    cont_id = int(res['hits']['total'])

except:
    #If it's the first gruop of elements indexed
    print("First indexed")
    cont_id = 0
    EXIST_INDEX = False
    FIRST_ITERATION = True

number_entries_homes = ES.search(index=ELASTICSEARCH_INDEX_FOLLER, body=doc, size=0)
res_foller = utils.search_elastic(ELASTICSEARCH_INDEX_FOLLER, ELASTICSEARCH_DOC_TYPE)

for row_foller in res_foller:

    row_foller = row_foller['_source']
    item = {}

    for entry in row_foller:
        item[entry] = row_foller[entry]

    item[DATE_FIELD] = item[DATE_FIELD][:10]
    #Search
    doc = {
        "query": {
            "bool": {
                "filter": {
                    "term" : { MAIN_FIELD : item[MAIN_FIELD] },
                },
                "must": [
                    {
                        "range" : {
                            "date" : {
                                "gte": item[DATE_FIELD],
                                "lte": item[DATE_FIELD]
                            }
                        },
                    }
                ]

            }
        },
        'sort': [
            {"_id": "asc"}
        ]
    }

    res_tweetearch = ES.search(index=ELASTICSEARCH_INDEX_TWEETSEARCH, doc_type=ELASTICSEARCH_DOC_TYPE, body=doc, size=10000)

    #if exists row_description
    try:
        row_tweetearch = res_tweetearch['hits']['hits'][0]['_source']

        for entry in reference_tweetearch:
            if entry != 'date' and entry != 'name':
                item[entry] = row_tweetearch[entry]
    except:
        for entry in reference_tweetearch:
            if entry != 'date' and entry != 'name':
                item[entry] = ''

    if not EXIST_INDEX and FIRST_ITERATION is True:
        NAMES_ITEM_FINAL = utils.get_names_item_final(item)
        FIRST_ITERATION=False

    action = {
        "_index": ELASTICSEARCH_INDEX,
        "_type": ELASTICSEARCH_DOC_TYPE,
        "_id": cont_id,
        "_source": item
    }

    ACTIONS.append(action)

    cont_id += 1

    FILE_COUNT += 1

if FILE_COUNT > 0:
    if EXIST_INDEX is False:
        es_new = utils.set_properties(NAMES_ITEM_FINAL, ELASTICSEARCH_DOC_TYPE, ELASTICSEARCH_INDEX)
        helpers.bulk(es_new, ACTIONS)
    else:
        helpers.bulk(ES, ACTIONS)
    print "leftovers"
    print "indexed %d" %cont_id

