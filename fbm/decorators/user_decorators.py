
from selenium.common.exceptions import (
WebDriverException, StaleElementReferenceException,
NoSuchElementException
)

def except_element_errors(function):
    
    def func_wrapper(self, *args):
        try:
            print(
                f"""Trying to find an element on page.
                Executing function: {function.__name__}."""
            )
            return function(self, *args)
        except NoSuchElementException as e:
            print(" ----- No such elemet on page. -----")
            print(e)
        except WebDriverException as w:
            print(" ----- Web Driver Exception. -----")
            print(w)

    return func_wrapper