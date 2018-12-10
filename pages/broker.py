from core.client import create_dealtap_driver


class Broker(object):
    LOCATOR_DICT = {
        'broker video link': "css=div[class*='hero-broker-video']",
    }

    def __init__(self):
        self._dealtap_driver = create_dealtap_driver()
        self._dealtap_driver.locator_dictionary = self.LOCATOR_DICT

    def verify_broker_page_contains_broker_video(self):
        return self._dealtap_driver.is_element_visible('broker video link')
