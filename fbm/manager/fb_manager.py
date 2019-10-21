from fbm.manager.webcontent_manager import WebContentManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import (WebDriverException,
StaleElementReferenceException, NoSuchElementException)
import time
import os
import re

class FbContentManager(WebContentManager):

    def __init__(self, webpage="http://www.facebook.com", email=None, password=None, **kwargs):
        super().__init__(**kwargs)
        self.webpage = webpage
        self.__email = email
        self.__password = password
        
    def sign_in(self):
        '''
        This function allows us to log into Facebook.com.

        '''
        if self.browser:
            self.redirect_to_website(self.browser, self.webpage)
        else:
            print("Connection: Page not responding error.")

        email_input = self.browser.find_element_by_name("email")
        email_input.send_keys(self.__email)
        time.sleep(self._sleep_seconds)

        password_input = self.browser.find_element_by_name("pass")
        password_input.send_keys(self.__password)
        password_input.send_keys(Keys.ENTER)

        time.sleep(self._sleep_seconds)
    
    def __str__(self):
        return f"Content Manager of website: {self.webpage}."



