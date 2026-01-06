from selenium.webdriver.common.by import By
from pages.base_page import BasePage

""" Page Object Model for OrangeHRM Login Page """
class LoginPage(BasePage):

    # ------------------ LOCATORS ------------------
    USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    # Stable post-login identifiers
    USER_PROFILE_NAME = (By.XPATH, "//p[contains(@class,'oxd-userdropdown-name')]")

    # ------------------ PAGE ACTIONS ------------------
    def login(self, username: str, password: str):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)


    # ------------------ VALIDATIONS ------------------
    def is_login_successful(self) -> bool:
        """
        Verify successful login by checking dashboard URL
        and presence of user profile name
        """
        self.wait_for_url_contains("/dashboard")
        return self.is_displayed(self.USER_PROFILE_NAME)
