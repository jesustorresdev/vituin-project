# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_normalTable

file =  sys.argv[1]


excel = file
sheet = 0
name_index = "index_facebook_likealyzer"
type_index = "structured"


table_start_and_end = {
    "start_row": 0,
    "start_col": 0,
    "end_row": 2,
    "end_col": 33,
    "start_value_row": 2,
    "start_value_col": 0
}

type_items = {
    "about" : int,
    "aboutAvailable" : str,
    "achievementsQuality" : str,
    "activity" : int,
    "answerToUserResponseTime" : str,
    "answerToUsersRatio" : str,
    "comments" : str,
    "contactInfoAvailable" : str,
    "dailyMessages" : float,
    "date" : str,
    "emailAvailable" : str,
    "engagement" : int,
    "frontPage" : int,
    "likedPages" : int,
    "locationAvailable" : str,
    "messageLengthRatio" : int,
    "name" : str,
    "originalFBVideos" : int,
    "participationRatio" : str,
    "peopleTalking" : int,
    "percentageOfNotes" : int,
    "percentageOfPhotos" : int,
    "percentageOfVideos" : int,
    "phoneAvailable" : str,
    "platform" : str,
    "response" : str,
    "source" : str,
    "summary" : str,
    "totalPageLikes" : int,
    "userPhotoAvailable" : str,
    "usernameAvailable" : str,
    "usersCanPost" : str,
    "websiteAvailable" : str,
}



name_items = [
    "about",
    "aboutAvailable",
    "achievementsQuality",
    "activity",
    "answerToUserResponseTime",
    "answerToUsersRatio",
    "comments",
    "contactInfoAvailable",
    "dailyMessages",
    "date",
    "emailAvailable",
    "engagement",
    "frontPage",
    "likedPages",
    "locationAvailable",
    "messageLengthRatio",
    "name",
    "originalFBVideos",
    "participationRatio",
    "peopleTalking",
    "percentageOfNotes",
    "percentageOfPhotos",
    "percentageOfVideos",
    "phoneAvailable",
    "platform",
    "response",
    "source",
    "summary",
    "totalPageLikes",
    "userPhotoAvailable",
    "usernameAvailable",
    "usersCanPost",
    "websiteAvailable",
]

date=['date']


index_excels_normalTable.main(excel, sheet, name_index, type_index, table_start_and_end, type_items, name_items, date=date)



