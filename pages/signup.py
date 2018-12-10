from core.client import create_dealtap_driver
from time import sleep


class SignUp(object):
    LOCATOR_DICT = {
        'work email': "css=input[name='emailNew']",
        'new password': "css=input[name='passwordNew']",
        'confirm new password': "css=input[name='passwordNewAgain']",
        'first name': "css=input[name='firstName']",
        'last name': "css=input[name='lastName']",
        'phone': "css=input[name='phone']",
        'next button': "xpath=(//div[@class='dtButton-caption dtEllipsis'])[2]",
        'submit button': "xpath=(//div[@class='dtButton-caption dtEllipsis'])[3]",
        'search broker': "css=input[class*='inputSearch-input dtEllipsis']",
        'choose broker': "css=div[class='dtSelectListItemSimple-caption']",
        'activate email account': "css=div[class='dtActivateEmailAlert-title']",
    }

    def __init__(self):
        self._dealtap_driver = create_dealtap_driver()
        self._dealtap_driver.locator_dictionary = self.LOCATOR_DICT

    def set_signup_page_email(self, email):
        self._dealtap_driver.set_text('work email', email)

    def set_signup_page_password(self, password):
        self._dealtap_driver.set_text('new password', password)

    def set_signup_page_confirm_password(self, password):
        self._dealtap_driver.set_text('confirm new password', password)

    def set_signup_page_firstname(self, firstname):
        self._dealtap_driver.set_text('first name', firstname)

    def set_signup_page_lastname(self, lastname):
        self._dealtap_driver.set_text('last name', lastname)

    def set_signup_page_phone(self, phone):
        self._dealtap_driver.set_text('phone', phone)

    def search_and_set_brokerage_information(self, brokerage_text):
        self._dealtap_driver.set_text('search broker', brokerage_text)
        sleep(2)
        elem = self._dealtap_driver.find_element('choose broker')
        self._dealtap_driver.execute_javascript("arguments[0].click();", elem)
        sleep(1)
        self.click_on_next_button()

    def click_on_next_button(self):
        elem = self._dealtap_driver.find_element('next button')
        self._dealtap_driver.execute_javascript("arguments[0].click();", elem)

    def click_on_submit_button(self):
        elem = self._dealtap_driver.find_element('submit button')
        self._dealtap_driver.execute_javascript("arguments[0].click();", elem)

    def get_activate_email_text(self):
        return self._dealtap_driver.get_text('activate email account')
