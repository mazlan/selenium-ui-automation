import unittest
from time import sleep
from core.client import DealTapAut
from pages.homepage import Home
from pages.login import Login


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.dealtap_aut = DealTapAut()
        self.dealtap_aut.launch()
        self.home_page = Home()
        self.home_page.click_login_from_homepage()

    def tearDown(self):
        self.dealtap_aut = DealTapAut()
        self.dealtap_aut.close_browser()

    def test_invalid_email_as_username(self):
        login_page = Login()
        login_page.set_login_page_username('john.doe')
        login_page.set_login_page_password('abc123')
        actual_invalid_email_text = login_page.get_invalid_email_text()
        expected_invalid_email_text = "Email is invalid."
        self.assertEqual(actual_invalid_email_text, expected_invalid_email_text)

    def test_failed_login_attempt(self):
        login_page = Login()
        login_page.set_login_page_username('john.doe@test.ca')
        login_page.set_login_page_password('abc123')
        sleep(3)
        login_page.click_on_login_button()
        actual_login_failed_text = login_page.get_login_failed_text()
        expected_login_failed_text = "Login failed. Incorrect username or password."
        login_page.click_on_login_failed_okay_button()
        self.assertEqual(actual_login_failed_text, expected_login_failed_text)

    def test_successful_login_attempt(self):
        login_page = Login()
        login_page.set_login_page_username('mazlanislam@outlook.com')
        login_page.set_login_page_password('Password1234')
        sleep(3)
        login_page.click_on_login_button()
        actual_login_passed_text = login_page.get_login_passed_text()
        expected_login_passed_text = "Dashboard - Home"
        self.assertEqual(actual_login_passed_text, expected_login_passed_text)


if __name__ == '__main__':
    unittest.main()
