import datetime
from facebook_reactions import getReactions
from facebook_comments import getComments
import requests
import hashlib


params = {'access_token': \
              'EAACEdEose0cBAGZCoXSQfuKRxaZAbOQNhNZBkMTXfcfm1hQnHuRcjZBQVXSyoKtqj0RJdVbI1Az74rrAnxBRleGHbWcMX1PioZCK4i1lvmHG97FG3AHaxUyd60vfO07b0dPSxDbdLxrY6yVZAnweBw9UpZCcy2PyQQhWp7aPDZA7S1qpy0QdTwAedyWfZBccmrf22Gn7ZC6AB2ZCAZDZD' \
          }

#Extract reactiones (numbers and people), shares, comments (id, numbers and people) of the posts
posts_elements_url='https://graph.facebook.com/v2.10/{post_id}?fields=\
shares, \
comments.summary(true), \
reactions.type(LIKE).summary(1).as(like), \
reactions.type(LOVE).summary(1).as(love), \
reactions.type(WOW).summary(1).as(wow), \
reactions.type(HAHA).summary(1).as(haha), \
reactions.type(SAD).summary(1).as(sad), \
reactions.type(ANGRY).summary(1).as(angry), \
reactions.type(THANKFUL).summary(1).as(thankful), \
reactions.type(PRIDE).summary(1).as(pride)'


def getPosts(data,comments, posts_comments, days):
    index_posts = posts_comments["index_posts"]
    samples_posts = posts_comments["samples_posts"]

    if comments:
        index_comments = posts_comments["index_comments"]
        samples_comments = posts_comments["samples_comments"]



    while True:
        try:
            for element in data['data']:

                now = datetime.datetime.today()
                creation_time = datetime.datetime.strptime(element['creation_time'], '%Y-%m-%dT%H:%M:%S+%f')
                extraction_time = now

                if (now - creation_time).days < days:
                    samples_posts.append(element['id'])

                    if 'message' in element: #Could not have message
                        samples_posts[index_posts].append(element['message'])
                    else:
                        samples_posts[index_posts].append('')

                    if 'story' in element: #Could not have story
                        samples_posts[index_posts].append(element['story'])
                    else:
                        samples_posts[index_posts].append('')

                    this_post_elements_url = posts_elements_url.replace("{post_id}",element['id'])
                    posts_elements = requests.get(this_post_elements_url, params = params).json()

                    #Number of comments
                    samples_posts[index_posts].append(posts_elements['comments']['summary']['total_count'])

                    #Shares
                    try:
                        samples_posts[index_posts].append(posts_elements['shares']['count'])
                    except:
                        samples_posts[index_posts].append(0)

                    #Reactions posts
                    for reaction in getReactions(posts_elements):
                        samples_posts[index_posts].append(reaction)

                    #Create key
                    str_key = ''
                    for element in samples_posts[index_posts]:
                        if element == int or element == float:
                            str_key += str(element)
                        else:
                            str_key += element

                    key = hashlib.md5(str_key.encode('utf-8')).hexdigest()
                    samples_posts[index_posts].append(key)
                    samples_posts[index_posts].append(creation_time)
                    samples_posts[index_posts].append(extraction_time)

                    index_posts=index_posts+1

                    if comments:

                        comment = getComments(posts_elements['comments']['data'], index_comments)

                        for com in comment["samples_comments"]:
                            samples_comments.append(com)

                        index_comments = comment["index_comments"]

                else:
                    break

            #Next page of posts
            data = requests.get(data['paging']['next']).json()

        except KeyError as e:
            print(e)
            break


    dict_posts = {
        "samples_posts" : samples_posts,
        "index_posts" : index_posts
    }


    dict_comments = {}
    if comments:
        dict_comments = {
            "samples_comments" : samples_comments,
            "index_comments" : index_comments
        }


    dict_returned = {
        "posts" : dict_posts,
        "comments" : dict_comments
    }

    return dict_returned