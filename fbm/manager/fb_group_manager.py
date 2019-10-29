from fbm.manager.fb_manager import FbContentManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import (WebDriverException,
StaleElementReferenceException, NoSuchElementException)
import time 
import re
from fbm.decorators.user_decorators import except_element_errors

class FbGroupContentManager(FbContentManager):

    __INVITES = 0

    def __init__(self, fb_group_id, **kwargs):
        super().__init__(**kwargs)
        self.fb_group_id = fb_group_id
    
    def redirect_to_group(self):
        '''
        This function redirects us to the group page and scrolls page to half of the page.
        
        '''
        self.browser.get(self.webpage + '/groups/' + self.fb_group_id)
        time.sleep(self._sleep_seconds)
        self.browser.execute_script('window.scrollTo(0,400)')

    @except_element_errors
    def check_new_members(self):
        '''
        This function finds a section with the number of new users 
        and returns TRUE if it is more than 40.

        '''
        element = self.browser.find_element_by_class_name('_3ip6')
        number_of_members = re.findall('\d+', element.text)

        return int(number_of_members[0]) > 40

    @except_element_errors
    def write_post(self):
        '''
        This method writes a welcome message to new group fans.

        '''
        if self.check_new_members() == True:
            buttons = self.browser.find_elements_by_css_selector(
                '._42ft._4jy0._4jy3._517h._51sy.mls'
            )
            clicks = [button.click() for button in buttons if button.text == 'Write Post']
            time.sleep(self._sleep_seconds)
            self.browser.execute_script('window.scrollTo(0,2000)')

            time.sleep(self._sleep_seconds)
            post_button = self.browser.find_element_by_css_selector(
                '._1mf7._4jy0._4jy3._4jy1._51sy.selected._42ft'
            )
            time.sleep(self._sleep_seconds)
            post_button.click()
        else:
            print("There are no new users.")
    
    @except_element_errors
    def invite_people_to_group(self):
        '''
        This function finds elements with the 'INVITE' button and clicks on each.

        '''
        element = self.browser.find_element_by_xpath("//div[@class='_6a rfloat _ohf']")

        while element:
            FbGroupContentManager.__INVITES += 1
            element.click()
            time.sleep(self.sleep_seconds * 2)
            element = self.browser.find_element_by_xpath("//div[@class='_6a rfloat _ohf']")
            time.sleep(self.sleep_seconds * 2)

        print("No more people to invite.")
    
    @except_element_errors
    def approve_new_users(self):
        '''
        This function finds elements with 'pending users' button and clicks on each.

        '''
        self.browser.execute_script('window.scrollTo(0,100)')
        request_button = self.browser.find_element_by_css_selector('._39g3')
        print(request_button.text)
        request_button.click()

        submit_button = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.NAME, "approve_all"))
        )
        submit_button.click()
        time.sleep(self.sleep_seconds)

        confirm_button = self.browser.find_element_by_css_selector(
            '.layerConfirm._4jy0._4jy3._4jy1._51sy.selected._42ft'
        )
        confirm_button.click()
        time.sleep(self.sleep_seconds)
    
    @property
    def invites(self):
        return FbGroupContentManager.__INVITES
