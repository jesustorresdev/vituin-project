# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, datetime
import hashlib

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

def get_reactions(reactions, name, driver):
    number_like = None
    number_love = None
    number_wow = None
    number_enjoy = None
    number_sad = None
    number_angry = None
    body=driver.find_element_by_tag_name("body")


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

    reactions_values= {
        'likes':number_like,
        'loves':number_love,
        'wows':number_wow,
        'enjoyes':number_enjoy,
        'sads':number_sad,
        'angries':number_angry
    }
    return reactions_values

def get_data_Facebook(days, result):
    samples_posts = result["samples_posts"]

    fp = webdriver.FirefoxProfile()
    fp.set_preference("dom.webnotifications.enabled", False)
    driver = webdriver.Firefox(fp)
    # driver_posts = webdriver.Firefox(fp)
    #driver_posts = webdriver.Firefox(fp)
    #ChromeDriver options notification
    #chrome_options = webdriver.ChromeOptions()
    #prefs = {"profile.default_content_setting_values.notifications" : 2}
    #chrome_options.add_experimental_option("prefs",prefs)
    #driver = webdriver.Chrome(chrome_options=chrome_options)

    #GeckoDriver options notification

    page = 'VisitPuertodelaCruz'

    driver.get('https://www.facebook.com/')


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


    i = 0
    n_posts_old = 0

    now = datetime.datetime.today()
    last_creation_time = now

    contador_load = 0
    last_day = False
    while 500 > (now - last_creation_time).days or last_day is True:
        # while days > (now - last_creation_time).days:
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
                contador_load +=1
            else:
                contador_load = 0
                creation_time = posts[len(posts)-1].find_elements_by_xpath(".//abbr")
                date = creation_time[0].get_attribute('title')
                last_creation_time = datetime.datetime.strptime(date, '%d/%m/%Y %H:%M')
                print 'iteracion',i,', number of posts-->',len(posts),', día-->',date
                n_posts_old = len(posts)
                load = True
                i += 1

            if contador_load >= 10:
                last_day = True


        # Scroll
        html=driver.find_element_by_tag_name("html")
        html.send_keys(Keys.END)

    result['index_posts'] = len(posts)

    #START
    n = 0
    for post in posts:
        url = None
        creation_time = None

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
                creation_time = creation_time[0].get_attribute('title')
                print 'creation_time-->',creation_time
                load = True
            except Exception as error:
                print 'Error',contador,'en creation_time', error
                contador += 1
                pass



        load = False
        contador = 0
        while load is False and contador < 5:
            try:
                url = post.find_elements_by_xpath(".//a[@class='_5pcq']")[0].get_attribute('href')
                print 'url-->', url
                load = True
            except Exception as error:
                print 'Error',contador,'en id_post', error
                contador += 1
                pass

        creation_time = datetime.datetime.strptime(creation_time, '%d/%m/%Y %H:%M')

        extraction_time = datetime.datetime.today()
        year = creation_time.year
        month = creation_time.month
        day = creation_time.day
        samples_posts.append([url,creation_time,year, month, day, extraction_time])
        result["samples_posts"] = samples_posts
        # samples_posts.append([id, message, comments, shares,reproductions,likes,loves,wows,enjoyes,sads,angries])
        # key = get_key(samples_posts[n+1])
        # samples_posts[n+1].extend([key, creation_time,year, month, day, extraction_time])

        #Pasamos al siguiente Post
        print ''
        print '--------------------'
        print '--------------------'
        print ''

        n += 1


    return result

