import unittest
from time import sleep
from core.client import DealTapAut
from pages.homepage import Home
from pages.signup import SignUp


class TestSignUp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dealtap_aut = DealTapAut()
        cls.dealtap_aut.launch()
        cls.home_page = Home()
        cls.home_page.click_signup_from_homepage()
        sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.dealtap_aut = DealTapAut()
        cls.dealtap_aut.close_browser()

    def _create_a_new_account(self):
        signup_page = SignUp()
        signup_page.set_signup_page_email('random3@myworkemail.com')
        signup_page.set_signup_page_password('Password1234')
        signup_page.set_signup_page_confirm_password('Password1234')
        sleep(1)
        signup_page.click_on_next_button()
        sleep(1)

    def _create_personal_information(self):
        signup_page = SignUp()
        signup_page.set_signup_page_firstname('John')
        signup_page.set_signup_page_lastname('Doe')
        signup_page.set_signup_page_phone('519-222-3333')
        sleep(1)
        signup_page.click_on_next_button()

    def test_valid_signup_for_user(self):
        self._create_a_new_account()
        self._create_personal_information()
        signup_page = SignUp()
        sleep(1)
        signup_page.search_and_set_brokerage_information('Centu')
        sleep(4)
        signup_page.click_on_submit_button()
        actual_signup_passed_text = signup_page.get_activate_email_text()
        expected_signup_passed_text = "Your account was created successfully."
        self.assertEqual(actual_signup_passed_text, expected_signup_passed_text)


if __name__ == '__main__':
    unittest.main()
