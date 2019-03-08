# -*- coding: UTF-8 -*-

__authors__='Sergio Díaz, Jesús Torres'
__organization__='Universidad de La Laguna'
__licensed__='UNLICENSED'
__contact__="jmtorres@ull.edu.es, sdiazgon@ull.edu.es"
# __copyright__=f"Copyright 2017-2018 {__organization__}"

import sys, time, os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from scrapy.exceptions import CloseSpider
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options


class SeleniumSpider():

    def __init__(self, width=False, height=False):
        self.driver=webdriver.Chrome()
        if width is not False and height is not False:
            self.driver.set_window_size(width,height)

    # def __del__(self):
    #     try:
    #         self.clear_cache(self.driver)
    #     except:
    #         pass
    #     try:
    #         self.driver.close()
    #     except:
    #         pass

    def reset_browser(self):
        try:
            self.close_browser()
        except:
            pass

        self.driver=webdriver.Chrome()
        self.driver.get(self.url)
        time.sleep(.5)

    # def close_browser(self):
    #     try:
    #         self.clear_cache(self.driver)
    #     except:
    #         pass
    #     try:
    #         self.driver.close()
    #     except:
    #         pass

    def close_browser(self):
        try:
            self.clear_cache(self.driver)
        except:
            pass
        try:
            self.driver.close()
        except:
            pass

    def close_and_kill_browser(self):
        try:
            self.clear_cache(self.driver)
        except:
            pass
        try:
            self.driver.close()
        except:
            pass

        self.kill_chrome()
        self.kill_chromedriver()

    def set_url(self, url):
        self.url=url
        self.open_url()

    def open_url(self):
        # try:
        self.driver.get(self.url)
        # except:
        #     self.reset_browser()

    def kill_chromedriver(self):
        os.system("pkill -f chromedriver")

    def kill_chrome(self):
        os.system("pkill -f chrome")

    def xpath(self, xpath, selenium_object=None, type='text', attribute=None, pos_array=None, stop_if_error=False,
              number_of_attemps=3, time_sleep_if_error=False, **kwords):

        driver = selenium_object if selenium_object else self.driver

        n=kwords['n'] if 'n' in kwords else 0
        m=kwords['m'] if 'm' in kwords else 0
        try:
            if xpath != './':
                element = driver.find_element_by_xpath(xpath) if pos_array is None and type != 'object' else \
                    driver.find_elements_by_xpath(xpath)
            else:
                element = driver


            if pos_array:
                element = element[pos_array]


            element = element.text if type == 'text' else \
                element.get_attribute(attribute) if type == 'attribute' else \
                element

            if not element and time_sleep_if_error and m < 3:
                time.sleep(.5)
                return self.xpath(xpath, selenium_object, type, attribute, pos_array, stop_if_error, number_of_attemps,
                                  time_sleep_if_error, m=m+1)
            return element

        except Exception as error:
            print('Error en línea', ' --- ', error, 'al extraer', xpath, ', ', str(self.url), ': ', str(error))
            if time_sleep_if_error and m < 3:
                time.sleep(.5)
                return self.xpath(xpath, selenium_object, type, attribute, pos_array, stop_if_error, number_of_attemps,
                                  time_sleep_if_error, m=m+1)

            if  stop_if_error:
                self.close_and_kill_browser()
                message = 'STOP obligatorio en caso de error selenium. Hay error en '+str(self.url)+'", '+xpath+' : '+\
                          str(error)
                # self.send_email(message)
                raise CloseSpider(message)

            if  n >= number_of_attemps or selenium_object:
                return ''
            else:
                self.open_url()
                time.sleep(.5)
                return self.xpath(xpath, selenium_object, type, attribute, pos_array, stop_if_error, number_of_attemps,
                                  time_sleep_if_error, n=n+1)

    def get_coordinates_google_map(self, pos_above=False, english_page=False, **kwords):
        n=kwords['n'] if 'n' in kwords else 0
        print ''
        print ''
        print 'INTENTO--->', n
        print ''
        print ''
        try:
            if pos_above:
                ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(pos_above)).perform()
                time.sleep(n*2)

            title='Report errors in the road map or imagery to Google' if english_page \
                else 'Informar a Google acerca de errores en las imágenes o en el mapa de carreteras'

            script_coordinates=self.driver.find_element_by_xpath("//a[@title ='"+title+"']").get_attribute('href')
            coordinates_string=script_coordinates[script_coordinates.find('@')+1:]
            lat=coordinates_string.split(',')[0]
            lng=coordinates_string.split(',')[1]
            return (lat,lng)
        except Exception as error:
            print('Error en línea',format(sys.exc_info()[-1].tb_lineno), ' --- ', error)
            if n >= 3:
                return '',''
            else:
                self.open_url()
                time.sleep(.5)
                return self.get_coordinates_google_map(pos_above, english_page, n=n+1)

    def get_clear_browsing_button(self):
        """Find the "CLEAR BROWSING BUTTON" on the Chrome settings page."""
        return self.driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm')

    def clear_cache(self, timeout=60):
        """Clear the cookies and cache for the ChromeDriver instance."""
        # navigate to the settings page
        self.driver.get('chrome://settings/clearBrowserData')

        # wait for the button to appear
        wait=WebDriverWait(self.driver, timeout)
        wait.until(self.get_clear_browsing_button)

        # click the button to clear the cache
        self.get_clear_browsing_button(self.driver).click()

        # wait for the button to be gone before returning
        wait.until_not(self.get_clear_browsing_button)