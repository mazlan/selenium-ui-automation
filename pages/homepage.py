from core.client import create_dealtap_driver


class Home(object):
    LOCATOR_DICT = {
        'home nav bar link': "css=a[class*='logo nav-link logo--homepage']",
        'agent nav bar link': "css=div.nav-item.nav-homepage > a[href*=agent]",
        'broker nav bar link': "css=a[href*=broker][class*='nav-link nav-link--homepage']",
        'pricing nav bar link': "css=a[href*=pricing][class*='nav-link nav-link--homepage']",
        'support nav bar link': "css=a[href*=zendesk][class*='nav-link nav-link--homepage']",
        'home page header': "css=div.hero-content-wrap>div.hero-content.hero-content-main>"
                            "h1.hero-heading.home-hero-heading",
        'login link': "css=a[href*=login][class*='nav-link nav-link-bold']",
        'signup link': "css=a[href*=signup][class*='btn-small nav-link hero-content-wrap']",
    }

    def __init__(self):
        self._dealtap_driver = create_dealtap_driver()
        self._dealtap_driver.locator_dictionary = self.LOCATOR_DICT

    def click_home_link_from_navigation_menu(self):
        self._dealtap_driver.click('home nav bar link')

    def click_agent_link_from_navigation_menu(self):
        self._dealtap_driver.click('agent nav bar link')

    def click_broker_link_from_navigation_menu(self):
        self._dealtap_driver.click('broker nav bar link')

    def click_pricing_link_from_navigation_menu(self):
        self._dealtap_driver.click('pricing nav bar link')

    def click_support_link_from_navigation_menu(self):
        self._dealtap_driver.click('support nav bar link')

    def get_homepage_page_header_text(self):
        return self._dealtap_driver.get_text('home page header')

    def click_login_from_homepage(self):
        self._dealtap_driver.click('login link')

    def click_signup_from_homepage(self):
        self._dealtap_driver.click('signup link')
