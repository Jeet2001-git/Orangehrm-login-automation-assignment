from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

"""
   BasePage contains all common Selenium actions.
   All page classes should inherit from this class.
"""
class BasePage:

    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ------------------ WAIT METHODS ------------------

    def wait_for_visibility(self, locator):
        """Wait until element is visible on UI"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        """Wait until element is clickable"""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_url_contains(self, partial_url):
        """Wait until URL contains expected value"""
        self.wait.until(EC.url_contains(partial_url))


    # ------------------ ACTION METHODS ------------------

    def click(self, locator):
        element = self.wait_for_clickable(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.wait_for_visibility(locator)
        element.clear()
        element.send_keys(text)

    # ------------------ VALIDATION METHODS ------------------

    def is_displayed(self, locator):
        try:
            return self.wait_for_visibility(locator).is_displayed()
        except TimeoutException:
            return False
