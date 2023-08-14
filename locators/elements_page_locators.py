from selenium.webdriver.common.by import By

class LogInLocators:

    LOGIN = (By.ID, 'passp-field-login')
    PASS = (By.ID, 'passp-field-passwd')
    BATTON_LOG_IN = (By.ID, 'passp:sign-in')
    HINT  = (By.ID, 'field:input-login:hint')
    PHONE_BATTON = (By.CSS_SELECTOR, 'button[data-type="phone"]')
    PHONE = (By.ID, 'passp-field-phone')
    PHONE_HINT = (By.ID, 'field:input-phone:hint')
    PHONE_CODE = (By.ID, 'passp-field-phoneCode')