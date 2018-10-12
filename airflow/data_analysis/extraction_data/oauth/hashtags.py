from elasticsearch import Elasticsearch
from elasticsearch import helpers
import datetime
import hashlib


def hashtag(message, id_parent, social_network, type_parent, creation_time):
    samples_hashtags=[]
    words = []
    message = message.lower()                          #we transform to lower letters

    #Get all hashtags words
    for word in message.split(' '):
        if word[:1] == "#":
            words.append(word[1:])

    number_hashtag = {}                                  #If there is a hashtag duplicated in the message we put the number (by order of found)
    repeat_hashtags = repeathashtagInMessage(words)      #Search hashtags repeat in the message

    #For to all hashtags words
    for i in range(0,len(words)-1):
        extraction_time = datetime.datetime.today()
        number_total_this_hashtag_in_message = 1           #If there are a hashtag duplicated in the message we put the number in total


        if words[i] in repeat_hashtags:                      #if this word is repeat we change the number of this hashtag in the message
            number_total_this_hashtag_in_message = len(repeat_hashtags[word])

        if not words[i] in number_hashtag:                   #If it's the first time to this hashtag in the words, create the key in number_hashtag
            number_hashtag.update({words[i] : 0})
        else:
            number_hashtag[words[i]] += 1


        str_key = str(id_parent) + str(creation_time) + words[i] + number_hashtag[word]
        key = hashlib.md5(str_key.encode('utf-8')).hexdigest()

        samples_hashtags.append([words[i][1:], id_parent, social_network, type_parent, key, creation_time, extraction_time, number_hashtag[words[i]], number_total_this_hashtag_in_message])

    return samples_hashtags

def repeathashtagInMessage(words):
    repeat_hashtags = {}
    for i in range(0,len(words)):
        for j in range(i+1,len(words)):
            if words[i] == words[j]:
                if words[i] in repeat_hashtags:
                    repeat_hashtags[words[i]].append(j)
                    print words[i]                                      #second or more than this world have been matched
                    break                                               #break this iteration

                else:
                    repeat_hashtags.update({words[i]:[]})
                    repeat_hashtags[words[i]]= [i,j]
                    print words[i]                                      #first than this world have been matched
                    break                                               #break this iteration

    return repeat_hashtags
#
# def deletehashtags(id_parent, name_index):
#     es = Elasticsearch(
#         [
#             'elasticsearch:9200/'
#         ]
#     )
#
#     res = es.search(index=name_index, body={
#         "query": {
#             "match_phrase": {
#                 "id": id
#             }
#         }
#     })
#
#     for hit in res['hits']['hits']:
#         hit["_source"]["id"]