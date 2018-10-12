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

f = open(filename)

es = Elasticsearch(
    [
        'elasticsearch:9200/'
    ]
)
now = datetime.datetime.today()
timeAgo =  now.day - 100

res = es.search(index="index_facebook_comments", body={
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

count = 0
id=''


for hit in res['hits']['hits']:
    exist = False
    for row in csv.reader(f):

        id = row[0]
        if hit["_source"]["id"] == id:
            exist = True
            break

    if not exist:
        es.update(index='index_facebook_comments',doc_type='unstructured',id=id,
                  body={"doc": {"exist_now": 0 }})
        count += 1

if count > 0:
    print "Delete %d" %count
else:
    print "Nothing was deleted"


