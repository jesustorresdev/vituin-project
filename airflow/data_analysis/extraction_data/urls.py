# -*- coding: utf-8 -*-

# Here, it is define the urls where scrapy will go to work


def TripAdvisorHotelsURLs(place):
    urls = {
        'Puerto de la Cruz' : [
            "https://www.tripadvisor.co.uk/Hotels-g187481-Puerto_de_la_Cruz_Tenerife_Canary_Islands-Hotels.html"
        ]
    }
    return urls[place]
#
# def TripAdvisorZoneTenerifeURLs():
#     urls = [
#         "https://www.tripadvisor.co.uk/Hotels-g187479-Tenerife_Canary_Islands-Hotels.html"
#     ]
#
#     return urls
#
# def TripAdvisorZonePuertoDeLaCruzURLs():
#     urls = [
#         "https://www.tripadvisor.co.uk/Hotels-g187481-Puerto_de_la_Cruz_Tenerife_Canary_Islands-Hotels.html"
#     ]
#
#     return urls
#
# def TripAdvisorZoneFuerteventuraURLs():
#     urls = [
#         "https://www.tripadvisor.co.uk/Hotels-g187467-Fuerteventura_Canary_Islands-Hotels.html"
#     ]
#
#     return urls


def BookingURLs(place):
    urls= {
        'Puerto de la Cruz' : [
            "https://www.booking.com/searchresults.en-gb.html?aid=356984&label=gog235jc-country-en-gb-gb-unspec-es-com-L%3Aen-O%3Ax11-B%3Achrome-N%3Ayes-S%3Abo-U%3Ac-H%3As&lang=en-gb&sid=b9b5230609de880a1134cf7bbe706add&sb=1&src=searchresults&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fsearchresults.en-gb.html%3Faid%3D356984%3Blabel%3Dgog235jc-country-en-gb-gb-unspec-es-com-L%253Aen-O%253Ax11-B%253Achrome-N%253Ayes-S%253Abo-U%253Ac-H%253As%3Bsid%3Db9b5230609de880a1134cf7bbe706add%3Bclass_interval%3D1%3Bdest_id%3D777%3Bdest_type%3Dregion%3Bdtdisc%3D0%3Binac%3D0%3Bindex_postcard%3D0%3Blabel_click%3Dundef%3Boffset%3D0%3Bpostcard%3D0%3Bregion%3D777%3Broom1%3DA%252CA%3Bsb_price_type%3Dtotal%3Bss_all%3D0%3Bssb%3Dempty%3Bsshis%3D0%26%3B&ss=Puerto+de+la+Cruz%2C+Canary+Islands%2C+Spain&ssne=Tenerife&ssne_untouched=Tenerife&checkin_monthday=&checkin_month=&checkin_year=&checkout_monthday=&checkout_month=&checkout_year=&group_adults=2&group_children=0&no_rooms=1&from_sf=1&ss_raw=Puerto+de+la+Cruz&ac_position=0&ac_langcode=en&dest_id=-397851&dest_type=city&place_id_lat=28.4159&place_id_lon=-16.5533&search_pageview_id=d89861ac613f030f&search_selected=true&search_pageview_id=d89861ac613f030f&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0"
        ],
        'Adeje' : [
            "https://www.booking.com/searchresults.en-gb.html?aid=356984&label=gog235jc-country-en-gb-gb-unspec-es-com-L%3Aen-O%3Ax11-B%3Achrome-N%3Ayes-S%3Abo-U%3Ac-H%3As&sid=b9b5230609de880a1134cf7bbe706add&ac_click_type=b&ac_position=1&city=-369166&class_interval=1&dest_id=3490&dest_type=region&from_sf=1&group_adults=2&group_children=0&label_click=undef&no_rooms=1&raw_dest_type=region&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&src=searchresults&src_elem=sb&srpvid=342a09a8d61600ff&ss=Costa%20Adeje%2C%20Spain&ss_raw=Costa%20adeje&ssb=empty&ssne_untouched=Adeje&rows=15"
        ],
        'Tenerife' : [
            "https://www.booking.com/searchresults.es.html?label=gen173nr-1DCAEoggI46AdIM1gEaEaIAQGYAQq4ARnIAQzYAQPoAQGIAgGoAgO4Au6FgeQFwAIB&sid=b9b5230609de880a1134cf7bbe706add&sb=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.es.html%3Flabel%3Dgen173nr-1DCAEoggI46AdIM1gEaEaIAQGYAQq4ARnIAQzYAQPoAQGIAgGoAgO4Au6FgeQFwAIB%3Bsid%3Db9b5230609de880a1134cf7bbe706add%3Bsb_price_type%3Dtotal%26%3B&ss=Tenerife%2C+Espa%C3%B1a&is_ski_area=&ssne=Puerto+de+la+Cruz&ssne_untouched=Puerto+de+la+Cruz&checkin_year=2019&checkin_month=3&checkin_monthday=15&checkout_year=2019&checkout_month=3&checkout_monthday=17&group_adults=2&group_children=0&no_rooms=1&map=1&b_h4u_keep_filters=&from_sf=1&ss_raw=Tenerife&ac_position=0&ac_langcode=es&ac_click_type=b&dest_id=777&dest_type=region&place_id_lat=28.195009&place_id_lon=-16.621984&search_pageview_id=a5d99ab7476200a3&search_selected=true&search_pageview_id=a5d99ab7476200a3&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0#map_closed",
        ],
        'Gran Canaria' : [
            "https://www.booking.com/searchresults.en-gb.html?aid=356984&label=gog235jc-country-en-gb-gb-unspec-es-com-L%3Aen-O%3Ax11-B%3Achrome-N%3Ayes-S%3Abo-U%3Ac-H%3As&lang=en-gb&sid=b9b5230609de880a1134cf7bbe706add&sb=1&src=searchresults&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fsearchresults.en-gb.html%3Faid%3D356984%3Blabel%3Dgog235jc-country-en-gb-gb-unspec-es-com-L%253Aen-O%253Ax11-B%253Achrome-N%253Ayes-S%253Abo-U%253Ac-H%253As%3Bsid%3Db9b5230609de880a1134cf7bbe706add%3Bac_click_type%3Db%3Bac_position%3D0%3Bcheckin_month%3D3%3Bcheckin_monthday%3D15%3Bcheckin_year%3D2019%3Bcheckout_month%3D3%3Bcheckout_monthday%3D17%3Bcheckout_year%3D2019%3Bclass_interval%3D1%3Bdest_id%3D1405%3Bdest_type%3Dregion%3Bdtdisc%3D0%3Bfrom_sf%3D1%3Bgroup_adults%3D2%3Bgroup_children%3D0%3Binac%3D0%3Bindex_postcard%3D0%3Blabel_click%3Dundef%3Bno_rooms%3D1%3Boffset%3D0%3Bpostcard%3D0%3Braw_dest_type%3Dregion%3Broom1%3DA%252CA%3Bsb_price_type%3Dtotal%3Bsearch_selected%3D1%3Bshw_aparth%3D1%3Bslp_r_match%3D0%3Bsrc%3Dsearchresults%3Bsrc_elem%3Dsb%3Bsrpvid%3D990f9ba203a10199%3Bss%3DLa%2520Palma%2520Island%252C%2520Spain%3Bss_all%3D0%3Bss_raw%3DLa%2520palma%3Bssb%3Dempty%3Bsshis%3D0%3Bssne_untouched%3DEl%2520Hierro%26%3B&ss=Gran+Canaria%2C+Spain&is_ski_area=&ssne=La+Palma+Island&ssne_untouched=La+Palma+Island&checkin_year=2019&checkin_month=3&checkin_monthday=15&checkout_year=2019&checkout_month=3&checkout_monthday=17&group_adults=2&group_children=0&no_rooms=1&from_sf=1&ss_raw=Gran+Canaria&ac_position=0&ac_langcode=en&ac_click_type=b&dest_id=754&dest_type=region&place_id_lat=27.922889&place_id_lon=-15.548813&search_pageview_id=990f9ba203a10199&search_selected=true&search_pageview_id=990f9ba203a10199&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0",
        ],
        'La Palma' : [
            "https://www.booking.com/searchresults.en-gb.html?aid=356984&label=gog235jc-country-en-gb-gb-unspec-es-com-L%3Aen-O%3Ax11-B%3Achrome-N%3Ayes-S%3Abo-U%3Ac-H%3As&lang=en-gb&sid=b9b5230609de880a1134cf7bbe706add&sb=1&src=searchresults&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fsearchresults.en-gb.html%3Faid%3D356984%3Blabel%3Dgog235jc-country-en-gb-gb-unspec-es-com-L%253Aen-O%253Ax11-B%253Achrome-N%253Ayes-S%253Abo-U%253Ac-H%253As%3Bsid%3Db9b5230609de880a1134cf7bbe706add%3Bac_click_type%3Db%3Bac_position%3D0%3Bcheckin_month%3D3%3Bcheckin_monthday%3D15%3Bcheckin_year%3D2019%3Bcheckout_month%3D3%3Bcheckout_monthday%3D17%3Bcheckout_year%3D2019%3Bclass_interval%3D1%3Bdest_id%3D3450%3Bdest_type%3Dregion%3Bdtdisc%3D0%3Bfrom_sf%3D1%3Bgroup_adults%3D2%3Bgroup_children%3D0%3Binac%3D0%3Bindex_postcard%3D0%3Blabel_click%3Dundef%3Bno_rooms%3D1%3Boffset%3D0%3Bpostcard%3D0%3Braw_dest_type%3Dregion%3Broom1%3DA%252CA%3Bsb_price_type%3Dtotal%3Bsearch_selected%3D1%3Bshw_aparth%3D1%3Bslp_r_match%3D0%3Bsrc%3Dsearchresults%3Bsrc_elem%3Dsb%3Bsrpvid%3D3dd09b9a4dbe00f5%3Bss%3DEl%2520Hierro%252C%2520Spain%3Bss_all%3D0%3Bss_raw%3DEl%2520hierro%3Bssb%3Dempty%3Bsshis%3D0%3Bssne_untouched%3DLa%2520Gomera%26%3B&ss=La+Palma+Island%2C+Spain&is_ski_area=&ssne=El+Hierro&ssne_untouched=El+Hierro&checkin_year=2019&checkin_month=3&checkin_monthday=15&checkout_year=2019&checkout_month=3&checkout_monthday=17&group_adults=2&group_children=0&no_rooms=1&from_sf=1&search_pageview_id=3dd09b9a4dbe00f5&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0&ac_position=0&ac_langcode=en&ac_click_type=b&dest_id=1405&dest_type=region&place_id_lat=28.650089&place_id_lon=-17.868876&search_pageview_id=3dd09b9a4dbe00f5&search_selected=true&ss_raw=La+palma",
        ],
        'El Hierro' : [
            "https://www.booking.com/searchresults.en-gb.html?aid=356984&label=gog235jc-country-en-gb-gb-unspec-es-com-L%3Aen-O%3Ax11-B%3Achrome-N%3Ayes-S%3Abo-U%3Ac-H%3As&lang=en-gb&sid=b9b5230609de880a1134cf7bbe706add&sb=1&src=searchresults&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fsearchresults.en-gb.html%3Faid%3D356984%3Blabel%3Dgog235jc-country-en-gb-gb-unspec-es-com-L%253Aen-O%253Ax11-B%253Achrome-N%253Ayes-S%253Abo-U%253Ac-H%253As%3Bsid%3Db9b5230609de880a1134cf7bbe706add%3Bac_click_type%3Db%3Bac_position%3D0%3Bcheckin_month%3D3%3Bcheckin_monthday%3D15%3Bcheckin_year%3D2019%3Bcheckout_month%3D3%3Bcheckout_monthday%3D17%3Bcheckout_year%3D2019%3Bcity%3D-397851%3Bclass_interval%3D1%3Bdest_id%3D1775%3Bdest_type%3Dregion%3Bdtdisc%3D0%3Bfrom_sf%3D1%3Bgroup_adults%3D2%3Bgroup_children%3D0%3Binac%3D0%3Bindex_postcard%3D0%3Blabel_click%3Dundef%3Bno_rooms%3D1%3Boffset%3D0%3Bpostcard%3D0%3Braw_dest_type%3Dregion%3Broom1%3DA%252CA%3Bsb_price_type%3Dtotal%3Bsearch_selected%3D1%3Bshw_aparth%3D1%3Bslp_r_match%3D0%3Bsrc%3Dsearchresults%3Bsrc_elem%3Dsb%3Bsrpvid%3D8b059b92bacb016c%3Bss%3DLa%2520Gomera%252C%2520Spain%3Bss_all%3D0%3Bss_raw%3Dla%2520gomera%3Bssb%3Dempty%3Bsshis%3D0%3Bssne_untouched%3DPuerto%2520de%2520la%2520Cruz%26%3B&ss=El+Hierro%2C+Spain&is_ski_area=&ssne=La+Gomera&ssne_untouched=La+Gomera&checkin_year=2019&checkin_month=3&checkin_monthday=15&checkout_year=2019&checkout_month=3&checkout_monthday=17&group_adults=2&group_children=0&no_rooms=1&from_sf=1&ss_raw=El+hierro&ac_position=0&ac_langcode=en&ac_click_type=b&dest_id=3450&dest_type=region&place_id_lat=27.761785&place_id_lon=-17.968376&search_pageview_id=8b059b92bacb016c&search_selected=true&search_pageview_id=8b059b92bacb016c&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0",
        ],
        'La Gomera' : [
            "https://www.booking.com/searchresults.en-gb.html?aid=356984&label=gog235jc-country-en-gb-gb-unspec-es-com-L%3Aen-O%3Ax11-B%3Achrome-N%3Ayes-S%3Abo-U%3Ac-H%3As&lang=en-gb&sid=b9b5230609de880a1134cf7bbe706add&sb=1&src=searchresults&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fsearchresults.en-gb.html%3Faid%3D356984%3Blabel%3Dgog235jc-country-en-gb-gb-unspec-es-com-L%253Aen-O%253Ax11-B%253Achrome-N%253Ayes-S%253Abo-U%253Ac-H%253As%3Bsid%3Db9b5230609de880a1134cf7bbe706add%3Bac_position%3D0%3Bcheckin_year_month_monthday%3D2019-03-15%3Bcheckout_year_month_monthday%3D2019-03-17%3Bclass_interval%3D1%3Bdest_id%3D-397851%3Bdest_type%3Dcity%3Bdtdisc%3D0%3Bfrom_sf%3D1%3Bgroup_adults%3D2%3Bgroup_children%3D0%3Binac%3D0%3Bindex_postcard%3D0%3Blabel_click%3Dundef%3Bno_rooms%3D1%3Boffset%3D0%3Bpostcard%3D0%3Braw_dest_type%3Dcity%3Broom1%3DA%252CA%3Bsb_price_type%3Dtotal%3Bsearch_selected%3D1%3Bshw_aparth%3D1%3Bslp_r_match%3D0%3Bsrc%3Dsearchresults%3Bsrc_elem%3Dsb%3Bsrpvid%3Def639b644620005e%3Bss%3DPuerto%2520de%2520la%2520Cruz%252C%2520Canary%2520Islands%252C%2520Spain%3Bss_all%3D0%3Bss_raw%3DPuerto%2520de%2520la%2520Cruz%3Bssb%3Dempty%3Bsshis%3D0%3Bssne_untouched%3DTenerife%26%3B&ss=La+Gomera%2C+Spain&is_ski_area=&ssne=Puerto+de+la+Cruz&ssne_untouched=Puerto+de+la+Cruz&city=-397851&checkin_year=2019&checkin_month=3&checkin_monthday=15&checkout_year=2019&checkout_month=3&checkout_monthday=17&group_adults=2&group_children=0&no_rooms=1&from_sf=1&ss_raw=la+gomera&ac_position=0&ac_langcode=en&ac_click_type=b&dest_id=1775&dest_type=region&place_id_lat=28.122121&place_id_lon=-17.244863&search_pageview_id=ef639b644620005e&search_selected=true&search_pageview_id=ef639b644620005e&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0",
        ],
        'Lanzarote' : [
            "https://www.booking.com/searchresults.es.html?label=gen173nr-1DCAEoggI46AdIM1gEaEaIAQGYAQq4ARnIAQzYAQPoAQGIAgGoAgO4Au6FgeQFwAIB&sid=b9b5230609de880a1134cf7bbe706add&sb=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.es.html%3Flabel%3Dgen173nr-1DCAEoggI46AdIM1gEaEaIAQGYAQq4ARnIAQzYAQPoAQGIAgGoAgO4Au6FgeQFwAIB%3Bsid%3Db9b5230609de880a1134cf7bbe706add%3Bsb_price_type%3Dtotal%26%3B&ss=Lanzarote%2C+Espa%C3%B1a&is_ski_area=&ssne=Puerto+de+la+Cruz&ssne_untouched=Puerto+de+la+Cruz&checkin_year=2019&checkin_month=3&checkin_monthday=15&checkout_year=2019&checkout_month=3&checkout_monthday=17&group_adults=2&group_children=0&no_rooms=1&map=1&b_h4u_keep_filters=&from_sf=1&ss_raw=Lanzarote&ac_position=0&ac_langcode=es&ac_click_type=b&dest_id=760&dest_type=region&place_id_lat=28.973121&place_id_lon=-13.64921&search_pageview_id=a5d99ab7476200a3&search_selected=true&search_pageview_id=a5d99ab7476200a3&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0#map_closed",
        ],
        'Fuerteventura' : [
            "https://www.booking.com/searchresults.es.html?label=gen173nr-1DCAEoggI46AdIM1gEaEaIAQGYAQq4ARnIAQzYAQPoAQGIAgGoAgO4Au6FgeQFwAIB&sid=b9b5230609de880a1134cf7bbe706add&sb=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.es.html%3Flabel%3Dgen173nr-1DCAEoggI46AdIM1gEaEaIAQGYAQq4ARnIAQzYAQPoAQGIAgGoAgO4Au6FgeQFwAIB%3Bsid%3Db9b5230609de880a1134cf7bbe706add%3Bsb_price_type%3Dtotal%26%3B&ss=Fuerteventura&is_ski_area=0&ssne=Puerto+de+la+Cruz&ssne_untouched=Puerto+de+la+Cruz&checkin_year=2019&checkin_month=3&checkin_monthday=15&checkout_year=2019&checkout_month=3&checkout_monthday=17&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&ss_raw=P&dest_id=&dest_type=&search_pageview_id=a5d99ab7476200a3&search_selected=false"
        ]

    }
    return urls[place]
#
# def TripadvisorPtoCruzRestaurantsURLs():
#
#     urls = [
#         "https://www.tripadvisor.es/Restaurants-g187481-Puerto_de_la_Cruz_Tenerife_Canary_Islands.html"
#     ]
#     return urls

def TripadvisorHolidaysRentURLs(place):
    urls= {
        'Puerto de la Cruz' : [
            "https://www.tripadvisor.es/VacationRentals-g187481-Reviews-Puerto_de_la_Cruz_Tenerife_Canary_Islands-Vacation_Rentals.html"
        ],
        'Adeje' : [
            ""
        ],
        'Tenerife' : [
            "https://www.tripadvisor.es/VacationRentals-g187479-Reviews-Tenerife_Canary_Islands-Vacation_Rentals.html",
        ],
        'Gran Canaria' : [
            "https://www.tripadvisor.es/VacationRentals-g187471-Reviews-Gran_Canaria_Canary_Islands-Vacation_Rentals.html",
        ],
        'La Palma' : [
            "https://www.tripadvisor.es/VacationRentals-g187467-Reviews-Fuerteventura_Canary_Islands-Vacation_Rentals.html",
        ],
        'El Hierro' : [
            "https://www.tripadvisor.es/VacationRentals-g187473-Reviews-El_Hierro_Canary_Islands-Vacation_Rentals.html",
        ],
        'La Gomera' : [
            "https://www.tripadvisor.es/VacationRentals-g187469-Reviews-La_Gomera_Canary_Islands-Vacation_Rentals.html",
        ],
        'Lanzarote' : [
            "https://www.tripadvisor.es/VacationRentals-g187477-Reviews-Lanzarote_Canary_Islands-Vacation_Rentals.html",
        ],
        'Fuerteventura' : [
            "https://www.tripadvisor.es/VacationRentals-g187467-Reviews-Fuerteventura_Canary_Islands-Vacation_Rentals.html"
        ]
    }

    return urls[place]

def AirbnbURLs(place):
    urls= {
        'Puerto de la Cruz' : [
            "https://www.airbnb.es/s/Puerto-de-la-Cruz--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJBxuTnlXVQQwRQWOmKGEY6s0&query=Puerto%20de%20la%20Cruz%2C%20Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&s_tag=o78DH6Gz"
        ],
        'Adeje' : [
            "https://www.airbnb.es/s/Avenida-Rafael-Puig-Lluvina--Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Avenida%20Rafael%20Puig%20Lluvina%2C%20Adeje%2C%20Espa%C3%B1a&place_id=EitBdmVuaWRhIFJhZmFlbCBQdWlnIExsdXZpbmEsIEFkZWplLCBFc3Bhw7FhIi4qLAoUChIJ2_n_92SXagwRoNry88wONDsSFAoSCe0sQ9WbkGoMEQNBP_KTXbsq&allow_override%5B%5D=&s_tag=-MMLU5YD",
            "https://www.airbnb.es/s/Avenida-de-los-Pueblos--Costa-Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Avenida%20de%20los%20Pueblos%2C%20Costa%20Adeje%2C%20Espa%C3%B1a&place_id=EixBdmVuaWRhIGRlIGxvcyBQdWVibG9zLCBDb3N0YSBBZGVqZSwgRXNwYcOxYSIuKiwKFAoSCTcyujxhl2oMEb43GcnxZNX3EhQKEgnLOPMeWpdqDBGfTgTVe4yMug&allow_override%5B%5D=&s_tag=3nBv6zZn",
            "https://www.airbnb.es/s/Calle-Gran-Breta%C3%B1a--Costa-Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Calle%20Gran%20Breta%C3%B1a%2C%20Costa%20Adeje%2C%20Espa%C3%B1a&place_id=EilDYWxsZSBHcmFuIEJyZXRhw7FhLCBDb3N0YSBBZGVqZSwgRXNwYcOxYSIuKiwKFAoSCXnJ2n9el2oMEYaLQS41eqFJEhQKEgnLOPMeWpdqDBGfTgTVe4yMug&allow_override%5B%5D=&s_tag=lLtmkocG",
            "https://www.airbnb.es/s/Avenida-de-Espa%C3%B1a--Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Avenida%20de%20Espa%C3%B1a%2C%20Adeje%2C%20Espa%C3%B1a&place_id=EiJBdmVuaWRhIGRlIEVzcGHDsWEsIEFkZWplLCBFc3Bhw7FhIi4qLAoUChIJJcugjVyXagwR1xge9Dwm0hYSFAoSCe0sQ9WbkGoMEQNBP_KTXbsq&allow_override%5B%5D=&s_tag=JITVUhln",
            # "https://www.airbnb.es/s/Playa-de-Troya--Islas-Canarias--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Playa%20de%20Troya%2C%20Islas%20Canarias%2C%20Espa%C3%B1a&place_id=ChIJZ7ou-miXagwRPZd98Sj8Knw&map_toggle=true&allow_override%5B%5D=&s_tag=2UqOQOXc",
            # "https://www.airbnb.es/s/Puerto-Colon--Playa-de-la-Am%C3%A9ricas--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Puerto%20Colon%2C%20Playa%20de%20la%20Am%C3%A9ricas%2C%20Espa%C3%B1a&place_id=ChIJv56cUEOXagwRR4J2T1JFI9Y&map_toggle=true&allow_override%5B%5D=&s_tag=9YeuCGCc",
            # "https://www.airbnb.es/s/Playa-Fa%C3%B1abe--Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Playa%20Fa%C3%B1abe%2C%20Adeje%2C%20Espa%C3%B1a&place_id=ChIJmW_f_06XagwRnJ62y5AbUzQ",
            # "https://www.airbnb.es/s/Playa-Fa%C3%B1abe--Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Playa%20Fa%C3%B1abe%2C%20Adeje%2C%20Espa%C3%B1a&place_id=ChIJmW_f_06XagwRnJ62y5AbUzQ",
            # "https://www.airbnb.es/s/Playa-del-Duque--Santa-Cruz-de-Tenerife--Spain/homes?refinement_paths%5B%5D=%2Fhomes&query=Playa%20del%20Duque%2C%20Santa%20Cruz%20de%20Tenerife%2C%20Spain&place_id=ChIJ0cRmSUqXagwR6qRnp8xGs4I&map_toggle=true&allow_override%5B%5D=&s_tag=Ru9Zh_yf",
            # "https://www.airbnb.es/s/La-Caleta-de-Adeje--La-Caleta/homes?refinement_paths%5B%5D=%2Fhomes&query=La%20Caleta%20de%20Adeje%2C%20La%20Caleta&place_id=ChIJI5Gz9s6QagwR5e8KupQk354&map_toggle=true&allow_override%5B%5D=&s_tag=O8OCFjjT",
            # "https://www.airbnb.es/s/Golf-Costa-Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Golf%20Costa%20Adeje%2C%20Espa%C3%B1a&place_id=ChIJl1EFE2-aagwRf2htVeWBRxk&map_toggle=true&allow_override%5B%5D=&s_tag=eBC8f0Nd",
            # "https://www.airbnb.es/s/Avenida-Madro%C3%B1al--Costa-Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Avenida%20Madro%C3%B1al%2C%20Costa%20Adeje%2C%20Espa%C3%B1a&place_id=EidBdmVuaWRhIE1hZHJvw7FhbCwgQ29zdGEgQWRlamUsIEVzcGHDsWEiLiosChQKEgmLQHuK_ZlqDBHSxM3Kv0my4hIUChIJyzjzHlqXagwRn04E1XuMjLo&map_toggle=true&allow_override%5B%5D=&s_tag=ya8prbvn",
            # "https://www.airbnb.es/s/Calle-Extremadura--Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Calle%20Extremadura%2C%20Adeje%2C%20Espa%C3%B1a&place_id=EiFDYWxsZSBFeHRyZW1hZHVyYSwgQWRlamUsIEVzcGHDsWEiLiosChQKEgmFqDKJ-ZlqDBHPAtLr7x8yQhIUChIJ7SxD1ZuQagwRA0E_8pNduyo&map_toggle=true&allow_override%5B%5D=&s_tag=OIIZPy6K",
            # "https://www.airbnb.es/s/Avenida-Francia--Costa-Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Avenida%20Francia%2C%20Costa%20Adeje%2C%20Espa%C3%B1a&place_id=EiVBdmVuaWRhIEZyYW5jaWEsIENvc3RhIEFkZWplLCBFc3Bhw7FhIi4qLAoUChIJSVq4suOZagwRva1C36s0UqsSFAoSCcs48x5al2oMEZ9OBNV7jIy6&map_toggle=true&allow_override%5B%5D=&s_tag=W5eCnmgU",
            # "https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=Avenida%20europa%2C%20Costa%20Adeje%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&s_tag=9otg5AwJ",
            # "https://www.airbnb.es/s/Callao-Salvaje--Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&query=Callao%20Salvaje%2C%20Tenerife&place_id=ChIJXY2y6QWRagwRwNKxQOqEKYo&map_toggle=true&allow_override%5B%5D=&s_tag=W3rd-CIE",
            # "https://www.airbnb.es/s/Calle-el-Puertito--Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Calle%20el%20Puertito%2C%20Adeje%2C%20Espa%C3%B1a&place_id=EiFDYWxsZSBlbCBQdWVydGl0bywgQWRlamUsIEVzcGHDsWEiLiosChQKEgm5kc4a4JBqDBFc76yYNYDOBRIUChIJ7SxD1ZuQagwRA0E_8pNduyo&map_toggle=true&allow_override%5B%5D=&s_tag=LWB0xg1-",
            # "https://www.airbnb.es/s/Marazul--Tenerife--Spanje/homes?refinement_paths%5B%5D=%2Fhomes&query=Marazul%2C%20Tenerife%2C%20Spanje&place_id=ChIJSbJ82LyRagwRlvYCvJUtX58&map_toggle=true&allow_override%5B%5D=&s_tag=MllgsHUt",
            # "https://www.airbnb.es/s/Avenida-San-Borondon--Fa%C3%B1ab%C3%A9--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Avenida%20San%20Borondon%2C%20Fa%C3%B1ab%C3%A9%2C%20Espa%C3%B1a&place_id=EidBdmVuaWRhIFNhbiBCb3JvbmRvbiwgRmHDsWFiw6ksIEVzcGHDsWEiLiosChQKEgmjtW_FqJBqDBEon4YXdkLYahIUChIJ3y_vyqiQagwRUOgQKm7zeAY&map_toggle=true&allow_override%5B%5D=&s_tag=WkC2INvb",
            # "https://www.airbnb.es/s/Calle-Hermano-Pedro--Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Calle%20Hermano%20Pedro%2C%20Adeje%2C%20Espa%C3%B1a&place_id=EiNDYWxsZSBIZXJtYW5vIFBlZHJvLCBBZGVqZSwgRXNwYcOxYSIuKiwKFAoSCS9_6JWfkGoMEb4wkDfukQdCEhQKEgntLEPVm5BqDBEDQT_yk127Kg&map_toggle=true&allow_override%5B%5D=&s_tag=818jPPLl",
            # "https://www.airbnb.es/s/Avenida-del-Poniente--Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Avenida%20del%20Poniente%2C%20Adeje%2C%20Espa%C3%B1a&place_id=EiRBdmVuaWRhIGRlbCBQb25pZW50ZSwgQWRlamUsIEVzcGHDsWEiLiosChQKEgmzHhh3pJBqDBGyyIqnZMBMpBIUChIJ7SxD1ZuQagwRA0E_8pNduyo&map_toggle=true&allow_override%5B%5D=&s_tag=NJp9ZbKh&section_offset=4&items_offset=54",
            # "https://www.airbnb.es/s/Avenida-de-Ayyo--Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Avenida%20de%20Ayyo%2C%20Adeje%2C%20Espa%C3%B1a&place_id=Eh9BdmVuaWRhIGRlIEF5eW8sIEFkZWplLCBFc3Bhw7FhIi4qLAoUChIJRcBJwZaQagwR2rylPPxvws4SFAoSCe0sQ9WbkGoMEQNBP_KTXbsq&map_toggle=true&allow_override%5B%5D=&s_tag=mx4lW3Rb",
            # "https://www.airbnb.es/s/Arme%C3%B1ime--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&query=Arme%C3%B1ime%2C%20Santa%20Cruz%20de%20Tenerife&place_id=ChIJyaWIKO6QagwROO9OnpFk9Ak&map_toggle=true&allow_override%5B%5D=&s_tag=cxcaf8I3",
            # "https://www.airbnb.es/s/Calle-Pedro-Garcia-Cabrera--Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Calle%20Pedro%20Garcia%20Cabrera%2C%20Adeje%2C%20Espa%C3%B1a&place_id=EipDYWxsZSBQZWRybyBHYXJjaWEgQ2FicmVyYSwgQWRlamUsIEVzcGHDsWEiLiosChQKEgm9kfYS8ZBqDBHTj2XbgLrsAxIUChIJ7SxD1ZuQagwRA0E_8pNduyo&map_toggle=true&allow_override%5B%5D=&s_tag=sCO-D9Nq",
            # "https://www.airbnb.es/s/Carretera-Taucho--Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Carretera%20Taucho%2C%20Adeje%2C%20Espa%C3%B1a&place_id=EiBDYXJyZXRlcmEgVGF1Y2hvLCBBZGVqZSwgRXNwYcOxYSIuKiwKFAoSCf1D1r95kGoMERFexCCeII08EhQKEgntLEPVm5BqDBEDQT_yk127Kg&allow_override%5B%5D=&map_toggle=true&s_tag=DW7sVNRW",
            # "https://www.airbnb.es/s/Calle-la-Un%C3%AD%C3%B3n--Tijoco-Bajo--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Calle%20la%20Un%C3%AD%C3%B3n%2C%20Tijoco%20Bajo%2C%20Espa%C3%B1a&place_id=EiZDYWxsZSBsYSBVbsOtw7NuLCBUaWpvY28gQmFqbywgRXNwYcOxYSIuKiwKFAoSCYv8RmZKkGoMEYYPzBRWvKOcEhQKEgmJNxKJNZBqDBGKVf3re-SNOg&allow_override%5B%5D=&map_toggle=true&s_tag=9w0QyO0x",
        ],
        'Gran Canaria' : [
            # Las Palmas
            # - Tafira Baja - Alta
            "https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Tafira%2C%20Las%20Palmas&map_toggle=true&allow_override%5B%5D=&s_tag=4DvS5ykn",
            "https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Tafira%2C%20Las%20Palmas&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.022685629710075&sw_lng=-15.492859946094061&ne_lat=28.081746997825146&ne_lng=-15.440700053905882&s_tag=39c8_8D3",
            "https://www.airbnb.es/s/Tafira-Baja--Tafira-Baja--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Tafira%20Baja%2C%20Tafira%20Baja%2C%20Espa%C3%B1a&place_id=ChIJm1eITdSVQAwRMlDq7IStICE&map_toggle=true&allow_override%5B%5D=&s_tag=ZjE-Y7ob",
            "https://www.airbnb.es/s/Monte-Luz--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Monte%20Luz%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.052120719338628&sw_lng=-15.469022547052178&ne_lat=28.081647031182644&ne_lng=-15.442942600958089&s_tag=MxJ846IR",
            # - San Lorenzo
            "https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=San%20Lorenzo%2C%20Las%20Palmas%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.06397508506377&sw_lng=-15.489247645166175&ne_lat=28.09349780814779&ne_lng=-15.463167699072086&s_tag=k6DOBUQI",
            # - Almatriche
            "https://www.airbnb.es/s/Almatriche--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Almatriche%2C%20Espa%C3%B1a&place_id=ChIJ2UdqqjGUQAwRULPfviiO9VU&allow_override%5B%5D=&s_tag=JspTTJRA",
            # - Tamaraceite
            "https://www.airbnb.es/s/Tamaraceite--Tamaraceite--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Tamaraceite%2C%20Tamaraceite%2C%20Espa%C3%B1a&place_id=ChIJWyd_HmiUQAwRDe5POWhMvc0&map_toggle=true&allow_override%5B%5D=&s_tag=LnkRWsnB",
            "https://www.airbnb.es/s/Calle-Pedro-Hidalgo--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Calle%20Pedro%20Hidalgo%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.087833954224813&sw_lng=-15.49854466594272&ne_lat=28.14685586691995&ne_lng=-15.446384773754541&s_tag=NmiJXZx5",
            # - Siete Palmas
            "https://www.airbnb.es/s/Siete-Palmas--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Siete%20Palmas%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&place_id=ChIJ40nGb0uUQAwRD3yQARAy1bs&map_toggle=true&allow_override%5B%5D=&s_tag=WWC7lKC8",
            # - Escaleritas
            "https://www.airbnb.es/s/Avenida-Escaleritas--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Avenida%20Escaleritas%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&place_id=EjhBdmVuaWRhIEVzY2FsZXJpdGFzLCBMYXMgUGFsbWFzIGRlIEdyYW4gQ2FuYXJpYSwgRXNwYcOxYSIuKiwKFAoSCdWGcH-olUAMEbLEr-u4S2zKEhQKEgnRl8CRDpVADBFlujhTrLU2qw&map_toggle=true&allow_override%5B%5D=&s_tag=0DZeZVyj",
            # - Paseo Chill
            "https://www.airbnb.es/s/Paseo-Chil--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Paseo%20Chil%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&place_id=Ei9QYXNlbyBDaGlsLCBMYXMgUGFsbWFzIGRlIEdyYW4gQ2FuYXJpYSwgRXNwYcOxYSIuKiwKFAoSCdm8qux0lUAMEbw4CUTqHjcdEhQKEgnRl8CRDpVADBFlujhTrLU2qw&map_toggle=true&allow_override%5B%5D=&s_tag=fz_dbstw",
            "https://www.airbnb.es/s/Paseo-Chil--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Paseo%20Chil%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.099672020571692&sw_lng=-15.435588565576255&ne_lat=28.12918392845325&ne_lng=-15.409508619482166&s_tag=tlROcEa8",
            # - Las Rehoyas
            "https://www.airbnb.es/s/Las-Rehoyas--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Las%20Rehoyas%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&place_id=ChIJMYZBK72VQAwR7hwWiPk7IN8&map_toggle=true&allow_override%5B%5D=&s_tag=nFVmF5JV",
            # - Mesa y López
            "https://www.airbnb.es/s/Mesa-y-L%C3%B3pez--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Mesa%20y%20L%C3%B3pez%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&zoom=17&search_by_map=true&sw_lat=28.126332905820888&sw_lng=-15.44405499326174&ne_lat=28.133709712892344&ne_lng=-15.43753500673822&allow_override%5B%5D=&s_tag=_jJ352_3",
            "https://www.airbnb.es/s/Plaza-de-Espa%C3%B1a--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Plaza%20de%20Espa%C3%B1a%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=18&search_by_map=true&sw_lat=28.13305756922958&sw_lng=-15.436897996630831&ne_lat=28.136745788714762&ne_lng=-15.43363800336907&s_tag=E19h5XZq",
            "https://www.airbnb.es/s/Parque-Santa-Catalina--Las-Palmas-de-Gran-Canaria/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Parque%20Santa%20Catalina%2C%20Las%20Palmas%20de%20Gran%20Canaria&zoom=17&search_by_map=true&sw_lat=28.131806764526672&sw_lng=-15.434973096441606&ne_lat=28.139183156455235&ne_lng=-15.428453109918085&allow_override%5B%5D=&s_tag=iNb4bfSM",
            # - Las Canteras
            "https://www.airbnb.es/s/Parque-Santa-Catalina--Las-Palmas-de-Gran-Canaria/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Parque%20Santa%20Catalina%2C%20Las%20Palmas%20de%20Gran%20Canaria&zoom=18&search_by_map=true&sw_lat=28.138748832356217&sw_lng=-15.435199188449031&ne_lat=28.14243683598685&ne_lng=-15.43193919518727&allow_override%5B%5D=&s_tag=z-WDsBz9",
            "https://www.airbnb.es/s/Las-Canteras-Beach--Las-Palmas-de-Gran-Canaria--Spain/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Las%20Canteras%20Beach%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Spain&place_id=ChIJOZUfwBeVQAwRMY-lsCJwETw&allow_override%5B%5D=&s_tag=K25e6_j7",
            "https://www.airbnb.es/s/Las-Canteras-Beach--Las-Palmas-de-Gran-Canaria--Spain/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Las%20Canteras%20Beach%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Spain&zoom=18&search_by_map=true&sw_lat=28.137214376270748&sw_lng=-15.436337996630881&ne_lat=28.140902438103186&ne_lng=-15.43307800336912&allow_override%5B%5D=&s_tag=OzG_0uTi",
            "https://www.airbnb.es/s/Las-Canteras-Beach--Las-Palmas-de-Gran-Canaria--Spain/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Las%20Canteras%20Beach%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Spain&zoom=18&search_by_map=true&sw_lat=28.137214376270748&sw_lng=-15.436337996630881&ne_lat=28.140902438103186&ne_lng=-15.43307800336912&allow_override%5B%5D=&s_tag=OzG_0uTi",
            "https://www.airbnb.es/s/Las-Canteras-Beach--Las-Palmas-de-Gran-Canaria--Spain/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Las%20Canteras%20Beach%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Spain&zoom=17&search_by_map=true&sw_lat=28.145116352959796&sw_lng=-15.432667948248334&ne_lat=28.152491735166574&ne_lng=-15.426147961724812&allow_override%5B%5D=&s_tag=WEuMp7Il",
            # - Parque Santa Catalina
            "https://www.airbnb.es/s/Parque-Santa-Catalina--Las-Palmas-de-Gran-Canaria/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Parque%20Santa%20Catalina%2C%20Las%20Palmas%20de%20Gran%20Canaria&place_id=ChIJE4Gq8z-VQAwR4SOIu2lyDms&allow_override%5B%5D=&s_tag=SHV8aQyp",
            # - La Isleta
            "https://www.airbnb.es/s/Isleta--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Isleta%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&place_id=ChIJC8iFX0eVQAwRR5XLwS8vBno&map_toggle=true&allow_override%5B%5D=&s_tag=Cv-5SQHL",
            "https://www.airbnb.es/s/Isleta--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Isleta%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.14494664487054&sw_lng=-15.433626994427577&ne_lat=28.159696867177555&ne_lng=-15.420587021380534&s_tag=38x_gEab",
            "https://www.airbnb.es/s/Isleta--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Isleta%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.1486880500068&sw_lng=-15.430367001165816&ne_lat=28.156063161174902&ne_lng=-15.423847014642295&s_tag=ZdDaOnBO",
            "https://www.airbnb.es/s/Isleta--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Isleta%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.1482150526966&sw_lng=-15.426687010397384&ne_lat=28.155590199759978&ne_lng=-15.420167023873862&s_tag=9jyKVfsU",
            "https://www.airbnb.es/s/Isleta--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Isleta%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.14786037277454&sw_lng=-15.44127665453805&ne_lat=28.162610152834333&ne_lng=-15.428236681491008&s_tag=A9FMScAg",
            "https://www.airbnb.es/s/Isleta--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Isleta%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.15277463562048&sw_lng=-15.43553672724618&ne_lat=28.167523669695544&ne_lng=-15.422496754199138&s_tag=iieMNy1j",
            # - Vegueta
            "https://www.airbnb.es/s/Vegueta--Las-Palmas-de-Gran-Canaria/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Vegueta%2C%20Las%20Palmas%20de%20Gran%20Canaria&place_id=ChIJrwI0U4yVQAwR8LymoTFQnJo&map_toggle=true&allow_override%5B%5D=&s_tag=iAJf_zS9",
            # - Barrio San Juan
            "https://www.airbnb.es/s/Barrio-San-Juan--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Barrio%20San%20Juan%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&place_id=EjRCYXJyaW8gU2FuIEp1YW4sIExhcyBQYWxtYXMgZGUgR3JhbiBDYW5hcmlhLCBFc3Bhw7FhIi4qLAoUChIJs7COt-yVQAwRHpPiAERtcTYSFAoSCdGXwJEOlUAMEWW6OFOstTar&map_toggle=true&allow_override%5B%5D=&s_tag=gMIOOhIM",
            # - Triana
            "https://www.airbnb.es/s/Calle-Triana--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Calle%20Triana%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&place_id=EjFDYWxsZSBUcmlhbmEsIExhcyBQYWxtYXMgZGUgR3JhbiBDYW5hcmlhLCBFc3Bhw7FhIi4qLAoUChIJG9iZhI-VQAwRistCxhUGWTESFAoSCdGXwJEOlUAMEWW6OFOstTar&map_toggle=true&allow_override%5B%5D=&s_tag=0BBnado-",
            # - Fuente luminosa
            "https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Fuente%20luminosa%20las%20palmas&map_toggle=true&allow_override%5B%5D=&s_tag=qStfQquk",
            # - San Cristobal
            "https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=San%20cristobal%20las%20palmas&map_toggle=true&allow_override%5B%5D=&s_tag=2cTMetXQ",
            # - Calle Pedro Hidalgo
            "https://www.airbnb.es/s/Calle-Pedro-Hidalgo--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Calle%20Pedro%20Hidalgo%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&place_id=EjhDYWxsZSBQZWRybyBIaWRhbGdvLCBMYXMgUGFsbWFzIGRlIEdyYW4gQ2FuYXJpYSwgRXNwYcOxYSIuKiwKFAoSCU1WgfvhlUAMEWu3mrAC-N_9EhQKEgnRl8CRDpVADBFlujhTrLU2qw&map_toggle=true&allow_override%5B%5D=&s_tag=IpqMEjr4",
            # - Los Hoyos - Santa Margarita
            "https://www.airbnb.es/s/Calle-Pedro-Hidalgo--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Calle%20Pedro%20Hidalgo%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.02585616201679&sw_lng=-15.44945580373552&ne_lat=28.055390420166766&ne_lng=-15.42337585764143&s_tag=wnzP-u43",
            # La Aldea
            "https://www.airbnb.es/s/La-Aldea-de-San-Nicol%C3%A1s--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=La%20Aldea%20de%20San%20Nicol%C3%A1s%2C%20Las%20Palmas&place_id=ChIJ-ejmwKliQAwRIBRNvvNAAwQ&allow_override%5B%5D=&s_tag=8brCVoYt",
            # Agaete
            "https://www.airbnb.es/s/Agaete--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Agaete%2C%20Las%20Palmas&place_id=ChIJM_M6DY-LQAwR8BJNvvNAAwQ&map_toggle=true&allow_override%5B%5D=&s_tag=f5VABcpt",
            # Gáldar
            # - Gáldar
            "https://www.airbnb.es/s/G%C3%A1ldar--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=G%C3%A1ldar%2C%20Las%20Palmas&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.110396195275186&sw_lng=-15.682006668262122&ne_lat=28.16940442414025&ne_lng=-15.629846776073943&s_tag=yMv2BlDI",
            # - Puerto Sardina
            "https://www.airbnb.es/s/G%C3%A1ldar--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=G%C3%A1ldar%2C%20Las%20Palmas&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.100212981162347&sw_lng=-15.703721832446693&ne_lat=28.159227387317685&ne_lng=-15.651561940258514&s_tag=h2PkkjA8",
            "https://www.airbnb.es/s/G%C3%A1ldar--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=G%C3%A1ldar%2C%20Las%20Palmas&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.13938845322273&sw_lng=-15.712948631457923&ne_lat=28.1983790837139&ne_lng=-15.660788739269744&s_tag=g_qNy1L4",
            # Santa María de Guía
            "https://www.airbnb.es/s/Santa-Mar%C3%ADa-de-Gu%C3%ADa-de-Gran-Canaria--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=Santa%20Mar%C3%ADa%20de%20Gu%C3%ADa%20de%20Gran%20Canaria%2C%20Las%20Palmas&place_id=ChIJp4EY7nKNQAwRUBRNvvNAAwQ&allow_override%5B%5D=&s_tag=SG6j6442",
            # Valleseco
            "https://www.airbnb.es/s/Valleseco--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=Valleseco%2C%20Las%20Palmas&place_id=ChIJqfQ0ePCRQAwR4BRNvvNAAwQ&allow_override%5B%5D=&s_tag=gZsK4wX8",
            # Teror
            "https://www.airbnb.es/s/Teror--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Teror%2C%20Las%20Palmas&place_id=ChIJZ9O4Dy2SQAwRjwlG_UHQOng&map_toggle=true&allow_override%5B%5D=&s_tag=qhH7Mao_",
            # Arucas
            "https://www.airbnb.es/s/Arucas--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=Arucas%2C%20Las%20Palmas&place_id=ChIJXSpcqAyTQAwRYt9QML-g3jc&allow_override%5B%5D=&s_tag=-dYod5SP",
            "https://www.airbnb.es/s/Arucas--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Arucas%2C%20Las%20Palmas&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.074564825324053&sw_lng=-15.521754284472966&ne_lat=28.13359478094188&ne_lng=-15.469594392284787&s_tag=wS-8D2I7",
            # Telde
            # - Telde
            "https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Telde&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=27.966662177463977&sw_lng=-15.441623295398333&ne_lat=28.02575740754085&ne_lng=-15.389463403210154&s_tag=DKV8jcMV",
            # - Estrella - Melenara
            "https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Telde&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=27.97128644207278&sw_lng=-15.413899983020404&ne_lat=28.03037887948377&ne_lng=-15.361740090832225&s_tag=RqORAnux",
            # - Melenara
            "https://www.airbnb.es/s/Melenara/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Melenara&place_id=ChIJxS7SVDO9QAwRSKSOX1C7aZk&map_toggle=true&allow_override%5B%5D=&s_tag=tts9rUle",
            # - La estrella
            "https://www.airbnb.es/s/La-Estrella--Spain/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=La%20Estrella%2C%20Spain&place_id=ChIJ-XQYUWu9QAwRaJgmbnFTzOM&map_toggle=true&allow_override%5B%5D=&s_tag=hllwprkv",
            # - Las Remudas
            "https://www.airbnb.es/s/Las-Remudas--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Las%20Remudas%2C%20Espa%C3%B1a&place_id=ChIJ4flbYWi9QAwRPG7k3C32sMY&map_toggle=true&allow_override%5B%5D=&s_tag=50l5_lGp",
            # - Marpequeña
            "https://www.airbnb.es/s/Marpeque%C3%B1a--Las-Palmas--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Marpeque%C3%B1a%2C%20Las%20Palmas%2C%20Espa%C3%B1a&place_id=ChIJjcuRskO9QAwRBXUHrZTjnkQ&map_toggle=true&allow_override%5B%5D=&s_tag=wDYXmk0m",
            # - Balcon de Telde
            "https://www.airbnb.es/s/Balcon-de-Telde--Balcon-de-Telde--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Balcon%20de%20Telde%2C%20Balcon%20de%20Telde%2C%20Espa%C3%B1a&place_id=ChIJE_tU056XQAwRI77irrgyf0A&map_toggle=true&allow_override%5B%5D=&s_tag=hmhe8KlL",
            # - Valle de Jinamar
            "https://www.airbnb.es/s/Valle-de-Jinamar--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Valle%20de%20Jinamar%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=12&search_by_map=true&sw_lat=27.90415305385133&sw_lng=-15.518981937696607&ne_lat=28.140467442081988&ne_lng=-15.310342368943894&s_tag=GRNSC7un",
            # Ingenio
            "https://www.airbnb.es/s/Ingenio--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Ingenio%2C%20Las%20Palmas&place_id=ChIJg2CfL-qYQAwRd7OF_K7A2IY&map_toggle=true&allow_override%5B%5D=&s_tag=Z7Ot_-KL",
            # Agüimes
            "https://www.airbnb.es/s/Ag%C3%BCimes--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Ag%C3%BCimes%2C%20Las%20Palmas&place_id=ChIJ099rjSWZQAwRABNNvvNAAwQ&map_toggle=true&allow_override%5B%5D=&s_tag=nOoQgJte",
            "https://www.airbnb.es/s/Ag%C3%BCimes--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Ag%C3%BCimes%2C%20Las%20Palmas&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=27.88757948679693&sw_lng=-15.454477702441839&ne_lat=27.94672241055732&ne_lng=-15.40231781025366&s_tag=dxBAM6gQ",
            "https://www.airbnb.es/s/Ag%C3%BCimes--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Ag%C3%BCimes%2C%20Las%20Palmas&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=27.85616693860174&sw_lng=-15.434135829272893&ne_lat=27.915328772433462&ne_lng=-15.381975937084714&s_tag=WfMNfJ4P",
            # San Bartolomé de Tirajana
            # - Playa del Águila
            "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=15&search_by_map=true&sw_lat=27.768199206197078&sw_lng=-15.536038804934366&ne_lat=27.806133666189414&ne_lng=-15.503009925834943&allow_override%5B%5D=&s_tag=6i7witC4",
            # - San Agustín
            "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=16&search_by_map=true&sw_lat=27.764474591143784&sw_lng=-15.553444961014002&ne_lat=27.78344432753015&ne_lng=-15.536930521464292&allow_override%5B%5D=&s_tag=6n-Ca_DS",
            "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=16&search_by_map=true&sw_lat=27.760164374588552&sw_lng=-15.569721346329565&ne_lat=27.77913492189227&ne_lng=-15.553206906779856&allow_override%5B%5D=&s_tag=BHWWxewj",
            # - Playa del Inglés
            "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=16&search_by_map=true&sw_lat=27.737749772770506&sw_lng=-15.582724695633765&ne_lat=27.756724535254587&ne_lng=-15.566210256084055&allow_override%5B%5D=&s_tag=c_RTdGdo",
            "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=17&search_by_map=true&sw_lat=27.7551691509456&sw_lng=-15.573585719306518&ne_lat=27.764655345565682&ne_lng=-15.565328499531663&allow_override%5B%5D=&s_tag=S53UkR2C",
            "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=17&search_by_map=true&sw_lat=27.75534005117439&sw_lng=-15.582318991859008&ne_lat=27.764826229723585&ne_lng=-15.574061772084153&allow_override%5B%5D=&s_tag=91IRp5yN",
            "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=17&search_by_map=true&sw_lat=27.752368283581415&sw_lng=-15.579884380729052&ne_lat=27.76185474157272&ne_lng=-15.571627160954197&allow_override%5B%5D=&s_tag=A5QERr0C",
            "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=16&search_by_map=true&sw_lat=27.76204503101316&sw_lng=-15.579093039278227&ne_lat=27.78101522450737&ne_lng=-15.562578599728518&allow_override%5B%5D=&s_tag=ZaXKDGBp",
            # - San Fernando
            "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=16&search_by_map=true&sw_lat=27.760296491712925&sw_lng=-15.595460576086047&ne_lat=27.77926701416203&ne_lng=-15.578946136536338&allow_override%5B%5D=&s_tag=vk0HBWXg",
            # - Maspalomas
            "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=17&search_by_map=true&sw_lat=27.75490976165389&sw_lng=-15.588659733970214&ne_lat=27.764395980665903&ne_lng=-15.58040251419536&allow_override%5B%5D=&s_tag=iMz6quvU",
            "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=17&search_by_map=true&sw_lat=27.76108905427124&sw_lng=-15.597292138728019&ne_lat=27.770574692150365&ne_lng=-15.589034918953164&allow_override%5B%5D=&s_tag=L4y1a4mr",
            "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=17&search_by_map=true&sw_lat=27.756636301439524&sw_lng=-15.604587747248527&ne_lat=27.7661223580907&ne_lng=-15.596330527473672&allow_override%5B%5D=&s_tag=ObRE7aVQ",
            "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=17&search_by_map=true&sw_lat=27.75105566717079&sw_lng=-15.596694437176918&ne_lat=27.76054224858166&ne_lng=-15.588437217402063&allow_override%5B%5D=&s_tag=W3kEEPYK",
            "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=16&search_by_map=true&sw_lat=27.74151065896432&sw_lng=-15.596353302298944&ne_lat=27.76048471441323&ne_lng=-15.579838862749234&allow_override%5B%5D=&s_tag=2OcMoH7b",
            # - Sonnerland
            "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=16&search_by_map=true&sw_lat=27.74568867955053&sw_lng=-15.612012094755919&ne_lat=27.764661949440885&ne_lng=-15.59549765520621&allow_override%5B%5D=&s_tag=aWaSO_Ay",
            # - Meloneras
            "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=16&search_by_map=true&sw_lat=27.736895659079423&sw_lng=-15.604503037832778&ne_lat=27.755870582121982&ne_lng=-15.587988598283069&allow_override%5B%5D=&s_tag=HRc95TyY",
            # - Costa Meloneras y Pasito Blanco
            "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=16&search_by_map=true&sw_lat=27.736477830510076&sw_lng=-15.616174883147032&ne_lat=27.75545283209546&ne_lng=-15.599660443597323&allow_override%5B%5D=&s_tag=mO0wpVvu",
            "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=15&search_by_map=true&sw_lat=27.727090583905348&sw_lng=-15.634281174424574&ne_lat=27.76504050806059&ne_lng=-15.601252295325152&allow_override%5B%5D=&s_tag=QZFP7kjr",
            # - El Tablero - Montaña la Data
            "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=15&search_by_map=true&sw_lat=27.762603561112517&sw_lng=-15.625569359544203&ne_lat=27.80054012730241&ne_lng=-15.59254048044478&allow_override%5B%5D=&s_tag=gdlMfvXN",
            # - Ayagures - Arteara
            "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=14&search_by_map=true&sw_lat=27.802583216066537&sw_lng=-15.628036807960004&ne_lat=27.878411771839488&ne_lng=-15.56197904976116&allow_override%5B%5D=&s_tag=b1631OCJ",
            # San Bartolomé y Santa Lucía
            "https://www.airbnb.es/s/Cruce-de-Arinaga/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Cruce%20de%20Arinaga&map_toggle=true&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=27.85030733647081&sw_lng=-15.589910718482038&ne_lat=27.96860190702207&ne_lng=-15.48559093410568&s_tag=bWtdf2xX",
            # Santa Lucía Tirajana
            # - Arinaga
            "https://www.airbnb.es/s/Arinaga--Playa-de-Arinaga/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Arinaga%2C%20Playa%20de%20Arinaga&place_id=ChIJSYxAwsKhQAwR-g9FlPdpyFI&map_toggle=true&allow_override%5B%5D=&s_tag=PhKz7hH-",
            # - Sardina
            "https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Vecindario%2C%20Gran%20Canaria%2C%20Spagna&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=27.837314814913807&sw_lng=-15.473324213922284&ne_lat=27.86690591527811&ne_lng=-15.447244267828195&s_tag=ukTIxcD2",
            # - Cruce de Arinaga
            "https://www.airbnb.es/s/Cruce-de-Arinaga/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Cruce%20de%20Arinaga&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=27.841591374969102&sw_lng=-15.449075141894784&ne_lat=27.900761976512182&ne_lng=-15.396915249706606&s_tag=9Xp8zkU-",
            # - Vecindario
            "https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Vecindario%2C%20Gran%20Canaria%2C%20Spagna&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=27.825511877387378&sw_lng=-15.458861742913983&ne_lat=27.85510652442225&ne_lng=-15.432781796819894&s_tag=AJLTjT6T",
            # - Castillo de Romeral
            "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=14&search_by_map=true&sw_lat=27.76732183621934&sw_lng=-15.497821712959169&ne_lat=27.843176965743343&ne_lng=-15.431763954760324&allow_override%5B%5D=&s_tag=FzcxDqIw",
            # Mogán
            "https://www.airbnb.es/s/Mog%C3%A1n--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=Mog%C3%A1n%2C%20Las%20Palmas&place_id=ChIJ21QCFCyBQAwRoBNNvvNAAwQ&map_toggle=true&allow_override%5B%5D=&s_tag=Abr2TN0h",
            "https://www.airbnb.es/s/mogan--Gran-Canaria--Mog%C3%A1n--Spain/homes?refinement_paths%5B%5D=%2Fhomes&query=mogan%2C%20Gran%20Canaria%2C%20Mog%C3%A1n%2C%20Spain&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=27.846710858503627&sw_lng=-15.755023879099415&ne_lat=27.922506115101164&ne_lng=-15.68896612090057&s_tag=lgNQFRrt",
            # - Puerto Rico
            "https://www.airbnb.es/s/Puerto-mogan--Gran-Canaria--Lomoquiebre--Lomo-Quiebre--Spanien/homes?refinement_paths%5B%5D=%2Fhomes&query=Puerto%20mogan%2C%20Gran%20Canaria%2C%20Lomoquiebre%2C%20Lomo%20Quiebre%2C%20Spanien&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=27.795800383889734&sw_lng=-15.735810550783462&ne_lat=27.81476422321165&ne_lng=-15.719296111233753&s_tag=lhoCx0Cf",
            "https://www.airbnb.es/s/Puerto-mogan--Gran-Canaria--Lomoquiebre--Lomo-Quiebre--Spanien/homes?refinement_paths%5B%5D=%2Fhomes&query=Puerto%20mogan%2C%20Gran%20Canaria%2C%20Lomoquiebre%2C%20Lomo%20Quiebre%2C%20Spanien&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=27.78710632861439&sw_lng=-15.724201950167007&ne_lat=27.806071805200972&ne_lng=-15.707687510617298&s_tag=1zJYKk_a",
            "https://www.airbnb.es/s/Puerto-mogan--Gran-Canaria--Lomoquiebre--Lomo-Quiebre--Spanien/homes?refinement_paths%5B%5D=%2Fhomes&query=Puerto%20mogan%2C%20Gran%20Canaria%2C%20Lomoquiebre%2C%20Lomo%20Quiebre%2C%20Spanien&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=27.775772640816562&sw_lng=-15.71237877282936&ne_lat=27.79474025105609&ne_lng=-15.695864333279651&s_tag=Y_rLZ_Sb"
            # - Los caideros
            "https://www.airbnb.es/s/Los-Caideros--Las-Palmas--Spania/homes?refinement_paths%5B%5D=%2Fhomes&query=Los%20Caideros%2C%20Las%20Palmas%2C%20Spania&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=27.767834139976156&sw_lng=-15.705778050463373&ne_lat=27.78680324422201&ne_lng=-15.689263610913663&s_tag=Zz0Ruc5Z",
            # - Arguineguín
            "https://www.airbnb.es/s/Arguineguin--Las-Palmas--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Arguineguin%2C%20Las%20Palmas%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=27.743795545672736&sw_lng=-15.690116338841664&ne_lat=27.781739188328302&ne_lng=-15.657087459742241&s_tag=vUz_e5VP",
            # - Tasarte - Casas Blancas
            "https://www.airbnb.es/s/Arguineguin--Las-Palmas--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Arguineguin%2C%20Las%20Palmas%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=27.893823334975455&sw_lng=-15.80116452119032&ne_lat=27.969582986516773&ne_lng=-15.735106762991474&s_tag=ia-abicb",
            # - Puerto Mogán - Taurito
            "https://www.airbnb.es/s/Puerto-mogan--Gran-Canaria--Lomoquiebre--Lomo-Quiebre--Spanien/homes?refinement_paths%5B%5D=%2Fhomes&query=Puerto%20mogan%2C%20Gran%20Canaria%2C%20Lomoquiebre%2C%20Lomo%20Quiebre%2C%20Spanien&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=27.80605608477467&sw_lng=-15.772561027575863&ne_lat=27.8439762852101&ne_lng=-15.73953214847644&s_tag=fODyMZUS",
            # Santa Brígida
            "https://www.airbnb.es/s/Santa-Br%C3%ADgida--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=Santa%20Br%C3%ADgida%2C%20Las%20Palmas&place_id=ChIJDUxGV86WQAwRMBRNvvNAAwQ&map_toggle=true&allow_override%5B%5D=&s_tag=XR6sOzus",
            # Artenara
            "https://www.airbnb.es/s/Artenara--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=Artenara%2C%20Las%20Palmas&place_id=ChIJaWQNmTWJQAwRMBNNvvNAAwQ&allow_override%5B%5D=&s_tag=c6AnBFwh",
            # Tejeda
            "https://www.airbnb.es/s/Tejeda--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=Tejeda%2C%20Las%20Palmas&place_id=ChIJi3GUBWaPQAwRcBRNvvNAAwQ&allow_override%5B%5D=&s_tag=rWc-3odn",
            # Moya
            "https://www.airbnb.es/s/Moya--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=Moya%2C%20Las%20Palmas&place_id=ChIJhc4WuHaSQAwRsBNNvvNAAwQ&allow_override%5B%5D=&s_tag=2RfnDMWD",
            # San Mateo
            "https://www.airbnb.es/s/San-Mateo--Vega-de-San-Mateo--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=San%20Mateo%2C%20Vega%20de%20San%20Mateo%2C%20Espa%C3%B1a&place_id=ChIJb7DwmOOQQAwR4_IRfBwwjGc&allow_override%5B%5D=&s_tag=Tpyg_olO",
            # Valsequillo
            "https://www.airbnb.es/s/Valsequillo-de-Gran-Canaria--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=Valsequillo%20de%20Gran%20Canaria%2C%20Las%20Palmas&place_id=ChIJ2SLlma2QQAwR0BRNvvNAAwQ&allow_override%5B%5D=&s_tag=380yajmk",
            # Firgas
            "https://www.airbnb.es/s/Firgas--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=Firgas%2C%20Las%20Palmas&place_id=ChIJmal1WVqSQAwR_qTY6bck_ss&allow_override%5B%5D=&s_tag=R5PCRjmo",
        ],
        'La Palma' : [
            # S/C La Palma
            # - S/C
            "https://www.airbnb.es/s/Santa-Cruz-de-la-Palma--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Santa%20Cruz%20de%20la%20Palma%2C%20Espa%C3%B1a&place_id=ChIJEcBHIqruawwRbVPCS4_tXXM&map_toggle=true&allow_override%5B%5D=&s_tag=8FJR0oyZ",
            "https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=Santa%20Cruz%20de%20la%20Palma%2C%20Espa%C3%B1a&place_id=ChIJEcBHIqruawwRbVPCS4_tXXM&allow_override%5B%5D=&s_tag=kmmQJQX6",
            "https://www.airbnb.es/s/Santa-Cruz-de-la-Palma--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=Santa%20Cruz%20de%20la%20Palma%2C%20Santa%20Cruz%20de%20Tenerife&place_id=ChIJ4dcyMAHsawwRbPZTyGcKgwI&allow_override%5B%5D=&s_tag=38aAmgyQ",
            # - Las Nieves
            "https://www.airbnb.es/s/Las-Nieves--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Las%20Nieves%2C%20Espa%C3%B1a&place_id=ChIJLS2_ZKPuawwRxbOGDxDKDHk&map_toggle=true&allow_override%5B%5D=&s_tag=Te3l1dxZ",
            # - Buenavista arriba
            "https://www.airbnb.es/s/Calle-Buenavista-Arriba--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Calle%20Buenavista%20Arriba%2C%20Espa%C3%B1a&place_id=EiBDYWxsZSBCdWVuYXZpc3RhIEFycmliYSwgRXNwYcOxYSIuKiwKFAoSCckG7fUZ7GsMEUPWDRBncn0NEhQKEgm1wBQKQuxrDBHgOqnQCkWC-w&allow_override%5B%5D=&s_tag=-ynoJDO6",
            # - Buenavista abajo
            "https://www.airbnb.es/s/Buenavista-de-Abajo--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Buenavista%20de%20Abajo%2C%20Espa%C3%B1a&place_id=ChIJY2iSGxfsawwRj1c9y-khkUI&map_toggle=true&allow_override%5B%5D=&s_tag=Gs1bX8Rj",
            # Breña Alta
            "https://www.airbnb.es/s/Bre%C3%B1a-Alta--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=Bre%C3%B1a%20Alta%2C%20Santa%20Cruz%20de%20Tenerife&place_id=ChIJtcAUCkLsawwR4Dqp0ApFgvs&map_toggle=true&allow_override%5B%5D=&s_tag=PQCuEUYV",
            # Breña Baja
            # - Breña Baja
            "https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=Bre%C3%B1a%20Alta%2C%20Santa%20Cruz%20de%20Tenerife&place_id=ChIJtcAUCkLsawwR4Dqp0ApFgvs&allow_override%5B%5D=&s_tag=1LEWgTAs",
            "https://www.airbnb.es/s/Bre%C3%B1a-Baja/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=Bre%C3%B1a%20Baja&place_id=ChIJbZQ9LHzsawwRyADhQuvo_js&map_toggle=true&allow_override%5B%5D=&s_tag=SkivkJPV",
            # - Los Cancajos
            "https://www.airbnb.es/s/Bre%C3%B1a-Baja--Los-Cancajos/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=Bre%C3%B1a%20Baja%2C%20Los%20Cancajos&place_id=ChIJaxPrRIHrawwR7_kN63GdtTA&map_toggle=true&allow_override%5B%5D=&s_tag=f3tdo1bT"
            # - La Polvacera
            "https://www.airbnb.es/s/La-Polvacera--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=La%20Polvacera%2C%20Espa%C3%B1a&place_id=ChIJJ1fjd4PsawwRgOKsKsadAq0&map_toggle=true&allow_override%5B%5D=&s_tag=XTdykirc"
            # Los Llanos
            # - Los Llanos 
            "https://www.airbnb.es/s/Los-Llanos-de-Aridane--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=Los%20Llanos%20de%20Aridane%2C%20Santa%20Cruz%20de%20Tenerife&place_id=ChIJF_CHhTXyawwRozp80m3jG4c&map_toggle=true&allow_override%5B%5D=&s_tag=Yu_LzQsV",
            "https://www.airbnb.es/s/Los-Llanos-de-Aridane/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=Los%20Llanos%20de%20Aridane&place_id=ChIJZX2xJM7zawwRU0WnUOVinWQ&allow_override%5B%5D=&s_tag=GfDsexwO",
            # - Puerto Naos
            "https://www.airbnb.es/s/Puerto-Naos--La-Palma--Puerto-de-Naos--Spanien/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=Puerto%20Naos%2C%20La%20Palma%2C%20Puerto%20de%20Naos%2C%20Spanien&place_id=ChIJAZ0RcCnzawwRnsyDoXKJmUI&map_toggle=true&allow_override%5B%5D=&s_tag=H3y95fBE",
            "https://www.airbnb.es/s/Los-Llanos-de-Aridane--Puerto-Naos--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=Los%20Llanos%20de%20Aridane%2C%20Puerto%20Naos%2C%20Espa%C3%B1a&place_id=ChIJvS70wSjzawwR4MfPdPZAAwo&map_toggle=true&allow_override%5B%5D=&s_tag=W0rBXc9S",
            # - Todoque
            "https://www.airbnb.es/s/Todoque--Los-Llanos--Spanien/all?refinement_paths%5B%5D=%2Ffor_you&adults=0&children=0&infants=0&toddlers=0&query=Todoque%2C%20Los%20Llanos%2C%20Spanien&place_id=ChIJRxnLXvzyawwRUdmHc_4zj8U",
            # - Triana
            "https://www.airbnb.es/s/Triana--Los-Llanos--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=Triana%2C%20Los%20Llanos%2C%20Espa%C3%B1a&place_id=ChIJ1WT7kcvzawwR83gZ6w6ZEK4&map_toggle=true&allow_override%5B%5D=&s_tag=t_8V6pKG"
            # Tazacorte
            "https://www.airbnb.es/s/Tazacorte--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&map_toggle=true&query=Tazacorte%2C%20Santa%20Cruz%20de%20Tenerife&place_id=ChIJuTPL55fzawwRL4A4KlWC0rc&allow_override%5B%5D=&s_tag=NpDjndKP",
            "https://www.airbnb.es/s/Tazacorte--Puerto--Spanien/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=Tazacorte%2C%20Puerto%2C%20Spanien&place_id=ChIJZUR79vrzawwRrV_3mlUbM28&allow_override%5B%5D=&s_tag=D8HWGIh0"
            # Fuencaliente
            "https://www.airbnb.es/s/Fuencaliente-de-la-Palma--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=Fuencaliente%20de%20la%20Palma%2C%20Santa%20Cruz%20de%20Tenerife&place_id=ChIJH46lEBqSawwRUDBNvvNAAwQ&map_toggle=true&allow_override%5B%5D=&s_tag=8ZLVrluQ",
            # Tijarafe
            "https://www.airbnb.es/s/Tijarafe--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&query=Tijarafe%2C%20Santa%20Cruz%20de%20Tenerife&place_id=ChIJ_eAhHi_xawwRYDJNvvNAAwQ&allow_override%5B%5D=&s_tag=qU8p1u79",
            # Puntagorda
            "https://www.airbnb.es/s/Puntagorda--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&query=Puntagorda%2C%20Santa%20Cruz%20de%20Tenerife&place_id=ChIJ2WoS-8f5awwRPILdmgIY5dA&allow_override%5B%5D=&s_tag=ybwZLnyB",
            # Garafía
            "https://www.airbnb.es/s/Garaf%C3%ADa--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&query=Garaf%C3%ADa%2C%20Santa%20Cruz%20de%20Tenerife&place_id=ChIJ_Uzkaa37awwRcDBNvvNAAwQ&allow_override%5B%5D=&s_tag=cJBTx_oj",
            # Barlovento
            "https://www.airbnb.es/s/Barlovento--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&query=Barlovento%2C%20Santa%20Cruz%20de%20Tenerife&place_id=ChIJB8qU5FDkawwRRbI8nfSZDK8&allow_override%5B%5D=&s_tag=gyh6634p",
            #San Andrés y Sauces
            "https://www.airbnb.es/s/San-Andr%C3%A9s-y-Sauces--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&query=San%20Andr%C3%A9s%20y%20Sauces%2C%20Santa%20Cruz%20de%20Tenerife&place_id=ChIJ5eM9tIXlawwRgDFNvvNAAwQ&allow_override%5B%5D=&s_tag=EGcHs8rY",
            # El Paso
            "https://www.airbnb.es/s/El-Paso--La-Palma--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=El%20Paso%2C%20La%20Palma%2C%20Santa%20Cruz%20de%20Tenerife&place_id=ChIJWzaeahHyawwRIDFNvvNAAwQ&map_toggle=true&allow_override%5B%5D=&s_tag=8Ol9QCG5",
            # Villa de Mazo
            "https://www.airbnb.es/s/Villa-de-Mazo--Santa-Cruz-de-Tenerife--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Villa%20de%20Mazo%2C%20Santa%20Cruz%20de%20Tenerife%2C%20Espa%C3%B1a&place_id=ChIJ14WrlKjsawwRLHFr6MTvX7o&allow_override%5B%5D=&s_tag=J_VGpt0u",
            # Puntallana
            "https://www.airbnb.es/s/Puntallana--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&query=Puntallana%2C%20Santa%20Cruz%20de%20Tenerife&place_id=ChIJc1sbwSbpawwRLEOwdIEbPtU&allow_override%5B%5D=&s_tag=yXNFPeCi",
        ],
        'El Hierro' : [
            "https://www.airbnb.es/s/El-Hierro--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&query=El%20Hierro%2C%20Santa%20Cruz%20de%20Tenerife&place_id=ChIJYZqqMcpYawwRgUq_IX0pFz4&allow_override%5B%5D=&map_toggle=true&s_tag=YDr20vn2",
        ],
        'La Gomera' : [
            # San Sebastián
            "https://www.airbnb.es/s/San-Sebasti%C3%A1n-de-La-Gomera/homes?refinement_paths%5B%5D=%2Fhomes&query=San%20Sebasti%C3%A1n%20de%20La%20Gomera&place_id=ChIJl3Yqk3flagwRSTHtquTgCdU&allow_override%5B%5D=&s_tag=ddjkdmBI",
            # Agulo
            "https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=Agulo&is_user_submitted_query=true&allow_override%5B%5D=&map_toggle=true&s_tag=GUlHODI3",
            # Alajeró
            "https://www.airbnb.es/s/Alajer%C3%B3/homes?refinement_paths%5B%5D=%2Fhomes&query=Alajer%C3%B3&place_id=ChIJnxl_37PjagwRZFsNDmqFSYQ&allow_override%5B%5D=&s_tag=97UWC7TP",
            # Hermigua
            "https://www.airbnb.es/s/Hermigua--Santa-Cruz-de-Tenerife/all?refinement_paths%5B%5D=%2Ffor_you&query=Hermigua%2C%20Santa%20Cruz%20de%20Tenerife&place_id=ChIJO3r0mVn7agwRwDBNvvNAAwQ",
            # Valle Gran Rey
            "https://www.airbnb.es/s/Valle-Gran-Rey--La-Gomera--Spanien/homes?refinement_paths%5B%5D=%2Fhomes&query=Valle%20Gran%20Rey%2C%20La%20Gomera%2C%20Spanien&place_id=ChIJ3fabU0AdawwRqOCm30D5HFk&allow_override%5B%5D=&s_tag=tGB-psaZ",
            # Vallehermoso
            "https://www.airbnb.es/s/Alajer%C3%B3/homes?refinement_paths%5B%5D=%2Fhomes&query=Alajer%C3%B3&place_id=ChIJnxl_37PjagwRZFsNDmqFSYQ&allow_override%5B%5D=&s_tag=97UWC7TP",
        ],
        'Lanzarote' : [
            #Tías
            # - Puerto del Carmen
            "https://www.airbnb.es/s/Puerto-del-Carmen/homes?refinement_paths%5B%5D=%2Fhomes&query=Puerto%20del%20Carmen&place_id=ChIJswVYlpUlRgwRvmEXSirwP3I&map_toggle=true&allow_override%5B%5D=&s_tag=s7_JGVNR",
            "https://www.airbnb.es/s/Puerto-del-carmen--T%C3%ADas--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Puerto%20del%20carmen%2C%20T%C3%ADas%2C%20Espa%C3%B1a&place_id=ChIJq6qqquclRgwR6hx2zWRRbdc&map_toggle=true&allow_override%5B%5D=&s_tag=qr0zG3M_",
            # - Tías
            "https://www.airbnb.es/s/Tias--Lanzarote--T%C3%ADas--Spanien/homes?refinement_paths%5B%5D=%2Fhomes&query=Tias%2C%20Lanzarote%2C%20T%C3%ADas%2C%20Spanien&place_id=ChIJJT9WJeklRgwRWuu7CgfKoqE&allow_override%5B%5D=&s_tag=zEpqq8Un",
            "https://www.airbnb.es/s/T%C3%ADas--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=T%C3%ADas%2C%20Las%20Palmas&place_id=ChIJxa3PyTIkRgwRRrtXXJxBigc&allow_override%5B%5D=&s_tag=ynDpnXuM",
            "https://www.airbnb.es/s/T%C3%ADas--Spain/homes?refinement_paths%5B%5D=%2Fhomes&query=T%C3%ADas%2C%20Spain&place_id=ChIJvxJ8PzEkRgwRqIyHmLAemuo&allow_override%5B%5D=&s_tag=9Khj54Hp",
            #Yaiza
            # - Yaiza
            "https://www.airbnb.es/s/Yaiza--Spain/homes?refinement_paths%5B%5D=%2Fhomes&query=Yaiza%2C%20Spain&place_id=ChIJk3arBgw7RgwRRx6fPURa1XI&map_toggle=true&allow_override%5B%5D=&s_tag=4qqNuVoY",
            "https://www.airbnb.es/s/Yaiza--Lanzarote--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=Yaiza%2C%20Lanzarote%2C%20Las%20Palmas&place_id=ChIJt9tt_AU7RgwRtg8SuktKwO0&map_toggle=true&allow_override%5B%5D=&s_tag=c2ViiApm",
            # - Playa Blanca
            "https://www.airbnb.es/s/Yaiza-Playa-Blanca-Sl--Avenida-de-Papagayo--Playa-Blanca--Spain/homes?refinement_paths%5B%5D=%2Fhomes&query=Yaiza%20Playa%20Blanca%20Sl%2C%20Avenida%20de%20Papagayo%2C%20Playa%20Blanca%2C%20Spain&place_id=ChIJY7eMw0k3RgwRX5MirsvW6HM&map_toggle=true&allow_override%5B%5D=&s_tag=wk6Pg_AP",
            "https://www.airbnb.es/s/Yaiza--Playa-Blanca/homes?refinement_paths%5B%5D=%2Fhomes&query=Yaiza%2C%20Playa%20Blanca&place_id=ChIJCX-kHUY3RgwRgDDZzodRc0c&map_toggle=true&allow_override%5B%5D=&s_tag=c5v7_XjH&section_offset=7&items_offset=288",
            # - Papagayo
            "https://www.airbnb.es/s/Papagayo--Lanzarote--Province-de-Las-Palmas--Espagne/homes?refinement_paths%5B%5D=%2Fhomes&query=Papagayo%2C%20Lanzarote%2C%20Province%20de%20Las%20Palmas%2C%20Espagne&place_id=ChIJu4gHZJs3RgwRm-4uOFDvwr0&allow_override%5B%5D=&s_tag=kmV3LUG9"
            # - Montaña Roja
            "https://www.airbnb.es/s/Monta%C3%B1a-Roja--Spain/homes?refinement_paths%5B%5D=%2Fhomes&query=Monta%C3%B1a%20Roja%2C%20Spain&place_id=ChIJkeBtAJ03RgwRYJq4mXDTvVg&map_toggle=true&allow_override%5B%5D=&s_tag=UXREkMry"
            # - Femés
            "https://www.airbnb.es/s/Fem%C3%A9s/homes?refinement_paths%5B%5D=%2Fhomes&query=Fem%C3%A9s&place_id=ChIJWwp2o186RgwR0NHPdPZAAwo&map_toggle=true"
            # - Playa quemada
            "https://www.airbnb.es/s/Playa-Quemada/homes?refinement_paths%5B%5D=%2Fhomes&query=Playa%20Quemada&place_id=ChIJr2YHbbI6RgwRECBje00nX6k&allow_override%5B%5D=&s_tag=KC1zZGHI"
            # - El Golfo
            "https://www.airbnb.es/s/El-Golfo-Lanzarote--Avenida-Mar%C3%ADtima--El-Golfo/homes?refinement_paths%5B%5D=%2Fhomes&query=El%20Golfo%20Lanzarote%2C%20Avenida%20Mar%C3%ADtima%2C%20El%20Golfo&place_id=ChIJzRiBzK0-RgwRNPfMnDOk5b0&map_toggle=true&allow_override%5B%5D=&s_tag=vCA9cuLj"
            #Arrecife
            # - Arrecife
            "https://www.airbnb.es/s/Arrecife-LANZAROTE--Arrecife/homes?refinement_paths%5B%5D=%2Fhomes&query=Arrecife%20LANZAROTE%2C%20Arrecife&place_id=ChIJGf-tTWUnRgwR4qaER8eTee0&map_toggle=true&allow_override%5B%5D=&s_tag=QQC-MqN1",
            "https://www.airbnb.es/s/Arrecife--Lanzarote--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Arrecife%2C%20Lanzarote%2C%20Espa%C3%B1a&place_id=ChIJTSSL02MnRgwRg19TPfTimFE&allow_override%5B%5D=&s_tag=1megRxG3",
            "https://www.airbnb.es/s/Arrecife/homes?refinement_paths%5B%5D=%2Fhomes&query=Arrecife&place_id=ChIJV7qzxW8nRgwRxC6aWPbVxZM&allow_override%5B%5D=&s_tag=PD0oZyOW"
            # - Volcán de Tahiche
            "https://www.airbnb.es/s/Volcan-de-Tahiche--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Volcan%20de%20Tahiche%2C%20Espa%C3%B1a&place_id=ChIJEUDHmFgnRgwRi-Z9dRb1EJU&map_toggle=true&allow_override%5B%5D=&s_tag=csbevhkT"
            #San Bartolomé
            # - Playa Honda
            "https://www.airbnb.es/s/Playa-Honda--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=Playa%20Honda%2C%20Las%20Palmas&place_id=ChIJsQ-pnVMmRgwRQ5LR4FYH9-I&allow_override%5B%5D=&s_tag=hdo1VlgF",
            # - San Bartolome
            "https://www.airbnb.es/s/San-Bartolom%C3%A9--Lanzarote--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=San%20Bartolom%C3%A9%2C%20Lanzarote%2C%20Las%20Palmas&place_id=ChIJz8NQLUshRgwRIE1Fp65s-mc&allow_override%5B%5D=&s_tag=PzcQj8Yu",
            # - El Islote
            "https://www.airbnb.es/s/El-Islote--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=El%20Islote%2C%20Espa%C3%B1a&place_id=ChIJoalEvF8hRgwRhCbN6XtSNyI&map_toggle=true&allow_override%5B%5D=&s_tag=aaCS1Qpw",
            #Haria
            # - Haría
            "https://www.airbnb.es/s/Har%C3%ADa--Lanzarote--Las-Palmas--Spain/homes?refinement_paths%5B%5D=%2Fhomes&query=Har%C3%ADa%2C%20Lanzarote%2C%20Las%20Palmas%2C%20Spain&place_id=ChIJo0M4UlGgSAwRaf6H56a9-24&allow_override%5B%5D=&s_tag=6dydEVQt",
            # - Punta Mujeres
            "https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=Har%C3%ADa%2C%20Lanzarote%2C%20Punta%20Mujeres%2C%20Espa%C3%B1a&allow_override%5B%5D=&s_tag=51cg_ALe",
            # - Charco del Palo
            "https://www.airbnb.es/s/Charco-del-Palo/homes?refinement_paths%5B%5D=%2Fhomes&query=Charco%20del%20Palo&place_id=ChIJsQ0NWzWfSAwRVLaYOt_WThQ&map_toggle=true&allow_override%5B%5D=&s_tag=cdInC-Om",
            # - Orzola
            "https://www.airbnb.es/s/Orzola--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Orzola%2C%20Espa%C3%B1a&place_id=ChIJuz4CBiCkSAwRoKzPdPZAAwo&map_toggle=true&allow_override%5B%5D=&s_tag=FWOEOFbq",
            # - Los Valles
            "https://www.airbnb.es/s/Los-Valles--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Los%20Valles%2C%20Espa%C3%B1a&place_id=ChIJQTX3E-6fSAwR5Ta4vg6lEBA&map_toggle=true&allow_override%5B%5D=&s_tag=iRo7mMA7",
            #La Graciosa
            "https://www.airbnb.es/s/La-Graciosa--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=La%20Graciosa%2C%20Las%20Palmas&place_id=ChIJhabBGwunSAwRlbY2WanmXHM&allow_override%5B%5D=&s_tag=JpVmO4WS",
            #Tinajo
            # - Tinajo
            "https://www.airbnb.es/s/Tinajo/homes?refinement_paths%5B%5D=%2Fhomes&query=Tinajo&place_id=ChIJybS9RGYiRgwRU5Hlo61Y-1U&allow_override%5B%5D=&s_tag=iOnLmTgv",
            "https://www.airbnb.es/s/Tinajo--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=Tinajo%2C%20Las%20Palmas&place_id=ChIJ430vAGgiRgwRAgQgpR4F8LA&map_toggle=true&allow_override%5B%5D=&s_tag=WaN0WPJV",
            # - La Santa
            "https://www.airbnb.es/s/Tinajo--La-Santa/homes?refinement_paths%5B%5D=%2Fhomes&query=Tinajo%2C%20La%20Santa&place_id=ChIJ73uRUpMYRgwR4FP2PhwYoLk&allow_override%5B%5D=&s_tag=9JN36_b9",
            # - Tajaste
            "https://www.airbnb.es/s/Tajaste--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Tajaste%2C%20Espa%C3%B1a&place_id=ChIJM3TZqFgiRgwR-GMVeVKPnZ4&map_toggle=true&allow_override%5B%5D=&s_tag=kTD7V5ug"
            #Teguise
            # - Famara
            "https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=Famara&allow_override%5B%5D=&s_tag=WsqmuV2y",
            # - Teguise
            "https://www.airbnb.es/s/Teguise----Lanzarote--Calle-San-Miguel--Teguise--Spain/homes?refinement_paths%5B%5D=%2Fhomes&query=Teguise%20%2C%20Lanzarote%2C%20Calle%20San%20Miguel%2C%20Teguise%2C%20Spain&place_id=ChIJo1QixmUgRgwRrHuFec7gcmA&map_toggle=true&allow_override%5B%5D=&s_tag=zt1kBzon"
            # - Costa Teguise
            "https://www.airbnb.es/s/Costa-Teguise/homes?refinement_paths%5B%5D=%2Fhomes&query=Costa%20Teguise&place_id=ChIJMUHIODKcSAwRQGjPdPZAAwo&map_toggle=true&allow_override%5B%5D=&s_tag=VD2EJH6T",
            # - Las Caletas
            "https://www.airbnb.es/s/Las-Caletas--Spain/homes?refinement_paths%5B%5D=%2Fhomes&query=Las%20Caletas%2C%20Spain&place_id=ChIJ6VTkPbmdSAwRgQsFUrC7S88&map_toggle=true&allow_override%5B%5D=&s_tag=1DCwyMRw",
            # - Los Ancones
            "https://www.airbnb.es/s/Los-Ancones--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Los%20Ancones%2C%20Espa%C3%B1a&place_id=ChIJpe2Z3aGeSAwRJA0Rylh4ULc&map_toggle=true&allow_override%5B%5D=&s_tag=aH0gxou0",
        ],
        'Fuerteventura' : [
            "https://www.airbnb.es/s/Fuerteventura--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJgQ_Cr3OkRwwRI3-1tRMcxyo&query=Fuerteventura%2C%20Las%20Palmas&allow_override%5B%5D=&s_tag=0fn5-6DG"
            "https://www.airbnb.es/s/COSTA-CALMA--P%C3%A1jara--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJAQAAAPCbRwwR47xhAJraNE0&query=COSTA%20CALMA%2C%20P%C3%A1jara%2C%20Espa%C3%B1a&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=kIWvGUxb",
            # La Oliva
            # - La Oliva
            "https://www.airbnb.es/s/La-Oliva--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=La%20Oliva%2C%20Las%20Palmas&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&ne_lat=28.781945916027258&ne_lng=-13.733527842439116&sw_lat=28.374168287219444&sw_lng=-14.080283823884429&zoom=11&search_by_map=true&s_tag=TA-yLyvt",
            # - Lajares
            "https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Lajares%2C%20Fuerteventura%2C%20Calle%20la%20Cancela%2C%20La%20Oliva%2C%20Spain&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.654296856998357&sw_lng=-13.963646385303125&ne_lat=28.712972171106365&ne_lng=-13.911486493114946&s_tag=PSQ8Elt_",
            # - El Cotillo
            "https://www.airbnb.es/s/El-Cotillo-Beach--La-Oliva--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJn_SzJlizRwwRnlqslkb2yH4&query=El%20Cotillo%20Beach%2C%20La%20Oliva%2C%20Espa%C3%B1a&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=M7KQuUYM",
            # - Corralejo
            "https://www.airbnb.es/s/Corralejo--Las-Palmas--Corralejo--Spanien/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJ2daP6eM0RgwRdZXnYcB3rvw&query=Corralejo%2C%20Las%20Palmas%2C%20Corralejo%2C%20Spanien&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&allow_override%5B%5D=&s_tag=B97N61wU",
            "https://www.airbnb.es/s/Corralejo--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Corralejo%2C%20Espa%C3%B1a&place_id=ChIJj3I0rOM0RgwRR4k9qASVfgc&map_toggle=true&allow_override%5B%5D=&s_tag=U99_zUim",
            "https://www.airbnb.es/s/corralejo--La-Oliva/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=corralejo%2C%20La%20Oliva&place_id=ChIJAQAAADA1RgwR8pU5ydolkTw&map_toggle=true&allow_override%5B%5D=&s_tag=tMELjg30",
            "https://www.airbnb.es/s/Corralejo--Las-Palmas--Corralejo--Spanien/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Corralejo%2C%20Las%20Palmas%2C%20Corralejo%2C%20Spanien&place_id=ChIJ2daP6eM0RgwRdZXnYcB3rvw&map_toggle=true&allow_override%5B%5D=&s_tag=4EyaIzNk"
            # - Majanicho
            "https://www.airbnb.es/s/Majanicho/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=Majanicho&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.69108570219361&sw_lng=-13.958075734668316&ne_lat=28.749738287713274&ne_lng=-13.905915842480137&s_tag=XKcilzTB",
            "https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=Majanicho&allow_override%5B%5D=&s_tag=RqaJbSfp",
            # Puerto del Rosario
            # - Puerto del Rosario
            "https://www.airbnb.es/s/Puerto-del-Rosario--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJbQDwZyy4RwwR8BNNvvNAAwQ&query=Puerto%20del%20Rosario%2C%20Las%20Palmas&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&allow_override%5B%5D=&s_tag=nHwc6liq",
            "https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=Puerto%20del%20Rosario%2C%20Las%20Palmas&place_id=ChIJbQDwZyy4RwwR8BNNvvNAAwQ&allow_override%5B%5D=&s_tag=VFP3zBAG",
            "https://www.airbnb.es/s/Puerto-del-Rosario--Fuerteventura--Los-Estancos--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=Puerto%20del%20Rosario%2C%20Fuerteventura%2C%20Los%20Estancos%2C%20Espa%C3%B1a&place_id=ChIJgwAT2h3IRwwREyQzimpWVaE&allow_override%5B%5D=&s_tag=gQ8ZUtex",
            # - Tetir
            "https://www.airbnb.es/s/Tetir--Puerto-del-Rosario/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Tetir%2C%20Puerto%20del%20Rosario&allow_override%5B%5D=&map_toggle=true&zoom=13&search_by_map=true&sw_lat=28.476771279105154&sw_lng=-13.984618892188173&ne_lat=28.594303856052118&ne_lng=-13.880299107811815&s_tag=UyuLBpGn",
            # - Teífa
            "https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=Te%C3%ADfa%20Fuerteventura&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=MGjMyB-c",
            # - El Matorral
            "https://www.airbnb.es/s/El-Matorral--Puerto-del-Rosario/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=El%20Matorral%2C%20Puerto%20del%20Rosario&place_id=Eh9FbCBNYXRvcnJhbCwgUHVlcnRvIGRlbCBSb3Nhcmlv&map_toggle=true&allow_override%5B%5D=&s_tag=k-sc5yI4",
            # - Castillo Caleta de Fuste
            "https://www.airbnb.es/s/Castillo-Caleta-de-Fuste/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Castillo%20Caleta%20de%20Fuste&place_id=ChIJowUIMR7BRwwR1CFGcqWf_aU&map_toggle=true&allow_override%5B%5D=&s_tag=TUHSbquY",
            # Pajara
            # - Pajara
            "https://www.airbnb.es/s/P%C3%A1jara--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJW7aK4CCeRwwR0BNNvvNAAwQ&query=P%C3%A1jara%2C%20Las%20Palmas&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=lBg70n0z",
            # - Ajuy
            "https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=ajuy%20fuerteventura&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&is_user_submitted_query=true&allow_override%5B%5D=&map_toggle=true&s_tag=6BT2BPH_",
            # La Lajita
            "https://www.airbnb.es/s/La-Lajita--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=La%20Lajita%2C%20Espa%C3%B1a&place_id=ChIJu988GLSbRwwRZSHfIzL2bJI&map_toggle=true&allow_override%5B%5D=&s_tag=JprDdTtn",
            # - Morro Jable
            "https://www.airbnb.es/s/Cofete/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Cofete&place_id=ChIJJ8Fr3qZwRwwRQ9B51Cp6-UE&allow_override%5B%5D=&map_toggle=true&s_tag=xYvh60-3",
            "https://www.airbnb.es/s/Morro-Jable/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJt2AGAwl5RwwRFdR28SwU6X0&query=Morro%20Jable&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=vpTJa7RO",
            # - Jandía
            "https://www.airbnb.es/s/Jand%C3%ADa--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJ7dMyziCeRwwRoL7TLC8P2G8&query=Jand%C3%ADa%2C%20Las%20Palmas&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&allow_override%5B%5D=&s_tag=eREYvjZj",
            # Bentacuria
            "https://www.airbnb.es/s/Betancuria--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJt3cGxDq7RwwRUBNNvvNAAwQ&query=Betancuria%2C%20Las%20Palmas&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=lr9wzhYD",
            # Antigua
            # - Antigua
            "https://www.airbnb.es/s/Antigua--Fuerteventura--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJJbEGZvu7RwwRuUYQC3VGftw&query=Antigua%2C%20Fuerteventura%2C%20Las%20Palmas&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=0TOCC4Ck",
            #Almacigo
            "https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=Almacigo%20Fuerteventura&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=YGaHzCZq",
            # - Salinas del Carmen
            "https://www.airbnb.es/s/COSTA-CALMA--P%C3%A1jara--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJAQAAAPCbRwwR47xhAJraNE0&query=COSTA%20CALMA%2C%20P%C3%A1jara%2C%20Espa%C3%B1a&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=kIWvGUxb",
            # - Pozo negro
            "https://www.airbnb.es/s/Pozo-Negro--Espagne/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=Pozo%20Negro%2C%20Espagne&place_id=ChIJM8SaWaHqRwwRskbKtp4OZ6w&allow_override%5B%5D=&s_tag=IUhJzWBI"
            # Tuineje
            # - Tuineje
            "https://www.airbnb.es/s/Tuineje--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJDWKIAkWWRwwRwBRNvvNAAwQ&query=Tuineje%2C%20Las%20Palmas&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=TAXBIYPr",
            # - Gran Tarajal
            "https://www.airbnb.es/s/Gran-Tarajal--Tuineje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=Gran%20Tarajal%2C%20Tuineje%2C%20Espa%C3%B1a&place_id=Eh5HcmFuIFRhcmFqYWwsIFR1aW5lamUsIEVzcGHDsWE&allow_override%5B%5D=&s_tag=3Bqs_iYd"
        ]
    }
    return urls[place]

def AtraveoURLs(place):
    urls= {
        'Puerto de la Cruz' : [
            "https://www.atraveo.es/puerto_de_la_cruz#eyJkYXRhIjp7ImNvdW50cnlJZCI6IkVTIiwicmVnaW9uSWQiOiIxNzUiLCJzdWJSZWdpb25JZCI6Ijg4MyIsImNpdHlJZCI6Ijk4MjciLCJkdXJhdGlvbiI6N30sImNvbmZpZyI6eyJwYWdlIjoiMCJ9fQ=="
        ],
        'Adeje' : [
            "https://www.atraveo.es/adeje#eyJkYXRhIjp7ImNvdW50cnlJZCI6IkVTIiwicmVnaW9uSWQiOiIxNzUiLCJzdWJSZWdpb25JZCI6Ijg5NSIsImNpdHlJZCI6IjczNDM3MiIsImR1cmF0aW9uIjo3fSwiY29uZmlnIjp7InBhZ2UiOiIwIn19",
            "https://www.atraveo.es/costa_adeje_%28costa_oeste_de_tenerife%29#eyJkYXRhIjp7ImNvdW50cnlJZCI6IkVTIiwicmVnaW9uSWQiOjE3NSwiY2l0eUlkIjo1ODQwNzQsImR1cmF0aW9uIjo3fSwiY29uZmlnIjp7fX0="
        ],
        'Gran Canaria' : [
            "https://www.atraveo.es/gran_canaria#eyJkYXRhIjp7ImNvdW50cnlJZCI6IkVTIiwicmVnaW9uSWQiOiIxNjMiLCJwcml2YXRlUG9vbCI6MX0sImNvbmZpZyI6eyJwYWdlIjoiMCJ9fQ==",
        ],
        'La Palma' : [
            "https://www.atraveo.es/la_palma#eyJkYXRhIjp7ImNvdW50cnlJZCI6IkVTIiwicmVnaW9uSWQiOiIxNjkiLCJwcml2YXRlUG9vbCI6MX0sImNvbmZpZyI6eyJwYWdlIjoiMCJ9fQ==",
        ],
        'El Hierro' : [
            "https://www.atraveo.es/el_hierro#eyJkYXRhIjp7ImNvdW50cnlJZCI6IkVTIiwicmVnaW9uSWQiOiIxNTgiLCJwcml2YXRlUG9vbCI6MX0sImNvbmZpZyI6eyJwYWdlIjoiMCJ9fQ==",
        ],
        'La Gomera' : [
            "https://www.atraveo.es/la_gomera#eyJkYXRhIjp7ImNvdW50cnlJZCI6IkVTIiwicmVnaW9uSWQiOiIxNjciLCJwcml2YXRlUG9vbCI6MX0sImNvbmZpZyI6eyJwYWdlIjoiMCJ9fQ==",
        ],
        'Lanzarote' : [
            "https://www.atraveo.es/lanzarote#eyJkYXRhIjp7ImNvdW50cnlJZCI6IkVTIiwicmVnaW9uSWQiOiIxNzAiLCJwcml2YXRlUG9vbCI6MX0sImNvbmZpZyI6eyJwYWdlIjoiMCJ9fQ==",
        ],
        'Fuerteventura' : [
            "https://www.atraveo.es/fuerteventura#eyJkYXRhIjp7ImNvdW50cnlJZCI6IkVTIiwicmVnaW9uSWQiOiIxNjEiLCJwcml2YXRlUG9vbCI6MX0sImNvbmZpZyI6eyJwYWdlIjoiMCJ9fQ==",
        ]
    }
    return urls[place]

def HomewayURLs(place):
    urls= {
        'Puerto de la Cruz' : [
            "https://www.homeaway.es/results/region:1976/@28.33705961045927,-16.61179916612673,28.48894858941568,-16.464631721897604,12z?petIncluded=false&ssr=true&legacyRegionPath=canarias&legacyRegionPath=puerto-de-la-cruz"
        ],
        'Adeje' : [
            "https://www.homeaway.es/search/keywords:Adeje,%20Canarias,%20Espa%C3%B1a"
        ],
        'Gran Canaria' : [
            # Las Palmas
            "https://www.homeaway.es/search/keywords:Las%20Palmas%20de%20Gran%20Canaria%2C%20Canarias%2C%20España/",
            # - Isleta
            "https://www.homeaway.es/search/keywords:Las%20Palmas%20de%20Gran%20Canaria%2C%20Canarias%2C%20Espa%C3%B1a/@28.14449631375144,-15.439403411249486,28.167662592933247,-15.408182498316137,15z?petIncluded=false&ssr=true&adultsCount=4",
            # - Santa Catalina
            "https://www.homeaway.es/search/keywords:Las%20Palmas%20de%20Gran%20Canaria%2C%20Canarias%2C%20Espa%C3%B1a/@28.133850658411266,-15.438298382178345,28.1454355760286,-15.42268792571167,16z?petIncluded=false&ssr=true&adultsCount=4",
            # - Mesa y Lopez
            "https://www.homeaway.es/search/keywords:Las%20Palmas%20de%20Gran%20Canaria%2C%20Canarias%2C%20Espa%C3%B1a/@28.125467700879998,-15.441645779028931,28.13705352487331,-15.426035322562257,16z?petIncluded=false&ssr=true&adultsCount=4",
            # - Guanarteme
            "https://www.homeaway.es/search/keywords:Las%20Palmas%20de%20Gran%20Canaria%2C%20Canarias%2C%20Espa%C3%B1a/@28.122909202369847,-15.4504734291163,28.134495302941872,-15.434862972649626,16z?petIncluded=false&ssr=true&adultsCount=4",
            # - Triana - Escaleritas
            "https://www.homeaway.es/search/keywords:Las%20Palmas%20de%20Gran%20Canaria%2C%20Canarias%2C%20Espa%C3%B1a/@28.101803965940068,-15.442140340132255,28.124979476308344,-15.410919427198905,15z?petIncluded=false&ssr=true&adultsCount=4",
            # - San Juan - Vegueta
            "https://www.homeaway.es/search/keywords:Las%20Palmas%20de%20Gran%20Canaria%2C%20Canarias%2C%20Espa%C3%B1a/@28.085751761458074,-15.438878773970146,28.108930739399653,-15.407657861036796,15z?petIncluded=false&ssr=true&adultsCount=4",
            # Tafira - San Cristobal
            "https://www.homeaway.es/search/keywords:Las%20Palmas%20de%20Gran%20Canaria%2C%20Canarias%2C%20Espa%C3%B1a/@28.042916494684203,-15.472170352262992,28.089287936524876,-15.409728526396293,14z?petIncluded=false&ssr=true&adultsCount=4",
            # Tamaraceite - Siete Palmas - Otros
            "https://www.homeaway.es/search/keywords:Las%20Palmas%20de%20Gran%20Canaria%2C%20Canarias%2C%20Espa%C3%B1a/@28.03290646684617,-15.54561996392681,28.12563796968533,-15.420736312193412,13z?petIncluded=false&ssr=true&adultsCount=4",
            # La Aldea
            "https://www.homeaway.es/search/keywords:La%20Aldea%20de%20San%20Nicol%C3%A1s%2C%20Canarias%2C%20Espa%C3%B1a/@27.878397002005652,-15.868897375737333,28.064046170921813,-15.619130072270536,12z?petIncluded=false&ssr=true&adultsCount=4",
            # Agaete
            "https://www.homeaway.es/search/keywords:Agaete%2C%20Canarias%2C%20España/",
            # Galdar
            "https://www.homeaway.es/search/keywords:Gáldar%2C%20Canarias%2C%20España/",
            # Santa María de Guía
            "https://www.homeaway.es/search/keywords:Santa%20María%20de%20Guía%20de%20Gran%20Canaria%2C%20Canarias%2C%20España/",
            # Valleseco
            "https://www.homeaway.es/search/keywords:Valleseco%2C%20Canarias%2C%20España/",
            # Teror
            "https://www.homeaway.es/search/keywords:Teror%2C%20Canarias%2C%20España/",
            # Firgas
            "https://www.homeaway.es/search/keywords:Firgas%2C%20Canarias%2C%20España/",
            # Telde
            "https://www.homeaway.es/search/keywords:Telde%2C%20Canarias%2C%20Espa%C3%B1a/arrival:2019-05-06/departure:2019-05-08?petIncluded=false&ssr=true&adultsCount=4",
            # Ingenio
            "https://www.homeaway.es/search/keywords:Ingenio%2C%20Canarias%2C%20España/",
            # Agüimes
            "https://www.homeaway.es/search/keywords:Agüimes%2C%20Canarias%2C%20España/",
            # San Bartolomé de Tirajana
            "https://www.homeaway.es/search/keywords:San%20Bartolomé%20de%20Tirajana%2C%20Canarias%2C%20España/",
            #   - Maspalomas
            "https://www.homeaway.es/search/keywords:Maspalomas%2C%20Canarias%2C%20España/",
            #   - Playa del Inglés
            "https://www.homeaway.es/search/keywords:Playa%20del%20Inglés%2C%20San%20Bartolomé%20de%20Tirajana%2C%20Canarias%2C%20España/",
            # Santa Lucía Tirajana
            "https://www.homeaway.es/search/keywords:Santa%20Lucía%2C%20Canarias%2C%20España/",
            # Mogán
            "https://www.homeaway.es/search/keywords:Mogán%2C%20Canarias%2C%20España/",
            # Santa Brígida
            "https://www.homeaway.es/search/keywords:Santa%20Brígida%2C%20Canarias%2C%20España/",
            # Artenara
            "https://www.homeaway.es/search/keywords:Artenara%2C%20Canarias%2C%20España/",
            # Tejeda
            "https://www.homeaway.es/search/keywords:Tejeda%2C%20Canarias%2C%20España/",
            # Moya
            "https://www.homeaway.es/search/keywords:Moya%2C%20Canarias%2C%20España/",
            # San Mateo
            "https://www.homeaway.es/search/keywords:Vega%20de%20San%20Mateo%2C%20Canarias%2C%20España/",
            # Valsequillo
            "https://www.homeaway.es/search/keywords:Valsequillo%20de%20Gran%20Canaria%2C%20Canarias%2C%20España/",
            # Arucas
            "https://www.homeaway.es/search/keywords:Arucas%2C%20Canarias%2C%20España/",
        ],
        'La Palma' : [
            "https://www.homeaway.es/search/keywords:La%20Palma%2C%20Canarias%2C%20Espa%C3%B1a",
            "https://www.homeaway.es/search/keywords:Santa%20Cruz%20de%20la%20Palma%2C%20Canarias%2C%20Espa%C3%B1a/@28.575786590144624,-18.030298895429382,28.760223068281125,-17.780531591962585,12z?petIncluded=false&ssr=true&adultsCount=4",
            "https://www.homeaway.es/search/keywords:Santa%20Cruz%20de%20la%20Palma%2C%20Canarias%2C%20Espa%C3%B1a/@28.5667411725275,-17.8390681215036,28.75119355457948,-17.589300818036804,12z?petIncluded=false&ssr=true&adultsCount=4",
            "https://www.homeaway.es/search/keywords:Santa%20Cruz%20de%20la%20Palma%2C%20Canarias%2C%20Espa%C3%B1a/@28.69886635568806,-18.08377141435028,29.066979430394174,-17.584236807416687,11z?petIncluded=false&ssr=true&adultsCount=4",
            "https://www.homeaway.es/search/keywords:Santa%20Cruz%20de%20la%20Palma%2C%20Canarias%2C%20Espa%C3%B1a/@28.41633923678712,-17.958467956543473,28.601055387633107,-17.708700653076676,12z?petIncluded=false&ssr=true&adultsCount=4"
        ],
        'El Hierro' : [
            "https://www.homeaway.es/search/keywords:El%20Hierro%2C%20Canarias%2C%20España/",
        ],
        'La Gomera' : [
            "https://www.homeaway.es/search/keywords:La%20Gomera%2C%20Canarias%2C%20España/",
        ],
        'Lanzarote' : [
            #Tías
            "https://www.homeaway.es/search/keywords:Tías%2C%20Canarias%2C%20España/",
            #Yaiza
            "https://www.homeaway.es/search/keywords:Yaiza%2C%20Canarias%2C%20España/",
            #Arrecife
            "https://www.homeaway.es/search/keywords:Arrecife%2C%20Canarias%2C%20España/",
            #San Bartolomé
            "https://www.homeaway.es/search/keywords:San%20Bartolomé%2C%20Canarias%2C%20España/",
            #Haríaa
            "https://www.homeaway.es/search/keywords:Haría%2C%20Canarias%2C%20España/",
            #Tinajo
            "https://www.homeaway.es/search/keywords:Tinajo%2C%20Canarias%2C%20España/",
            #Teguise
            "https://www.homeaway.es/search/keywords:Teguise%2C%20Canarias%2C%20España/"
        ],
        'Fuerteventura' : [
            #La Oliva
            "https://www.homeaway.es/search/keywords:La%20Oliva%2C%20Canarias%2C%20España/",
            #Puerto del Rosario
            "https://www.homeaway.es/search/keywords:Puerto%20del%20Rosario%2C%20Canarias%2C%20Espa%C3%B1a/arrival:2019-04-11/departure:2019-04-13/@28.41883727576645,-14.065818776733408,28.60354905601564,-13.816051473266612,12z?petIncluded=false&ssr=true&adultsCount=4",
            #Pajara
            "https://www.homeaway.es/search/keywords:Pájara%2C%20Canarias%2C%20España",
            #Bentacuria
            "https://www.homeaway.es/search/keywords:Betancuria%2C%20Canarias%2C%20España/",
            #Antigua
            "https://www.homeaway.es/search/keywords:Antigua%2C%20Canarias%2C%20España/",
            #Tuineje
            "https://www.homeaway.es/search/keywords:Tuineje%2C%20Canarias%2C%20España/"
        ]
    }
    return urls[place]

def HometogoURLs(place):
    urls= {
        'Puerto de la Cruz' : [
            "https://www.hometogo.es/search/5460aedcd4609?bedrooms=1&bounds=28.42563%2C-16.56022%3B28.39316%2C-16.53416&lastZoom=15&mapZoom=15&persons=2&pricetype=perNight"
        ],
        'Adeje' : [
            ""
        ]
    }
    return urls[place]

def NiumbaURLs(place):
    urls= {
        'Puerto de la Cruz' : [
            "https://www.niumba.com/islas-canarias/santa-cruz-de-tenerife/puerto-de-la-cruz"
        ],
        'Tenerife' : [
            "https://www.niumba.com/tenerife/orderby.default/hom_sleeps_max.2",
        ],
        'Gran Canaria' : [
            "https://www.niumba.com/gran-canaria/orderby.default/",
        ],
        'La Palma' : [
            "https://www.niumba.com/la-palma/orderby.default/hom_sleeps_max.2",
        ],
        'El Hierro' : [
            "https://www.niumba.com/el-hierro/orderby.default/hom_sleeps_max.2",
        ],
        'La Gomera' : [
            "https://www.niumba.com/la-gomera/orderby.default/hom_sleeps_max.2",
        ],
        'Lanzarote' : [
            "https://www.niumba.com/lanzarote/orderby.default/",
        ],
        'Fuerteventura' : [
            "https://www.niumba.com/fuerteventura/orderby.default/hom_sleeps_max.2",
        ]
    }
    return urls[place]

def HolidaylettingsURLs(place):
    urls= {
        'Puerto de la Cruz' : [
            "https://www.holidaylettings.co.uk/puerto-de-la-cruz/hom_sleeps_max.2/"
        ],
        'Tenerife' : [
            "https://www.holidaylettings.co.uk/tenerife/hom_sleeps_max.2/",
        ],
        'Gran Canaria' : [
            "https://www.holidaylettings.co.uk/gran-canaria/hom_sleeps_max.2",
        ],
        'La Palma' : [
            "https://www.holidaylettings.co.uk/la-palma/hom_sleeps_max.2/",
        ],
        'El Hierro' : [
            "https://www.holidaylettings.co.uk/el-hierro/hom_sleeps_max.2/",
        ],
        'La Gomera' : [
            "https://www.holidaylettings.co.uk/la-gomera/hom_sleeps_max.2/",
        ],
        'Lanzarote' : [
            "https://www.holidaylettings.co.uk/lanzarote/hom_sleeps_max.2/",
        ],
        'Fuerteventura' : [
            "https://www.holidaylettings.co.uk/fuerteventura/hom_sleeps_max.2/",
        ]

    }
    return urls[place]

def FlipkeyURLs(place):
    urls= {
        'Puerto de la Cruz' : [
            "https://www.flipkey.com/book/puerto-de-la-cruz/222392922/"
        ],
        'Tenerife' : [
            "https://www.flipkey.com/book/tenerife/222284361/hom_sleeps_max.1/orderby.default/",
        ],
        'Gran Canaria' : [
            "https://www.flipkey.com/book/gran-canaria/222284349/hom_sleeps_max.1/orderby.default/",
        ],
        'La Palma' : [
            "https://www.flipkey.com/book/la-palma/222284442/hom_sleeps_max.1/orderby.default/",
        ],
        'El Hierro' : [
            "https://www.flipkey.com/book/pinar-el-v-hierro/222392850/hom_sleeps_max.1/orderby.default/",
        ],
        'La Gomera' : [
            "https://www.flipkey.com/book/la-gomera/222284445/hom_sleeps_max.1/orderby.default/",
        ],
        'Lanzarote' : [
            "https://www.flipkey.com/book/lanzarote/222284358/hom_sleeps_max.1/orderby.default/"
        ],
        'Fuerteventura' : [
            "https://www.flipkey.com/book/fuerteventura/222284355/hom_sleeps_max.1/orderby.default/",
        ]
    }
    return urls[place]

def HousetripURLs(place):
    urls= {
        'Puerto de la Cruz' : [
            "https://www.housetrip.es/buscar-alquileres/puerto-de-la-cruz/170700"
        ],
        'Tenerife' : [
            "https://www.housetrip.es/buscar-alquileres/tenerife/62139/hom_sleeps_max.2",
        ],
        'Gran Canaria' : [
            "https://www.housetrip.es/buscar-alquileres/gran-canaria/62127/hom_sleeps_max.2/orderby.default",
        ],
        'La Palma' : [
            "https://www.housetrip.es/buscar-alquileres/isla-de-la-palma/62220/hom_sleeps_max.2/orderby.default",
        ],
        'El Hierro' : [
            "https://www.housetrip.es/el-hierro/hom_sleeps_max.2/orderby.default",
        ],
        'La Gomera' : [
            "https://www.housetrip.es/la-gomera/hom_sleeps_max.2/orderby.default",
        ],
        'Lanzarote' : [
            "https://www.housetrip.es/buscar-alquileres/lanzarote/62136/hom_sleeps_max.2/orderby.default",
        ],
        'Fuerteventura' : [
            "https://www.housetrip.es/buscar-alquileres/fuerteventura/62133/hom_sleeps_max.2/orderby.default",
        ]
    }
    return urls[place]

def OnlyApartmentsURLs(place):
    urls= {
        'Puerto de la Cruz' : [
            "https://www.only-apartments.es/apartamentos-en-puerto-de-la-cruz.html"
        ],
        'Adeje' : [
            "https://www.only-apartments.es/apartamentos-en-costa-adeje.html",
            "https://www.only-apartments.es/apartamentos-en-adeje.html",
            "https://www.only-apartments.es/apartamentos-en-callao-salvaje.html"
        ],
        'Tenerife' : [
            "https://www.only-apartments.es/apartamentos-en-tenerife-espana.r.html"
        ],
        'Gran Canaria' : [
            "https://www.only-apartments.es/apartamentos-en-gran-canaria-espana.r.html",
        ],
        'La Palma' : [
            "https://www.only-apartments.es/apartamentos-en-la-palma-espana.r.html",
        ],
        'El Hierro' : [
            "https://www.only-apartments.es/apartamentos-en-el-hierro-espana.r.html",
        ],
        'La Gomera' : [
            "https://www.only-apartments.es/apartamentos-en-la-gomera-espana.r.html",
        ],
        'Lanzarote' : [
            "https://www.only-apartments.es/apartamentos-en-lanzarote-espana.r.html",
        ],
        'Fuerteventura' : [
            "https://www.only-apartments.es/apartamentos-en-fuerteventura-espana.r.html",
        ]
    }
    return urls[place]

def Flats9URLs(place):
    urls= {
        'Puerto de la Cruz' : [
            "https://www.9flats.com/es/searches?utf8=%E2%9C%93&mode=list&search%5Bplace_type%5D=&search%5Bprice_min%5D=&search%5Bprice_max%5D=&search%5Bcurrency%5D=EUR&search%5Bsort_by%5D=top_ranking&search%5Bview_index%5D=0&search%5Bnumber_of_bathrooms%5D=0&search%5Bnumber_of_bedrooms%5D=0&search%5Bradius%5D=25&search%5Bamenities%5D=&search%5Bwoeid%5D=770966&search%5Bbb_sw%5D=&search%5Bbb_ne%5D=&search%5Blat%5D=28.4142&search%5Blng%5D=-16.5474&search%5Biso%5D=&search%5Bis_country%5D=&search%5Bcategory%5D=&search%5Bgeo_search%5D=&search%5Bgeo_region%5D=false&search%5Bpoint_of_interest%5D=false&search%5Bprice_range%5D=&search%5Bancestries%5D=&search%5Bcontinuous_update%5D=&search%5Bbooking_type%5D=&search%5Bpayment_type%5D=&search%5Bstart_date_alt%5D=&search%5Bend_date_alt%5D=&search%5Bquery%5D=Puerto+de+la+Cruz%2C+Pto+de+la+Cruz"
        ],
        'Adeje' : [
            "https://www.9flats.com/es/searches?utf8=%E2%9C%93&mode=list&search%5Bcurrency%5D=EUR&search%5Bsort_by%5D=top_ranking&search%5Bradius%5D=25&search%5Bwoeid%5D=751413&search%5Blat%5D=28.4142&search%5Blng%5D=-16.5474&search%5Bgeo_region%5D=false&search%5Bpoint_of_interest%5D=false&search%5Bquery%5D=Adeje%2C+Adeje+Municipio%2C+Tenerife%2C+Islas+Canarias%2C+Espa%C3%B1a&search%5Bstart_date%5D=&search%5Bend_date%5D=&search%5Bnumber_of_beds%5D=2&number_of_adults=2&search%5Bnumber_of_children%5D=0&number_of_bedrooms=&number_of_bathrooms="
        ],
        'Gran Canaria' : [
            "",
        ],
        'La Palma' : [
            "",
        ],
        'El Hierro' : [
            "",
        ],
        'La Gomera' : [
            "",
        ],
        'Lanzarote' : [
            "",
        ],
        'Fuerteventura' : [
            "",
        ]
    }
    return urls[place]

def RentaliaURLs(place):
    urls= {
        'Puerto de la Cruz' : [
            "https://es.rentalia.com/alquiler-vacaciones-puerto-de-la-cruz/"
        ],
        'Adeje' : [
            "https://es.rentalia.com/alquiler-vacaciones-adeje/"
        ],
        'Tenerife' : [
            "https://es.rentalia.com/alquiler-vacaciones-tenerife/",
        ],
        'Gran Canaria' : [
            "https://es.rentalia.com/alquiler-vacaciones-gran-canaria/",
        ],
        'La Palma' : [
            "https://es.rentalia.com/alquiler-vacaciones-la-palma/",
        ],
        'El Hierro' : [
            "https://es.rentalia.com/alquiler-vacaciones-el-hierro/",
        ],
        'La Gomera' : [
            "https://es.rentalia.com/alquiler-vacaciones-la-gomera/",
        ],
        'Lanzarote' : [
            "https://es.rentalia.com/alquiler-vacaciones-lanzarote/",
        ],
        'Fuerteventura' : [
            "https://es.rentalia.com/alquiler-vacaciones-fuerteventura/",
        ]
    }
    return urls[place]

def CasamundoURLs(place):
    urls= {
        'Puerto de la Cruz' : [
            "https://www.casamundo.es/busca?anchor=188840&destination_id=13573"
        ]
    }
    return urls[place]