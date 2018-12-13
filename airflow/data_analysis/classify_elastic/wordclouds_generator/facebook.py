import nltk
from wordcloud import WordCloud, STOPWORDS
from nltk.tokenize import RegexpTokenizer

from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

import datetime
import sys
sys.path.append('../../')

from classify_elastic import utils


nltk.download('stopwords')
nltk.download('punkt')

WORD_COUNT = 0
ACTIONS = []
ELASTICSEARCH_INDEX_SEARCHED = 'index_comments_facebook_selenium'
ELASTICSEARCH_INDEX = 'index_comments_facebook_wordscloud'
ELASTICSEARCH_DOC_TYPE = 'unstructured'
EXIST_INDEX = True
FIRST_ITERATION = False
NAMES_ITEM = []

doc = {
    'query': {
        'match_all' : {}
    }
}

res=[]
try:
    res = utils.search_elastic(ELASTICSEARCH_INDEX_SEARCHED,ELASTICSEARCH_DOC_TYPE)
except:
    print("Not exists index")


if res:

    try:
        size = utils.size_index(ELASTICSEARCH_INDEX)
        #The next element indexed going to be the next id doesn't used
        count_id = int(size['hits']['total'])

    except:
        #If it's the first gruop of elements indexed
        print("First indexed")
        count_id = 0
        EXIST_INDEX = False
        FIRST_ITERATION = True


    wordsFiltered = []
    stopWordsSpanish = set(stopwords.words('spanish'))
    stopWordsItalian = set(stopwords.words('italian'))
    stopWordsFrench = set(stopwords.words('french'))
    stopWordsGerman = set(stopwords.words('german'))
    stopWordsEnglish = set(stopwords.words('english'))

    data = [
        entry['_source']['message'] for entry in res
    ]
    text = ''
    for dat in data:
        text += dat

    tokenizer = RegexpTokenizer("[\w']+")

    textToken = tokenizer.tokenize(text)
    for t in textToken:
        if t not in stopWordsSpanish and \
                t not in stopWordsItalian and \
                t not in stopWordsFrench and \
                t not in stopWordsGerman and \
                t not in stopWordsEnglish:
            wordsFiltered.append(t)
    print(textToken)
    exit()
    text = ''
    for dat in wordsFiltered:
        text += ' ' + dat

    wc = WordCloud(stopwords = set(STOPWORDS),
                   max_words = 100,
                   max_font_size = 100)
    wc.generate(text)
    word_list=[]
    freq_list=[]
    fontsize_list=[]
    position_list=[]
    orientation_list=[]
    color_list=[]

    for (word, freq), fontsize, position, orientation, color in wc.layout_:
        word_list.append(word)
        freq_list.append(freq)
        fontsize_list.append(fontsize)
        position_list.append(position)
        orientation_list.append(orientation)
        color_list.append(color)

    # get the positions
    x=[]
    y=[]
    for i in position_list:
        x.append(i[0])
        y.append(i[1])

    # get the relative occurence frequencies
    new_freq_list = []
    for i in freq_list:
        new_freq_list.append(i*100)


    for i in range(0,len(word_list)):


        item={}
        item["word"]=word_list[i]
        item["freq"]=freq_list[i]
        item["fontsize"]=fontsize_list[i]
        item["position"]=position_list[i]
        item["orientation"]=orientation_list[i]
        item["color"]=color_list[i]
        item["new_freq"]=new_freq_list[i]
        item["x"]=x[i]
        item["y"]=y[i]

        if not EXIST_INDEX and FIRST_ITERATION is True:
            NAMES_ITEM = utils.get_names_item(item)
            FIRST_ITERATION=False

        item['upload_date']=datetime.datetime.today()

        action = {
            "_index": ELASTICSEARCH_INDEX,
            "_type": ELASTICSEARCH_DOC_TYPE,
            "_id": count_id,
            "_source": item
        }

        ACTIONS.append(action)

        count_id += 1

        WORD_COUNT += 1



    if WORD_COUNT > 0:
        utils.update_elastic(ELASTICSEARCH_INDEX, ELASTICSEARCH_DOC_TYPE, ACTIONS, count_id, WORD_COUNT, EXIST_INDEX, NAMES_ITEM)

