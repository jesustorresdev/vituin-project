# -*- coding: utf-8 -*-
import requests
import json
from dateutil import parser
import datetime
import pytz
import hashlib
from hashtags import repeathashtagInMessage
from selenium import webdriver
import os, time

import sys



def extract_tweets_from_user(result,user, auth, days):
    user = user
    n = 0
    exist_pages = True                        #if there are pages

    mentions = extract_mentions(user,auth)

    result['index_mentions'] = len(mentions)

    get_tweets_items(mentions, auth, result, 'mentions', days=days)


    n_tweet = 0
    while exist_pages:
        n += 1
        url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name='+user+'&page='+str(n)

        res = requests.get(url, auth = auth)
        tweets = res.json()

        get_tweets_items(tweets, auth, result, 'tweets', days=days)

        print ''
        print ''
        print ''
        print '-----------------------'
        print 'tweets-->', len(tweets)
        n_tweet += len(tweets)
        print 'pagina', n, ', indice actual ', result['index_tweets'], ', tweets acumulados', n_tweet
        if len(tweets) == 0:
            exist_pages = False
        #Include mentions not saved yet
        # get_mentions_not_saved(mentions, result, user, auth)

    return result

def extract_tweets_from_words(result,words,auth):
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
            print 'try'
            last_date = parser.parse(tweets['statuses'][99]['created_at'])
            print 'last_date-->',last_date
            if last_date:
                tweets = get_mentions(auth, user = user, until = last_date.strftime('%Y-%m-%d'))
                mentions.extend(tweets['statuses'])

        except:
            print 'ehhhhh'
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
        mentions = 'https://api.Twitter.com/1.1/search/tweets.json?count=100&+='+str(kwords['sinceID'])
    #if there is date until
    elif 'until' in kwords:
        print 'until'
        mentions = 'https://api.Twitter.com/1.1/search/tweets.json?count=100&until='+str(kwords['until'])

    print 'mentions-->', mentions
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
    print tweets['statuses'][0]

    return tweets

#Save mentions not saved
def get_mentions_not_saved(mentions,result, user_searched, auth):
    print 'get_mentions_not_saved'
    # print "len mentions-->", len(mentions)
    # print "result--->",result['sample_tweets']
    # import sys
    # sys.exit()
    for mention in mentions:
        exist_tweet = False
        for tweet in result['sample_tweets']:
            #If it's the first tweet
            if tweet[0] == 'id':
                # print 'NO'
                # print "tweet[0]--->",tweet[0]
                exist_tweet = True
            else:
                # print "tweet[0]--->",tweet[0]
                # print "mention[id]--->",mention['id']
                if tweet[0] == mention['id']: #If ID are the same
                    exist_tweet = True

        if not exist_tweet:
            print "mention a guardar--->",mention
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
        print 'Dentro function. Padre del reply-->',reply
        return get_first_tweet(reply, auth)
    else:
        print 'Se acabo-->',reply_id
        return reply_id



def get_tweets_items(tweets, auth, result, name_list, **kwords):

    index_name = 'index_'+name_list
    sample_name = 'sample_'+name_list

    index = result[index_name]
    if 'statuses' in tweets:
        tws = tweets['statuses']
    else:
        tws = tweets

    for tweet in tws:

        exist_tuit = search_tweet(tweet['id'],result[sample_name])  #Search if this tuits is saving in the list

        if not exist_tuit:
            created_at = datetime.datetime.strptime((tweet['created_at']), '%a %b %d %H:%M:%S +0000 %Y')
            now = datetime.datetime.today()

            #If days is smaller than the date now and the tweet date created break the loop
            # if kwords['days'] < (now - created_at).days:
            #     break


            # get_hashtags_tweet(tweet, result['sample_hashtags'])


            if 'text' in tweet:
                print ('text reply--> ', tweet['text'])
            else:
                print "No texto en el tuit"
                print tweet

            if tweet['in_reply_to_status_id']:
                id_tweet_parent = tweet['in_reply_to_status_id']
            else:
                id_tweet_parent = 0

            tweet_RT = is_RT(tweet['text'])

            if tweet_RT is True:
                print 'is a RT. ID-->', tweet['retweeted_status']['id']
                number_replies = get_number_replies(tweet['retweeted_status']['id'],auth = auth)
            else:
                number_replies = get_number_replies(tweet['id'],user_name=tweet['user']['screen_name'])

            print number_replies

            #If tweet has parent
            if id_tweet_parent:
                id_first_parent = get_first_tweet(id_tweet_parent, auth)
            else:
                id_first_parent = 0

                #Set Items
                items = set_items(tweet,result, index, id_first_parent, number_replies,tweet_RT)
                result[sample_name].append(items)

            #print ('NORMAL in_reply_to_status_id--> ',tweet['in_reply_to_status_id'])
            # mentions = get_mentions(auth)

            # import sys
            # sys.exit()
            father_id = tweet['in_reply_to_status_id']
            print 'reply-->', father_id
            # print result[sample_name][index][0]
            index += 1

            if father_id:
                while father_id:
                    print ''
                    print 'result[sample_name]',result[sample_name]
                    print '[index-1]',[index-1]
                    print 'REPLY de: ', father_id
                    exist_tuit = search_tweet(father_id,result[sample_name])
                    print exist_tuit
                    if not exist_tuit:
                        url_reply = 'https://api.twitter.com/1.1/statuses/show.json?id=' + str(father_id)
                        res_reply = requests.get(url_reply, auth=auth)
                        tweet_father = res_reply.json()
                        try:
                            print '****'
                            print 'father'
                            try:
                                print ('text father--> ', tweet_father['text'])
                            except:
                                print "No texto father"
                                print tweet_father
                            print ('text id--> ', tweet_father['id'])
                            print '****'
                            tweet_RT = False

                            number_replies = get_number_replies(tweet_father['id'],user_name=tweet_father['user']['screen_name'])

                            print number_replies
                            set_items(tweet_father,result, index, id_first_parent, number_replies,tweet_father)

                            father_id = tweet_father['in_reply_to_status_id']
                            print ('REPLY in_reply_to_status_id--> ',tweet_father['in_reply_to_status_id'])
                            # print ''
                            # print result[sample_name][index][0]
                            index += 1
                        except:
                            print 'error'
                            print tweet_father
                            break

                    else:
                        # print 'REPLY REPETIDO'
                        # print (tweet['text'])
                        break

        # else:
            # print 'TUIT REPETIDO'
            # print ('REPETIDO--------->',tweet['text'])


    result[index_name] = index

def set_items(tweet,result, index, id_first_parent, number_replies,tweet_RT):
    print ''
    print ''
    print ''
    print ''
    print ''
    print 'EY'
    print 'tweet[favorite_count]-->',tweet['favorite_count']
    print 'tweet[retweet_count]-->',tweet['retweet_count']
    print 'id_first_parent-->',id_first_parent
    print 'tweet[id]-->',tweet['id']
    print 'tweet[in_reply_to_status_id]-->',tweet['in_reply_to_status_id']
    print 'number_replies-->', number_replies
    print 'tweet_RT-->',tweet_RT
    print ''
    print ''
    if 'text' in tweet:
        print ('text reply--> ', tweet['text'])
    else:
      print "No texto a la hora de dotar items"
      tweet['text'] = ''

    #If is retuit
    if tweet_RT is True:
        favorite_count = tweet['retweeted_status']['favorite_count']
    else:
        favorite_count = tweet['favorite_count']

    if tweet['in_reply_to_status_id']:
        parent_id =tweet['in_reply_to_status_id']
        print 'Entre aquí, parent_id-->', parent_id
    else:
        parent_id = 0
    if number_replies is None:
        number_replies = 0

    print 'parent_id-->',parent_id
    print 'tweet[text]-->',tweet['text']
    print 'tweet[screen_name]-->',tweet['user']['screen_name']


    items = [tweet['id'], tweet['text'],  tweet['user']['screen_name'], int(number_replies), tweet['retweet_count'], favorite_count, parent_id,id_first_parent,tweet_RT]
    created_at = datetime.datetime.strptime((tweet['created_at']), '%a %b %d %H:%M:%S +0000 %Y')
    now = datetime.datetime.today()

    key = get_key(items)

    # result['sample_tweets'][index].extend([key,tweet['entities']['hashtags'],created_at, now])
    items.extend([created_at, now, key])

    # print 'len(items)', len(items)
    # print 'items', items[3]
    # print 'len(items)', len(items)
    
    return items
    # print tweet
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

        print''
        print'HASTAGS'
        print  'id_parent--->',str(id_parent)
        print  'creation time--->',str(creation_time)
        print  'words[i]--->',words[i]
        print  'words--->',words
        print  'number hastags[i]--->',number_hashtag[words[i]]
        # print  'tweet--->',tweet
        str_key = str(id_parent) + str(creation_time) + words[i] + str(number_hashtag[words[i]])
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







def is_RT(tweet):
    if tweet[0:2] == 'RT':
        return True
    else:
        return False

def get_number_replies(tweet_id,**kwords):
    url ='https://twitter.com/lshyb_/status/'+str(tweet_id)
    url= 'https://api.twitter.com/1.1/statuses/show.json?id=' + str(tweet_id)

    #If the tweet is a RT
    if 'auth' in kwords:
        res = requests.get(url, auth=kwords['auth'])
        tweet = res.json()
        tweet_id = tweet['id']
        user_name = tweet['user']['screen_name']
    else:
        user_name = kwords['user_name']

    url_tweet ='https://twitter.com/'+user_name+'/status/'+str(tweet_id)
    print url_tweet

    driver = webdriver.Chrome()
    driver.get(url_tweet)

    no_load = True
    contador = 0
    number_replies = 0
    # It could be that no load at first
    while no_load is not False and contador <= 5:
        # print 'ENTRO'
        no_load = False

        # If isn't problems
        try:
            tweet = driver.find_element_by_xpath("//div[@data-tweet-id='"+str(tweet_id)+"']")
            number_replies = tweet.find_element_by_xpath(".//span[@class='ProfileTweet-actionCountForPresentation']").text
            print 'number_replies-->',number_replies
            try:
                number_replies = int(number_replies)
            except:
                number_replies = 0
            print 'tipo number_replies-->',type(number_replies)
            contador = 0
        except Exception as error:
            print 'No Load'
            print error
            time.sleep(1)
            contador += 1
            print "contador sube", contador
            if contador >= 5:
                no_load = False
                print "PROBLEMS"

                driver.close()
                # chromedriver dont stop itself
                os.system("pkill -f chromedriver")
                return None
            else:
                # print 'pass'
                no_load = True
                pass

    driver.close()
    # chromedriver dont stop itself
    os.system("pkill -f chromedriver")
    return number_replies








def get_user_info(user,**kwords):
    url ='https://twitter.com/'+str(user)


    driver = webdriver.Chrome()
    driver.get(url)

    result = {
    'followers' : 0,
    'friends' : 0,
    'tweets' : 0,
    'likes' : 0
    }
    no_load = True
    contador = 0
    number_replies = 0
    # It could be that no load at first
    while no_load is not False and contador <= 5:
        # print 'ENTRO'
        no_load = False

        # If isn't problems
        try:
            counts = driver.find_elements_by_xpath("//span[@class='ProfileNav-value']")
            result['tweets'] = counts[0].get_attribute('data-count')
            result['friends'] = counts[1].get_attribute('data-count')
            result['followers'] = counts[2].get_attribute('data-count')
            result['likes'] = counts[3].get_attribute('data-count')
            print 'result-->',result
            driver.close()
            # chromedriver dont stop itself
            os.system("pkill -f chromedriver")
            return result
        except Exception as error:
            print 'No Load'
            print error
            time.sleep(1)
            contador += 1
            print "contador sube", contador
            if contador >= 5:
                no_load = False
                print "PROBLEMS"

                driver.close()
                # chromedriver dont stop itself
                os.system("pkill -f chromedriver")
                return None
            else:
                return False






#Reply (el cuarto)
a = {u'contributors': None, u'truncated': False,
     u'text': u'Ya, bueno, me ha salido una cr\xedtica sobre un pa\xeds del quinto co\xf1o. Pero es que mi cerebro ya lo hace por costumbre.',
     u'is_quote_status': False, u'in_reply_to_status_id': 1042913468020600834, u'id': 1042914468651565056, u'favorite_count': 1,
     u'source': u'<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>', u'retweeted': False,
     u'coordinates': None, u'entities': {u'symbols': [], u'user_mentions': [], u'hashtags': [], u'urls': []},
     u'in_reply_to_screen_name': u'SerDiaz_', u'in_reply_to_user_id': 448386715, u'retweet_count': 0,
     u'id_str': u'1042914468651565056', u'favorited': False,
     u'user': {
                    u'follow_request_sent': False, u'has_extended_profile': True, u'profile_use_background_image': True,
                    u'default_profile_image': False, u'id': 448386715,
                    u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme19/bg.gif',
                   u'verified': False, u'translator_type': u'none', u'profile_text_color': u'333333',
                   u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/1039575523876327426/G7ROeO6c_normal.jpg',
                   u'profile_sidebar_fill_color': u'F6FFD1', u'entities': {u'description': {u'urls': []}},
                   u'followers_count': 1224, u'profile_sidebar_border_color': u'FFFFFF', u'id_str': u'448386715',
                   u'profile_background_color': u'ACDED6', u'listed_count': 23, u'is_translation_enabled': False,
                   u'utc_offset': None, u'statuses_count': 41577,
                   u'description': u'Ingeniero inform\xe1tico. Un d\xeda,mientras cagaba aburrido,cre\xe9 el universo de un chasquido. Luego me hice Twitter para contarlo.',
                   u'friends_count': 771,
                   u'location': u'Por ah\xed.',
                   u'profile_link_color': u'5C7FFF',
                   u'profile_image_url': u'http://pbs.twimg.com/profile_images/1039575523876327426/G7ROeO6c_normal.jpg',
                   u'following': False,
                   u'geo_enabled': False,
                   u'profile_banner_url': u'https://pbs.twimg.com/profile_banners/448386715/1536705159',
                   u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme19/bg.gif',
                   u'screen_name': u'SerDiaz_', u'lang': u'es', u'profile_background_tile': True, u'favourites_count': 18877, u'name': u'Sergio D\xedaz',
                   u'notifications': False, u'url': None, u'created_at': u'Tue Dec 27 23:20:49 +0000 2011', u'contributors_enabled': False,
                   u'time_zone': None, u'protected': False, u'default_profile': False, u'is_translator': False
     },
     u'geo': None,
     u'in_reply_to_user_id_str': u'448386715', u'lang': u'es', u'created_at': u'Thu Sep 20 23:12:40 +0000 2018',
     u'in_reply_to_status_id_str': u'1042913468020600834', u'place': None}

# user_first_tweet = tweet['in_reply_to_screen_name']
# id_reply = tweet['in_reply_to_status_id']

#First
b ={u'contributors': None, u'truncated': False, u'text': u's',
    u'is_quote_status': False, u'in_reply_to_status_id': None, u'id': 1043092220608479232, u'favorite_count': 0,
    u'source': u'<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>', u'retweeted': False, u'coordinates': None,
    u'entities': {u'symbols': [], u'user_mentions': [], u'hashtags': [], u'urls': []},
    u'in_reply_to_screen_name': None, u'in_reply_to_user_id': None, u'retweet_count': 0,
    u'id_str': u'1043092220608479232', u'favorited': False,
    u'user': {u'follow_request_sent': False, u'has_extended_profile': True, u'profile_use_background_image': True,
              u'default_profile_image': False, u'id': 448386715,
              u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme19/bg.gif',
              u'verified': False, u'translator_type': u'none', u'profile_text_color': u'333333',
              u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/1039575523876327426/G7ROeO6c_normal.jpg',
              u'profile_sidebar_fill_color': u'F6FFD1', u'entities': {u'description': {u'urls': []}}, u'followers_count': 1223,
              u'profile_sidebar_border_color': u'FFFFFF', u'id_str': u'448386715',
              u'profile_background_color': u'ACDED6', u'listed_count': 23, u'is_translation_enabled': False,
              u'utc_offset': None, u'statuses_count': 41578,
              u'description': u'Ingeniero inform\xe1tico. Un d\xeda,mientras cagaba aburrido,cre\xe9 el universo de un chasquido. Luego me hice Twitter para contarlo.',
              u'friends_count': 771, u'location': u'Por ah\xed.', u'profile_link_color': u'5C7FFF',
              u'profile_image_url': u'http://pbs.twimg.com/profile_images/1039575523876327426/G7ROeO6c_normal.jpg',
              u'following': False, u'geo_enabled': False, u'profile_banner_url': u'https://pbs.twimg.com/profile_banners/448386715/1536705159',
              u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme19/bg.gif', u'screen_name': u'SerDiaz_',
              u'lang': u'es', u'profile_background_tile': True, u'favourites_count': 18877, u'name': u'Sergio D\xedaz',
              u'notifications': False, u'url': None, u'created_at': u'Tue Dec 27 23:20:49 +0000 2011',
              u'contributors_enabled': False, u'time_zone': None, u'protected': False, u'default_profile': False,
              u'is_translator': False},
    u'geo': None, u'in_reply_to_user_id_str': None, u'lang': u'und',
    u'created_at': u'Fri Sep 21 10:58:59 +0000 2018', u'in_reply_to_status_id_str': None, u'place': None}


{u'contributors': None, u'truncated': False,
 u'text': u"RT @lshyb_: Don't you dare disrespect the snowman from la rotonda de la avenida de los majuelos ever again https://t.co/RTDTL9nt45",
 u'is_quote_status': True, u'in_reply_to_status_id': None, u'id': 1043099562334937088,
 u'favorite_count': 0, u'source': u'<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>',
 u'quoted_status_id': 1043084448596717568, u'retweeted': True, u'coordinates': None,
 u'entities': {u'symbols': [],
               u'user_mentions':
                    [{u'id': 254773569, u'indices': [3, 10], u'id_str': u'254773569', u'screen_name': u'lshyb_', u'name': u'Violet Hill'}],
               u'hashtags': [],
               u'urls': [{u'url': u'https://t.co/RTDTL9nt45', u'indices': [107, 130], u'expanded_url': u'https://twitter.com/grande_tete/status/1043084448596717568', u'display_url': u'twitter.com/grande_tete/st\u2026'}]},
u'in_reply_to_screen_name': None, u'in_reply_to_user_id': None, u'retweet_count': 1, u'id_str': u'1043099562334937088', u'favorited': True,
 u'retweeted_status':
     {u'contributors': None, u'truncated': False,
      u'text': u"Don't you dare disrespect the snowman from la rotonda de la avenida de los majuelos ever again https://t.co/RTDTL9nt45",
      u'is_quote_status': True, u'in_reply_to_status_id': None,
      u'id': 1043098170849456129, u'favorite_count': 3,
      u'source': u'<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>',
      u'quoted_status_id': 1043084448596717568, u'retweeted': True, u'coordinates': None,
      u'quoted_status': {u'contributors': None, u'truncated': False,
                         u'text': u'De 0 a la estatua del mu\xf1eco de nieve \xbfc\xf3mo de feo te has levantado hoy? https://t.co/Ib4okk1dg8',
                         u'is_quote_status': False, u'in_reply_to_status_id': None,
                         u'id': 1043084448596717568, u'favorite_count': 26,
                         u'source': u'<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>',
                         u'retweeted': False, u'coordinates': None,
                         u'entities':
                             {u'symbols': [], u'user_mentions': [], u'hashtags': [], u'urls': [],
                              u'media': [{u'expanded_url': u'https://twitter.com/grande_tete/status/1043084448596717568/photo/1',
                                          u'display_url': u'pic.twitter.com/Ib4okk1dg8', u'url': u'https://t.co/Ib4okk1dg8',
                                          u'media_url_https': u'https://pbs.twimg.com/media/DnnHxe3X4AICJoB.jpg',
                                          u'id_str': u'1043084441625812994',
                                          u'sizes': {u'large': {u'h': 480, u'resize': u'fit', u'w': 640},
                                                     u'small': {u'h': 480, u'resize': u'fit', u'w': 640},
                                                     u'medium': {u'h': 480, u'resize': u'fit', u'w': 640},
                                                     u'thumb': {u'h': 150, u'resize': u'crop', u'w': 150}},
                                          u'indices': [73, 96], u'type': u'photo', u'id': 1043084441625812994,
                                          u'media_url': u'http://pbs.twimg.com/media/DnnHxe3X4AICJoB.jpg'}]},
                         u'in_reply_to_screen_name': None, u'in_reply_to_user_id': None, u'retweet_count': 8,
                         u'id_str': u'1043084448596717568', u'favorited': False,
                         u'user': {u'follow_request_sent': False, u'has_extended_profile': True,
                                   u'profile_use_background_image': True, u'default_profile_image': False,
                                   u'id': 2862909465,
                                   u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme1/bg.png',
                                   u'verified': False, u'translator_type': u'none',
                                   u'profile_text_color': u'333333',
                                   u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/995624809215283200/jUn3EtU__normal.jpg',
                                   u'profile_sidebar_fill_color': u'DDEEF6',
                                   u'entities':
                                       {u'url':
                                            {u'urls':
                                                 [{u'url': u'https://t.co/oF8DNMYScJ',
                                                   u'indices': [0, 23],
                                                   u'expanded_url': u'https://www.facebook.com/Don-Tinerfe\xf1ismo-756731657786775',
                                                   u'display_url': u'facebook.com/Don-Tinerfe\xf1is\u2026'}]},
                                        u'description': {u'urls': []}},
                                   u'followers_count': 1856,
                                   u'profile_sidebar_border_color': u'C0DEED',
                                   u'id_str': u'2862909465',
                                   u'profile_background_color': u'C0DEED',
                                   u'listed_count': 12,
                                   u'is_translation_enabled': False, u'utc_offset': None,
                                   u'statuses_count': 3840,
                                   u'description': u'Apoyo \xedntegro al Club Deportivo Tenerife.\n\nMemes, montajes cutres, zoom a la cara, and otras mierdas, siempre con el esp\xedritu keep it cutre.', u'friends_count': 250,
                                   u'location': u'Heliodoro Rodr\xedguez L\xf3pez', u'profile_link_color': u'1DA1F2', u'profile_image_url': u'http://pbs.twimg.com/profile_images/995624809215283200/jUn3EtU__normal.jpg',
                                   u'following': True, u'geo_enabled': False,
                                   u'profile_banner_url': u'https://pbs.twimg.com/profile_banners/2862909465/1512470086',
                                   u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme1/bg.png', u'screen_name': u'grande_tete',
                                   u'lang': u'es', u'profile_background_tile': False, u'favourites_count': 5161, u'name': u'Don Tinerfe\xf1ismo.',
                                   u'notifications': False, u'url': u'https://t.co/oF8DNMYScJ', u'created_at': u'Wed Nov 05 18:08:18 +0000 2014',
                                   u'contributors_enabled': False, u'time_zone': None, u'protected': False, u'default_profile': True, u'is_translator': False},
                         u'geo': None, u'in_reply_to_user_id_str': None, u'possibly_sensitive': False, u'lang': u'es', u'created_at': u'Fri Sep 21 10:28:06 +0000 2018', u'in_reply_to_status_id_str': None, u'place': None,
                         u'extended_entities':
                             {u'media':
                                  [{u'expanded_url': u'https://twitter.com/grande_tete/status/1043084448596717568/photo/1', u'display_url': u'pic.twitter.com/Ib4okk1dg8', u'url': u'https://t.co/Ib4okk1dg8',
                                    u'media_url_https': u'https://pbs.twimg.com/media/DnnHxe3X4AICJoB.jpg', u'id_str': u'1043084441625812994', u'sizes':
                                        {u'large': {u'h': 480, u'resize': u'fit', u'w': 640},
                                         u'small': {u'h': 480, u'resize': u'fit', u'w': 640},
                                    u'medium': {u'h': 480, u'resize': u'fit', u'w': 640}, u'thumb': {u'h': 150, u'resize': u'crop', u'w': 150}}, u'indices': [73, 96], u'type': u'photo', u'id': 1043084441625812994, u'media_url': u'http://pbs.twimg.com/media/DnnHxe3X4AICJoB.jpg'}]}}, u'entities': {u'symbols': [], u'user_mentions': [], u'hashtags': [], u'urls': [{u'url': u'https://t.co/RTDTL9nt45', u'indices': [95, 118], u'expanded_url': u'https://twitter.com/grande_tete/status/1043084448596717568', u'display_url': u'twitter.com/grande_tete/st\u2026'}]}, u'in_reply_to_screen_name': None, u'in_reply_to_user_id': None, u'retweet_count': 1, u'id_str': u'1043098170849456129', u'favorited': True,
                                    u'user': {u'follow_request_sent': False, u'has_extended_profile': True, u'profile_use_background_image': False, u'default_profile_image': False, u'id': 254773569, u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme18/bg.gif', u'verified': False, u'translator_type': u'regular', u'profile_text_color': u'E3DDDA', u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/1041830856577507330/s-XhIKdo_normal.jpg', u'profile_sidebar_fill_color': u'FFFFFF', u'entities': {u'description': {u'urls': []}}, u'followers_count': 2367, u'profile_sidebar_border_color': u'FFFFFF', u'id_str': u'254773569', u'profile_background_color': u'FFFFFF', u'listed_count': 38, u'is_translation_enabled': False, u'utc_offset': None, u'statuses_count': 129081, u'description': u'La vida es corta pero el arte es eterno', u'friends_count': 972, u'location': u'Tenerife ', u'profile_link_color': u'ABB8C2', u'profile_image_url': u'http://pbs.twimg.com/profile_images/1041830856577507330/s-XhIKdo_normal.jpg', u'following': True, u'geo_enabled': True, u'profile_banner_url': u'https://pbs.twimg.com/profile_banners/254773569/1537227119',
                                    u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme18/bg.gif', u'screen_name': u'lshyb_', u'lang': u'en', u'profile_background_tile': True, u'favourites_count': 120775, u'name': u'Violet Hill', u'notifications': False, u'url': None, u'created_at': u'Sun Feb 20 00:10:21 +0000 2011', u'contributors_enabled': False, u'time_zone': None, u'protected': False, u'default_profile': False, u'is_translator': False}, u'geo': None, u'in_reply_to_user_id_str': None, u'possibly_sensitive': False, u'lang': u'en', u'created_at': u'Fri Sep 21 11:22:38 +0000 2018', u'quoted_status_id_str': u'1043084448596717568', u'in_reply_to_status_id_str': None, u'place': None}, u'user': {u'follow_request_sent': False, u'has_extended_profile': True, u'profile_use_background_image': True, u'default_profile_image': False, u'id': 448386715, u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme19/bg.gif', u'verified': False, u'translator_type': u'none', u'profile_text_color': u'333333', u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/1039575523876327426/G7ROeO6c_normal.jpg', u'profile_sidebar_fill_color': u'F6FFD1', u'entities': {u'description': {u'urls': []}}, u'followers_count': 1223, u'profile_sidebar_border_color': u'FFFFFF', u'id_str': u'448386715', u'profile_background_color': u'ACDED6', u'listed_count': 23, u'is_translation_enabled': False, u'utc_offset': None, u'statuses_count': 41579, u'description': u'Ingeniero inform\xe1tico. Un d\xeda,mientras cagaba aburrido,cre\xe9 el universo de un chasquido. Luego me hice Twitter para contarlo.', u'friends_count': 770, u'location': u'Por ah\xed.', u'profile_link_color': u'5C7FFF', u'profile_image_url': u'http://pbs.twimg.com/profile_images/1039575523876327426/G7ROeO6c_normal.jpg', u'following': False, u'geo_enabled': False, u'profile_banner_url': u'https://pbs.twimg.com/profile_banners/448386715/1536705159', u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme19/bg.gif', u'screen_name': u'SerDiaz_', u'lang': u'es', u'profile_background_tile': True, u'favourites_count': 18881, u'name': u'Sergio D\xedaz', u'notifications': False, u'url': None, u'created_at': u'Tue Dec 27 23:20:49 +0000 2011', u'contributors_enabled': False, u'time_zone': None, u'protected': False, u'default_profile': False, u'is_translator': False}, u'geo': None, u'in_reply_to_user_id_str': None, u'possibly_sensitive': False, u'lang': u'en', u'created_at': u'Fri Sep 21 11:28:10 +0000 2018', u'quoted_status_id_str': u'1043084448596717568', u'in_reply_to_status_id_str': None, u'place': None}


{u'contributors': None, u'truncated': False, u'text': u'RT @tinguarorest: Hoy se celebra el #DiaMundialDeLaPaella para todos los amantes del #arroz #PaellaLovers pueden disfrutarla en nuestro res\u2026', u'is_quote_status': False, u'in_reply_to_status_id': None, u'id': 1042806635536756737, u'favorite_count': 0, u'source': u'<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>', u'retweeted': False, u'coordinates': None, u'entities': {u'symbols': [], u'user_mentions': [{u'id': 158065716, u'indices': [3, 16], u'id_str': u'158065716', u'screen_name': u'tinguarorest', u'name': u'Restaurante Tinguaro'}], u'hashtags': [{u'indices': [36, 57], u'text': u'DiaMundialDeLaPaella'}, {u'indices': [85, 91], u'text': u'arroz'}, {u'indices': [92, 105], u'text': u'PaellaLovers'}], u'urls': []}, u'in_reply_to_screen_name': None, u'in_reply_to_user_id': None, u'retweet_count': 7, u'id_str': u'1042806635536756737', u'favorited': False, u'retweeted_status': {u'contributors': None, u'truncated': True, u'text': u'Hoy se celebra el #DiaMundialDeLaPaella para todos los amantes del #arroz #PaellaLovers pueden disfrutarla en nuest\u2026 https://t.co/yFe38c3nex', u'is_quote_status': False, u'in_reply_to_status_id': None, u'id': 1042771900227878912, u'favorite_count': 10, u'source': u'<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>', u'retweeted': False, u'coordinates': None, u'entities': {u'symbols': [], u'user_mentions': [], u'hashtags': [{u'indices': [18, 39], u'text': u'DiaMundialDeLaPaella'}, {u'indices': [67, 73], u'text': u'arroz'}, {u'indices': [74, 87], u'text': u'PaellaLovers'}], u'urls': [{u'url': u'https://t.co/yFe38c3nex', u'indices': [117, 140], u'expanded_url': u'https://twitter.com/i/web/status/1042771900227878912', u'display_url': u'twitter.com/i/web/status/1\u2026'}]}, u'in_reply_to_screen_name': None, u'in_reply_to_user_id': None, u'retweet_count': 7, u'id_str': u'1042771900227878912', u'favorited': False, u'user': {u'follow_request_sent': False, u'has_extended_profile': False, u'profile_use_background_image': False, u'default_profile_image': False, u'id': 158065716, u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme1/bg.png', u'verified': False, u'translator_type': u'none', u'profile_text_color': u'333333', u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/869530101729382400/j-OvHMMl_normal.jpg', u'profile_sidebar_fill_color': u'FFFFFF', u'entities': {u'url': {u'urls': [{u'url': u'https://t.co/u4MEPewxnv', u'indices': [0, 23], u'expanded_url': u'http://restaurantetinguaro.es', u'display_url': u'restaurantetinguaro.es'}]}, u'description': {u'urls': []}}, u'followers_count': 192, u'profile_sidebar_border_color': u'D9E075', u'id_str': u'158065716', u'profile_background_color': u'E3E5E6', u'listed_count': 1, u'is_translation_enabled': False, u'utc_offset': None, u'statuses_count': 1970, u'description': u'Abiertos de 11:00 a 23:00 Parking privado Comida Internacional Parque Taoro 28 Puerto de la Cruz', u'friends_count': 72, u'location': u'Puerto de la Cruz', u'profile_link_color': u'D9E079', u'profile_image_url': u'http://pbs.twimg.com/profile_images/869530101729382400/j-OvHMMl_normal.jpg', u'following': False, u'geo_enabled': True, u'profile_banner_url': u'https://pbs.twimg.com/profile_banners/158065716/1496147108', u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme1/bg.png', u'screen_name': u'tinguarorest', u'lang': u'es', u'profile_background_tile': False, u'favourites_count': 2340, u'name': u'Restaurante Tinguaro', u'notifications': False, u'url': u'https://t.co/u4MEPewxnv', u'created_at': u'Mon Jun 21 17:48:49 +0000 2010', u'contributors_enabled': False, u'time_zone': None, u'protected': False, u'default_profile': False, u'is_translator': False}, u'geo': None, u'in_reply_to_user_id_str': None, u'possibly_sensitive': False, u'lang': u'es', u'created_at': u'Thu Sep 20 13:46:09 +0000 2018', u'in_reply_to_status_id_str': None, u'place': {u'full_name': u'Puerto de la Cruz, Espa\xf1a', u'url': u'https://api.twitter.com/1.1/geo/id/88b5a72f641ba0e7.json', u'country': u'Espa\xf1a', u'place_type': u'city', u'bounding_box': {u'type': u'Polygon', u'coordinates': [[[-16.5694252, 28.3909623], [-16.5184146, 28.3909623], [-16.5184146, 28.4211478], [-16.5694252, 28.4211478]]]}, u'contained_within': [], u'country_code': u'ES', u'attributes': {}, u'id': u'88b5a72f641ba0e7', u'name': u'Puerto de la Cruz'}}, u'user': {u'follow_request_sent': False, u'has_extended_profile': False, u'profile_use_background_image': True, u'default_profile_image': False, u'id': 1261875690, u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme1/bg.png', u'verified': False, u'translator_type': u'none', u'profile_text_color': u'333333', u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/870197560841048065/8RLDTYpf_normal.jpg', u'profile_sidebar_fill_color': u'DDEEF6', u'entities': {u'url': {u'urls': [{u'url': u'https://t.co/vHwgewZJfO', u'indices': [0, 23], u'expanded_url': u'http://www.visitpuertodelacruz.es/', u'display_url': u'visitpuertodelacruz.es'}]}, u'description': {u'urls': []}}, u'followers_count': 1865, u'profile_sidebar_border_color': u'FFFFFF', u'id_str': u'1261875690', u'profile_background_color': u'C0DEED', u'listed_count': 75, u'is_translation_enabled': False, u'utc_offset': None, u'statuses_count': 7255, u'description': u'Como viajar por #PuertodelaCruz. Qu\xe9 ver, a donde ir... Experiencias urbanas y rurales alrededor de #Tenerife. Turismo activo o de relax', u'friends_count': 174, u'location': u'Puerto de la Cruz', u'profile_link_color': u'91D2FA', u'profile_image_url': u'http://pbs.twimg.com/profile_images/870197560841048065/8RLDTYpf_normal.jpg', u'following': False, u'geo_enabled': True, u'profile_banner_url': u'https://pbs.twimg.com/profile_banners/1261875690/1537194092', u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme1/bg.png', u'screen_name': u'VisitPtoCruz', u'lang': u'es', u'profile_background_tile': False, u'favourites_count': 5858, u'name': u'VisitPuertodelaCruz', u'notifications': False, u'url': u'https://t.co/vHwgewZJfO', u'created_at': u'Tue Mar 12 12:43:01 +0000 2013', u'contributors_enabled': False, u'time_zone': None, u'protected': False, u'default_profile': False, u'is_translator': False}, u'geo': None, u'in_reply_to_user_id_str': None, u'lang': u'es', u'created_at': u'Thu Sep 20 16:04:10 +0000 2018', u'in_reply_to_status_id_str': None, u'place': None}
