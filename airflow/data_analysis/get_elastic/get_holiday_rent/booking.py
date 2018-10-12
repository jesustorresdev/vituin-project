# -*- coding: utf-8 -*-
import sys,os
sys.path.append('../')


from get_elastic import general_functions


#Fields where data will be write
booking_file ='booking.xls'
CSVdir='/usr/local/airflow/data_analysis/get_elastic/excels'
booking_file = os.path.join(CSVdir, booking_file)


sheets_and_indexes  = {'0':["index_list_homes_booking"]}
types_index = {'0':["unstructured"]}

main_field = "id_booking"
name_items = {"index_list_homes_booking":["id_booking",
                                          "value_for_money_rating",
                                          "facilities_rating",
                                          "comfort_rating",
                                          "lng",
                                          "review_count",
                                          "staff_rating",
                                          "price_min",
                                          "type_establishment",
                                          "score",
                                          "stars",
                                          "postalCode",
                                          "cleanliness_rating",
                                          "location_rating",
                                          "description",
                                          "phone",
                                          "wifi_rating",
                                          "address",
                                          "lat",
                                          "name",
                                          "url",
                                          "region",
                                          "upload_date",
                                          "place"
                                          ]}

restriction = {'place':'Puerto de la Cruz'}

general_functions.write_excel(sheets_and_indexes, types_index, name_items, booking_file, main_field=main_field, restriction = restriction)


