from core.client import create_dealtap_driver


class Login(object):
    LOCATOR_DICT = {
        'login form header title': "css=div[class='formFrame-headerTitle']",
        'username field': "css=input[name='email']",
        'password field': "css=input[name='password']",
        'login button': "xpath=(//div[@class='dtButton-caption dtEllipsis'])[2]",
        'login failed': "css=div[class='dtFormDescription-line']",
        'login failed okay button': "css=div[class='dtToolbarItem-caption dtEllipsis']",
        'email invalid': "css=div[class='inputText-validationText']",
        'login passed': "css=div[class='appHeader-section appHeader-section--label']",
    }

    def __init__(self):
        self._dealtap_driver = create_dealtap_driver()
        self._dealtap_driver.locator_dictionary = self.LOCATOR_DICT

    def get_login_page_header_text(self):
        return self._dealtap_driver.get_text('login form header title')

    def set_login_page_username(self, username):
        self._dealtap_driver.set_text('username field', username)

    def set_login_page_password(self, password):
        self._dealtap_driver.set_text('password field', password)

    def click_on_login_button(self):
        elem = self._dealtap_driver.find_element('login button')
        self._dealtap_driver.execute_javascript("arguments[0].click();", elem)

    def get_login_failed_text(self):
        return self._dealtap_driver.get_text('login failed')

    def get_login_passed_text(self):
        return self._dealtap_driver.get_text('login passed')

    def click_on_login_failed_okay_button(self):
        elem = self._dealtap_driver.find_element('login failed okay button')
        self._dealtap_driver.execute_javascript("arguments[0].click();", elem)

    def get_invalid_email_text(self):
        return self._dealtap_driver.get_text('email invalid')
