import sys
import unicodecsv as csv
from elasticsearch import Elasticsearch
from elasticsearch import helpers

#takes two arguments:
#   the name of the file to index
#   the starting index for the id
#       the ids shouldn't overlap or you will replace existing opinion units
#IMPORTANT: before indexing opinion units you must index the parent reviews

filename =  sys.argv[1]

f = open(filename)
reference = ["id",
             "message",
             "story",
             "comments",
             "shares",
             "likes",
             "loves",
             "wows",
             "hahas",
             "sads",
             "angries",
             "thankfuls",
             "prides",
             "key"
             "created_time",
             "extract_time"
            ]

es = Elasticsearch(
   [
     'elasticsearch:9200/' 
   ]
)

#Search the last indexed id
doc = {
        'size' : 10000,
        'query': {
             'match_all' : {}
         }
       }
try:
    res = es.search(index='index_facebook_posts', body=doc, size=0)
    #The next element indexed going to be the next id doesn't used
    cont_id = int(res['hits']['total'])

except:
    #If it's the first gruop of elements indexed
    print("First indexed")
    cont_id = 0


count = 0
actions = []


for row in csv.reader(f):

    if(count!=0):
        item = {}

        for i in range(len(reference)):
                item[reference[i]] = row[i]

        #ID in facebook
        id = item['id']
        res = es.search(index="index_facebook_posts", body={
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
            exist = True

            if exist:
                if hit["_source"]["key"] != item['key']:
                    same = False
                    _id = hit["_source"]["_id"]

        #If not exists in de index this element
        if exist is False:

            action = {
                    "_index": "index_facebook_posts",
                    "_type": "posts",
                    "_id": cont_id,
                    "_source": item
            }

            actions.append(action)

            cont_id += 1

        #If exists but it hasn't modified
        elif same is False:

            action = {
                "_index": "index_facebook_posts",
                "_type": "posts",
                "_id": _id,
                "_source": item
            }


    count += 1

if count > 0:
        helpers.bulk(es, actions)
        print "leftovers"
        print "indexed %d" %cont_id


