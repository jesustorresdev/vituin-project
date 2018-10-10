# -*- coding: utf-8 -*-
import sys
sys.path.append('../')


from get_elastic import general_functions


excel = "excels_holiday_rent/booking.xls"

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
name_excel = "booking"


restriction = {'place':'Puerto de la Cruz'}

general_functions.write_excel(sheets_and_indexes, types_index, name_items, name_excel, main_field=main_field, restriction = restriction)


