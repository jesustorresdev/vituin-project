import sys
import unicodecsv as csv
import json
import datetime
import ast
from elasticsearch import Elasticsearch
from elasticsearch import helpers

#Extract fields in dictonaries.

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
                   "created_time"

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
#cont_id = int(sys.argv[2])
cont_id = int(1)
f = open(filename)
reference = []
es = Elasticsearch(['elasticsearch:9200'])

count = 0
actions = []




for row in csv.reader(f):

    if(count!=0):
        item = {}

        #create item to go up to Elasticsearch
        item=createItem(row, item)

        action = {
                "_index": "index_facebook",
                "_type": "insights",
                "_id": cont_id,
                "_source": item
                }
        ''' 
        if item['created_time'] ==  now - 7:
                id = item['id']
                #busqueda de una entrada igual
                res = es.search(index="index_facebook", doc_type="posts",body={
                        "query": {
                                "match_phrase": {
                                        "id": id
                                        }
                                }
                        })
                exist = ''
                for hit in res['hits']['hits']:
                        exist = hit["_source"]

                if exist = '':
                        actions.append(action)
        else:
        '''
        actions.append(action)

        cont_id += 1
    count += 1

if count > 0:
        helpers.bulk(es, actions)
        print "leftovers"
        print "indexed %d" %cont_id

