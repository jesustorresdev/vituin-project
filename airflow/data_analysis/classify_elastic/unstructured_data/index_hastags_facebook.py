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

#It return all hastags of one message and its number in the message
def hastags_of_message(res, id):

    words=[]
    number_hastag = []
    for hit in res['hits']['hits']:
        if element["_source"]["parent"] == id:
            words.append()
            number_hastag.append()

    result = {id: {"words":words, "number_hastag" : number_hastag}}

    return  result

F = open(filename)
reference = ["hastag",
             "parent",
             "social_network",
             "type_parent",
             "key",
             "creation_time",
             "extraction_time",
             "number_hastag",
             "number_of_this_hastags_in_message"
             ]

ES = Elasticsearch(
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
    res = ES.search(index='index_facebook_hastags', body=doc, size=0)
    #The next element indexed going to be the next id doesn't used
    cont_id = int(res['hits']['total'])

except:
    #If it's the first gruop of elements indexed
    print("First indexed")
    cont_id = 0
    EXIST_INDEX = False
    FIRST_ITERATION = True


FILE_COUNT = 0
ACTIONS = []

EXIST_INDEX = True
FIRST_ITERATION = False
ELASTICSEARCH_INDEX='index_tripadvisor_hoteles'
ELASTICSEARCH_DOC_TYPE='unstructured'
NAMES_ITEM_FINAL = []

messages_visited = {}

for row in csv.reader(F):

    if(FILE_COUNT!=0):
        item = {}

        for i in range(len(reference)):
            item[reference[i]] = row[i]

        #ID parent in facebook
        parent = item['parent']
        res = ES.search(index="index_facebook_hastags", body={
            "query": {
                "match_phrase": {
                    "id_parent": parent
                }
            }
        })


        #If it's the first hastag for this message in the document
        if not parent in messages_visited:
            messages_visited.update(hastags_of_message(res, parent))

        exist = False
        element = {}


        #ID parent in facebook
        key = item['key']
        res = ES.search(index="index_facebook_hastags", body={
            "query": {
                "match_phrase": {
                    "id_parent": key
                }
            }
        })

        #Exist hastag with this key
        for hit in res['hits']['hits']:
            exist = True
            element = hit

        #If not exists in de index this element
        if not exist:

            action = {
                "_index": "index_facebook_posts",
                "_type": "posts",
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

    #Delete all hastags in elastic that now it isn't exist
    for message in messages_visited:
        for i in range(0, len(message['word'])):
            es.delete_by_query(index='index_facebook_hastags',doc_type='unstructured', q={'parent': message, 'hastag':message['word'][i], 'number_hastag':message['number_hastag'][i]})





