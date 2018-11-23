import sys
import unicodecsv as csv
import json
import datetime
import ast
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import utils#Extract fields in dictonaries.

def fieldsDictionaries(dic, i, item):
    for element in dic:
        if isinstance(dic[element],dict):
            #if there are more dictionaries behind fields it call itself 
            item = fieldsDictionaries(dic[element], i, item)
        else:
            #if isn't there, save de item field
            key = element + str(i)
            item[key] = dic[element]

    return item

#Create array with the references
def createItem(row, item):
    #Firsts fields
    reference = [  "name",
                   "id",
                   "period",
                   "title",
                   "description",
                   "creation_time"

          ]

    for i in range(len(reference)):
        j=i
        if i >= 2:         #row[2] is a dictionary. After we extract its data 
           j = j+1
        item[reference[i]] = row[j]

    field = ast.literal_eval(row[2])

    i = 0 #Each element behind the dictionary
    for dic in field:
        #Go to extract fields in the dictionary
        item=fieldsDictionaries(dic,i,item)

        i=i+1

    return item

#takes two arguments:
#   the name of the file to index
#   the starting index for the id
#       the ids shouldn't overlap or you will replace existing opinion units
#IMPORTANT: before indexing opinion units you must index the parent reviews

filename =  sys.argv[1]

F = open(filename)
reference = []
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
    res = ES.search(index='index_facebook_insights', body=doc, size=0)
    #The next element indexed going to be the next id doesn't used
    cont_id = int(res['hits']['total'])

except:
    #If it's the first gruop of elements indexed
    print("First indexed")
    cont_id = 0
    EXIST_INDEX = False
    FIRST_ITERATION = True



#now = datetime.datetime.today()


for row in csv.reader(F):

    if(FILE_COUNT!=0):
        item = {}

        #create item to go up to Elasticsearch
        item=createItem(row, item)

        action = {
                "_index": "index_facebook_insights",
                "_type": "insights",
                "_id": cont_id,
                "_source": item
                }
        ''' 
        if item['creation_time'] ==  day.now - 7:
                id = item['id']
                #busqueda de una entrada igual
                res = ES.search(index="index_facebook", doc_type="posts",body={
                        "query": {
                                "match_phrase": {
                                        "id": id
                                        }
                                }
                        })
                exist = '0'
                for hit in res['hits']['hits']:
                        exist = hit["_source"]

                if exist == '':
                        ACTIONS.append(action)
        else:
        '''
        ACTIONS.append(action)

        cont_id += 1
    FILE_COUNT += 1

if FILE_COUNT > 0:
    if EXIST_INDEX is False:
        es_new = utils.set_properties(NAMES_ITEM_FINAL, ELASTICSEARCH_DOC_TYPE, ELASTICSEARCH_INDEX)
        helpers.bulk(es_new, ACTIONS)
    else:
        helpers.bulk(ES, ACTIONS)        helpers.bulk(ES, ACTIONS)
        print "leftovers"
        print "indexed %d" %cont_id

