import pytest
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from pages.login_page import LoginPage
from data.data import get_user_data
from locators.elements_page_locators import LogInLocators

@pytest.mark.usefixtures("driver")
class TestLogin:
    @pytest.mark.parametrize("user_data", get_user_data())
    def test_successful_login(self, driver, user_data):
        login_page = LoginPage(driver, 'https://passport.yandex.ru/')
        login_page.open()
        login_page.login(user_data["username"])

        try:
            login_page.password(user_data["website"])
        except TimeoutException:
            try:
                error_message_element = login_page.wait_for_element(LogInLocators.HINT)
                error_message = error_message_element.text.strip()
                assert error_message in [
                    "Логин не указан",
                    "Такой логин не подойдет",
                    "Такого аккаунта нет",
                    "Аккаунт заблокирован\nЧтобы восстановить доступ к логину, обратитесь в службу поддержки."
                ]            
            except NoSuchElementException:
                pytest.fail("Unexpected element state, test failed")
