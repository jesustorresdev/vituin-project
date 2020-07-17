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
            "https://www.booking.com/searchresults.es.html?label=gen173nr-1DCAEoggI46AdIM1gEaEaIAQGYAQq4ARnIAQzYAQPoAQGIAgGoAgO4Au6FgeQFwAIB&sid=b9b5230609de880a1134cf7bbe706add&sb=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.es.html%3Flabel%3Dgen173nr-1DCAEoggI46AdIM1gEaEaIAQGYAQq4ARnIAQzYAQPoAQGIAgGoAgO4Au6FgeQFwAIB%3Bsid%3Db9b5230609de880a1134cf7bbe706add%3Bsb_price_type%3Dtotal%26%3B&ss=Tenerife%2C+Espa%C3%B1a&is_ski_area=&ssne=Puerto+de+la+Cruz&ssne_untouched=Puerto+de+la+Cruz&checkin_year=&checkin_month=&checkout_year=&checkout_month=&no_rooms=1&group_adults=2&group_children=0&map=1&b_h4u_keep_filters=&from_sf=1&ss_raw=tenerife&ac_position=0&ac_langcode=es&ac_click_type=b&dest_id=777&dest_type=region&place_id_lat=28.194826&place_id_lon=-16.621949&search_pageview_id=0184041f26e20227&search_selected=true&search_pageview_id=0184041f26e20227&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0#map_closed",
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
            "https://www.tripadvisor.es/VacationRentals-g187475-Reviews-La_Palma_Canary_Islands-Vacation_Rentals.html",
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
            "https://www.airbnb.es/s/Puerto-de-la-Cruz--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJBxuTnlXVQQwRQWOmKGEY6s0&query=Puerto%20de%20la%20Cruz%2C%20Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&s_tag=o78DH6Gz",
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
# GRAN CANARIA -------------

              # Las Palmas
              'Gran Canaria LP ciudad alta' : [
                  # - Tafira - San Lorenzo
                  'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Tafira%2C%20Las%20Palmas&map_toggle=true&allow_override%5B%5D=&s_tag=4DvS5ykn',
                  #  - Siete Palmas - Tamaraceite - Almatriche
                  'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Tafira%2C%20Las%20Palmas&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.080369759148812&sw_lng=-15.495744091539354&ne_lat=28.137350731849875&ne_lng=-15.44554067042348&search_type=UNKNOWN&s_tag=uVJZRZLI',
                  # Santa Brígida
                  'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Tafira%2C%20Las%20Palmas&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=27.9997636661409&sw_lng=-15.516000134019823&ne_lat=28.056791896836117&ne_lng=-15.465796712903948&search_type=UNKNOWN&s_tag=9gEyx8d2',
              ],
              'Gran Canaria LP sur' : [
                  # - La Montañeta - Lomo Blanco - Jinamar - El Hoyo
                  'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Tafira%2C%20Las%20Palmas&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.0139051926494&sw_lng=-15.453509188320613&ne_lat=28.070925141419252&ne_lng=-15.403305767204738&search_type=UNKNOWN&s_tag=K1M-xH7Z',
                  # - San Cristobal - Vegueta - Triana
                  'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=San%20Cristobal%20las%20palmas&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.046608626580994&sw_lng=-15.43973942479126&ne_lat=28.103609408029985&ne_lng=-15.389536003675385&s_tag=mewHUoib',
              ],
              'Gran Canaria zona antigua': [
                  # - Vegueta - Triana
                  'https://www.airbnb.es/s/Vegueta--Las-Palmas-de-Gran-Canaria/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Vegueta%2C%20Las%20Palmas%20de%20Gran%20Canaria&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.091993924211437&sw_lng=-15.424081260983035&ne_lat=28.10624064589195&ne_lng=-15.411530405704065&search_type=UNKNOWN&s_tag=C1oMkrVA',
                  # - Barrio San Juan hasta Rehoyas
                  'https://www.airbnb.es/s/Barrio-San-Juan--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Barrio%20San%20Juan%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.087069985248366&sw_lng=-15.443455992913309&ne_lat=28.115562751160944&ne_lng=-15.418354282355372&search_type=UNKNOWN&s_tag=_apf8U0e',
              ],
              'Gran Canaria LP centro 1' : [
                  # - Escaleritas
                  'https://www.airbnb.es/s/Avenida-Escaleritas--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Avenida%20Escaleritas%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&place_id=EjhBdmVuaWRhIEVzY2FsZXJpdGFzLCBMYXMgUGFsbWFzIGRlIEdyYW4gQ2FuYXJpYSwgRXNwYcOxYSIuKiwKFAoSCdWGcH-olUAMEbLEr-u4S2zKEhQKEgnRl8CRDpVADBFlujhTrLU2qw&map_toggle=true&allow_override%5B%5D=&s_tag=0DZeZVyj',
                  # - Mesa y López
                  'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=doramas%20las%20palmas&is_user_submitted_query=true&allow_override%5B%5D=&zoom=18&search_by_map=true&sw_lat=28.136042567549804&sw_lng=-15.435227538278896&ne_lat=28.1396028299555&ne_lng=-15.432089824459153&search_type=UNKNOWN&s_tag=6I9JYlwQ',
                  'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=doramas%20las%20palmas&is_user_submitted_query=true&allow_override%5B%5D=&zoom=18&search_by_map=true&sw_lat=28.13620340490441&sw_lng=-15.43311932199319&ne_lat=28.139763661401677&ne_lng=-15.429981608173447&search_type=UNKNOWN&s_tag=njsyWi9B',

              ],
              'Gran Canaria LP centro 2' : [
                  # - Mesa y López
                  'https://www.airbnb.es/s/Mesa-y-L%C3%B3pez--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Mesa%20y%20L%C3%B3pez%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&zoom=17&search_by_map=true&sw_lat=28.122420227245158&sw_lng=-15.447512080364222&ne_lat=28.129541619950732&ne_lng=-15.441236652724738&allow_override%5B%5D=&search_type=UNKNOWN&s_tag=Yu5o0b_q',
                  'https://www.airbnb.es/s/Mesa-y-L%C3%B3pez--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Mesa%20y%20L%C3%B3pez%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&zoom=17&search_by_map=true&sw_lat=28.128252104228586&sw_lng=-15.440123977018574&ne_lat=28.135373068594518&ne_lng=-15.433848549379091&allow_override%5B%5D=&search_type=UNKNOWN&s_tag=EQHzYJx2',
                  'https://www.airbnb.es/s/Mesa-y-L%C3%B3pez--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Mesa%20y%20L%C3%B3pez%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&zoom=17&search_by_map=true&sw_lat=28.13042828003337&sw_lng=-15.435660781217793&ne_lat=28.137549084542634&ne_lng=-15.42938535357831&allow_override%5B%5D=&search_type=UNKNOWN&s_tag=IrCPvoih',
              ],
              'Gran Canaria LP centro 3': [
                  # - Triana - Fuente luminosa
                  'https://www.airbnb.es/s/Calle-Triana--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Calle%20Triana%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.101406235726653&sw_lng=-15.425394824490132&ne_lat=28.115651575956555&ne_lng=-15.412843969211162&search_type=UNKNOWN&s_tag=EtrURFBR',
                  # - Doramas
                  'https://www.airbnb.es/s/Calle-Triana--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Calle%20Triana%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.114619018493784&sw_lng=-15.434192594068127&ne_lat=28.128862418758757&ne_lng=-15.421641738789157&search_type=UNKNOWN&s_tag=VzuZztaO',
              ],
              'Gran Canaria Canteras': [
                  'https://www.airbnb.es/s/Parque-Santa-Catalina--Las-Palmas-de-Gran-Canaria/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Parque%20Santa%20Catalina%2C%20Las%20Palmas%20de%20Gran%20Canaria&zoom=18&search_by_map=true&sw_lat=28.13918799985705&sw_lng=-15.433625282843623&ne_lat=28.142748146708282&ne_lng=-15.43048756902388&allow_override%5B%5D=&search_type=UNKNOWN&s_tag=3POF77FC',
                  'https://www.airbnb.es/s/Parque-Santa-Catalina--Las-Palmas-de-Gran-Canaria/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Parque%20Santa%20Catalina%2C%20Las%20Palmas%20de%20Gran%20Canaria&zoom=18&search_by_map=true&sw_lat=28.139240033970513&sw_lng=-15.435073675711665&ne_lat=28.142800178910026&ne_lng=-15.431935961891922&allow_override%5B%5D=&search_type=UNKNOWN&s_tag=hUnBmtlx',
                  'https://www.airbnb.es/s/Parque-Santa-Catalina--Las-Palmas-de-Gran-Canaria/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Parque%20Santa%20Catalina%2C%20Las%20Palmas%20de%20Gran%20Canaria&zoom=18&search_by_map=true&sw_lat=28.141799135088934&sw_lng=-15.43296545942596&ne_lat=28.1453591860053&ne_lng=-15.429827745606216&allow_override%5B%5D=&search_type=UNKNOWN&s_tag=_tTkBaRr',
              ],
              'Gran Canaria Canteras2': [
                  'https://www.airbnb.es/s/Las-Canteras-Beach--Las-Palmas-de-Gran-Canaria--Spain/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Las%20Canteras%20Beach%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Spain&zoom=18&search_by_map=true&sw_lat=28.1372561925095&sw_lng=-15.437199536810995&ne_lat=28.140816410331347&ne_lng=-15.434061822991252&allow_override%5B%5D=&search_type=UNKNOWN&s_tag=H0udra6n',
                  'https://www.airbnb.es/s/Las-Canteras-Beach--Las-Palmas-de-Gran-Canaria--Spain/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Las%20Canteras%20Beach%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Spain&zoom=18&search_by_map=true&sw_lat=28.13593165541117&sw_lng=-15.433632198821188&ne_lat=28.139491921891235&ne_lng=-15.430494485001445&allow_override%5B%5D=&search_type=UNKNOWN&s_tag=cJ4Jc4pb',
                  'https://www.airbnb.es/s/Las-Canteras-Beach--Las-Palmas-de-Gran-Canaria--Spain/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Las%20Canteras%20Beach%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Spain&zoom=18&search_by_map=true&sw_lat=28.135889080732813&sw_lng=-15.431883398543478&ne_lat=28.139449348776868&ne_lng=-15.428745684723735&allow_override%5B%5D=&search_type=UNKNOWN&s_tag=n8xSyoNU',
              ],
              'Gran Canaria Canteras3':[
                  # Guanarteme
                  'https://www.airbnb.es/s/Las-Canteras-Beach--Las-Palmas-de-Gran-Canaria--Spain/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Las%20Canteras%20Beach%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Spain&zoom=17&search_by_map=true&sw_lat=28.127961712204485&sw_lng=-15.446309459462045&ne_lat=28.135082697901044&ne_lng=-15.440034031822561&allow_override%5B%5D=&search_type=UNKNOWN&s_tag=7YM4Y4De',
                  'https://www.airbnb.es/s/Las-Canteras-Beach--Las-Palmas-de-Gran-Canaria--Spain/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Las%20Canteras%20Beach%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Spain&zoom=17&search_by_map=true&sw_lat=28.127365619942402&sw_lng=-15.45116962219703&ne_lat=28.13448664942406&ne_lng=-15.444894194557547&allow_override%5B%5D=&search_type=UNKNOWN&s_tag=7XdGDDXO',
              ],
              'Gran Canaria Isleta': [
                  "https://www.airbnb.es/s/Isleta--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Isleta%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.1486880500068&sw_lng=-15.430367001165816&ne_lat=28.156063161174902&ne_lng=-15.423847014642295",
                  'https://www.airbnb.es/s/Isleta--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Isleta%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.14501403683339&sw_lng=-15.43266943867326&ne_lat=28.152133769614988&ne_lng=-15.426394011033777',
                  'https://www.airbnb.es/s/Isleta--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Isleta%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.146054830211387&sw_lng=-15.427331372005943&ne_lat=28.160293611552845&ne_lng=-15.414780516726973',
              ],
              'Gran Canaria Isleta2': [
                  # "https://www.airbnb.es/s/Isleta--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Isleta%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.1482150526966&sw_lng=-15.426687010397384&ne_lat=28.155590199759978&ne_lng=-15.420167023873862",
                  # "https://www.airbnb.es/s/Isleta--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Isleta%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.14786037277454&sw_lng=-15.44127665453805&ne_lat=28.162610152834333&ne_lng=-15.428236681491008",
                  'https://www.airbnb.es/s/Isleta--Las-Palmas-de-Gran-Canaria--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Isleta%2C%20Las%20Palmas%20de%20Gran%20Canaria%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.15034716376715&sw_lng=-15.437810402300492&ne_lat=28.16924383394484&ne_lng=-15.421295962750783',
              ],
            'Gran Canaria San Agustin' : [
                  # - San Agustín
                  "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=16&search_by_map=true&sw_lat=27.764474591143784&sw_lng=-15.553444961014002&ne_lat=27.78344432753015&ne_lng=-15.536930521464292&allow_override%5B%5D=&s_tag=6n-Ca_DS",
                  "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=16&search_by_map=true&sw_lat=27.760164374588552&sw_lng=-15.569721346329565&ne_lat=27.77913492189227&ne_lng=-15.553206906779856&allow_override%5B%5D=&s_tag=BHWWxewj",
            ],
            'Gran Canaria San Agustin2' : [
                'https://www.airbnb.es/s/Maspalomas--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Maspalomas%2C%20Espa%C3%B1a&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=27.770047287049326&sw_lng=-15.544890043032687&ne_lat=27.78901597482582&ne_lng=-15.528375603482978&s_tag=MsSeI377',
                # - Playa del Águila
                "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=15&search_by_map=true&sw_lat=27.768199206197078&sw_lng=-15.536038804934366&ne_lat=27.806133666189414&ne_lng=-15.503009925834943&allow_override%5B%5D=&s_tag=6i7witC4",
            ],
            'Gran Canaria Resto San Bartolome': [
                # - Sonnerland
                "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=16&search_by_map=true&sw_lat=27.74568867955053&sw_lng=-15.612012094755919&ne_lat=27.764661949440885&ne_lng=-15.59549765520621&allow_override%5B%5D=&s_tag=aWaSO_Ay",
                # - Meloneras
                "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=16&search_by_map=true&sw_lat=27.736895659079423&sw_lng=-15.604503037832778&ne_lat=27.755870582121982&ne_lng=-15.587988598283069&allow_override%5B%5D=&s_tag=HRc95TyY",
                # - Costa Meloneras y Pasito Blanco
                "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=16&search_by_map=true&sw_lat=27.736477830510076&sw_lng=-15.616174883147032&ne_lat=27.75545283209546&ne_lng=-15.599660443597323&allow_override%5B%5D=&s_tag=mO0wpVvu",
            ],
            'Gran Canaria Resto San Bartolome2': [
                "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=15&search_by_map=true&sw_lat=27.727090583905348&sw_lng=-15.634281174424574&ne_lat=27.76504050806059&ne_lng=-15.601252295325152&allow_override%5B%5D=&s_tag=QZFP7kjr",
                # - El Tablero - Montaña la Data
                "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=15&search_by_map=true&sw_lat=27.762603561112517&sw_lng=-15.625569359544203&ne_lat=27.80054012730241&ne_lng=-15.59254048044478&allow_override%5B%5D=&s_tag=gdlMfvXN",
                # - Ayagures - Arteara
                "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=14&search_by_map=true&sw_lat=27.802583216066537&sw_lng=-15.628036807960004&ne_lat=27.878411771839488&ne_lng=-15.56197904976116&allow_override%5B%5D=&s_tag=b1631OCJ",
                # San Bartolomé y Santa Lucía
                "https://www.airbnb.es/s/Cruce-de-Arinaga/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Cruce%20de%20Arinaga&map_toggle=true&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=27.85030733647081&sw_lng=-15.589910718482038&ne_lat=27.96860190702207&ne_lng=-15.48559093410568&s_tag=bWtdf2xX",
            ],
            # Santa Lucía Tirajana
            'Gran Canaria Santa Lucia': [
                # - Arinaga
                "https://www.airbnb.es/s/Arinaga--Playa-de-Arinaga/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Arinaga%2C%20Playa%20de%20Arinaga&place_id=ChIJSYxAwsKhQAwR-g9FlPdpyFI&map_toggle=true&allow_override%5B%5D=&s_tag=PhKz7hH-",
                # - Sardina
                "https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Vecindario%2C%20Gran%20Canaria%2C%20Spagna&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=27.837314814913807&sw_lng=-15.473324213922284&ne_lat=27.86690591527811&ne_lng=-15.447244267828195&s_tag=ukTIxcD2",
            ],
            'Gran Canaria Santa Lucia2': [
                # - Cruce de Arinaga
                "https://www.airbnb.es/s/Cruce-de-Arinaga/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Cruce%20de%20Arinaga&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=27.841591374969102&sw_lng=-15.449075141894784&ne_lat=27.900761976512182&ne_lng=-15.396915249706606&s_tag=9Xp8zkU-",
                # - Vecindario
                "https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Vecindario%2C%20Gran%20Canaria%2C%20Spagna&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=27.825511877387378&sw_lng=-15.458861742913983&ne_lat=27.85510652442225&ne_lng=-15.432781796819894&s_tag=AJLTjT6T",
                # - Castillo de Romeral
                "https://www.airbnb.es/s/Maspalomas/homes?refinement_paths%5B%5D=%2Fhomes&map_toggle=true&query=Maspalomas&zoom=14&search_by_map=true&sw_lat=27.76732183621934&sw_lng=-15.497821712959169&ne_lat=27.843176965743343&ne_lng=-15.431763954760324&allow_override%5B%5D=&s_tag=FzcxDqIw",
            ],
            'Gran Canaria Santa Lucia3':[
                # - Pozo I
                'https://www.airbnb.es/s/Cruce-de-Arinaga/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Cruce%20de%20Arinaga&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=27.76913581768383&sw_lng=-15.44495191608664&ne_lat=27.844989580907036&ne_lng=-15.378894157887796',
                # - Santa Lucía
                'https://www.airbnb.es/s/Cruce-de-Arinaga/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Cruce%20de%20Arinaga&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=27.854348633267556&sw_lng=-15.557894467212552&ne_lat=27.93013812140037&ne_lng=-15.491836709013707',
                # - Los Corralillos - Cueva Bermeja - Temisas
                'https://www.airbnb.es/s/Cruce-de-Arinaga/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=Cruce%20de%20Arinaga&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=27.835380339649348&sw_lng=-15.519789564667324&ne_lat=27.911184150999006&ne_lng=-15.453731806468479',

            ],
            # Mogan
            'Gran Canaria Mogan': [
                # Mogán
                "https://www.airbnb.es/s/Mog%C3%A1n--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=Mog%C3%A1n%2C%20Las%20Palmas&place_id=ChIJ21QCFCyBQAwRoBNNvvNAAwQ&map_toggle=true&allow_override%5B%5D=&s_tag=Abr2TN0h",
                "https://www.airbnb.es/s/mogan--Gran-Canaria--Mog%C3%A1n--Spain/homes?refinement_paths%5B%5D=%2Fhomes&query=mogan%2C%20Gran%20Canaria%2C%20Mog%C3%A1n%2C%20Spain&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=27.846710858503627&sw_lng=-15.755023879099415&ne_lat=27.922506115101164&ne_lng=-15.68896612090057&s_tag=lgNQFRrt",
                # - Los Caideros
                "https://www.airbnb.es/s/Los-Caideros--Las-Palmas--Spania/homes?refinement_paths%5B%5D=%2Fhomes&query=Los%20Caideros%2C%20Las%20Palmas%2C%20Spania&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=27.767834139976156&sw_lng=-15.705778050463373&ne_lat=27.78680324422201&ne_lng=-15.689263610913663&s_tag=Zz0Ruc5Z",
            ],
            'Gran Canaria Mogan1': [
                # - Puerto Rico
                "https://www.airbnb.es/s/Puerto-mogan--Gran-Canaria--Lomoquiebre--Lomo-Quiebre--Spanien/homes?refinement_paths%5B%5D=%2Fhomes&query=Puerto%20mogan%2C%20Gran%20Canaria%2C%20Lomoquiebre%2C%20Lomo%20Quiebre%2C%20Spanien&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=27.795800383889734&sw_lng=-15.735810550783462&ne_lat=27.81476422321165&ne_lng=-15.719296111233753&s_tag=lhoCx0Cf",
                "https://www.airbnb.es/s/Puerto-mogan--Gran-Canaria--Lomoquiebre--Lomo-Quiebre--Spanien/homes?refinement_paths%5B%5D=%2Fhomes&query=Puerto%20mogan%2C%20Gran%20Canaria%2C%20Lomoquiebre%2C%20Lomo%20Quiebre%2C%20Spanien&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=27.78710632861439&sw_lng=-15.724201950167007&ne_lat=27.806071805200972&ne_lng=-15.707687510617298&s_tag=1zJYKk_a",
                "https://www.airbnb.es/s/Puerto-mogan--Gran-Canaria--Lomoquiebre--Lomo-Quiebre--Spanien/homes?refinement_paths%5B%5D=%2Fhomes&query=Puerto%20mogan%2C%20Gran%20Canaria%2C%20Lomoquiebre%2C%20Lomo%20Quiebre%2C%20Spanien&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=27.775772640816562&sw_lng=-15.71237877282936&ne_lat=27.79474025105609&ne_lng=-15.695864333279651&s_tag=Y_rLZ_Sb",
            ],
            'Gran Canaria Mogan2': [
                # - Arguineguín
                "https://www.airbnb.es/s/Arguineguin--Las-Palmas--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Arguineguin%2C%20Las%20Palmas%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=27.743795545672736&sw_lng=-15.690116338841664&ne_lat=27.781739188328302&ne_lng=-15.657087459742241&s_tag=vUz_e5VP",
                # - Tasarte - Casas Blancas
                "https://www.airbnb.es/s/Arguineguin--Las-Palmas--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Arguineguin%2C%20Las%20Palmas%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=27.893823334975455&sw_lng=-15.80116452119032&ne_lat=27.969582986516773&ne_lng=-15.735106762991474&s_tag=ia-abicb",
                # - Puerto Mogán - Taurito
                "https://www.airbnb.es/s/Puerto-mogan--Gran-Canaria--Lomoquiebre--Lomo-Quiebre--Spanien/homes?refinement_paths%5B%5D=%2Fhomes&query=Puerto%20mogan%2C%20Gran%20Canaria%2C%20Lomoquiebre%2C%20Lomo%20Quiebre%2C%20Spanien&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=27.80605608477467&sw_lng=-15.772561027575863&ne_lat=27.8439762852101&ne_lng=-15.73953214847644&s_tag=fODyMZUS",
            ],
            'Gran Canaria Santa Brigida': [
                # Santa Brígida
                "https://www.airbnb.es/s/Santa-Br%C3%ADgida--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=Santa%20Br%C3%ADgida%2C%20Las%20Palmas&place_id=ChIJDUxGV86WQAwRMBRNvvNAAwQ&map_toggle=true&allow_override%5B%5D=&s_tag=XR6sOzus",
            ],
            'Gran Canaria Artenara': [
                # Artenara
                "https://www.airbnb.es/s/Artenara--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=Artenara%2C%20Las%20Palmas&place_id=ChIJaWQNmTWJQAwRMBNNvvNAAwQ&allow_override%5B%5D=&s_tag=c6AnBFwh",
            ],
            'Gran Canaria Tejeda': [
                # Tejeda
                "https://www.airbnb.es/s/Tejeda--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=Tejeda%2C%20Las%20Palmas&place_id=ChIJi3GUBWaPQAwRcBRNvvNAAwQ&allow_override%5B%5D=&s_tag=rWc-3odn",
            ],
            'Gran Canaria Moya': [
                # Moya
                "https://www.airbnb.es/s/Moya--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=Moya%2C%20Las%20Palmas&place_id=ChIJhc4WuHaSQAwRsBNNvvNAAwQ&allow_override%5B%5D=&s_tag=2RfnDMWD",
            ],
            'Gran Canaria San Mateo': [
                # San Mateo
                "https://www.airbnb.es/s/San-Mateo--Vega-de-San-Mateo--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=San%20Mateo%2C%20Vega%20de%20San%20Mateo%2C%20Espa%C3%B1a&place_id=ChIJb7DwmOOQQAwR4_IRfBwwjGc&allow_override%5B%5D=&s_tag=Tpyg_olO",
            ],
            'Gran Canaria Valsequillo': [
                # Valsequillo
                "https://www.airbnb.es/s/Valsequillo-de-Gran-Canaria--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=Valsequillo%20de%20Gran%20Canaria%2C%20Las%20Palmas&place_id=ChIJ2SLlma2QQAwR0BRNvvNAAwQ&allow_override%5B%5D=&s_tag=380yajmk",
            ],
            'Gran Canaria Firgas': [
                # Firgas
                "https://www.airbnb.es/s/Firgas--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=Firgas%2C%20Las%20Palmas&place_id=ChIJmal1WVqSQAwR_qTY6bck_ss&allow_override%5B%5D=&s_tag=R5PCRjmo",
            ],
# LA PALMA --------------
        # S/C La Palma - Breñas - Villa Mazo - Fuencaliente
        'La Palma Este' : [
            # S/C
            'https://www.airbnb.es/s/Santa-Cruz-de-la-Palma/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=La%20Polvacera%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.660861319310623&sw_lng=-17.807351006944618&ne_lat=28.71749828691342&ne_lng=-17.757147585828744&search_type=UNKNOWN&s_tag=AV0xzxY9',
            # Los Cancajos - Breñas - Villa Mazo - Breñas - San Pedro
            'https://www.airbnb.es/s/Los-Cancajos/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=La%20Polvacera%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.60993531277377&sw_lng=-17.80108536668583&ne_lat=28.666602717236813&ne_lng=-17.750881945569954&search_type=UNKNOWN&s_tag=KfS08kQ_',
            # Villa Mazo a Fuencaliente
            'https://www.airbnb.es/s/Villa-de-Mazo--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&query=Barlovento%2C%20Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&map_toggle=true&search_type=UNKNOWN&zoom=12&search_by_map=true&sw_lat=28.41440849425452&sw_lng=-17.859486974067707&ne_lat=28.641338066752624&ne_lng=-17.65867328960421&s_tag=73zEAEwK',
        ],
        # - Tijarafe - Puntagorda - Garafía - Barlovento - Puntallana - San Andrés y Sauces
        'La Palma Norte': [
            # Barlovento - Puntallana - San Andrés y Sauces
            'https://www.airbnb.es/s/Barlovento--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&query=Barlovento%2C%20Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&map_toggle=true&search_type=UNKNOWN&zoom=12&search_by_map=true&sw_lat=28.682551666901688&sw_lng=-17.88935605365755&ne_lat=28.908840784567307&ne_lng=-17.688542369194053&s_tag=6ep0Gtkz',
            # Tijarafe - Puntagorda - Garafía
            'https://www.airbnb.es/s/Tijarafe--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&query=Tijarafe%2C%20Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&map_toggle=true&search_type=UNKNOWN&zoom=12&search_by_map=true&sw_lat=28.682727435313627&sw_lng=-18.001871148872354&ne_lat=28.90901613136657&ne_lng=-17.801057464408856&s_tag=vPtXk0k9',
        ],
        # Los Llanos - El Paso - Tazacorte - Fuencaliente
        'La Palma Oeste': [
            # Los Llanos
            'https://www.airbnb.es/s/Los-Llanos-de-Aridane/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=Los%20Llanos%20de%20Aridane&allow_override%5B%5D=&map_toggle=true&search_type=UNKNOWN&zoom=14&search_by_map=true&sw_lat=28.64034873115483&sw_lng=-17.926929662828474&ne_lat=28.69699796442989&ne_lng=-17.8767262417126&s_tag=F4Uo3lsE',
            # El Paso
            'https://www.airbnb.es/s/Los-Llanos-de-Aridane/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=Los%20Llanos%20de%20Aridane&allow_override%5B%5D=&map_toggle=true&search_type=UNKNOWN&zoom=14&search_by_map=true&sw_lat=28.63040459714668&sw_lng=-17.891996572618513&ne_lat=28.68705977371158&ne_lng=-17.84179315150264&s_tag=BX9NH7t8',
            # - La Punta - Los Llanos - Puerto de Tazacorte
            'https://www.airbnb.es/s/Los-Llanos-de-Aridane/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=Los%20Llanos%20de%20Aridane&allow_override%5B%5D=&map_toggle=true&search_type=UNKNOWN&zoom=14&search_by_map=true&sw_lat=28.64410136510103&sw_lng=-17.966555502279125&ne_lat=28.700748355057137&ne_lng=-17.91635208116325&s_tag=WL9a1ncH',
        ],
        'La Palma Oeste2': [
            # - Todoque - El Paraíso - El Pedregal - La Laguna - Tajuya - Dos Pinos
            'https://www.airbnb.es/s/Puerto-Naos--La-Palma--Puerto-de-Naos--Spanien/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=Puerto%20Naos%2C%20La%20Palma%2C%20Puerto%20de%20Naos%2C%20Spanien&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.592392446314904&sw_lng=-17.927910035905843&ne_lat=28.649070324138794&ne_lng=-17.877706614789968&search_type=UNKNOWN&s_tag=H67yCIds',
            # - Puerto Naos
            'https://www.airbnb.es/s/Puerto-Naos--La-Palma--Puerto-de-Naos--Spanien/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=Puerto%20Naos%2C%20La%20Palma%2C%20Puerto%20de%20Naos%2C%20Spanien&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.58040277838984&sw_lng=-17.915144603905684&ne_lat=28.60874958756741&ne_lng=-17.890042893347744&search_type=UNKNOWN&s_tag=X5hQEzB-',
            # - Las Manchas - Jedey - Puerto Naos
            'https://www.airbnb.es/s/Puerto-Naos--La-Palma--Puerto-de-Naos--Spanien/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=Puerto%20Naos%2C%20La%20Palma%2C%20Puerto%20de%20Naos%2C%20Spanien&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.55756796721669&sw_lng=-17.904049104509358&ne_lat=28.61426661839299&ne_lng=-17.853845683393484&search_type=UNKNOWN&s_tag=cpk-2uvD',
        ],
        'La Palma Oeste3': [
            # Tazacorte - Argual - San Borondón
            'https://www.airbnb.es/s/Tazacorte--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&map_toggle=true&query=Tazacorte%2C%20Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.613857843171786&sw_lng=-17.9726885916614&ne_lat=28.670522905020814&ne_lng=-17.922485170545524&search_type=UNKNOWN&s_tag=x-rFtitx',
            # Fuencaliente
            'https://www.airbnb.es/s/Fuencaliente-de-la-Palma--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=Fuencaliente%20de%20la%20Palma%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=28.453465590423846&sw_lng=-17.89161602426524&ne_lat=28.566952541714368&ne_lng=-17.79120918203349&search_type=UNKNOWN&s_tag=XVOPfKn5',
            # - La Bombilla a San Borondón
            'https://www.airbnb.es/s/Los-Llanos-de-Aridane/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=Los%20Llanos%20de%20Aridane&allow_override%5B%5D=&map_toggle=true&search_type=UNKNOWN&zoom=14&search_by_map=true&sw_lat=28.587758909367867&sw_lng=-17.95496835933479&ne_lat=28.644439552504387&ne_lng=-17.904764938218914&s_tag=QWz91our',
         ],
        'La Palma Centro': [
            # Centro
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=La%20palma%20canarias&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=28.570549118285758&sw_lng=-17.883466445739977&ne_lat=28.68389657958604&ne_lng=-17.783059603508228&s_tag=GjA4rXcc',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=La%20palma%20canarias&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=28.70220829280535&sw_lng=-17.919207181905485&ne_lat=28.81539827494689&ne_lng=-17.818800339673736&s_tag=8DoMCor6',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=La%20palma%20canarias&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=28.69934730307102&sw_lng=-17.87560519215939&ne_lat=28.812540714295025&ne_lng=-17.775198349927642&s_tag=Tq4wXh4v',
        ],
# EL HIERRO -------------
        'El Hierro' : [
            "https://www.airbnb.es/s/El-Hierro--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&query=El%20Hierro%2C%20Santa%20Cruz%20de%20Tenerife&place_id=ChIJYZqqMcpYawwRgUq_IX0pFz4&allow_override%5B%5D=&map_toggle=true&s_tag=YDr20vn2",
        ],
# LA GOMERA -------------
        'La Gomera 1' : [
            # San Sebastián
            'https://www.airbnb.es/s/San-Sebasti%C3%A1n-de-La-Gomera/homes?refinement_paths%5B%5D=%2Fhomes&query=San%20Sebasti%C3%A1n%20de%20La%20Gomera&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=28.03574825012823&sw_lng=-17.16376342111588&ne_lat=28.149728591352584&ne_lng=-17.063356578884132&s_tag=8dcmr0Cg',
            # Agulo - Hermigua
            'https://www.airbnb.es/s/Agulo--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&query=Agulo%2C%20Santa%20Cruz%20de%20Tenerife&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=12&search_by_map=true&sw_lat=28.12781547920144&sw_lng=-17.25429074652864&ne_lat=28.35542351807889&ne_lng=-17.05347706206514&s_tag=6rrdOVDv',
            # Alajeró - Playa Santiago
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=Alajer%C3%B3%2C%20La%20Gomera%2C%20Provinz%20Santa%20Cruz%20de%20Tenerife%2C%20Spanien&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=28.012781308186607&sw_lng=-17.27797579061886&ne_lat=28.12678858333975&ne_lng=-17.177568948387112&s_tag=X2jraRiB',
        ],
        'La Gomera 2' : [
            # Valle Gran Rey
            'https://www.airbnb.es/s/Valle-Gran-Rey--La-Gomera--Spanien/homes?refinement_paths%5B%5D=%2Fhomes&query=Valle%20Gran%20Rey%2C%20La%20Gomera%2C%20Spanien&place_id=ChIJ3fabU0AdawwRqOCm30D5HFk&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&s_tag=KswqnFTP',
            'https://www.airbnb.es/s/Valle-Gran-Rey--La-Gomera--Spanien/homes?refinement_paths%5B%5D=%2Fhomes&query=Valle%20Gran%20Rey%2C%20La%20Gomera%2C%20Spanien&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.10060519329533&sw_lng=-17.344608596666394&ne_lat=28.157574282739287&ne_lng=-17.29440517555052&s_tag=UfQYLlSi',
            # Centro de la isla
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=valle%20hermoso%20la%20gomera&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=28.05889258010822&sw_lng=-17.298921225070934&ne_lat=28.172845758932276&ne_lng=-17.198514382839186&s_tag=sx4y3KGT',
        ],
        'La Gomera 3' : [
            # Vallehermoso - Resto de Valle Gran Rey
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=valle%20hermoso%20la%20gomera&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=28.122651928638007&sw_lng=-17.335313436984997&ne_lat=28.236530172792015&ne_lng=-17.234906594753248&s_tag=6iBb0yc3',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=valle%20hermoso%20la%20gomera&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=28.130221781687357&sw_lng=-17.32999193429945&ne_lat=28.24409111885708&ne_lng=-17.2295850920677&s_tag=5NsmEZO6'
        ],
# LANZAROTE -------------
        # Tías
        'Lanzarote Puerto del Carmen' : [
            # - Puerto del Carmen
            'https://www.airbnb.es/s/Puerto-del-Carmen/homes?refinement_paths%5B%5D=%2Fhomes&query=Puerto%20del%20Carmen&map_toggle=true&allow_override%5B%5D=&search_type=UNKNOWN&zoom=16&search_by_map=true&sw_lat=28.920118963687607&sw_lng=-13.68160318113508&ne_lat=28.93424251930726&ne_lng=-13.669052325856109&s_tag=EW1y87rt',
            'https://www.airbnb.es/s/Puerto-del-Carmen/homes?refinement_paths%5B%5D=%2Fhomes&query=Puerto%20del%20Carmen&map_toggle=true&allow_override%5B%5D=&search_type=UNKNOWN&zoom=16&search_by_map=true&sw_lat=28.910257994937336&sw_lng=-13.6720974323863&ne_lat=28.924383036417282&ne_lng=-13.65954657710733&s_tag=PS78Brma',
            'https://www.airbnb.es/s/Puerto-del-Carmen/homes?refinement_paths%5B%5D=%2Fhomes&query=Puerto%20del%20Carmen&map_toggle=true&allow_override%5B%5D=&search_type=UNKNOWN&zoom=16&search_by_map=true&sw_lat=28.910319473508206&sw_lng=-13.659201371442697&ne_lat=28.924444505725923&ne_lng=-13.646650516163726&s_tag=G_dlI_RN',
        ],
        'Lanzarote Puerto del Carmen2' : [
            'https://www.airbnb.es/s/Puerto-del-Carmen/homes?refinement_paths%5B%5D=%2Fhomes&query=Puerto%20del%20Carmen&map_toggle=true&allow_override%5B%5D=&search_type=UNKNOWN&zoom=16&search_by_map=true&sw_lat=28.92403065313944&sw_lng=-13.665368056465587&ne_lat=28.938153619213747&ne_lng=-13.652817201186616&s_tag=xhIbPpbB',
            'https://www.airbnb.es/s/Puerto-del-Carmen/homes?refinement_paths%5B%5D=%2Fhomes&query=Puerto%20del%20Carmen&map_toggle=true&allow_override%5B%5D=&search_type=UNKNOWN&zoom=16&search_by_map=true&sw_lat=28.918640309698322&sw_lng=-13.646227812935313&ne_lat=28.932764088152478&ne_lng=-13.633676957656343&s_tag=YcBk8Grs',
            'https://www.airbnb.es/s/Puerto-del-Carmen/homes?refinement_paths%5B%5D=%2Fhomes&query=Puerto%20del%20Carmen&map_toggle=true&allow_override%5B%5D=&search_type=UNKNOWN&zoom=15&search_by_map=true&sw_lat=28.922165364315973&sw_lng=-13.640284927019033&ne_lat=28.950409697274132&ne_lng=-13.615183216461096&s_tag=g95GrNN2',
        ],
        'Lanzarote Tias' : [
            # - Tías centro - Conil - Montaña Blanca
            'https://www.airbnb.es/s/Tias--Lanzarote--T%C3%ADas--Spanien/homes?refinement_paths%5B%5D=%2Fhomes&query=Tias%2C%20Lanzarote%2C%20T%C3%ADas%2C%20Spanien&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.93525145938239&sw_lng=-13.678073095605459&ne_lat=28.99172358237962&ne_lng=-13.627869674489585&s_tag=HdzS-L53',
            # - La Asomada
            'https://www.airbnb.es/s/Tias--Lanzarote--T%C3%ADas--Spanien/homes?refinement_paths%5B%5D=%2Fhomes&query=Tias%2C%20Lanzarote%2C%20T%C3%ADas%2C%20Spanien&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.93697916021897&sw_lng=-13.71626775197753&ne_lat=28.993450240730578&ne_lng=-13.666064330861655&s_tag=DBHKFP-q',
        ],
        'Lanzarote Tias2' : [
            # - Puerto Calero
            'https://www.airbnb.es/s/Tias--Lanzarote--T%C3%ADas--Spanien/homes?refinement_paths%5B%5D=%2Fhomes&query=Tias%2C%20Lanzarote%2C%20T%C3%ADas%2C%20Spanien&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.913533348017427&sw_lng=-13.712877449191078&ne_lat=28.941780282948137&ne_lng=-13.68777573863314&s_tag=AHEcW7yl',
            # - Macher
            'https://www.airbnb.es/s/Tias--Lanzarote--T%C3%ADas--Spanien/homes?refinement_paths%5B%5D=%2Fhomes&query=Tias%2C%20Lanzarote%2C%20T%C3%ADas%2C%20Spanien&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.93163878576064&sw_lng=-13.702234443819984&ne_lat=28.9598802623032&ne_lng=-13.677132733262047&s_tag=9IZjclcL',
        ],
        'Lanzarote Yaiza': [
            # - Yaiza - Femés - Maicot - Las Breñas - El Golfo - Uga
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=yaiza&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=28.899047392317765&sw_lng=-13.839932671853411&ne_lat=29.01200070219056&ne_lng=-13.739525829621662&s_tag=8H1VgliJ',
            # Uga - La Geria - Barranco del Agua
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=yaiza&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.923146309520938&sw_lng=-13.753633680411685&ne_lat=28.979625735109853&ne_lng=-13.70343025929581&s_tag=MmI1JHue',
         ],
        'Lanzarote Yaiza2': [
            # - Playa Blanca
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=yaiza&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.841602704652313&sw_lng=-13.858627953001369&ne_lat=28.869871294260417&ne_lng=-13.833526242443432&s_tag=yoXh-mE9',
            # - Playa Blanca - Castillo del Águila
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=yaiza&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.84697828556626&sw_lng=-13.83386579937588&ne_lat=28.87524525856182&ne_lng=-13.808764088817943&s_tag=uH4oTFYU',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=yaiza&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.849158511933453&sw_lng=-13.813609756895412&ne_lat=28.877424829185408&ne_lng=-13.788508046337475&s_tag=-_3_JlwQ',
        ],
        'Lanzarote Yaiza3': [
            # - Montaña Roja
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=yaiza&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.84308110492967&sw_lng=-13.898226335191811&ne_lat=28.899608760726004&ne_lng=-13.848022914075937&s_tag=0xG7Cx9s',
            # - Residencial El Pueblito
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=yaiza&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.86855231416669&sw_lng=-13.874311628409732&ne_lat=28.925064639675817&ne_lng=-13.824108207293857&s_tag=ht7l-BUX',
            # - Playa quemada - Papagayo
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=yaiza&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=28.795256354747885&sw_lng=-13.791867486306536&ne_lat=28.908334642903917&ne_lng=-13.691460644074787&s_tag=B1GAd8-X',
        ],
        'Lanzarote Arrecife': [
            # - Arrecife Oeste - Urbanización Playa del Cable
            'https://www.airbnb.es/s/Lanzarote--Arrecife/homes?refinement_paths%5B%5D=%2Fhomes&query=Lanzarote%2C%20Arrecife&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.95547281602313&sw_lng=-13.577569553704288&ne_lat=28.983707102379178&ne_lng=-13.552467843146351&s_tag=UITTqF37',
            # - Arrecife centro
            'https://www.airbnb.es/s/Lanzarote--Arrecife/homes?refinement_paths%5B%5D=%2Fhomes&query=Lanzarote%2C%20Arrecife&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.953144613569915&sw_lng=-13.564094135613468&ne_lat=28.98137960252998&ne_lng=-13.53899242505553&s_tag=zLMWE68G',
            # - Volcan de Tahiche
            'https://www.airbnb.es/s/Lanzarote--Arrecife/homes?refinement_paths%5B%5D=%2Fhomes&query=Lanzarote%2C%20Arrecife&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.968915283853434&sw_lng=-13.565338680596378&ne_lat=28.997145512538655&ne_lng=-13.54023697003844&s_tag=piPbc_Mh',
        ],
        'Lanzarote Arrecife2': [
            # - Arrecife Este
            'https://www.airbnb.es/s/Lanzarote--Arrecife/homes?refinement_paths%5B%5D=%2Fhomes&query=Lanzarote%2C%20Arrecife&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.960701861860457&sw_lng=-13.540190288872745&ne_lat=28.98893457000919&ne_lng=-13.515088578314808&s_tag=Cm8BakrG',
            # - Arrecife Norte - Tahiche
            'https://www.airbnb.es/s/Lanzarote--Arrecife/homes?refinement_paths%5B%5D=%2Fhomes&query=Lanzarote%2C%20Arrecife&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.975430917946564&sw_lng=-13.58655843541148&ne_lat=29.03187878218285&ne_lng=-13.536355014295605&s_tag=fde2FyY0',
            'https://www.airbnb.es/s/Lanzarote--Arrecife/homes?refinement_paths%5B%5D=%2Fhomes&query=Lanzarote%2C%20Arrecife&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.977758648175676&sw_lng=-13.603638742418315&ne_lat=29.034205106080474&ne_lng=-13.553435321302441&s_tag=YC4OuY1O',
        ],
        'Lanzarote San Bartolome': [
            # - Playa Honda
            'https://www.airbnb.es/s/Playa-Honda--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=Playa%20Honda%2C%20Las%20Palmas&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.937338482338774&sw_lng=-13.600585183281973&ne_lat=28.96557823990371&ne_lng=-13.575483472724036&s_tag=7LHTvmEG',
            # - San Bartolome
            'https://www.airbnb.es/s/Playa-Honda--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=Playa%20Honda%2C%20Las%20Palmas&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.956128152261496&sw_lng=-13.630516752977446&ne_lat=29.012587674571485&ne_lng=-13.580313331861571&s_tag=qjrAF8AE',
            # - El Islote - Tao - San Bartolomé
            'https://www.airbnb.es/s/Playa-Honda--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=Playa%20Honda%2C%20Las%20Palmas&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.989093084240977&sw_lng=-13.654806837816313&ne_lat=29.045532692812436&ne_lng=-13.604603416700439&s_tag=S2339cqa',
        ],
        'Lanzarote Haria': [
            # - Haría
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=haria%20lanzarote&map_toggle=true&search_type=UNKNOWN&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=29.127026930721723&sw_lng=-13.5242268643665&ne_lat=29.183382991108026&ne_lng=-13.474023443250626&s_tag=Azj3woEg',
            # - Punta Mujeres - Orzola
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=haria%20lanzarote&map_toggle=true&search_type=UNKNOWN&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=29.097655600994496&sw_lng=-13.474484214572875&ne_lat=29.210368619309882&ne_lng=-13.374077372341127&s_tag=NxCW5rTz',
       ],
        'Lanzarote Haria2': [
            # - Charco del Palo - Mala - Guatiza
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=haria%20lanzarote&map_toggle=true&search_type=UNKNOWN&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=29.021275344853272&sw_lng=-13.482552299289672&ne_lat=29.134080951093413&ne_lng=-13.382145457057923&s_tag=zjGkxCt6',
            # - Los Valles - Teguesite -
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=haria%20lanzarote&map_toggle=true&search_type=UNKNOWN&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=29.04624323813962&sw_lng=-13.546628674058883&ne_lat=29.10264827402119&ne_lng=-13.496425252943009&s_tag=1OGZVP1t',
            # - La Graciosa
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=haria%20lanzarote&map_toggle=true&search_type=UNKNOWN&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=29.19941373843746&sw_lng=-13.55851245859143&ne_lat=29.312003062128323&ne_lng=-13.458105616359681&s_tag=4tgV1j9U',
        ],
        'Lanzarote Tinajo': [
            # - Tinajo centro: Tiagua, Soo, El cuchillo, Tajaste, Mancha Blanca, Tinguatón - Tajaste
            'https://www.airbnb.es/s/Tinajo--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=Tinajo%2C%20Las%20Palmas&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=29.03128671341957&sw_lng=-13.694736819078361&ne_lat=29.087700803168243&ne_lng=-13.644533397962487&s_tag=Woignr9p',
            'https://www.airbnb.es/s/Tinajo--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=Tinajo%2C%20Las%20Palmas&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=29.046445366937057&sw_lng=-13.659202914049065&ne_lat=29.102850280431745&ne_lng=-13.60899949293319&s_tag=0fAPos4K',
            # - La Santa - Urb. La Santa Sport
            'https://www.airbnb.es/s/Tinajo--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=Tinajo%2C%20Las%20Palmas&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=29.085232370277133&sw_lng=-13.672849993516838&ne_lat=29.141613784283305&ne_lng=-13.622646572400964&s_tag=w1plBfnN',

        ],
        'Lanzarote Teguise': [
            # - Famara
            'https://www.airbnb.es/s/Teguise/homes?refinement_paths%5B%5D=%2Fhomes&query=Teguise&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=29.108223413488695&sw_lng=-13.581848474297553&ne_lat=29.136411490230337&ne_lng=-13.556746763739616&s_tag=_0147phi',
            'https://www.airbnb.es/s/Teguise/homes?refinement_paths%5B%5D=%2Fhomes&query=Teguise&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=29.089861053966754&sw_lng=-13.563328620348006&ne_lat=29.14623966173121&ne_lng=-13.513125199232132&s_tag=KJUVyLpa',
            # - Teguise
            'https://www.airbnb.es/s/Teguise/homes?refinement_paths%5B%5D=%2Fhomes&query=Teguise&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=28.994882012789233&sw_lng=-13.617355272922545&ne_lat=29.107719561483268&ne_lng=-13.516948430690796&s_tag=fU8w1KPL',
        ],
        'Lanzarote Teguise2' : [
            # - Zonas intermedias
            'https://www.airbnb.es/s/Teguise/homes?refinement_paths%5B%5D=%2Fhomes&query=Teguise&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.99776916164594&sw_lng=-13.542664882097274&ne_lat=29.05420352566486&ne_lng=-13.4924614609814&s_tag=LXsdE2C4',
            'https://www.airbnb.es/s/Teguise/homes?refinement_paths%5B%5D=%2Fhomes&query=Teguise&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=29.055277608695636&sw_lng=-13.614054557237655&ne_lat=29.111677173601816&ne_lng=-13.56385113612178&s_tag=cKpsxueV',
        ],
        'Lanzarote Costa Teguise': [
            # - Centro
            'https://www.airbnb.es/s/Teguise/homes?refinement_paths%5B%5D=%2Fhomes&query=Teguise&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.991709179812553&sw_lng=-13.502209265682728&ne_lat=29.005821934277876&ne_lng=-13.489658410403758&s_tag=QpF5k-dt',
            # - Las Caletas
            'https://www.airbnb.es/s/Teguise/homes?refinement_paths%5B%5D=%2Fhomes&query=Teguise&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.9733006000375&sw_lng=-13.52425608232978&ne_lat=29.001529504623075&ne_lng=-13.499154371771843&s_tag=Tib8IKI4',
            # - Centro - Los Ancones
            'https://www.airbnb.es/s/Teguise/homes?refinement_paths%5B%5D=%2Fhomes&query=Teguise&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.997645514759373&sw_lng=-13.49355015352729&ne_lat=29.02586706533102&ne_lng=-13.468448442969352&s_tag=dLUG3rq3',
        ],
# FUERTEVENTURA ----------
        'Fuerteventura La Oliva': [
            # La Oliva
            # - La Oliva
            'https://www.airbnb.es/s/El-Cotillo-Fuerteventura--El-Cotillo--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=El%20Cotillo%20Fuerteventura%2C%20El%20Cotillo%2C%20Espa%C3%B1a&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=28.56409613617585&sw_lng=-13.953562979593052&ne_lat=28.677451298987695&ne_lng=-13.853156137361303&s_tag=ZYB7TfTj',
            # - Lajares
            'https://www.airbnb.es/s/El-Cotillo-Fuerteventura--El-Cotillo--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=El%20Cotillo%20Fuerteventura%2C%20El%20Cotillo%2C%20Espa%C3%B1a&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.649235823460607&sw_lng=-13.956098750724568&ne_lat=28.70587974361009&ne_lng=-13.905895329608693&s_tag=X67xhLt3',
            # - El Roscón - El Cotillo
            'https://www.airbnb.es/s/El-Cotillo-Fuerteventura--El-Cotillo--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=El%20Cotillo%20Fuerteventura%2C%20El%20Cotillo%2C%20Espa%C3%B1a&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.67600314059237&sw_lng=-14.009766271605267&ne_lat=28.70432139652573&ne_lng=-13.98466456104733&s_tag=EbOPpF14',
        ],
        'Fuerteventura La Oliva2': [
            # - Parque holandés - La Oliva
            'https://www.airbnb.es/s/El-Cotillo-Fuerteventura--El-Cotillo--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=El%20Cotillo%20Fuerteventura%2C%20El%20Cotillo%2C%20Espa%C3%B1a&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=28.58897100583523&sw_lng=-13.92489552964188&ne_lat=28.702296472229122&ne_lng=-13.824488687410131&s_tag=YCXwtCsd',
            #  - Tindaya - La Tasca
            'https://www.airbnb.es/s/El-Cotillo-Fuerteventura--El-Cotillo--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=El%20Cotillo%20Fuerteventura%2C%20El%20Cotillo%2C%20Espa%C3%B1a&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=28.557537236529797&sw_lng=-14.059306387796177&ne_lat=28.670900225637034&ne_lng=-13.958899545564428&s_tag=l9ggJTis',
            # - Majancho
            'https://www.airbnb.es/s/El-Cotillo-Fuerteventura--El-Cotillo--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=El%20Cotillo%20Fuerteventura%2C%20El%20Cotillo%2C%20Espa%C3%B1a&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.685987686551602&sw_lng=-13.959188655509724&ne_lat=28.74260961870321&ne_lng=-13.90898523439385&s_tag=mFhKSCAt',
        ],
        'Fuerteventura El Cotillo':[
            # - El Cotillo
            'https://www.airbnb.es/s/El-Cotillo-Fuerteventura--El-Cotillo--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=El%20Cotillo%20Fuerteventura%2C%20El%20Cotillo%2C%20Espa%C3%B1a&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.686981600994326&sw_lng=-14.019168152523553&ne_lat=28.701140162025826&ne_lng=-14.006617297244583&s_tag=hb_yJ1L0',
            'https://www.airbnb.es/s/El-Cotillo-Fuerteventura--El-Cotillo--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=El%20Cotillo%20Fuerteventura%2C%20El%20Cotillo%2C%20Espa%C3%B1a&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.68012060312897&sw_lng=-14.01385000590898&ne_lat=28.68720066551994&ne_lng=-14.007574578269496&s_tag=rJVUrKUH',
            'https://www.airbnb.es/s/El-Cotillo-Fuerteventura--El-Cotillo--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=El%20Cotillo%20Fuerteventura%2C%20El%20Cotillo%2C%20Espa%C3%B1a&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.686219773073425&sw_lng=-14.014128955646528&ne_lat=28.69329937935619&ne_lng=-14.007853528007045&s_tag=1uMG3fvq',
        ],
        'Fuerteventura Corralejo': [
            # - Corralejo sur
            'https://www.airbnb.es/s/El-Cotillo-Fuerteventura--El-Cotillo--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=El%20Cotillo%20Fuerteventura%2C%20El%20Cotillo%2C%20Espa%C3%B1a&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.64720204500415&sw_lng=-13.908891872062458&ne_lat=28.703847181175817&ne_lng=-13.858688450946584&s_tag=LMPDFMpX',
            # - Geafond
            'https://www.airbnb.es/s/El-Cotillo-Fuerteventura--El-Cotillo--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=El%20Cotillo%20Fuerteventura%2C%20El%20Cotillo%2C%20Espa%C3%B1a&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.693359329981458&sw_lng=-13.881063154234662&ne_lat=28.7216723927393&ne_lng=-13.855961443676724&s_tag=p8T--HH1',
            '',
         ],
        'Fuerteventura Corralejo2': [
            'https://www.airbnb.es/s/El-Cotillo-Fuerteventura--El-Cotillo--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=El%20Cotillo%20Fuerteventura%2C%20El%20Cotillo%2C%20Espa%C3%B1a&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.717288390328243&sw_lng=-13.875173964693323&ne_lat=28.731442415463153&ne_lng=-13.862623109414352&s_tag=dloMlTlv',
            'https://www.airbnb.es/s/El-Cotillo-Fuerteventura--El-Cotillo--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=El%20Cotillo%20Fuerteventura%2C%20El%20Cotillo%2C%20Espa%C3%B1a&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.730021218887263&sw_lng=-13.870375636394614&ne_lat=28.737097547003437&ne_lng=-13.864100208755131',
        ],
        'Fuerteventura Corralejo3': [
            'https://www.airbnb.es/s/El-Cotillo-Fuerteventura--El-Cotillo--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=El%20Cotillo%20Fuerteventura%2C%20El%20Cotillo%2C%20Espa%C3%B1a&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.729654302910674&sw_lng=-13.874774459179038&ne_lat=28.736730658506378&ne_lng=-13.868499031539555&s_tag=EtZK4haM',
            'https://www.airbnb.es/s/El-Cotillo-Fuerteventura--El-Cotillo--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=El%20Cotillo%20Fuerteventura%2C%20El%20Cotillo%2C%20Espa%C3%B1a&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.735016792873857&sw_lng=-13.872671607311363&ne_lat=28.74209274682306&ne_lng=-13.866396179671879&s_tag=RAGMQQD3',
            'https://www.airbnb.es/s/El-Cotillo-Fuerteventura--El-Cotillo--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=El%20Cotillo%20Fuerteventura%2C%20El%20Cotillo%2C%20Espa%C3%B1a&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.740162642934944&sw_lng=-13.870107415493125&ne_lat=28.747238211399367&ne_lng=-13.863831987853642&s_tag=99JLih9T',
        ],
        'Fuerteventura Corralejo4':[
            # - Este
            'https://www.airbnb.es/s/El-Cotillo-Fuerteventura--El-Cotillo--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=El%20Cotillo%20Fuerteventura%2C%20El%20Cotillo%2C%20Espa%C3%B1a&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.707099174621895&sw_lng=-13.863553693785443&ne_lat=28.735408124219994&ne_lng=-13.838451983227506&s_tag=iEbojGw8',
            # - Oeste
            'https://www.airbnb.es/s/El-Cotillo-Fuerteventura--El-Cotillo--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=El%20Cotillo%20Fuerteventura%2C%20El%20Cotillo%2C%20Espa%C3%B1a&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.732467034963413&sw_lng=-13.882476751058226&ne_lat=28.746618786724984&ne_lng=-13.869925895779255&s_tag=DRnWr2Vh',
            'https://www.airbnb.es/s/El-Cotillo-Fuerteventura--El-Cotillo--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=El%20Cotillo%20Fuerteventura%2C%20El%20Cotillo%2C%20Espa%C3%B1a&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.723115169732896&sw_lng=-13.885394994466429&ne_lat=28.73726832229497&ne_lng=-13.872844139187459&s_tag=DGUa2TZT',
        ],
        'Fuerteventura Pto Rosario': [
            # - Puerto del Rosario centro
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=Puerto%20del%20Rosario&map_toggle=true&search_type=UNKNOWN&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.472951035098777&sw_lng=-13.886908403673164&ne_lat=28.529700065157783&ne_lng=-13.83670498255729&s_tag=oXVY1lDc',
            # - Playa Blanca
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=Puerto%20del%20Rosario&map_toggle=true&search_type=UNKNOWN&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.43967206368936&sw_lng=-13.912142626085274&ne_lat=28.49644086978404&ne_lng=-13.8619392049694&s_tag=3vKPalFz',
            # Puerto Lajas
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=Puerto%20del%20Rosario&map_toggle=true&search_type=UNKNOWN&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.501864337405873&sw_lng=-13.879956117906563&ne_lat=28.558596168556456&ne_lng=-13.829752696790688&s_tag=hjYFN9pA',
        ],
        'Fuerteventura Pto Rosario2': [
            # - Tetir
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=Puerto%20del%20Rosario&map_toggle=true&search_type=UNKNOWN&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=28.48640956564011&sw_lng=-13.974409024753562&ne_lat=28.599857321278982&ne_lng=-13.874002182521814&s_tag=LUHvkqpK',
            # - Teífa
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=Puerto%20del%20Rosario&map_toggle=true&search_type=UNKNOWN&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=28.491086919914025&sw_lng=-14.05062667612075&ne_lat=28.604529107234704&ne_lng=-13.950219833889001&s_tag=MnHdOc_T',
        ],
        'Fuerteventura Pajara': [
            # - Costa Calma
            'https://www.airbnb.es/s/La-Lajita--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=La%20Lajita%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.154610289937484&sw_lng=-14.234596396719798&ne_lat=28.211547626473518&ne_lng=-14.184392975603924&search_type=UNKNOWN&s_tag=dgLA7aPK',
            'https://www.airbnb.es/s/La-Lajita--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=La%20Lajita%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.106098916336236&sw_lng=-14.264865274383983&ne_lat=28.163064778237143&ne_lng=-14.214661853268108&search_type=UNKNOWN&s_tag=k1MZDPgD',
            # - Pajara
            "https://www.airbnb.es/s/P%C3%A1jara--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=P%C3%A1jara%2C%20Las%20Palmas&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=28.155499495407646&sw_lng=-14.216184115350792&ne_lat=28.26933907394295&ne_lng=-14.115777273119043&s_tag=ViK_9GLw",
        ],
        'Fuerteventura Pajara2': [
            # - Esquinazo
            'https://www.airbnb.es/s/Morro-Jable/homes?refinement_paths%5B%5D=%2Fhomes&query=Morro%20Jable&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.05327536886764&sw_lng=-14.321834114251041&ne_lat=28.081778047910127&ne_lng=-14.296732403693104&search_type=UNKNOWN&s_tag=WSTmX5Xl',
            # - Morro Jable
            'https://www.airbnb.es/s/Morro-Jable/homes?refinement_paths%5B%5D=%2Fhomes&query=Morro%20Jable&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.039185428327386&sw_lng=-14.350029495415592&ne_lat=28.067692237200788&ne_lng=-14.324927784857655&search_type=UNKNOWN&s_tag=mtTIDeHs',
            'https://www.airbnb.es/s/Morro-Jable/homes?refinement_paths%5B%5D=%2Fhomes&query=Morro%20Jable&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.04664726654663&sw_lng=-14.373203781304264&ne_lat=28.075151888555773&ne_lng=-14.348102070746327&search_type=UNKNOWN',
        ],
        'Fuerteventura Pajara3': [
            # La Lajita
            'https://www.airbnb.es/s/La-Lajita--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=La%20Lajita%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=12&search_by_map=true&sw_lat=28.14577772126996&sw_lng=-14.225350863227805&ne_lat=28.373343421311144&ne_lng=-14.024537178764303&search_type=UNKNOWN&s_tag=ch3XVXq8',
            # - Ajuy
            "https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=ajuy%20fuerteventura&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&is_user_submitted_query=true&allow_override%5B%5D=&map_toggle=true&s_tag=6BT2BPH_",
            # - Jandía
            'https://www.airbnb.es/s/La-Lajita--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=La%20Lajita%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&zoom=11&search_by_map=true&sw_lat=27.965463248995082&sw_lng=-14.664733845081773&ne_lat=28.420897701728876&ne_lng=-14.263106476154771&search_type=UNKNOWN&s_tag=fxD61zSB',
        ],
        "Fuerteventura Betancuria": [
            "https://www.airbnb.es/s/Betancuria--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJt3cGxDq7RwwRUBNNvvNAAwQ&query=Betancuria%2C%20Las%20Palmas&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=lr9wzhYD",
        ],
        'Fuerteventura Antigua': [
            # - Antigua casco
            "https://www.airbnb.es/s/Antigua--Fuerteventura--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJJbEGZvu7RwwRuUYQC3VGftw&query=Antigua%2C%20Fuerteventura%2C%20Las%20Palmas&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=0TOCC4Ck",
            # - Almacigo
            "https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=Almacigo%20Fuerteventura&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=YGaHzCZq",
            # - Salinas del Carmen - Pozo Negro
            "https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=Pozo%20negro%20fuerteventura&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=28.261899750034413&sw_lng=-13.966644907932313&ne_lat=28.375613798971507&ne_lng=-13.866238065700564&s_tag=FjOsg6Ay",
        ],
        'Fuerteventura Antigua2': [
            # - El Matorral - Caleta blanca
            "https://www.airbnb.es/s/El-Matorral--Puerto-del-Rosario/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&query=El%20Matorral%2C%20Puerto%20del%20Rosario&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.40777016184625&sw_lng=-13.895431112718615&ne_lat=28.46455790578874&ne_lng=-13.84522769160274&s_tag=6OtchJRl",
            # - Castillo Caleta de Fuste
            'https://www.airbnb.es/s/Caleta-de-Fuste/homes?refinement_paths%5B%5D=%2Fhomes&query=Caleta%20de%20Fuste&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.379749613742547&sw_lng=-13.875806045708723&ne_lat=28.408156068786766&ne_lng=-13.850704335150786&s_tag=tpsQRy4m',
            'https://www.airbnb.es/s/Caleta-de-Fuste/homes?refinement_paths%5B%5D=%2Fhomes&query=Caleta%20de%20Fuste&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.373406064700884&sw_lng=-13.889238548455305&ne_lat=28.401814399143966&ne_lng=-13.864136837897368&s_tag=H2VTk1eS',
        ],
        'Fuerteventura Tuineje': [
             # - Tuineje
            "https://www.airbnb.es/s/Gran-Tarajal--Tuineje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&refinemenhttps%3A%2F%2Fwww.airbnb.es%2Fs%2FTuineje--Las-Palmas%2Fhomes%3Frefinement_paths%5B%5D=%2Fhomes&query%5B%5D=Tuineje%2C%20Las%20Palmas&query%5B%5D=Gran%20Tarajal%2C%20Tuineje%2C%20Espa%C3%B1a&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&adults=0&children=0&infants=0&toddlers=0&zoom=13&search_by_map=true&sw_lat=28.21487401889729&sw_lng=-14.116407627658909&ne_lat=28.328643601562543&ne_lng=-14.01600078542716&s_tag=LCRf7xwf",
            # - Gran Tarajal
            "https://www.airbnb.es/s/Gran-Tarajal--Tuineje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&toddlers=0&query=Gran%20Tarajal%2C%20Tuineje%2C%20Espa%C3%B1a&allow_override%5B%5D=&map_toggle=true&zoom=12&search_by_map=true&sw_lat=28.064528550506207&sw_lng=-14.15699801166541&ne_lat=28.29228556672055&ne_lng=-13.956184327201909&s_tag=4plNtrJO",
        ],
# TENERIFE -----------------

        #Zona metropolitana
        'Tenerife Anaga' : [
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&zoom=12&search_by_map=true&sw_lat=28.478831615576627&sw_lng=-16.223669133529896&ne_lat=28.705607814014947&ne_lng=-16.022855449066398&s_tag=_vIP4LJJ',
            # Valleseco
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.478954724634608&sw_lng=-16.247927600488897&ne_lat=28.535700184747466&ne_lng=-16.197724179373022&s_tag=0Ps8Skas',
            # Barrio de la Alegría
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.473458923406216&sw_lng=-16.250580447361703&ne_lat=28.487649317301422&ne_lng=-16.238029592082736&s_tag=DOBr4bno',
        ],
        'Tenerife SC centro' : [
            # - El toscal
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.46910994476742&sw_lng=-16.252603303686616&ne_lat=28.47620573228955&ne_lng=-16.24632787604713&s_tag=_BYET-aG',
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.462293648474116&sw_lng=-16.253150474325654&ne_lat=28.46938994219343&ne_lng=-16.246875046686167&s_tag=BCVfflsP',
            # - Zona Centro
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.466792532788133&sw_lng=-16.256476343943238&ne_lat=28.473888492420205&ne_lng=-16.25020091630375&s_tag=wTYWQbPc',
        ],
        'Tenerife SC centro2':[
            # - Tres de mayo
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.43369708818798&sw_lng=-16.266639148112755&ne_lat=28.462087544700253&ne_lng=-16.241537437554815&s_tag=h8L3mGAs',
            # - Los Campitos - Ifara
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.47444489361908&sw_lng=-16.26607146125696&ne_lat=28.488635141022083&ne_lng=-16.253520605977993&s_tag=t_s4bS4a',
            # - La Salud
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.464051136857897&sw_lng=-16.28545099382921&ne_lat=28.482887724410244&ne_lng=-16.2689365542795&s_tag=2RBinbkG',
          ],
        'Tenerife SC centro3':[
            # - Duggi
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.46195599809333&sw_lng=-16.26352231215267&ne_lat=28.47137495196162&ne_lng=-16.255265092377815&s_tag=7mjqlWBm',
            # - Salamanca
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.467258208457917&sw_lng=-16.268946789320925&ne_lat=28.481449523528497&ne_lng=-16.256395934041958&s_tag=61x4Uu_I',
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.466512959717043&sw_lng=-16.26722984843607&ne_lat=28.475931475023735&ne_lng=-16.258972628661216&s_tag=jI2qoXbj',
        ],
        'Tenerife barrios del medio' : [
            # - La Salud
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.45569435321707&sw_lng=-16.274997852858522&ne_lat=28.469887385717715&ne_lng=-16.262446997579556&s_tag=5oQfvPEE',
            # - Desde Cruz del señor hasta la Cuesta
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.458461523024575&sw_lng=-16.288354312297326&ne_lat=28.486844626138943&ne_lng=-16.263252601739385&s_tag=LixMYk4R',
            # - Ofra
            'https://www.airbnb.es/s/La-Laguna--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=La%20Laguna%2C%20Santa%20Cruz%20de%20Tenerife&zoom=15&search_by_map=true&sw_lat=28.443854682379396&sw_lng=-16.290314308379276&ne_lat=28.47224212346762&ne_lng=-16.265212597821336&allow_override%5B%5D=&s_tag=iKY2g-4v',
        ],
        'Tenerife barrios del medio2' : [
            # La Cuesta - Finca España
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.457809477473017&sw_lng=-16.304104243632775&ne_lat=28.48619277427691&ne_lng=-16.279002533074834&s_tag=9QE8kFOO',
            # La Cuesta - Taco
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.444074768305903&sw_lng=-16.31174317490719&ne_lat=28.47246214404762&ne_lng=-16.28664146434925&s_tag=NuwvQ5m9',
            # Geneto - Las Chumberas
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.453363424373453&sw_lng=-16.32483942045361&ne_lat=28.4817480417648&ne_lng=-16.29973770989567&s_tag=JzHczP2w',
        ],
        'Tenerife barrios oeste' : [
            # Taco - Sobradillo - Añaza
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.39865504224423&sw_lng=-16.32937514130403&ne_lat=28.455448193600425&ne_lng=-16.279171720188156&s_tag=CGEjTEBY',
            # Radazul - Tabaiba
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.390817114110792&sw_lng=-16.343128194429266&ne_lat=28.41922028927287&ne_lng=-16.318026483871325&s_tag=TfDp_X2w',
         ],
        'Tenerife barrios oeste2':[
          # - Chorrillo - Radazul
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.405589644422296&sw_lng=-16.341615006365927&ne_lat=28.443281642107078&ne_lng=-16.30858612726651&s_tag=prbfc0hw',
            # - LLano del Moro -  Geneto - El tablero
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.41399952682205&sw_lng=-16.36876822970091&ne_lat=28.470783574369868&ne_lng=-16.318564808585034&s_tag=41RbIqNg',
        ],
        'Tenerife LL centro' : [
            'https://www.airbnb.es/s/La-Laguna--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=La%20Laguna%2C%20Santa%20Cruz%20de%20Tenerife&zoom=15&search_by_map=true&sw_lat=28.46960581735279&sw_lng=-16.33090893188456&ne_lat=28.497985609437197&ne_lng=-16.30580722132662',
            'https://www.airbnb.es/s/La-Laguna--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=La%20Laguna%2C%20Santa%20Cruz%20de%20Tenerife&zoom=15&search_by_map=true&sw_lat=28.48953320330136&sw_lng=-16.326924018184865&ne_lat=28.51790707189358&ne_lng=-16.301822307626924&allow_override%5B%5D=&s_tag=UG30wz5M',
            'https://www.airbnb.es/s/La-Laguna--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=La%20Laguna%2C%20Santa%20Cruz%20de%20Tenerife&zoom=15&search_by_map=true&sw_lat=28.477457370108358&sw_lng=-16.358513566480962&ne_lat=28.50583482874142&ne_lng=-16.33341185592302&allow_override%5B%5D=&s_tag=MnILGynF',
        ],
        'Tenerife La Esperanza' : [
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.42336020801838&sw_lng=-16.399838938929424&ne_lat=28.480138699709638&ne_lng=-16.34963551781355&s_tag=dsmxLnGD',
        ],
        'Tenerife Tegueste' : [
            # - Las Mercedes - Pedro Álvarez
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.498606216391444&sw_lng=-16.315188396832557&ne_lat=28.573903910028076&ne_lng=-16.249130638633712&s_tag=rJ6S5_lt',
            # - Casco
            'https://www.airbnb.es/s/La-Laguna--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=La%20Laguna%2C%20Santa%20Cruz%20de%20Tenerife&zoom=13&search_by_map=true&sw_lat=28.5111163362891&sw_lng=-16.344066904412593&ne_lat=28.62453466945949&ne_lng=-16.243660062180844&allow_override%5B%5D=&s_tag=IYd88i9Z',
        ],
        'Tenerife Tejina' : [
            'https://www.airbnb.es/s/La-Laguna--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=La%20Laguna%2C%20Santa%20Cruz%20de%20Tenerife&zoom=14&search_by_map=true&sw_lat=28.523734256546366&sw_lng=-16.379769460533243&ne_lat=28.580453067900134&ne_lng=-16.32956603941737&allow_override%5B%5D=&s_tag=_xOXf32q',
            'https://www.airbnb.es/s/La-Laguna--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=La%20Laguna%2C%20Santa%20Cruz%20de%20Tenerife&zoom=13&search_by_map=true&sw_lat=28.52706293174313&sw_lng=-16.33921069440661&ne_lat=28.640462262281904&ne_lng=-16.23880385217486',
        ],
        'Tenerife LL Resto' : [
            # - Valle Guerra
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.507307988828757&sw_lng=-16.406808945736074&ne_lat=28.544960826520814&ne_lng=-16.373780066636655&s_tag=QhYPFkfj',
            # - Guamasa - Portezuelo
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.477602374712088&sw_lng=-16.387958489112393&ne_lat=28.515266661851175&ne_lng=-16.354929610012974&s_tag=B1QHL82l',
        ],
        'Tenerife Tacoronte' : [
            'https://www.airbnb.es/s/La-Laguna--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=La%20Laguna%2C%20Santa%20Cruz%20de%20Tenerife&zoom=14&search_by_map=true&sw_lat=28.461480049120865&sw_lng=-16.429379598472696&ne_lat=28.51823589820501&ne_lng=-16.379176177356822&allow_override%5B%5D=&s_tag=RcAsL4cW',
        ],
        'Tenerife Sauzal' : [
            'https://www.airbnb.es/s/El-Sauzal/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&allow_override%5B%5D=&map_toggle=true&s_tag=iztYbVLN',
        ],
        'Tenerife Matanza' : [
            'https://www.airbnb.es/s/La-Matanza-de-Acentejo--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=La%20Matanza%20de%20Acentejo%2C%20Santa%20Cruz%20de%20Tenerife&place_id=ChIJS_gfL5rUQQwRG3hz8pzB1HU&allow_override%5B%5D=&s_tag=qL5T4qUy',
        ],
        'Tenerife Victoria' : [
            'https://www.airbnb.es/s/La-Victoria-de-Acentejo/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=La%20Victoria%20de%20Acentejo&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.418513633346215&sw_lng=-16.488807423558555&ne_lat=28.456200662600907&ne_lng=-16.455778544459136',
        ],
        'Tenerife Santa Ursula' : [
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&query=Santa%20Ursula&search_type=AUTOCOMPLETE_CLICK&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.40544017402148&sw_lng=-16.52172334476939&ne_lat=28.45137476585284&ne_lng=-16.47824982718577&s_tag=4a2hwtMT',
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&query=Santa%20Ursula&search_type=AUTOCOMPLETE_CLICK&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.382465832485575&sw_lng=-16.498720720257673&ne_lat=28.42841169382418&ne_lng=-16.45524720267405&s_tag=AY4uZ9sT',
        ],
        'Tenerife Puerto de la Cruz' : [
            # - Botanico
            'https://www.airbnb.es/s/Puerto-de-la-Cruz--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Puerto%20de%20la%20Cruz%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.400426366688695&sw_lng=-16.53259964275258&ne_lat=28.419275189402445&ne_lng=-16.51608520320287&s_tag=saG-VjhG',
            'https://www.airbnb.es/s/Puerto-de-la-Cruz--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Puerto%20de%20la%20Cruz%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.395856069000985&sw_lng=-16.548510551187682&ne_lat=28.41470576962589&ne_lng=-16.531996111637973&s_tag=usHKe69H',
            'https://www.airbnb.es/s/Puerto-de-la-Cruz--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Puerto%20de%20la%20Cruz%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.4124920965383&sw_lng=-16.545905436020714&ne_lat=28.42191580666923&ne_lng=-16.53764821624586&s_tag=nTPDumcM',
        ],
        'Tenerife Puerto de la Cruz2' : [
            # - Centro
            'https://www.airbnb.es/s/Puerto-de-la-Cruz--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Puerto%20de%20la%20Cruz%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.41380162750235&sw_lng=-16.549563969117028&ne_lat=28.423225211811403&ne_lng=-16.541306749342173&s_tag=VbkNngEd',
            'https://www.airbnb.es/s/Puerto-de-la-Cruz--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Puerto%20de%20la%20Cruz%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.41379219109739&sw_lng=-16.554381216507775&ne_lat=28.42321577631313&ne_lng=-16.54612399673292&s_tag=AEBP0gir',
            'https://www.airbnb.es/s/Puerto-de-la-Cruz--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Puerto%20de%20la%20Cruz%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.409949340727675&sw_lng=-16.55953105781637&ne_lat=28.41937329515558&ne_lng=-16.551273838041514&s_tag=fDngOxUz',
        ],
        'Tenerife Puerto de la Cruz3':[
             # - Centro
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.411985946330713&sw_lng=-16.55281779477505&ne_lat=28.421409705091968&ne_lng=-16.544560575000194&s_tag=_jB8XKOK',
             # - Punta Brava - Playa Jardin
            'https://www.airbnb.es/s/Puerto-de-la-Cruz--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Puerto%20de%20la%20Cruz%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.39803907802924&sw_lng=-16.569772786530102&ne_lat=28.4168883593348&ne_lng=-16.553258346980392&s_tag=oG_Ku-FZ',
            'https://www.airbnb.es/s/Puerto-de-la-Cruz--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Puerto%20de%20la%20Cruz%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.392149703949467&sw_lng=-16.57605988446101&ne_lat=28.411000116437165&ne_lng=-16.5595454449113&s_tag=mbgyKGFJ',
        ],
        'Tenerife Puerto de la Cruz4':[
            #TF-312 - Taoro - Durazno
            'https://www.airbnb.es/s/Puerto-de-la-Cruz--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Puerto%20de%20la%20Cruz%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.393622078148077&sw_lng=-16.560524529846752&ne_lat=28.41247220785449&ne_lng=-16.544010090297043&s_tag=EC6NiuJw',
            'https://www.airbnb.es/s/Puerto-de-la-Cruz--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Puerto%20de%20la%20Cruz%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.39509443189468&sw_lng=-16.551898545654858&ne_lat=28.413944278810316&ne_lng=-16.53538410610515&s_tag=oXDfpPSw',
            'https://www.airbnb.es/s/Puerto-de-la-Cruz--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Puerto%20de%20la%20Cruz%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.393964528560428&sw_lng=-16.53628482289701&ne_lat=28.41281459249457&ne_lng=-16.5197703833473&s_tag=IwLbOsnH',
        ],
        'Tenerife Orotava' : [
            'https://www.airbnb.es/s/La-Orotava--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=La%20Orotava%2C%20Santa%20Cruz%20de%20Tenerife&zoom=14&search_by_map=true&sw_lat=28.32593201511869&sw_lng=-16.553808400583737&ne_lat=28.401362529527844&ne_lng=-16.487750642384892&allow_override%5B%5D=&s_tag=zpG-Qb85',
            #Teide
            'https://www.airbnb.es/s/La-Orotava--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=La%20Orotava%2C%20Santa%20Cruz%20de%20Tenerife&zoom=13&search_by_map=true&sw_lat=28.210413577370208&sw_lng=-16.651896941548394&ne_lat=28.361393048883098&ne_lng=-16.519781425150704&allow_override%5B%5D=&s_tag=srG3EW6K',
        ],
        'Tenerife Realejos' : [
            'https://www.airbnb.es/s/La-Orotava--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=La%20Orotava%2C%20Santa%20Cruz%20de%20Tenerife&zoom=14&search_by_map=true&sw_lat=28.325384136978688&sw_lng=-16.606594273996823&ne_lat=28.400815071639855&ne_lng=-16.540536515797978&allow_override%5B%5D=&s_tag=ltf3ZJZO',
            'https://www.airbnb.es/s/La-Orotava--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=La%20Orotava%2C%20Santa%20Cruz%20de%20Tenerife&zoom=14&search_by_map=true&sw_lat=28.33251925768096&sw_lng=-16.639553258371823&ne_lat=28.407944718738353&ne_lng=-16.573495500172978'],
        'Tenerife La Guancha' : [
            'https://www.airbnb.es/s/La-Guancha--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=La%20Guancha%2C%20Santa%20Cruz%20de%20Tenerife&place_id=ChIJv4y8tjuHagwRkDBNvvNAAwQ&map_toggle=true',
        ],
        'Tenerife San Juan de la Rambla' : [
            'https://www.airbnb.es/s/San-Juan-de-la-Rambla--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=San%20Juan%20de%20la%20Rambla%2C%20Santa%20Cruz%20de%20Tenerife&place_id=ChIJT_4kj_99agwRBE0pL7vWS4o&allow_override%5B%5D=&s_tag=QG80vyFG',
        ],
        'Tenerife Icod' : [
            # - San Marcos
            'https://www.airbnb.es/s/Icod-de-los-Vinos--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Icod%20de%20los%20Vinos%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.286835956198114&sw_lng=-16.742337662871453&ne_lat=28.36229644071435&ne_lng=-16.676279904672608&s_tag=yc_hXUw-',
            # Lanito Perera - Cueva del viento - El amparo
            'https://www.airbnb.es/s/Icod-de-los-Vinos--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Icod%20de%20los%20Vinos%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.346229655537336&sw_lng=-16.754705249994103&ne_lat=28.38394444667952&ne_lng=-16.721676370894684&s_tag=sJbeK7zD',
            # - Buen Paso - Mancha
            'https://www.airbnb.es/s/Icod-de-los-Vinos--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Icod%20de%20los%20Vinos%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.358722153342388&sw_lng=-16.700897883763545&ne_lat=28.39643215115731&ne_lng=-16.667869004664126&s_tag=jSzM-Yj6',
        ],
        'Tenerife Icod2' : [
            # - Centro
            'https://www.airbnb.es/s/Icod-de-los-Vinos--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Icod%20de%20los%20Vinos%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.36190644056212&sw_lng=-16.71799695605603&ne_lat=28.38488727855158&ne_lng=-16.69626019726422&s_tag=gMgWqrZn',
            'https://www.airbnb.es/s/Icod-de-los-Vinos--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Icod%20de%20los%20Vinos%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.348770369055483&sw_lng=-16.720029651849572&ne_lat=28.386484185491604&ne_lng=-16.687000772750153&s_tag=IrdCbag0',
        ],
        'Tenerife Silos' : [
            'https://www.airbnb.es/s/Los-Silos--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Los%20Silos%2C%20Santa%20Cruz%20de%20Tenerife&place_id=ChIJSyR4ZvmJagwREDJNvvNAAwQ&map_toggle=true'
        ],
        'Tenerife Garachico' : [
            'https://www.airbnb.es/s/Garachico--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Garachico%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.33295225172908&sw_lng=-16.80082072053003&ne_lat=28.40837738058082&ne_lng=-16.734762962331185&s_tag=02ahxCGH',
            # - Los Cruces
            'https://www.airbnb.es/s/Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&query=Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.360288232818124&sw_lng=-16.787361229951152&ne_lat=28.379144761265227&ne_lng=-16.770846790401443&s_tag=Uj_cUkrp',
        ],
        'Tenerife Buenavista' : [
            'https://www.airbnb.es/s/Buenavista-del-Norte--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=Buenavista%20del%20Norte%2C%20Santa%20Cruz%20de%20Tenerife&place_id=ChIJi3SvbNlhagwRx-RORHrv1As&allow_override%5B%5D=&s_tag=ijOpJPyV'
        ],
        'Tenerife Santiago del Teide' : [
            # Masca - Pueblo Santiago del Teide - Ergos
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=santiago%20del%20teide&is_user_submitted_query=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.280057362984078&sw_lng=-16.88319028319663&ne_lat=28.3555230399547&ne_lng=-16.817132524997785&s_tag=pdPOc1-5',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=santiago%20del%20teide&is_user_submitted_query=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.269472649678487&sw_lng=-16.821040358925504&ne_lat=28.344946432342745&ne_lng=-16.75498260072666&s_tag=Xzxv-2fD',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=santiago%20del%20teide&is_user_submitted_query=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.23408809673001&sw_lng=-16.82490273990695&ne_lat=28.309588956453638&ne_lng=-16.758844981708105&s_tag=0sPkmCWt',
        ],
        'Tenerife Santiago del Teide2' : [
            #Puerto Santiago
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=santiago%20del%20teide&is_user_submitted_query=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.240364800555806&sw_lng=-16.843686314455706&ne_lat=28.249805002679196&ne_lng=-16.83542909468085&s_tag=R080q-hO',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=santiago%20del%20teide&is_user_submitted_query=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.232387170725865&sw_lng=-16.845381470553118&ne_lat=28.24182813497936&ne_lng=-16.837124250778263',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=santiago%20del%20teide&is_user_submitted_query=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.224928870734626&sw_lng=-16.84358975493117&ne_lat=28.23437054732619&ne_lng=-16.835332535156315&s_tag=Ox9NUuX8',
        ],
        'Tenerife Santiago del Teide3' : [
            #Las Arenas, otras zonas, Chío
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=santiago%20del%20teide&is_user_submitted_query=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.22068205394855&sw_lng=-16.838852506738462&ne_lat=28.258444909807817&ne_lng=-16.805823627639043&s_tag=sqOxffls',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=santiago%20del%20teide&is_user_submitted_query=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.206205704716787&sw_lng=-16.841850144486948&ne_lat=28.22509172118562&ne_lng=-16.82533570493724&s_tag=Gcn-xwSZ',
        ],
        'Tenerife El Tanque' : [
            'https://www.airbnb.es/s/El-Tanque--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=El%20Tanque%2C%20Santa%20Cruz%20de%20Tenerife&place_id=ChIJpe5Tsq2JagwRMDJNvvNAAwQ&allow_override%5B%5D=&s_tag=CTnAbOtU'
        ],
        'Tenerife Guia Isora' : [
            #Alcala
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=santiago%20del%20teide&is_user_submitted_query=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.18432542776303&sw_lng=-16.837833277151738&ne_lat=28.23036813542131&ne_lng=-16.794359759568117&s_tag=cswYmpN-',
            #San Juan
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=santiago%20del%20teide&is_user_submitted_query=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.156783171889572&sw_lng=-16.822984568045293&ne_lat=28.202839292326747&ne_lng=-16.77951105046167&s_tag=gh38oG4k',
        ],
        'Tenerife Guia Isora2' : [
            #Guía de Isora pueblo
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=santiago%20del%20teide&is_user_submitted_query=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.1726738001218&sw_lng=-16.787193170950566&ne_lat=28.218722183463058&ne_lng=-16.743719653366945&s_tag=CtxKC1jj',
            #Chio
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=santiago%20del%20teide&is_user_submitted_query=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.219904777393833&sw_lng=-16.81630312709909&ne_lat=28.257667930217035&ne_lng=-16.78327424799967&s_tag=trjEmlOK',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=santiago%20del%20teide&is_user_submitted_query=true&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=28.165253998628863&sw_lng=-16.802664289483587&ne_lat=28.257335130310658&ne_lng=-16.715717254316345&s_tag=V224Nvv_',
        ],
        #Adeje
        'Tenerife Adeje Resto' : [
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.133321266773304&sw_lng=-16.756551615164433&ne_lat=28.17938880341969&ne_lng=-16.713078097580812&s_tag=SyJ-uI4_',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.13685243126843&sw_lng=-16.795507891162067&ne_lat=28.18291825026125&ne_lng=-16.752034373578446&s_tag=JciLzcUF',
        ],
        'Tenerife Callao Salvaje' : [
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.126394803175288&sw_lng=-16.786272921015954&ne_lat=28.13791466945824&ne_lng=-16.775404541620045&s_tag=e2yb1t3c',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.119194725558717&sw_lng=-16.77970417402159&ne_lat=28.124955274383343&ne_lng=-16.774269984323638&s_tag=lMUP7fwY',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.110836846552175&sw_lng=-16.782158446620887&ne_lat=28.133878933638847&ne_lng=-16.760421687829076&s_tag=NvTtl-08',
        ],
        'Tenerife Callao Salvaje2' : [
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.118042857031877&sw_lng=-16.772739285629715&ne_lat=28.1295637381439&ne_lng=-16.761870906233806&s_tag=mnhjNlCu',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.12737526700604&sw_lng=-16.77531985849993&ne_lat=28.13889501413656&ne_lng=-16.76445147910402&s_tag=AYx028FJ',
            # - El Puertito
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.111557616296157&sw_lng=-16.776770576411938&ne_lat=28.12307928522659&ne_lng=-16.76590219701603&s_tag=U-nlS7Ns',
        ],
        'Tenerife Adeje barrios' : [
            # - Adeje pueblo
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.1112031739479&sw_lng=-16.746840722697137&ne_lat=28.15728146493345&ne_lng=-16.703367205113516&s_tag=39b-gRbC',
            # - Las Moraditas
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.12937407102752&sw_lng=-16.766656814431602&ne_lat=28.15241165299021&ne_lng=-16.744920055639792&s_tag=CIU9eROv',
            # - Armeñime - Los menores
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.12937407102752&sw_lng=-16.766656814431602&ne_lat=28.15241165299021&ne_lng=-16.744920055639792&s_tag=CIU9eROv',
        ],
        'Tenerife Costa Adeje' : [
            # - La Caleta
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.098878619699892&sw_lng=-16.761335311746056&ne_lat=28.12192361156255&ne_lng=-16.739598552954245&s_tag=tEAcCKkH',
            # - Fañabe
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.096114977246135&sw_lng=-16.737688957070763&ne_lat=28.11916064026456&ne_lng=-16.715952198278952&s_tag=UcaDL9gD',
            # - El Duque
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.08437816863899&sw_lng=-16.754039703225548&ne_lat=28.107426681288207&ne_lng=-16.732302944433737&s_tag=EpsmSbqa',
        ],
        'Tenerife Costa Adeje2' : [
            # - San Eugenio
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.087238337273167&sw_lng=-16.74276902671119&ne_lat=28.09876295899123&ne_lng=-16.731900647315282&s_tag=DfvIRFnA',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.08848775972286&sw_lng=-16.733670973732675&ne_lat=28.100012229796278&ne_lng=-16.722802594336766&s_tag=qClf-yXh',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.0806502330108&sw_lng=-16.742618823006357&ne_lat=28.092175654236467&ne_lng=-16.731750443610448&s_tag=HXBABAcc',
        ],
        'Tenerife Costa Adeje3' : [
            # - Puerto Colón
            'https://www.airbnb.es/s/Puerto-Colon--Playa-de-la-Am%C3%A9ricas--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Puerto%20Colon%2C%20Playa%20de%20la%20Am%C3%A9ricas%2C%20Espa%C3%B1a&search_type=UNKNOWN&map_toggle=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.072655834094583&sw_lng=-16.734833215963675&ne_lat=28.078419207732743&ne_lng=-16.729399026265725&s_tag=koGOI5WV',
            # - Torviscas - Zona por encima de la autopista
        #     'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.08545126506705&sw_lng=-16.729947172570238&ne_lat=28.096976103674514&ne_lng=-16.71907879317433&s_tag=mwi4X_vM',
        #     'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.077392314758143&sw_lng=-16.726857267785082&ne_lat=28.088918131288924&ne_lng=-16.715988888389173&s_tag=w5DrD2Fz',
        ],
        'Tenerife Costa Adeje4' : [
            # - Zona por encima de la autopista
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.07069630543475&sw_lng=-16.729566178121278&ne_lat=28.082222934305054&ne_lng=-16.71869779872537&s_tag=pjZ0qUY6',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.084796354473966&sw_lng=-16.72222057027739&ne_lat=28.107844765608778&ne_lng=-16.70048381148558&s_tag=DsaRq_CZ',
        ],
        'Tenerife Fanabe' : [
            #Fañabé
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.081849352878816&sw_lng=-16.734512397800557&ne_lat=28.087612168830198&ne_lng=-16.729078208102607&s_tag=ATMlfgrf',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.085758666747388&sw_lng=-16.739093610797994&ne_lat=28.091521245505596&ne_lng=-16.733659421100043&s_tag=aaXBfnd1',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.08303561866946&sw_lng=-16.734040329013936&ne_lat=28.08879836264873&ne_lng=-16.728606139315986&s_tag=2lGjm8Fa'
        ],
        'Tenerife Fanabe2' : [
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.087190988795687&sw_lng=-16.735810586963765&ne_lat=28.092953480641807&ne_lng=-16.730376397265815&s_tag=diuJhKmL',
            #Colón
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.07827425658784&sw_lng=-16.73431316581886&ne_lat=28.084037289427584&ne_lng=-16.72887897612091',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.075915962295305&sw_lng=-16.736376859405226&ne_lat=28.081679138190466&ne_lng=-16.730942669707275&s_tag=_FWmGqed',
        ],
        'Tenerife Troya' : [
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.066902205491665&sw_lng=-16.735152631287832&ne_lat=28.072665928064588&ne_lng=-16.72971844158988&s_tag=yn2p2LzD',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.066166804884134&sw_lng=-16.729965614405472&ne_lat=28.071930572051436&ne_lng=-16.72453142470752',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&map_toggle=true&query=adeje&is_user_submitted_query=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.068970392015075&sw_lng=-16.732706746364983&ne_lat=28.07473398916824&ne_lng=-16.72727255666703&s_tag=weUM6jia'
        ],
        #Arona
        'Tenerife Americas' : [
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=17&search_by_map=true&sw_lat=28.060625900028032&sw_lng=-16.732936387175613&ne_lat=28.06639000315905&ne_lng=-16.727502197477662&allow_override%5B%5D=&s_tag=Bs3ubfIY',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=17&search_by_map=true&sw_lat=28.061267064524074&sw_lng=-16.727225658420906&ne_lat=28.06703112878225&ne_lng=-16.721791468722955&allow_override%5B%5D=&s_tag=l2pE_Rmb',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=17&search_by_map=true&sw_lat=28.056528216610197&sw_lng=-16.73594305435219&ne_lat=28.062292568158362&ne_lng=-16.73050886465424&allow_override%5B%5D=&s_tag=o9W_wkt2'
        ],
        'Tenerife Americas2' : [
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=17&search_by_map=true&sw_lat=28.056693042246376&sw_lng=-16.729713984621384&ne_lat=28.06245738380282&ne_lng=-16.724279794923433&allow_override%5B%5D=&s_tag=edc_hgka',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=16&search_by_map=true&sw_lat=28.049856004426843&sw_lng=-16.73942500893742&ne_lat=28.061385160440476&ne_lng=-16.72855662954151&allow_override%5B%5D=&s_tag=Zwn7KJuO',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=16&search_by_map=true&sw_lat=28.047537399922167&sw_lng=-16.734477147429008&ne_lat=28.059066836988595&ne_lng=-16.7236087680331&allow_override%5B%5D=&s_tag=l5CXZzUT',
        ],
        'Tenerife Cristianos' : [
            # Las Vistas
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=17&search_by_map=true&sw_lat=28.052431950433707&sw_lng=-16.725908752345248&ne_lat=28.058196550279792&ne_lng=-16.720474562647297&allow_override%5B%5D=&s_tag=f4yTgfQy',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=17&search_by_map=true&sw_lat=28.048379392414812&sw_lng=-16.72314071264188&ne_lat=28.05414423787666&ne_lng=-16.717706522943928&allow_override%5B%5D=&s_tag=6TOE-igW',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=16&search_by_map=true&sw_lat=28.055432517133212&sw_lng=-16.72254259714845&ne_lat=28.06696099709486&ne_lng=-16.71167421775254&allow_override%5B%5D=&s_tag=DaDdL-Bv',
        ],
        'Tenerife Cristianos2' : [
            # Pueblo
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=16&search_by_map=true&sw_lat=28.06092392081367&sw_lng=-16.727456404063734&ne_lat=28.072451734920676&ne_lng=-16.716588024667825&allow_override%5B%5D=&s_tag=9OAThOsI',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=17&search_by_map=true&sw_lat=28.05093593044442&sw_lng=-16.71914958562772&ne_lat=28.05670062096445&ne_lng=-16.713715395929768&allow_override%5B%5D=&s_tag=23D7kGE_',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=17&search_by_map=true&sw_lat=28.049553513723595&sw_lng=-16.71457910146634&ne_lat=28.055318288028115&ne_lng=-16.70914491176839'
        ],
        'Tenerife Cristianos3' : [
          'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=16&search_by_map=true&sw_lat=28.039621647340947&sw_lng=-16.713450904587436&ne_lat=28.051152043765335&ne_lng=-16.702582525191527&allow_override%5B%5D=&s_tag=ZeQTD4rP',
          'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=16&search_by_map=true&sw_lat=28.048405904565893&sw_lng=-16.709706156381746&ne_lat=28.05993523635784&ne_lng=-16.698837776985837&allow_override%5B%5D=&s_tag=ui5Ew-WI',
          'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=17&search_by_map=true&sw_lat=28.051757839953762&sw_lng=-16.71504476682341&ne_lat=28.05752248065832&ne_lng=-16.70961057712546&allow_override%5B%5D=&s_tag=wq58yww9',
        ],
        'Tenerife Arona barrios altos' : [
            # Chafoya - Los Cristianos
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=15&search_by_map=true&sw_lat=28.056356788540075&sw_lng=-16.7142374732606&ne_lat=28.079412100202156&ne_lng=-16.69250071446879&allow_override%5B%5D=&s_tag=aWcwlzQT',
            # Arona casco
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=14&search_by_map=true&sw_lat=28.0725995869429&sw_lng=-16.69824084716334&ne_lat=28.118696629318713&ne_lng=-16.65476732957972&allow_override%5B%5D=&s_tag=0tB0LYkm',
            # Buzanada
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=14&search_by_map=true&sw_lat=28.034725566794837&sw_lng=-16.686825365595958&ne_lat=28.080840983206727&ne_lng=-16.643351848012337&allow_override%5B%5D=&s_tag=e8vrs1vD'
        ],
        'Tenerife Arona barrios bajos' : [
            # Palmar
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=15&search_by_map=true&sw_lat=28.01548258179421&sw_lng=-16.704855730324315&ne_lat=28.038547799860766&ne_lng=-16.683118971532505&allow_override%5B%5D=&s_tag=TmjGryrV',
            # Las Galletas - El Fraile
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=15&search_by_map=true&sw_lat=27.999216110379834&sw_lng=-16.67442425758964&ne_lat=28.022285267151467&ne_lng=-16.652687498797828&allow_override%5B%5D=&s_tag=Sx2IpDxp',
            # - Orteanda Baja - Guargacho
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=15&search_by_map=true&sw_lat=28.026739225660894&sw_lng=-16.65379565292199&ne_lat=28.04980171685419&ne_lng=-16.63205889413018&allow_override%5B%5D=&s_tag=sBu6MVEc',
        ],
        'Tenerife Arona barrios bajos2':[
            # - Cho - La Estrella - Guaza
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=14&search_by_map=true&sw_lat=28.015554343435117&sw_lng=-16.688172458719244&ne_lat=28.061679051813865&ne_lng=-16.644698941135623&allow_override%5B%5D=&s_tag=BxqSx2DI',
            # - Guaza - Cho
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=14&search_by_map=true&sw_lat=28.026098311447953&sw_lng=-16.683866457185793&ne_lat=28.07221791006598&ne_lng=-16.640392939602172&allow_override%5B%5D=&s_tag=p19KNAqk',
            # Guargacho - Las Rosas - Coromoto
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=15&search_by_map=true&sw_lat=28.016147321404723&sw_lng=-16.65813972321519&ne_lat=28.03921237846896&ne_lng=-16.63640296442338&allow_override%5B%5D=&s_tag=kCu2jwux',
        ],
        'Tenerife Costa del Silencio' : [
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=16&search_by_map=true&sw_lat=27.99815596627583&sw_lng=-16.649580695376645&ne_lat=28.009691384112422&ne_lng=-16.638712315980737&allow_override%5B%5D=&s_tag=OMH_62fD',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=16&search_by_map=true&sw_lat=28.007155148266495&sw_lng=-16.65374348376776&ne_lat=28.018689476899947&ne_lng=-16.64287510437185&allow_override%5B%5D=&s_tag=i5qkDYdA',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=16&search_by_map=true&sw_lat=28.008988522914027&sw_lng=-16.644852025521633&ne_lat=28.020522629608145&ne_lng=-16.633983646125724&allow_override%5B%5D=&s_tag=QhQTIMb_',
        ],
        'Tenerife San Miguel' : [
            # - Pueblo
            'https://www.airbnb.es/s/San-Miguel-de-Abona--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=San%20Miguel%20de%20Abona%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=28.057786452468946&sw_lng=-16.666286792730048&ne_lat=28.14997210858564&ne_lng=-16.579339757562806&s_tag=Fp5ht1U8',
            # - Las Chafiras
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=15&search_by_map=true&sw_lat=28.030192585457772&sw_lng=-16.625417058176257&ne_lat=28.053254239887973&ne_lng=-16.603680299384447&allow_override%5B%5D=&s_tag=3nkAfXWr',
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=15&search_by_map=true&sw_lat=28.04433326463012&sw_lng=-16.629150693124988&ne_lat=28.06739149172889&ne_lng=-16.607413934333177&allow_override%5B%5D=&s_tag=9BME-gAM',
        ],
        'Tenerife San Miguel2' : [
            # - Los Abrigos
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=15&search_by_map=true&sw_lat=28.02255279299349&sw_lng=-16.60913779522105&ne_lat=28.04561629844949&ne_lng=-16.587401036429238&allow_override%5B%5D=&s_tag=dwCe3Xjd',
            # - Amarillo y Golf Sur
            'https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=arona&map_toggle=true&is_user_submitted_query=true&zoom=15&search_by_map=true&sw_lat=28.02255279299349&sw_lng=-16.60913779522105&ne_lat=28.04561629844949&ne_lng=-16.587401036429238&allow_override%5B%5D=&s_tag=dwCe3Xjd',
        ],
        'Tenerife Vilaflor' : [
            'https://www.airbnb.es/s/Vilaflor--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Vilaflor%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=12&search_by_map=true&sw_lat=28.096514404942276&sw_lng=-16.724085691173087&ne_lat=28.280719055112094&ne_lng=-16.550191620838604&s_tag=pFnvRkEW',
        ],
        # Granadilla
        'Tenerife Granadilla' : [
            'https://www.airbnb.es/s/Granadilla-de-Abona--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Granadilla%20de%20Abona%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=28.0704721142848&sw_lng=-16.60141019995673&ne_lat=28.16264545119973&ne_lng=-16.51446316478949&s_tag=uLpS5Ztj'
        ],
        'Tenerife El Medano' : [
            # - La Tejita
            'https://www.airbnb.es/s/Granadilla-de-Abona--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Granadilla%20de%20Abona%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.00649517336025&sw_lng=-16.58899044497833&ne_lat=28.05262427053575&ne_lng=-16.545516927394708&s_tag=IGF1rC-y',
            # - El Médano
            'https://www.airbnb.es/s/Granadilla-de-Abona--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Granadilla%20de%20Abona%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.041061822670247&sw_lng=-16.543899709410738&ne_lat=28.046827111549735&ne_lng=-16.538465519712787&s_tag=WIdNWLQn',
            'https://www.airbnb.es/s/Granadilla-de-Abona--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Granadilla%20de%20Abona%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.04206557609899&sw_lng=-16.538556749053072&ne_lat=28.04783080416101&ne_lng=-16.53312255935512&s_tag=l3CEyPLG',
        ],
        'Tenerife El Medano2' : [
            'https://www.airbnb.es/s/Granadilla-de-Abona--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Granadilla%20de%20Abona%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.046175185851084&sw_lng=-16.53960817498691&ne_lat=28.05194016489086&ne_lng=-16.53417398528896&s_tag=EarWrkmg',
            'https://www.airbnb.es/s/Granadilla-de-Abona--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Granadilla%20de%20Abona%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.04558756959008&sw_lng=-16.544228713651904&ne_lat=28.051352584238586&ne_lng=-16.538794523953953',
            'https://www.airbnb.es/s/Granadilla-de-Abona--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Granadilla%20de%20Abona%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=17&search_by_map=true&sw_lat=28.04732960348517&sw_lng=-16.537515504518723&ne_lat=28.05309451256684&ne_lng=-16.532081314820772&s_tag=_tf_PxB5',
        ],
        'Tenerife El Medano3' : [
            'https://www.airbnb.es/s/Granadilla-de-Abona--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Granadilla%20de%20Abona%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=16&search_by_map=true&sw_lat=28.048010458272152&sw_lng=-16.53351634799441&ne_lat=28.059539837997914&ne_lng=-16.522647968598502&s_tag=HjRmUb6M',
            # - Arenas del Mar
            'https://www.airbnb.es/s/Granadilla-de-Abona--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Granadilla%20de%20Abona%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=15&search_by_map=true&sw_lat=28.05147010371118&sw_lng=-16.550045446808898&ne_lat=28.07452660042386&ne_lng=-16.528308688017088&s_tag=deIOzC9q',
            # - Vista general
            'https://www.airbnb.es/s/Granadilla-de-Abona--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Granadilla%20de%20Abona%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.036531398513254&sw_lng=-16.58873990914072&ne_lat=28.082645939368543&ne_lng=-16.5452663915571&s_tag=7m-VQk1O',
        ],
        'Tenerife Arico' : [
            'https://www.airbnb.es/s/Arico--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Arico%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=28.086406442035646&sw_lng=-16.540083882573768&ne_lat=28.178564297702387&ne_lng=-16.453136847406526&s_tag=K00xklPP',
            'https://www.airbnb.es/s/Arico--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Arico%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=28.124874162959447&sw_lng=-16.50123586109318&ne_lat=28.216994611545758&ne_lng=-16.414288825925937&s_tag=dq5Z9mfC',
        ],
        'Tenerife Fasnia' : [
            'https://www.airbnb.es/s/Fasnia--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Fasnia%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=28.186649463845335&sw_lng=-16.475412221196862&ne_lat=28.27870974233277&ne_lng=-16.38846518602962&s_tag=xvINLiUR',
        ],
        'Tenerife Guimar' : [
            'https://www.airbnb.es/s/G%C3%BC%C3%ADmar--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=G%C3%BC%C3%ADmar%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=13&search_by_map=true&sw_lat=28.234918641857313&sw_lng=-16.442754988530865&ne_lat=28.326931821327666&ne_lng=-16.355807953363623&s_tag=nDyQ8M23',
        ],
        'Tenerife Arafo' : [
            'https://www.airbnb.es/s/Arafo--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Arafo%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.318702092201406&sw_lng=-16.438953536745892&ne_lat=28.364679187556114&ne_lng=-16.39548001916227&s_tag=TN8jkMG3',
        ],
        'Tenerife Candelaria' : [
            'https://www.airbnb.es/s/Candelaria--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Candelaria%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.333187392803083&sw_lng=-16.40313035400664&ne_lat=28.379157398328363&ne_lng=-16.35965683642302&s_tag=DUXJ6j8Q',
            'https://www.airbnb.es/s/Candelaria--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&adults=1&children=0&checkin=&checkout=&query=Candelaria%2C%20Santa%20Cruz%20de%20Tenerife&map_toggle=true&allow_override%5B%5D=&zoom=14&search_by_map=true&sw_lat=28.36378082914585&sw_lng=-16.379097761233204&ne_lat=28.409735849804964&ne_lng=-16.335624243649583&s_tag=g2FqULGw',
        ],
    }
    return urls[place]

def AtraveoURLs(place):
    urls= {
        'Puerto de la Cruz' : [
            "https://www.atraveo.es/puerto_de_la_cruz#eyJkYXRhIjp7ImNvdW50cnlJZCI6IkVTIiwicmVnaW9uSWQiOiIxNzUiLCJzdWJSZWdpb25JZCI6Ijg4MyIsImNpdHlJZCI6Ijk4MjciLCJkdXJhdGlvbiI6N30sImNvbmZpZyI6eyJwYWdlIjoiMCJ9fQ==",
        ],
        'Adeje' : [
            "https://www.atraveo.es/adeje#eyJkYXRhIjp7ImNvdW50cnlJZCI6IkVTIiwicmVnaW9uSWQiOiIxNzUiLCJzdWJSZWdpb25JZCI6Ijg5NSIsImNpdHlJZCI6IjczNDM3MiIsImR1cmF0aW9uIjo3fSwiY29uZmlnIjp7InBhZ2UiOiIwIn19",
            "https://www.atraveo.es/costa_adeje_%28costa_oeste_de_tenerife%29#eyJkYXRhIjp7ImNvdW50cnlJZCI6IkVTIiwicmVnaW9uSWQiOjE3NSwiY2l0eUlkIjo1ODQwNzQsImR1cmF0aW9uIjo3fSwiY29uZmlnIjp7fX0=",
        ],
        'Gran Canaria' : [
            "https://www.atraveo.es/costa_norte_de_gran_canaria",
            "https://www.atraveo.es/costa_este_de_gran_canaria",
            "https://www.atraveo.es/costa_oeste_de_gran_canaria",
            "https://www.atraveo.es/costa_sur_de_gran_canaria",
            "https://www.atraveo.es/interior_de_gran_canaria",
        ],
        'La Palma' : [
            "https://www.atraveo.es/costa_norte_de_la_palma",
            "https://www.atraveo.es/costa_este_de_la_palma",
            "https://www.atraveo.es/costa_oeste_de_la_palma",
            "https://www.atraveo.es/costa_sur_de_la_palma",
        ],
        'El Hierro' : [
            "https://www.atraveo.es/el_hierro",
        ],
        'La Gomera' : [
            "https://www.atraveo.es/la_gomera",
        ],
        'Lanzarote' : [
            "https://www.atraveo.es/costa_norte_de_lanzarote",
            "https://www.atraveo.es/costa_este_de_lanzarote",
            "https://www.atraveo.es/costa_oeste_de_lanzarote",
            "https://www.atraveo.es/costa_sur_de_lanzarote",
            "https://www.atraveo.es/interior_de_lanzarote",
        ],
        'Fuerteventura' : [
            "https://www.atraveo.es/costa_norte_de_fuerteventura",
            "https://www.atraveo.es/costa_este_de_fuerteventura",
            "https://www.atraveo.es/costa_oeste_de_fuerteventura",
            "https://www.atraveo.es/costa_sur_de_fuerteventura",
            "https://www.atraveo.es/interior_de_fuerteventura",
        ],
        'Tenerife' : [
            "https://www.atraveo.es/costa_norte_de_tenerife",
            "https://www.atraveo.es/costa_este_de_tenerife",
            "https://www.atraveo.es/costa_oeste_de_tenerife",
            "https://www.atraveo.es/costa_sur_de_tenerife",
            "https://www.atraveo.es/interior_de_tenerife",
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
        'Tenerife Norte' : ['https://www.homeaway.es/search/@28.260388910619195,-17.210066021502826,29.20326862247965,-15.8024427304872,10z?petIncluded=false&ssr=true&adultsCount=2'],
        'Tenerife Sur' :['https://www.homeaway.es/search/@27.798886730953853,-16.942617596209857,28.273436181273137,-16.238805950702044,11z?petIncluded=false&ssr=true&adultsCount=2'],
        'Gran Canaria' : ['https://www.homeaway.es/search/@27.510277440165147,-16.195730328945274,28.45981411134543,-14.788107037929649,10z?petIncluded=false&ssr=true&adultsCount=2'],
        'La Palma' : ['https://www.homeaway.es/search/@28.446554409724065,-18.21332744013671,28.918223492447652,-17.509515794628896,11z?petIncluded=false&ssr=true&adultsCount=2'],
        'El Hierro' : ['https://www.homeaway.es/search/@27.630438541406804,-18.187620931103538,27.868343501854973,-17.835715108349632,12z?petIncluded=false&ssr=true&adultsCount=2'],
        'La Gomera' : ['https://www.homeaway.es/search/@28.00225220591001,-17.400598836376957,28.239340824323325,-17.04869301362305,12z?petIncluded=false&ssr=true&adultsCount=2'],
        'Lanzarote' : ['https://www.homeaway.es/search/@28.78669221932801,-14.089172274628936,29.520983684627847,-13.090103060761749,10z?petIncluded=false&ssr=true&adultsCount=2'],
        'Fuerteventura' : ['https://www.homeaway.es/search/@27.87846870659744,-14.69857016281253,28.824757815508516,-13.290946871796905,10z?petIncluded=false&ssr=true&adultsCount=2'],
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
            "https://www.niumba.com/tenerife/apartamentos",
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
            "https://www.housetrip.es/buscar-alquileres/fuerteventura/62133/hom_sleeps_max.2",
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