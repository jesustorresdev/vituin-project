import sys
import unicodecsv as csv
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import utils
#takes two arguments:
#   the name of the file to index
#   the starting index for the id
#       the ids shouldn't overlap or you will replace existing opinion units
#IMPORTANT: before indexing opinion units you must index the parent reviews

filename =  sys.argv[1]

F = open(filename)
reference = ["id",
             "text",
             "likes",
             "retweets",
             "user_searched",
             "in_reply_to_status_id",
             "first_tweet_reply",
             "key",
             "creation_time",
             "extraction_time"
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
ELASTICSEARCH_INDEX='index_tripadvisor_hoteles'
ELASTICSEARCH_DOC_TYPE='unstructured'
NAMES_ITEM_FINAL = []

#Search the last indexed id
doc = {
    'size' : 10000,
    'query': {
        'match_all' : {}
    }
}
try:
    res = ES.search(index='index_tweets_user', body=doc, size=0)
    #The next element indexed going to be the next id doesn't used
    cont_id = int(res['hits']['total'])

except:
    #If it's the first gruop of elements indexed
    print("First indexed")
    cont_id = 0
    EXIST_INDEX = False
    FIRST_ITERATION = True


for row in csv.reader(F):

    if(FILE_COUNT!=0):
        item = {}

        for i in range(len(reference)):
            item[reference[i]] = row[i]

        #ID in facebook
        id = item['id']
        #busqueda de una entrada igual
        res = ES.search(index="index_tweets_user", body={
            "query": {
                "match_phrase": {
                    "id": id
                }
            }
        })
        exist = False
        same = True

        #ID of the index in elastic
        _id = 0
        for hit in res['hits']['hits']:
            exist = hit["_source"]
            element = hit

        if exist:
            #If exists but it has modified (new retweets or favorites)
            if element["_source"]["key"] != item['key']:

                _id = element["_source"]["_id"]

                if not EXIST_INDEX and FIRST_ITERATION is True:
            NAMES_ITEM_FINAL = utils.get_names_item_final(item)
            FIRST_ITERATION=False

        action = {
                    "_index": "index_tweets_user",
                    "_type": ELASTICSEARCH_DOC_TYPE,
                    "_id": _id,
                    "_source": item
                }

                ACTIONS.append(action)


        #If not exists in de index this element
        else:
            action = {
                "_index": "index_tweets_user",
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


