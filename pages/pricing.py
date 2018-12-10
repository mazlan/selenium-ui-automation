from core.client import create_dealtap_driver


class Pricing(object):
    LOCATOR_DICT = {
        'pricing page heading': "css=h1[class='hero-heading']",
    }

    def __init__(self):
        self._dealtap_driver = create_dealtap_driver()
        self._dealtap_driver.locator_dictionary = self.LOCATOR_DICT

    def get_pricing_page_header_text(self):
        return self._dealtap_driver.get_text('pricing page heading')
