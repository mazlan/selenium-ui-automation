import unittest
from core.client import DealTapAut
from pages.homepage import Home
from pages.agent import Agent
from pages.broker import Broker
from pages.pricing import Pricing
from pages.support import Support
from pages.login import Login


class TestHomePageNavigation(unittest.TestCase):

    def setUp(self):
        self.dealtap_aut = DealTapAut()
        self.dealtap_aut.launch()

    def tearDown(self):
        self.dealtap_aut = DealTapAut()
        self.dealtap_aut.close_browser()

    def test_agent_section_navigation_from_home(self):
        home_page = Home()
        home_page.click_agent_link_from_navigation_menu()
        agent_page = Agent()
        agent_video_exists = agent_page.verify_agent_page_contains_agent_video()
        self.assertTrue(agent_video_exists, "Agent Page is missing the Agent Introduction video!")

    def test_broker_section_navigation_from_home(self):
        home_page = Home()
        home_page.click_broker_link_from_navigation_menu()
        broker_page = Broker()
        broker_video_exists = broker_page.verify_broker_page_contains_broker_video()
        self.assertTrue(broker_video_exists, "Broker Page is missing the Broker Introduction video!")

    def test_pricing_section_navigation_from_home(self):
        home_page = Home()
        home_page.click_pricing_link_from_navigation_menu()
        pricing_page = Pricing()
        actual_pricing_header_text = pricing_page.get_pricing_page_header_text()
        expected_pricing_header_text = "Your Contract Processing Is About To Get A Whole Lot Better"
        self.assertEqual(actual_pricing_header_text, expected_pricing_header_text)

    def test_support_section_navigation_from_home(self):
        home_page = Home()
        home_page.click_support_link_from_navigation_menu()
        support_page = Support()
        actual_support_header_text = support_page.get_support_page_header_text()
        expected_support_header_text = "What Can We Help You With?"
        self.assertEqual(actual_support_header_text, expected_support_header_text)

    def test_navigation_back_home_from_home(self):
        home_page = Home()
        home_page.click_home_link_from_navigation_menu()
        actual_main_header_text = home_page.get_homepage_page_header_text()
        expected_main_header_text = "Real Estate Contracts\nDone Brilliantly"
        self.assertEqual(actual_main_header_text, expected_main_header_text)

    def test_login_page_navigation_from_home(self):
        home_page = Home()
        home_page.click_login_from_homepage()
        login_page = Login()
        actual_login_header_text = login_page.get_login_page_header_text()
        expected_login_header_text = "Log into Account"
        self.assertEqual(actual_login_header_text, expected_login_header_text)


if __name__ == '__main__':
    unittest.main()
