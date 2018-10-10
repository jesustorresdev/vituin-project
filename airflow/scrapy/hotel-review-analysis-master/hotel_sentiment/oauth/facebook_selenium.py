# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

def get_reactions(reactions, name):
    number_like = None
    number_love = None
    number_wow = None
    number_enjoy = None
    number_sad = None
    number_angry = None
    body=driver_posts.find_element_by_tag_name("body")

    print 'Hay', len(reactions), 'reacciones'
    m = 0
    for reaction in reactions:
        print 'Reaction numero', m
        print ''
        load = False
        contador = 0
        while load is False and contador < 5:
            try:
                span_reaction = reaction.find_element_by_xpath(".//a/span/span")
                type_reaction = span_reaction.get_attribute('aria-label')
                number_reaction = type_reaction[:type_reaction.find('p')].strip()
                print 'type_reaction-->',type_reaction
                print 'number_reaction-->',number_reaction

                load = True
            except Exception as error:
                print 'Error',contador,'en', name, error
                contador += 1
                pass

        if type_reaction[-8:len(type_reaction)] == 'Me gusta':
            number_like_all = number_reaction.split()
            print 'number_like_all-->', number_like_all
            print 'reaction.text-->', type_reaction

            number_like = int(number_like_all[0])
            if len(number_like_all) > 1:
                if number_like_all[1] == 'mil':
                    number_like *= 1000
            print 'El',name,'tiene',number_like,'me gusta'


        elif type_reaction[-10:len(type_reaction)] == 'Me encanta':
            number_love_all = number_reaction.split()
            number_love = int(number_love_all[0])
            if len(number_love_all) > 1:
                if number_love_all[1] == 'mil':
                    number_love *= 1000
            print 'El',name,'tiene',number_love,'me encanta'

        elif type_reaction[-10:len(type_reaction)] == 'Me asombra':
            number_wow_all = number_reaction.split()
            number_wow = int(number_wow_all[0])
            if len(number_wow_all) > 1:
                if number_wow_all[1] == 'mil':
                    number_wow *= 1000
            print 'El',name,'tiene',number_wow,'me asombra'

        elif type_reaction[-11:len(type_reaction)] == 'Me divierte':
            number_enjoy_all = number_reaction.split()
            number_enjoy = int(number_enjoy_all[0])
            if len(number_enjoy_all) > 1:
                if number_enjoy_all[1] == 'mil':
                    number_enjoy *= 1000
            print 'El',name,'tiene',number_enjoy,'me divierte'

        elif type_reaction[-13:len(type_reaction)] == 'Me entristece':
            number_sad_all = number_reaction.split()
            number_sad = int(number_sad_all[0])
            if len(number_sad_all) > 1:
                if number_sad_all[1] == 'mil':
                    number_sad *= 1000
            print 'El',name,'tiene',number_sad,'me entristece'

        elif type_reaction[-8:len(type_reaction)] == 'Me enoja':
            number_angry_all = number_reaction.split()
            number_angry = int(number_angry_all[0])
            if len(number_angry_all) > 1:
                if number_angry_all[1] == 'mil':
                    number_angry *= 1000
            print 'El',name,'tiene',number_angry,'me enoja'
        m += 1


#START
fp = webdriver.FirefoxProfile()
fp.set_preference("dom.webnotifications.enabled", False)
driver = webdriver.Firefox(fp)
#driver_posts = webdriver.Firefox(fp)
#ChromeDriver options notification
#chrome_options = webdriver.ChromeOptions()
#prefs = {"profile.default_content_setting_values.notifications" : 2}
#chrome_options.add_experimental_option("prefs",prefs)
#driver = webdriver.Chrome(chrome_options=chrome_options)

#GeckoDriver options notification

page = 'VisitPuertodelaCruz'

driver.get('https://www.facebook.com/')
#driver_posts.get('https://www.facebook.com/')

'''
driver.get("https://www.facebook.com/VisitPuertodelaCruz/posts/2089143344476650")



page.send_keys(Keys.END)
'''
#FOR DRIVER
inputEmailElement = driver.find_element_by_xpath("//input[@id='email']")
inputEmailElement.send_keys('sergio_7_blanquiazul@hotmail.com')
inputPassElement = driver.find_element_by_xpath("//input[@id='pass']")
inputPassElement.send_keys("SH47fkAm0we7Uq")
time.sleep(1)
buttonEnter = driver.find_element_by_xpath("//label[@id='loginbutton']")
print "Enter-->",buttonEnter
buttonEnter.click()

driver.get("https://www.facebook.com/pg/"+page+"/posts/")

# Scroll
#html=driver.find_element_by_tag_name("html")
#html.send_keys(Keys.END)
'''
#FOR DRIVER_POST
inputEmailElement = driver_posts.find_element_by_xpath("//input[@id='email']")
inputEmailElement.send_keys('sergio_7_blanquiazul@hotmail.com')
inputPassElement = driver_posts.find_element_by_xpath("//input[@id='pass']")
inputPassElement.send_keys("SH47fkAm0we7Uq")
time.sleep(1)
buttonEnter = driver_posts.find_element_by_xpath("//label[@id='loginbutton']")
print "Enter-->",buttonEnter
buttonEnter.click()
'''

i = 0
n_posts_old = 0
while i < 20:
    load = False
    contador = 0
    while load is False and contador < 5:

        try:
            posts = driver.find_elements_by_xpath("//div[@class='_4-u2 _4-u8']")
        except:
            print 'Error en posts', contador
            contador += 1
            pass

        #Time to load
        time.sleep(1)
        #If it doesnt load yet
        if n_posts_old == len(posts):
            time.sleep(1)
            load = False
        else:
            creation_time = posts[len(posts)-1].find_elements_by_xpath(".//abbr")
            date = creation_time[0].get_attribute('title')
            print 'iteracion',i,', number of posts-->',len(posts),', día-->',date
            n_posts_old = len(posts)
            load = True
            i += 1

    # Scroll
    html=driver.find_element_by_tag_name("html")
    html.send_keys(Keys.END)

import sys
sys.exit()
n = 0
for post in posts:
    print ''
    print ''
    print ''
    print ''
    print 'Post número', n

    # CREATE TIME
    load = False
    contador = 0
    while load is False and contador < 5:
        try:
            creation_time = post.find_elements_by_xpath(".//abbr")
            print 'creation_time-->',creation_time[0].get_attribute('title')
            load = True
        except Exception as error:
            print 'Error',contador,'en creation_time', error
            contador += 1
            pass



    load = False
    contador = 0
    while load is False and contador < 5:
        try:
            url_post = post.find_elements_by_xpath(".//a[@class='_5pcq']")[0].get_attribute('href')
            id_post = url_post[32+len(page):url_post.find('?')]
            print id_post
            load = True
        except Exception as error:
            print 'Error',contador,'en id_post', error
            contador += 1
            pass

    driver_posts.get(url_post)
    driver_post = (driver_posts.find_elements_by_xpath("//div[@class='_4-u2 _4-u8']"))[0]
    '''
    # SEE ALL TITLE 
    load = False
    contador = 0
    while load is False and contador < 5:
        try:	
            see_more = driver_post.find_element_by_xpath(".//a[@class='see_more_link']")
            print "see_more-->",see_more.text
            see_more.click()
        except Exception as error:
            print 'Error',contador,'en see more', error
            contador += 1
            pass
    '''
    # TITLE
    load = False
    contador = 0
    title = None
    while load is False and contador < 5:
        try:
            title = driver_post.find_elements_by_xpath("//div[contains(@class, 'userContent')]/p")
            print "title-->",title
            load = True
        except Exception as error:
            print 'Error',contador,'en title', error
            contador += 1
            pass

    if title:
        n_paragraph=0
        for paragraph in title:
            print "Parrafo", n_paragraph, ", texto-->", paragraph.text
            n_paragraph += 1
    print ''
    print 'se acabo titulo'

    #REACTIONS CLICK BUTTON
    load = False
    contador = 0
    post_click = False
    while load is False and contador < 5:
        print 'click reactions'
        try:
            driver_post.find_element_by_xpath("//span[@class='_3t54']").click()
            load = True
            post_click = True
        except Exception as error:
            print 'Error',contador,'en click reactions post', error
            contador += 1
            pass


    if post_click is True:
        load = False
        contador = 0
        while load is False and contador < 5:
            try:
                body=driver_posts.find_element_by_tag_name("body")
                print 'body-->', body
                load = True
            except Exception as error:
                print 'Error',contador,'get body', error
                time.sleep(3)
                contador += 1
                pass

        #REACTIONS
        load = False
        contador = 0
        reactions = None
        while load is False and contador < 5:
            try:

                print 'Estoy cogiendo REACTIONS'
                reactions = body.find_elements_by_xpath(".//li[contains(@class, '_ds-') and contains(@class, ' _45hc')]")
                print "reactions-->",reactions
                load = True
            except Exception as error:
                print 'Error',contador,'en reactions del post', error
                contador += 1
                pass
            #Could be not load
            if not reactions and load:
                print 'No ha cargado. Se repite'
                load = False
                time.sleep(3)
            if contador >= 5:
                load = True
                print 'Se sigue. No se cargó'


        if reactions:
            print 'Estoy en REACTIONS'

            name = 'posts'
            get_reactions(reactions, name)

        # CLOSE REACTIONS SQUARE
        load = False
        contador = 0
        while load is False and contador < 5:
            try:
                body.find_element_by_xpath("//a[@title='Cerrar']").click()
                load = True
            except Exception as error:
                print 'Error',contador,'en cerrar cuadro reactions del post', error
                contador += 1
                pass



    # NUMBER REVIEWS AND SHARE
    load = False
    contador = 0
    while load is False and contador < 5:
        try:
            number_rev_and_sh = driver_post.find_elements_by_xpath(".//div[@class='_ipo']/div")
            load = True
        except Exception as error:
            print 'Error',contador,'en number_rev_and_sh', error
            contador += 1
            pass

    if number_rev_and_sh:
        for element in number_rev_and_sh:
            try:
                shares = None
                reviews = None
                attribute = element.find_element_by_xpath(".//a").get_attribute('href')
                number_interaction =  element.find_element_by_xpath(".//a").text
                print 'attribute-->',attribute
                print 'el atributo cortado-->',attribute[25:25+6]
                print 'number_interaction-->',number_interaction
                if attribute[25:25+6] == 'shares':
                    shares_all = number_interaction.split()
                    print 'shares_all-->', shares_all

                    if len(shares_all) > 1:
                        if shares_all[1] == 'mil':
                            shares = shares_all[0] * 1000
                        else:
                            shares = shares_all[0]
                    print 'shares-->', shares
                else:
                    reviews_all = number_interaction.split()
                    print 'reviews_all-->', reviews_all

                    if len(reviews_all) > 1:
                        if reviews_all[1] == 'mil':
                            reviews = reviews_all[0] * 1000
                        else:
                            reviews = reviews_all[0]
                        print 'reviews-->', reviews

            except Exception as error:
                reproductions = None
                print 'Error',error
                #if it doesn't have href the element is reproductions
                reproductions_all = element.text[:element.text.find('r')].strip()
                if len(reproductions_all) > 1:
                    if reproductions_all[1] == 'mil':
                        reproductions = reproductions_all[0] * 1000
                    else:
                        reproductions = reproductions_all[0]
                print 'reproductions-->', reproductions

    '''
    # SEE ALL REVIEWS
    load = False
    contador = 0
    while load is False and contador < 5:
        try:			
            see_more_reviews = driver_post.find_element_by_xpath(".//div[contains(@class,'UFILastCommentComponent')]/div/a[@class='UFIPagerLink']")
            print "see_more_reviews-->",see_more_reviews.text
            see_more_reviews.click()
            load = True
        except Exception as error:
            print 'Error',contador,'en see more views', error
            contador += 1
            pass
    '''
    '''
    #driver_post.execute_script("window.scrollTo(900, Y)") 
    # REVIEWS
    print 'REVIEWS'
    load = False
    contador = 0
    while load is False and contador < 5:
        try:
            reviews = driver_post.find_elements_by_xpath(".//div[@aria-label='Comentario']")
            #reviews = driver_post.find_elements_by_xpath(".//div[contains(@class,'UFIRow') and contains(@class,'UFIComment')]")

            print 'reviews-->', reviews 
            load = True
        except Exception as error:
            print 'Error',contador,'en reviews', error
            contador += 1
            pass

    #reviews.location_once_scrolled_into_view
    time.sleep(1)
    m = 0
    if reviews:
        for review in reviews:
            print 'Comentario numero', m
            print 'aria label de la review-->',review.get_attribute('aria-label') 
            if review.get_attribute('aria-label') == 'Comentario':
                print 'Es comentario con identificador--> ', review.get_attribute('data-ft')
            elif review.get_attribute('aria-label') == 'Respuesta a un comentario':
                print 'Es una respuesta al comentario--> ', review.get_attribute('data-ft')

            load = False
            contador = 0
            while load is False and contador < 5:
                try:
                    #review_text = review.find_element_by_xpath(".//span[@class='UFICommentBody']/span")
                    review_text = review.find_element_by_xpath(".//span[@class='UFICommentBody']")

                    print 'review'+str(m)+'-->',review_text.text
                    load = True
                except Exception as error:
                    print 'Error',contador,'en review', error
                    contador += 1
                    pass	

            

            #REACTIONS REVIEW CLICK BUTTON
            review_click = False
            load = False
            contador = 0
            while load is False and contador < 5:
                try:
                    review.find_element_by_xpath("//span[@class='_3t54']").click()
                    load = True
                    review_click = True
                except Exception as error:
                    print 'Error',contador,'en click reactions comentario', error
                    contador += 1
                    pass
            if review_click is True:
                #review.find_element_by_xpath(".//div[contains(@class,'UFICommentReactionsBling')]").click()
                load = False
                contador = 0				
                try:
                    body=driver_posts.find_element_by_tag_name("body")
                    print 'body-->', body
                    load = True
                except Exception as error:
                    print 'Error',contador,'get body', error
                    time.sleep(3)
                    contador += 1
                    pass


                #REACTIONS REVIEWS
                load = False
                contador = 0
                reactions_reviews = None
                while load is False and contador < 5:
                    try:
                        print 'Estoy cogiendo REACTIONS REVIEW'
                        reactions_reviews = body.find_elements_by_xpath(".//li[contains(@class, '_ds-') and contains(@class, ' _45hc')]")
                        print "reactions_reviews-->",reactions_reviews
                        load = True
                    except Exception as error:
                        print 'Error',contador,'en reactions reviews', error
                        contador += 1
                        pass
                    #Could be not load
                    if not reactions_reviews and load:
                        print 'No ha cargado. Se repite'
                        load = False
                        time.sleep(3)
                    if contador >= 5:
                        load = True
                        print 'Se sigue. No se cargó'
                        


                if reactions_reviews:
                    print 'Estoy en REACTIONS REVIEW'
                    name = 'comentarios'
                    get_reactions(reactions_reviews, name)
                
                # CLOSE REACTIONS REVIEWS SQUARE
                load = False
                contador = 0
                while load is False and contador < 5:
                    try:
                        body.find_element_by_xpath(".//a[@title='Cerrar']").click()
                        load = True
                    except Exception as error:
                        print 'Error',contador,'en cerrar cuadro reactions comentario', error
                        contador += 1
                        pass
    

            m += 1
    
    
    # SEE ALL REVIEWS OF REVIEWS
    load = False
    contador = 0
    while load is False and contador < 5:
        try:			
            see_more_reviews_of_reviews = driver_post.find_element_by_xpath(".//div[@class=' UFIReplyList']")
            print "see_more_reviews_of_reviews-->",see_more_reviews_of_reviews.text
            see_more_reviews_of_reviews.click()
            load = True
        except Exception as error:
            print 'Error',contador,'en see_more_reviews_of_reviews', error
            contador += 1
            pass
    
    load = False
    contador = 0
    while load is False and contador < 5:
        try:
            reviews_reviews = driver_post.find_elements_by_xpath(".//div[@class=' UFIReplyList']/div[contains(@class,'UFIRow') and contains(@class,'UFIComment')]")
            print 'reviews_reviews-->', reviews_reviews 
            load = True
        except Exception as error:
            print 'Error',contador,'en reviews_reviews', error
            contador += 1
            pass

    m += 0
    if reviews_reviews:
        for review_reviews in reviews_reviews:
            print 'Comentario de comentario numero', m
            print 'aria label de la review-->',review_reviews.get_attribute('aria-label') 
            if review_reviews.get_attribute('aria-label') == 'Comentario':
                print 'Es comentario con identificador--> ', review_reviews.get_attribute('data-ft')
            elif review_reviews.get_attribute('aria-label') == 'Respuesta a un comentario':
                print 'Es una respuesta al comentario--> ', review_reviews.get_attribute('data-ft')

            load = False
            contador = 0
            while load is False and contador < 5:
                try:
                    #review_text = review.find_element_by_xpath(".//span[@class='UFICommentBody']/span")
                    review_reviews_text = review_reviews.find_element_by_xpath(".//span[@class='UFICommentBody']")

                    print 'review'+str(m)+'-->',review_reviews_text.text
                    load = True
                except Exception as error:
                    print 'Error',contador,'en review_reviews', error
                    contador += 1
                    pass	

            #REACTIONS REVIEW_REVIEWS CLICK BUTTON
            load = False
            contador = 0
            review_reviews_click = False
            while load is False and contador < 5:
                try:
                    review_reviews.find_element_by_xpath("//span[@class='_3t54']").click()
                    load = True
                    review_reviews_click = True

                except Exception as error:
                    print 'Error',contador,'en click reactions comentario de comentario', error
                    contador += 1
                    pass
            if review_click is True:
                #review_reviews.find_element_by_xpath(".//div[contains(@class,'UFICommentReactionsBling')]").click()
                load = False
                contador = 0				
                try:
                    body=driver_posts.find_element_by_tag_name("body")
                    print 'body-->', body
                    load = True
                except Exception as error:
                    print 'Error',contador,'get body', error
                    time.sleep(3)
                    contador += 1					
                    pass


                #REACTIONS REVIEW_REVIEWS
                load = False
                contador = 0
                reactions_review_reviews = None
                while load is False and contador < 5:
                    try:
                        print 'Estoy cogiendo REACTIONS REVIEW_REVIEWS'
                        reactions_review_reviews = body.find_elements_by_xpath(".//li[contains(@class, '_ds-') and contains(@class, ' _45hc')]")
                        print "reactions_review_reviews-->",reactions_review_reviews
                        load = True
                    except Exception as error:
                        print 'Error',contador,'en reactions review_reviews', error
                        contador += 1
                        pass
                    #Could be not load
                    if not reactions_review_reviews and load:
                        print 'No ha cargado. Se repite'
                        load = False
                        time.sleep(3)
                    if contador >= 5:
                        load = True
                        print 'Se sigue. No se cargó'


                if reactions_review_reviews:
                    print 'Estoy en REACTIONS REVIEW REVIEW'
                    name = 'comentarios de un comentario'
                    get_reactions(reactions_review_reviews, name)
                
                # CLOSE REACTIONS REVIEW_REVIEWS SQUARE
                load = False
                contador = 0
                while load is False and contador < 5:
                    try:
                        body.find_element_by_xpath(".//a[@title='Cerrar']").click()
                        load = True
                    except Exception as error:
                        print 'Error',contador,'en cerrar cuadro reactions comentario de comentario', error
                        contador += 1
                        pass
            m += 1
        '''
    if n == 2:
        import sys
        sys.exit()


    #Pasamos al siguiente Post
    print ''
    print '--------------------'
    print '--------------------'
    print ''
    n += 1



