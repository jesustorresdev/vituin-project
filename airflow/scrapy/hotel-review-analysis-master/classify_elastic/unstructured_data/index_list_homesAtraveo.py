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

place_type = ["Puerto de la Cruz", "Tenerife","Canarias"]
place = place_type[int(sys.argv[2])]


f = open(filename)
reference = ["id_atraveo",
             "url",
             "price",
             "type_residence",
             "numberReviews",
             "mainBubbles",
             "lat",
             "lng",
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
    res = es.search(index='index_list_homes_atraveo', body=doc, size=0)
    #The next element indexed going to be the next id doesn't used
    cont_id = int(res['hits']['total'])

except:
    #If it's the first gruop of elements indexed
    print("First indexed")
    cont_id = 0

j = 0
for row in csv.reader(f):
    j +=1
    if(count!=0):
        item = {}

        try:
            for i in range(len(reference)):
                item[reference[i]] = row[i]
            item['place'] = place

            item['upload_date']=datetime.datetime.today()
            item['search_date']="08/10/2018"
            item['stay'] = '7 noches'
            res ={}
            try:
                res = es.search(index="index_list_homes_atraveo", body={
                    "query": {
                        "match_phrase": {
                            "id_atraveo": item['id_atraveo'] #Use the key to compare
                        }
                    }
                })
            except:
                pass

            if not res or res['hits']['hits'] == []: #If there isn't result

                action = {
                    "_index": "index_list_homes_atraveo",
                    "_type": "unstructured",
                    "_id": cont_id,
                    "_source": item
                }

                actions.append(action)

                cont_id += 1
            else:
                print 'repeat ', count

        except Exception as error:
            print 'Error', error, ', en', count
            print '------'
            pass

    count += 1



if count > 0:
    helpers.bulk(es, actions)
    print "leftovers"
    print "indexed %d" %cont_id

