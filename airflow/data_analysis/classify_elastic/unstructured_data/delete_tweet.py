import sys
import unicodecsv as csv
from elasticsearch import Elasticsearch
from datetime import datetime

#takes two arguments:
#   the name of the file to index
#   the starting index for the id
#       the ids shouldn't overlap or you will replace existing opinion units
#IMPORTANT: before indexing opinion units you must index the parent reviews

filename =  sys.argv[1]

F = open(filename)

ES = Elasticsearch(
    [
        'elasticsearch:9200/'
    ]
)
now = datetime.datetime.today()
timeAgo =  now.day - 100

res = ES.search(index="index_tweets", body={
    "query": {
        "range" : {
            "timestamp" : {
                "gte": timeAgo,
                "lte": now,
                "time_zone": "+00:00"
            }
        }
    }
})

FILE_COUNT = 0
id=''


for hit in res['hits']['hits']:
    exist = False
    for row in csv.reader(F):

        id = row[0]
        if hit["_source"]["id"] == id:
            exist = True
            break

    if not exist:
        es.update(index='index_tweets',doc_type='unstructured',id=id,
                    body={"doc": {"exist_now": 0 }})
        FILE_COUNT += 1

if FILE_COUNT > 0:
    if EXIST_INDEX is False:
        es_new = utils.set_properties(NAMES_ITEM_FINAL, ELASTICSEARCH_DOC_TYPE, ELASTICSEARCH_INDEX)
        helpers.bulk(es_new, ACTIONS)
    else:
        helpers.bulk(ES, ACTIONS)    print "Delete %d" %FILE_COUNT
else:
    print "Nothing was deleted"


