import sys
import unicodecsv as csv
import json
import datetime

from elasticsearch import Elasticsearch
from elasticsearch import helpers

#takes two arguments:
#   the name of the file to index
#   the starting index for the id
#       the ids shouldn't overlap or you will replace existing opinion units
#IMPORTANT: before indexing opinion units you must index the parent reviews

filename =  sys.argv[1]

#cont_id = int(sys.argv[2])



cont_id = int(1)
f = open(filename)
reference = ["id",
             "created_time",
             "id_transmitter",
             "message",
             "likes",
             "loves",
             "wows",
             "hahas",
             "sads",
             "angries",
             "thankfuls",
             "prides",
             "parent"
            ]

es = Elasticsearch(
   [
     'elastic:vituinproject@elasticsearch:9200/',
   ]
)

count = 0
actions = []

now = datetime.datetime.today()

for row in csv.reader(f):

    if(count!=0):
        item = {}

        for i in range(len(reference)):
                item[reference[i]] = row[i]

        action = {
                "_index": "index_facebook",
                "_type": "comments",
                "_id": cont_id,
                "_source": item
                }
 

        if item['created_time'] ==  now.day - 7:
                id = item['id']
                #busqueda de una entrada igual
                res = es.search(index="index_facebook", doc_type="posts",body={
                        "query": {
                                "match_phrase": {
                                        "id": id
                                        }
                                }
                        })
                exist = '0'
                for hit in res['hits']['hits']:
                        exist = hit["_source"]

                if exist == '0':
                        actions.append(action)
        else:

                actions.append(action)

        cont_id += 1

    count += 1

if count > 0:
        helpers.bulk(es, actions)
        print "leftovers"
        print "indexed %d" %cont_id


