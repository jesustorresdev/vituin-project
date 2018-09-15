from facebook_reactions import getReactions
import requests
import datetime
import hashlib

params = {'access_token': \
              'EAACEdEose0cBAGZCoXSQfuKRxaZAbOQNhNZBkMTXfcfm1hQnHuRcjZBQVXSyoKtqj0RJdVbI1Az74rrAnxBRleGHbWcMX1PioZCK4i1lvmHG97FG3AHaxUyd60vfO07b0dPSxDbdLxrY6yVZAnweBw9UpZCcy2PyQQhWp7aPDZA7S1qpy0QdTwAedyWfZBccmrf22Gn7ZC6AB2ZCAZDZD' \
          }

page_url = 'https://graph.facebook.com/v2.10/VisitPuertodelaCruz/feed'

#Extract reactions of one comment
comments_reactions_url='https://graph.facebook.com/v2.10/{comment_id}?fields=\
reactions.type(LIKE).summary(1).as(like), \
reactions.type(LOVE).summary(1).as(love), \
reactions.type(WOW).summary(1).as(wow), \
reactions.type(HAHA).summary(1).as(haha), \
reactions.type(SAD).summary(1).as(sad), \
reactions.type(ANGRY).summary(1).as(angry), \
reactions.type(THANKFUL).summary(1).as(thankful), \
reactions.type(PRIDE).summary(1).as(pride)'


#Extract comments of one comment
counts_coments_of_comments_url = 'https://graph.facebook.com/v2.10/{comment_id}?fields=comment_count'
comments_of_comments_url = 'https://graph.facebook.com/v2.10/{comment_id}/comments'

samples_comments = []

def getComments(post, index_comments):
   for comment in post:

        sample_comment = []

        while True:
            try:
                sample_comment.append([comment['id'], comment['message']])

                #Reactions of comments
                this_comment_reactions_url = comments_reactions_url.replace("{comment_id}",comment['id'])
                comment_reactions = requests.get(this_comment_reactions_url, params = params).json()

                for reaction in getReactions(comment_reactions):
                    samples_comments[index_comments].append(reaction)

                #Create key
                str_key = ''
                for element in samples_comments[index_comments]:
                    if element == int or element == float:
                        str_key += str(element)
                    else:
                        str_key += element

                key = hashlib.md5(str_key.encode('utf-8')).hexdigest()
                samples_comments[index_comments].append(key)

                samples_comments[index_comments].append(comment['creation_time'])
                extraction_time = datetime.datetime.today()
                samples_comments[index_comments].append(extraction_time)

                #We add that it doesnt exist parent comment
                #In this point all comments are parent comment. Ever
                samples_comments[index_comments].append(0)

                index_comment=index_comments+1

                #Comments of comments (in this case we have comprobate if the comment has childrens comments)
                this_count_comments_of_comments_url = counts_coments_of_comments_url.replace("{comment_id}",comment['id'])
                count_comments_of_comments = requests.get(this_count_comments_of_comments_url, params = params).json()


                #If this comment have childrens comments
                if count_comments_of_comments['comment_count'] > 0:

                    this_comments_of_comments_url = comments_of_comments_url.replace("{comment_id}",comment['id'])
                    comments_of_comments = requests.get(this_comments_of_comments_url, params = params).json()

                    parent_id=comment['id'] #It saves the ID that the parent comment


                    for comment in comments_of_comments['data']:
                        samples_comments.append([comment['id'],comment['message']])

                        #Reactions of the comments of comments
                        this_comment_reactions_url = comments_reactions_url.replace("{comment_id}",comment['id'])
                        comment_reactions = requests.get(this_comment_reactions_url, params = params).json()

                        for reaction in getReactions(comment_reactions):
                            samples_comments[index_comment].append(reaction)

                        #Create key
                        str_key = ''
                        for element in samples_comments[index_comments]:
                            if element == int or element == float:
                                str_key += str(element)
                            else:
                                str_key += element

                        key = hashlib.md5(str_key.encode('utf-8')).hexdigest()
                        samples_comments[index_comments].append(key)

                        samples_comments[index_comments].append(comment['creation_time'])
                        extraction_time = datetime.datetime.today()
                        samples_comments[index_comments].append(extraction_time)

                        #Parent comment that it comes
                        samples_comments[index_comment].append(parent_id)

                        index_comments=index_comments+1

            except KeyError as e:
                print(e)
                break

        dict_comments = {
            "samples_comments" : samples_comments,
            "index_comments" : index_comments
        }

        return dict_comments
