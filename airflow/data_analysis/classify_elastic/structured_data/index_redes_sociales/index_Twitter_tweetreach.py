import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import utils

import unicodecsv as csv
import datetime

from elasticsearch import Elasticsearch
from elasticsearch import helpers

#takes two arguments:
#   the name of the file to index
#   the starting index for the id
#       the ids shouldn't overlap or you will replace existing opinion units
#IMPORTANT: before indexing opinion units you must index the parent reviews

filename =  sys.argv[1]

F = open(filename)
reference = [
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
ELASTICSEARCH_INDEX='index_twitter_tweetreach'
ELASTICSEARCH_DOC_TYPE='structured'
NAMES_ITEM_FINAL = []

#Search the last indexed id
doc = {
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

j = 0

for row in csv.reader(F):
    j +=1
    if(FILE_COUNT!=0):
        item = {}
        try:
            for i in range(len(reference)):
                print row[i]
                item[reference[i]] = row[i]
            item = utils.set_date(item,['date'])
            print item['date']
            res ={}
            try:
                res = ES.search(index=ELASTICSEARCH_INDEX, body={
                    "query": {
                        "bool": {
                            "must":[
                                {"term":{"date": item['date']}}, #Use the key to compare
                                {"term":{"name": item['name']}}, #Use the key to compare
                            ]
                        }
                    }
                })
            except:
                pass

            if not res or res['hits']['hits'] == []: #If there isn't result

                if not EXIST_INDEX and FIRST_ITERATION is True:
                    NAMES_ITEM_FINAL = utils.get_names_item_final(item)
                    FIRST_ITERATION=False

                item['upload_date']=datetime.datetime.today()

                action = {
                    "_index": ELASTICSEARCH_INDEX,
                    "_type": ELASTICSEARCH_DOC_TYPE,
                    "_id": cont_id,
                    "_source": item
                }
                ACTIONS.append(action)

                cont_id += 1
            else:
                print 'repeat ', FILE_COUNT

        except Exception as error:
            print 'Error', error, ', en', FILE_COUNT
            print '------'
            pass

    FILE_COUNT += 1



if FILE_COUNT > 0:
    if EXIST_INDEX is False:
        es_new = utils.set_properties(NAMES_ITEM_FINAL, ELASTICSEARCH_DOC_TYPE, ELASTICSEARCH_INDEX)
        helpers.bulk(es_new, ACTIONS)
    else:
        helpers.bulk(ES, ACTIONS)
    print "leftovers"
    print "indexed %d" %cont_id



