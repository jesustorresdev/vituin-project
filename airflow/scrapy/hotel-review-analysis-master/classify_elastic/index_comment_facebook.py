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
     'elasticsearch:9200/'
   ]
)

count = 0
actions = []

#Search the last indexed id
doc = {
        'size' : 10000,
        'query': {
             'match_all' : {}
         }
       }
try:
    res = es.search(index='index_facebook_comments', body=doc, size=0)
    #The next element indexed going to be the next id doesn't used
    cont_id = int(res['hits']['total'])

except:
    #If it's the first gruop of elements indexed
    print("First indexed")
    cont_id = 0



now = datetime.datetime.today()

for row in csv.reader(f):

    if(count!=0):
        item = {}

        for i in range(len(reference)):
                item[reference[i]] = row[i]

        action = {
                "_index": "index_facebook_comments",
                "_type": "comments",
                "_id": cont_id,
                "_source": item
                }

        if item['created_time'] ==  now.day - 7:
                id = item['id']
                #busqueda de una entrada igual
                res = es.search(index="index_facebook_comments", body={
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


