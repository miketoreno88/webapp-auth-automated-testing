import pytest
from selenium.common.exceptions import TimeoutException
from pages.login_page import LoginPage
from data.data import get_user_data_phone
from locators.elements_page_locators import LogInLocators

@pytest.mark.usefixtures("driver")
class TestLoginPhone:

    @pytest.mark.parametrize("user_data", get_user_data_phone())
    def test_successful_login_phone(self, driver, user_data):
        login_page = LoginPage(driver, 'https://passport.yandex.ru/')

        login_page.open()
        login_page.login_phone(user_data["phone"])

        try:
            error_message_element = login_page.wait_for_element(LogInLocators.PHONE_HINT)
            error_message = error_message_element.text.strip()
            assert error_message in [
                "Недопустимый формат номера",
                "Сервис не смог обработать запрос. Обновите страницу и попробуйте еще раз."
            ]
        except TimeoutException:
            try:
                login_page.wait_for_element(LogInLocators.PHONE_CODE)
            except TimeoutException:
                pytest.fail("Element LogInLocators.PHONE_CODE did not appear")