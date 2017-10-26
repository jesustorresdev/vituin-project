import requests
import json
import re
import os
from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import facebook_compliance_fix
import unicodecsv as csv




params = {'access_token': \
'EAAE3vGes1K8BAIKppZB4MK5l6l4EJ5EDRueuqs4oNsPE9ykV0hKAeYM431Wk0J9cGEBGfkRLsxFyFAaSnOzVSz3ZBPZBBwjZB7InNEdjlkSNBUQ7rh8ygUxkPEGQ2dEpiJZAnyZCDOZBiWL2RaGiCfAt8hWNn6fZAFXTXMj2V2lv45XwQcvdcgIvRM5ZAvbugwtfCKl4sYZCtetwZDZD' \
}

page_url = 'https://graph.facebook.com/v2.10/VisitPuertodelaCruz/feed'
#page_url = 'https://graph.facebook.com/v2.10/910220492463934/feed'


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

result = requests.get(page_url, params = params)
data = result.json()

#Fields where data will be write
posts_files='posts.csv'
comments_files='comments.csv'
CSVdir='/usr/local/airflow/scrapy-hotels/hotel-review-analysis-master/classify_elastic'
posts_files = os.path.join(CSVdir, posts_files)
comments_files = os.path.join(CSVdir, comments_files)


#Arrays will be save the dada
samples_posts=[]
samples_posts.append(["id", "created_time", "message", "story", "comments", "shares","likes","loves","wows","hahas","sads","angries","thankfuls","prides"])

samples_comments=[]
samples_comments.append(["id", "created_time", "id_transmitter", "message","likes","loves","wows","hahas","sads","angries","thankfuls","prides", "parent"])


index_post=1
index_comment=1




#Function to return reactions in post or comment
def reactions(element):
    reactions=[]
    reactions.append(posts_elements['like']['summary']['total_count'])
    reactions.append(posts_elements['love']['summary']['total_count'])
    reactions.append(posts_elements['wow']['summary']['total_count'])
    reactions.append(posts_elements['haha']['summary']['total_count'])
    reactions.append(posts_elements['sad']['summary']['total_count'])
    reactions.append(posts_elements['angry']['summary']['total_count'])
    reactions.append(posts_elements['thankful']['summary']['total_count'])
    reactions.append(posts_elements['pride']['summary']['total_count'])

    #If you like extract data of the extractor people
    #if posts_elements['like']['summary']['total_count'] > 0:
    #    for like in posts_elements['like']['data']:
    #        print('ID like:  ' + like['id'])
    #        print('Nombre usario del like:  ' + like['name'])
    #        print('+++++++++++++++++++++++++++++++')
    

    return reactions

while True:
    try:
        for element in data['data']:

            print(element['created_time'])
            samples_posts.append([element['id'],element['created_time']])
            
            if 'message' in element: #Could not have message
                samples_posts[index_post].append(element['message'])
            else:
                samples_posts[index_post].append('')

            if 'story' in element: #Could not have story
                samples_posts[index_post].append(element['story'])
            else:
                samples_posts[index_post].append('')

            this_post_elements_url = posts_elements_url.replace("{post_id}",element['id'])
            posts_elements = requests.get(this_post_elements_url, params = params).json()
            
            #Number of comments
            samples_posts[index_post].append(posts_elements['comments']['summary']['total_count'])

            #Shares
            try:
                samples_posts[index_post].append(posts_elements['shares']['count'])
            except KeyError as e:
                samples_posts[index_post].append(0)

            #Reactions posts
            for reaction in reactions(posts_elements):
                samples_posts[index_post].append(reaction)

            index_post=index_post+1
            
            #Comments
            for comment in posts_elements['comments']['data']:
                
                samples_comments.append([comment['id'],comment['created_time'], comment['from']['id'], comment['message']])

                #Reactions of comments
                this_comment_reactions_url = comments_reactions_url.replace("{comment_id}",comment['id'])
                comment_reactions = requests.get(this_comment_reactions_url, params = params).json()
                
                for reaction in reactions(comment_reactions):
                    samples_comments[index_comment].append(reaction)
                
                #We add that it doesnt exist parent comment
                #In this point all comments are parent comment. Ever
                samples_comments[index_comment].append(0)

                index_comment=index_comment+1

                #Comments of comments (in this case we have comprobate if the comment has childrens comments)
                this_count_comments_of_comments_url = counts_coments_of_comments_url.replace("{comment_id}",comment['id'])
                count_comments_of_comments = requests.get(this_count_comments_of_comments_url, params = params).json()
                

                #If this comment have childrens comments
                if count_comments_of_comments['comment_count'] > 0:

                    this_comments_of_comments_url = comments_of_comments_url.replace("{comment_id}",comment['id'])
                    comments_of_comments = requests.get(this_comments_of_comments_url, params = params).json()
                   
                    parent_id=comment['id'] #It saves the ID that the parent comment

                
                    for comment in comments_of_comments['data']:
                        samples_comments.append([comment['id'],comment['created_time'], comment['from']['id'], comment['message']])
                
                        #Reactions of the comments of comments
                        this_comment_reactions_url = comments_reactions_url.replace("{comment_id}",comment['id'])
                        comment_reactions = requests.get(this_comment_reactions_url, params = params).json()
                
                        for reaction in reactions(comment_reactions):
                            samples_comments[index_comment].append(reaction)
                        
                        #Parent comment that it comes
                        samples_comments[index_comment].append(parent_id)

                        index_comment=index_comment+1
        #Next page of posts
        data = requests.get(data['paging']['next']).json()


    except KeyError as e:
        print(e)
        break



print('--------------')
print(samples_posts[0])
print('Write ' + str(index_post-1) + ' posts')

print('--------------')
print(samples_comments[0])
print('Write ' + str(index_comment-1) + ' comments')


#It writes the comments and posts files
with open(posts_files, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(samples_posts)

with open(comments_files, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(samples_comments)

