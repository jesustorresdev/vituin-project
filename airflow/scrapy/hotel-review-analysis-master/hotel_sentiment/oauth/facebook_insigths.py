import requests
import json
import re, os
import unicodecsv as csv
import datetime

from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import facebook_compliance_fix
from elasticsearch import Elasticsearch

es = Elasticsearch(['elasticsearch:9200'])


params = {'access_token': \
'EAAE3vGes1K8BAFKuqr5QkYvNJOeHF2bTQMyZArlkbsKf6BkpZC0bBRNLsv3iLO6OcXzgdSqxgYZCqpUyIrbeGIwZCIN6CvB986VzDkmOHS2gxZABuunYjPGD17Kar6g5RmMnFIHNzrZA6PkoLpw3xnahbPJ28IM2XsWjIdwKnu9O4CHH1uWr3P7x00p5BV0npI74rVJ9JPigZDZD'
}

#Types of insights
page_url = 'https://graph.facebook.com/v2.10/910220492463934/insights/ \
page_impressions, page_impressions_unique, page_impressions_by_country_unique, \
page_engaged_users, \
page_actions_post_reactions_total, \
page_fans, \
page_posts_impressions, page_posts_impressions_unique '

#page_fans_locale, page_fans_country, page_fans_gender_age, \

result = requests.get(page_url, params = params)
data = result.json()

#Where we will save the insights
insights_file='insights.csv'
CSVdir='/usr/local/airflow/scrapy-hotels/hotel-review-analysis-master/classify_elastic'
insights_file = os.path.join(CSVdir, insights_file)

insights=[]
insights.append(["name", "id", "value", "period", "title", "description", "time_insert"])

try:
    while True:
        for element in data['data']:
            #Array with all insigths
            tem=[]
            for field in element:
               tem.insert(0, element[field])
            tem.append(datetime.datetime.today().isoformat()) #Add the time of create
            insights.append(tem)
        data = requests.get(data['paging']['next']).json()

except KeyError as e:
    print(e)

#Create the file
with open(insights_file, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(insights)

