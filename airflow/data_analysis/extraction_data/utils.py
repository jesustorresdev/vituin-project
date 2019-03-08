# -*- coding: UTF-8 -*-

import re
from mail_settings import mailfrom, smtphost, smtpport, smtpuser, smtppass
from scrapy.mail import MailSender
from scrapy.exceptions import CloseSpider

##QUITAR DE AQUI A SCRAPY SPIDER

def split_try(element, pos=None, separator=' ', pos_aray=None, splitline=False):
    if pos_aray != None:
        try:
            element=element[pos_aray]
        except:
            return ''

    if pos != None:
        if splitline:
            try:
                return element.splitlines()[pos]
            except:
                return ''
        else:
            try:
                return element.split(separator)[pos]
            except:
                return ''
    else:
        if splitline:
            try:
                return element.splitlines()
            except:
                return ''
        else:
            try:
                element.split(separator)
            except:
                return ''

def type_try(element, type_change):
    try:
        if type_change==int:
            return int(element)
        elif type_change==float:
            return float(element)
        elif type_change==str:
            return str(element)
        else:
            return ''
    except:
         return ''
#
# QUITAR DE AQUI
#
#
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
