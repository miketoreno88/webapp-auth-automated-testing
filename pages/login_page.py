from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.elements_page_locators import LogInLocators


class LoginPage(BasePage):

    def login(self, username):
        self.username_input = self.wait_for_element(LogInLocators.LOGIN)
        self.login_button = self.wait_for_element(LogInLocators.BATTON_LOG_IN)

        self.username_input.send_keys(username)
        self.login_button.click()


    def password(self, password):
        password_input = self.wait_for_element(LogInLocators.PASS)
        login_button = self.wait_for_element(LogInLocators.BATTON_LOG_IN)

        password_input.send_keys(password)
        login_button.click()

    def login_phone(self, userphone):
        self.phone_button = self.wait_for_element(LogInLocators.PHONE_BATTON)
        self.phone_button.click()
        self.userphone_input = self.wait_for_element(LogInLocators.PHONE)
        self.userphone_input.send_keys(userphone)

        self.login_button = self.wait_for_element(LogInLocators.BATTON_LOG_IN)
        self.login_button.click()