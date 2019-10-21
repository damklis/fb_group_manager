from abc import ABC, abstractclassmethod
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class WebContentManager(ABC):

    def __init__(self, headless=False):
        self.headless = headless
        self.browser = self.browser_with_options()
        self._sleep_seconds = 1

    @abstractclassmethod
    def sign_in(self):
        """
        Signs in provided webpage. Abstract method - need to be overwrited.

        """
        raise NotImplementedError("Must implement sign_in method.")

    def browser_with_options(self):
        """
        As default returns headless Chrome webdriver.

        """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.headless = self.headless
        prefs = {
            "profile.default_content_setting_values.notifications": 2
        }
        chrome_options.add_experimental_option("prefs", prefs)
        return webdriver.Chrome(options=chrome_options,
            executable_path="fbm/driver/chromedriver")
    
    @staticmethod
    def redirect_to_website(browser, site):
        """
        Redirects you to provided websire. Static method, you can use it
        on differetn sites, eg. "facebook, messenger, instagram".

        """
        browser.get(site)

    ### Creating setter for timesleep time in App.
    @property
    def sleep_seconds(self):
        return self._sleep_seconds

    @sleep_seconds.setter
    def sleep_seconds(self, seconds):
        self._sleep_seconds = seconds

    def close_browser_connection(self):
        '''
        This function closes browser.
        
        '''
        self.browser.close()