# -*- coding: UTF-8 -*-

import unicodecsv as csv
import sys, os
from selenium import webdriver
driver = webdriver.Chrome()

filename=sys.argv[1]
f = open(filename)
samples = [row for row in csv.reader(f)]
samples[0].append("key")
url_position=2
i = 1
bugNumber = 0


while i < len(samples):
    url=samples[i][url_position]
    driver.get(url)

    try:
        coordenates = driver.find_element_by_xpath("//div[@class='_59m2yxn']/img").get_attribute('src')
        str_coor = str(coordenates)
        pos1 = str_coor.find("center")+7
        pos2 = str_coor.find("scale")-1
        coor = str_coor[pos1:pos2]
        coor = coor.split(',')
        lat = coor[0]
        lo=coor[1]
        print i, '--->',lat, lo
        bugNumber=0
        samples[i].append(lo)
        samples[i].append(lat)
        i+=1

    except:
        print 'error en', samples[i][0], ',iteracion',i, ', numero de error', bugNumber
        #If there error in driver, we're going to close this driver and create other
        driver = webdriver.Chrome()
        driver.get(url)
        bugNumber+=1
        if bugNumber > 5:
            i+=1
            bugNumber=0
            samples[i].append('')
            samples[i].append('')
        pass



driver.close()
#chromedriver dont stop itself
os.system("pkill -f chromedriver")

pos_end_name_field = filename.find('/')

with open('unstructured_data/coordinates_' + filename[pos_end_name_field+1:], 'wb') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerows(samples)

