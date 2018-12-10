from core.client import create_dealtap_driver


class Support(object):
    LOCATOR_DICT = {
        'support page heading': "css=div[class='hero-inner']",
    }

    def __init__(self):
        self._dealtap_driver = create_dealtap_driver()
        self._dealtap_driver.locator_dictionary = self.LOCATOR_DICT

    def get_support_page_header_text(self):
        return self._dealtap_driver.get_text('support page heading')
