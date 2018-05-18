# -*- coding: utf-8 -*-
import requests
import json
from dateutil import parser
import datetime
import pytz
import hashlib
from hashtags import repeathashtagInMessage


import sys



def extract_tweets_from_user(result,user, auth, days):
    user = user
    n = 0
    exist_pages = True                        #if there are pages

    mentions = extract_mentions(user,auth)


    while exist_pages:
        n += 1
        url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name='+user+'&page='+str(n)

        res = requests.get(url, auth = auth)
        tweets = res.json()

        get_tweets_items(tweets, auth, result, mentions=mentions, days=days)

        print ''
        print ''
        print ''
        print '-----------------------'
        print 'pagina', n, ', indice actual ', result['index_tweets']

        #Include mentions not saved yet
        get_mentions_not_saved(mentions['statuses'], result, user, auth)

    return result

def extrac_tweets_from_words(result,words,auth):
    n = 0

    for word in words:
        n += 1
        mentions = extract_mentions(auth, words = word)         #Get all tweets in seven days with this word
        get_tweets_items(mentions, auth, result)                #Get items of these tweets and its replies and / or father tweets

    print '-----------------------'
    print result['index_tweets']


    return result

def extract_mentions(user, auth):

    tweets = get_mentions(auth, user=user)
    mentions = tweets['statuses']

    condition = True
    while condition:
        try:
            last_date = parser.parse(tweets['statuses'][99]['created_at'])
            print last_date
            if last_date:
                tweets = get_mentions(auth, user = user, until = last_date.strftime('%Y-%m-%d'))
                mentions.extend(tweets['statuses'])

        except:
            condition = False
            pass


    return mentions


def get_mentions(auth, **kwords):

    mentions = ''
    print 'entro'
    print kwords
    if not 'sinceID' in kwords and not 'until' in kwords:
        print 'TODO'
        mentions = 'https://api.Twitter.com/1.1/search/tweets.json?count=100'
    #if this definition is called in replies isn't important the rest of tuits.
    #if there is sinceID
    elif 'sinceID' in kwords:
        print 'SINCE'
        mentions = 'https://api.Twitter.com/1.1/search/tweets.json?count=100&sincdId='+str(kwords['sinceID'])
    #if there is date until
    elif 'until' in kwords:
        print 'until'
        mentions = 'https://api.Twitter.com/1.1/search/tweets.json?count=100&until='+str(kwords['until'])

    pms = {'q':'' }
    if 'user' in kwords:                     #Mention to use
        pms['q'] += 'to:'+kwords['user']
    if 'words' in kwords:                    #With specific word
        for word in kwords['words']:
            if pms['q']:
                pms['q'] += ' '
            else:
                pms['q'] += word

    res = requests.get(mentions, params=pms, auth=auth)

    tweets = res.json()

    return tweets

#Save mentions not saved
def get_mentions_not_saved(mentions,result, user_searched, auth):
    for mention in mentions:
        exist_tweet = False
        for tweet in result:
            if tweet[0] == mention['id']: #If ID are the same
                exist_tweet = True

        if not exist_tweet:
            id_first_tuit = get_first_tweet(mention['id'], auth)
            #Wee add the tuit because isn't saving yet
            set_items(mention,result['sample_tweets'], result['index_tweets'], id_first_tuit, user_searched)


#Recursive. Return the first tweet in a conversation
def get_first_tweet(reply_id, auth):

    url= 'https://api.twitter.com/1.1/statuses/show.json?id=' + str(reply_id)
    res = requests.get(url, auth=auth)
    tweet_father = res.json()
    reply = tweet_father['in_reply_to_status_id']

    if reply:
        get_first_tweet(tweet_father['id'], auth)
    else:
        return reply_id



def get_tweets_items(tweets, auth, result, **kwords):

    index = result['index_tweets']
    i = 0
    if 'statuses' in tweets:
        tws = tweets['statuses']
    else:
        tws = tweets

    for tweet in tws:

        exist_tuit = search_tweet(tweet['id'],result['sample_tweets'])  #Search if this tuits is saving in the list

        if not exist_tuit:
            created_at = datetime.datetime.strptime((tweet['created_at']), '%a %b %d %H:%M:%S +0000 %Y')
            now = datetime.datetime.today()

            #If days is smaller than the date now and the tweet date created break the loop
            if kwords['days'] < now - created_at:
                break

            i += 1

            get_hashtags_tweet(tweet, result['sample_hashtags'])


            user_first_tweet = tweet['user']['screen_name']
            id_first_reply = tweet['id']
            # print ('text---->',tweet['text'])
            set_items(tweet,result, index, id_first_reply, user_first_tweet)
            #print ('NORMAL in_reply_to_status_id--> ',tweet['in_reply_to_status_id'])

            reply = tweet['in_reply_to_status_id']

            # print result['sample_tweets'][index][0]
            index += 1

            if reply:
                while reply:
                    print ''
                    print 'REPLY de: ', result['sample_tweets'][index-1][0]
                    exist_tuit = search_tweet(reply,result['sample_tweets'])
                    print exist_tuit
                    if not exist_tuit:
                        i += 1
                        url_reply = 'https://api.twitter.com/1.1/statuses/show.json?id=' + str(reply)
                        res_reply = requests.get(url_reply, auth=auth)
                        tweet_reply = res_reply.json()
                        # print '****'
                        # print 'reply'
                        # # print ('text reply--> ', tweet_reply['text'])
                        # print ('text id--> ', tweet_reply['id'])
                        # print '****'
                        set_items(tweet_reply,result, index, id_first_reply, user_first_tweet)

                        reply = tweet_reply['in_reply_to_status_id']
                        print ('REPLY in_reply_to_status_id--> ',tweet_reply['in_reply_to_status_id'])
                        # print ''
                        print result['sample_tweets'][index][0]
                        index += 1

                    else:
                        # print 'REPLY REPETIDO'
                        # print (tweet['text'])
                        break

        # else:
            # print 'TUIT REPETIDO'
            # print ('REPETIDO--------->',tweet['text'])


    result['index_tweets'] = index

def set_items(tweet,result, index, id_first_reply, user_searched):
    items = [tweet['id'], tweet['text'], tweet['favorite_count'], tweet['retweet_count'], user_searched, tweet['in_reply_to_status_id'],id_first_reply]
    result['sample_tweets'].append(items)
    created_at = datetime.datetime.strptime((tweet['created_at']), '%a %b %d %H:%M:%S +0000 %Y')
    now = datetime.datetime.today()

    key = get_key(items)

    result['sample_tweets'][index].extend([key,tweet['entities']['hashtags'],created_at, now])

def get_key(items):
    str_key = ''
    for element in items:
        if isinstance(element, int) or isinstance(element,float):
            str_key += str(element)
        elif element is not None:
            str_key += element

    key = hashlib.md5(str_key.encode('utf-8')).hexdigest()
    return key

def search_tweet(id_searched, tweets):
    found = False
    if len(tweets) > 1:
        for i in range(1,len(tweets)-1):
            if tweets[i][0] == id_searched:
                found = True
                print 'exist tuit-->', id_searched
                break
        return found

def get_hashtags_tweet(tweet, result):
    hashtags = tweet['entities']['hashtags']
    words = []

    for hashtag in hashtags:
        words.append(hashtag['text'].lower())       #we transform to lower letters

    number_hashtag = {}                                  #If there is a hashtag duplicated in the message we put the number (by order of found)
    repeat_hashtags = repeathashtagInMessage(words)      #Search hashtags repeat in the message
    creation_time = datetime.datetime.strptime((tweet['created_at']), '%a %b %d %H:%M:%S +0000 %Y')
    extraction_time = datetime.datetime.today()
    id_parent = tweet['id']
    social_network = 'twitter'
    type_parent = 'tweet'


    #For to all hashtags words
    for i in range(0,len(words)-1):
        number_total_this_hashtag_in_message = 1           #If there are a hashtag duplicated in the message we put the number in total


        if words[i] in repeat_hashtags:                      #if this word is repeat we change the number of this hashtag in the message
            number_total_this_hashtag_in_message = len(repeat_hashtags[words[i]])

        if not words[i] in number_hashtag:                   #If it's the first time to this hashtag in the words, create the key in number_hashtag
            number_hashtag.update({words[i] : 0})
        else:
            number_hashtag[words[i]] += 1


        str_key = str(id_parent) + str(creation_time) + words[i] + number_hashtag[words[i]]
        key = hashlib.md5(str_key.encode('utf-8')).hexdigest()

        result.append([words[i][1:], id_parent, social_network, type_parent, key, creation_time, extraction_time, number_hashtag[words[i]], number_total_this_hashtag_in_message])





#             # mentionURL = 'https://api.Twitter.com/1.1/search/tweets.json?sincdId=991402008400875520'
#             # API_URL = 'https://data-api.twitter.com/insights/engagement/totals'
#             # pms = {'q':"to:serdiaz_"}
#             #res = requests.get(url, params=pms, auth=auth)
#             #res = requests.get(mentionURL, params=pms, auth=auth)
#             # params =   {
#             #     "tweet_ids": [
#             #         "991661438430339072"
#             #     ],
#             #     "engagement_types": [
#             #         "impressions",
#             #         "engagements",
#             #         "favorites"
#             #     ],
#             #     "groupings": {
#             #         "grouping name": {
#             #             "group_by": [
#             #                 "tweet.id",
#             #                 "engagement.type"
#             #             ]
#             #         }
#             #     }
#             # }
#             #
#             # req = requests.post(url=API_URL, data=json.dumps(params), auth=auth)
#             # tweet2 = res.json()
#             # print req.text
#
#             # print tweet2['statuses']
#             # for t2 in tweet2['statuses']:
#             #     if t2['in_reply_to_status_id'] == 991402008400875520 :
#             #         print t2
#             #         print '---------------'
#             #         print ''
#             #         print ''
#             #         print ''
#             #         print ''
#             #print tweet
#
#             break
#
#     there = False
#     print 'Numero de respuestas es', i
# # print tweets
# #print(tweets['statuses'][0]['text'])











