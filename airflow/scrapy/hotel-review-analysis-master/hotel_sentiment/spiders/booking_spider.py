import scrapy, datetime, os, re
from scrapy.loader import ItemLoader
from hotel_sentiment.items import BookingReviewItem
from scrapy.mail import MailSender
from scrapy.exceptions import CloseSpider
from datetime import timedelta
#crawl up to 6 pages of review per hotel
max_pages_per_hotel = 6
exceptionErrorItem=False

class BookingSpider(scrapy.Spider):
    name = "booking"
    start_urls = [
        #"http://www.booking.com/searchresults.html?aid=357026&label=gog235jc-city-XX-us-newNyork-unspec-uy-com-L%3Axu-O%3AosSx-B%3Achrome-N%3Ayes-S%3Abo-U%3Ac&sid=b9f9f1f142a364f6c36f275cfe47ee55&dcid=4&city=20088325&class_interval=1&dtdisc=0&from_popular_filter=1&hlrd=0&hyb_red=0&inac=0&label_click=undef&nflt=di%3D929%3Bdistrict%3D929%3B&nha_red=0&postcard=0&redirected_from_city=0&redirected_from_landmark=0&redirected_from_region=0&review_score_group=empty&room1=A%2CA&sb_price_type=total&score_min=0&ss_all=0&ssb=empty&sshis=0&rows=15&tfl_cwh=1",
        #add your city url here
        "https://www.booking.com/searchresults.en-gb.html?aid=356984&label=gog235jc-country-en-gb-gb-unspec-es-com-L%3Aen-O%3Ax11-B%3Achrome-N%3AXX-S%3Abo-U%3Ac-H%3As&lang=en-gb&sid=e4ce8c840d65e7df8712a2df06268dbd&sb=1&src=country&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fcountry%2Fgb.en-gb.html%3Faid%3D356984%3Blabel%3Dgog235jc-country-en-gb-gb-unspec-es-com-L%253Aen-O%253Ax11-B%253Achrome-N%253AXX-S%253Abo-U%253Ac-H%253As%3Bsid%3De4ce8c840d65e7df8712a2df06268dbd%3Binac%3D0%26%3B&ss=Costa+Del+Silencio%2C+Canary+Islands%2C+Spain&checkin_monthday=&checkin_month=&checkin_year=&checkout_monthday=&checkout_month=&checkout_year=&room1=A%2CA&no_rooms=1&group_adults=2&group_children=0&ss_raw=costa+del+silencio&ac_position=0&ac_langcode=en&dest_id=900040737&dest_type=city&search_pageview_id=17cd7243c13c03d6&search_selected=true&search_pageview_id=17cd7243c13c03d6&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0"
    ]

    pageNumber = 1

    #for every hotel
    def parse(self, response):
        for hotelurl in response.xpath('//a[@class="hotel_name_link url"]/@href'):
            url = response.urljoin(hotelurl.extract())
            yield scrapy.Request(url, callback=self.parse_hotel)

        next_page = response.xpath('//a[starts-with(@class,"paging-next")]/@href')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)

    #get its reviews page
    def parse_hotel(self, response):
        reviewsurl = response.xpath('//a[@class="show_all_reviews_btn"]/@href')
	url = response.urljoin(reviewsurl[0].extract())

        request = scrapy.Request(response.url, callback=self.parse_review)
        #It saves a fields that it will be send

        name = response.xpath('//div[@class="hp__hotel-title"]/h2/text()')
        request.meta['hotel_name']=hotel

        #This fields are optionals. Can be empty
        address = response.xpath('//span[@class="hp_address_subtitle jq_tooltip"]/text()')
        request.meta['hotel_address']=address

        score = response.xpath('//span[@class="review-score-badge"]/text()')
        request.meta['hotel_score']=score

        self.pageNumber = 1

        #If there is comment
        if has_review:
	        yield request

    #and parse the reviews
    def parse_reviews(self, response):

        now = datetime.datetime.combine(datetime.datetime.today(), datetime.time(0, 0))
        listErrors=[]

        if self.pageNumber > max_pages_per_hotel:
            return
        for rev in response.xpath('//li[starts-with(@class,"review_item")]'):
            item = BookingReviewItem()
            #sometimes the title is empty because of some reason, not sure when it happens but this works
	    item['hotel_name']=response.meta['hotel_name']
            item['hotel_address']=response.meta['hotel_address']
            item['hotel_score']=response.meta['hotel_score']

            review_date = rev.xpath('.//meta[@itemprop="datePublished"]/@content') 
            if review_date:
                item['review_date'] = review_date [0].extract()
                date = datetime.datetime.strptime(item['review_date'], '%Y-%m-%d') 

                #if (now - date).days < 7:
		if (now - date).days < 1000000:

                    title = rev.xpath('.//a[@class="review_item_header_content"]/span[@itemprop="name"]/text()')
                    if title:
                        item['title'] = title[0].extract()
                    else:
                        listErrors=listErrors + ['title']

                    positive_content = rev.xpath('.//p[@class="review_pos"]//span/text()')
                    if positive_content:
                        item['positive_content'] = positive_content[0].extract()
                    negative_content = rev.xpath('.//p[@class="review_neg"]//span/text()')
                    if negative_content:
                        item['negative_content'] = negative_content[0].extract()

                    score=rev.xpath('.//span[@itemprop="reviewRating"]/meta[@itemprop="ratingValue"]/@content')
                    if score:
                        item['score'] = score[0].extract()
                    else:
                        listErrors=listErrors + ['score']

                    #tags are separated by ;
                    # comento las tags. No la usamos en el proyecto
                    #item['tags'] = ";".join(rev.xpath('.//li[@class="review_info_tag"]/text()').extract())
                    # anado codigo para sar la fecha de la revision y la localizacion del revisor

                    item['reviewer_location'] = rev.xpath('.//span[@class="reviewer_country"]/span[@itemprop="nationality"]/span[@itemprop="name"]/text()')[0].extract()

                    yield item

                else:
                    break
            else:
                listErrors=listErrors + ['review_date']

        if len(listErrors)>0:

          #self.send_email(listErrors)
          raise CloseSpider('Error spider parse review')


        next_page = response.xpath('//a[@id="review_next_page_link"]/@href')
        if next_page:
            self.pageNumber += 1
            url = response.urljoin(next_page[0].extract())
            request = scrapy.Request(url, self.parse_review)
            #We send the meta data to the request of the next pages
            request.meta['hotel_name']=response.meta['hotel_name']
            request.meta['hotel_address']=response.meta['hotel_address']
            request.meta['hotel_score']=response.meta['hotel_score']
            yield request

    #
    # def send_email(self, listErrors):
    #
    #     global exceptionErrorItem
    #
    #     if exceptionErrorItem == False:
    #         message = 'Al hacer el scrapy de Tripadvisor no existen los campos '
    #
    #         for elementError in listErrors:
    #             message = message + elementError + ', '
    #
    #         message = re.sub(', $', '.' , message)
    #
    #         #Send a email saying if some bug have ocurred
    #         mailer = MailSender(mailfrom="erroresSpider@gmail.com",smtphost="smtp.gmail.com",smtpport=587,smtpuser="erroresSpider@gmail.com",smtppass="errores1234")
    #         #mailer.send(to=["erroresSpider@gmail.com"], subject='Errores en el Spider', body=message)
    #         exceptionErrorItem=True
    #
    #         #In this case we delete the extract file until this moment
    #         os.remove('itemsBooking.csv')
