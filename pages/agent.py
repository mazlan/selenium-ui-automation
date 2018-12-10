from core.client import create_dealtap_driver


class Agent(object):
    LOCATOR_DICT = {
        'agent video link': "css=div[class*='hero-agent-video']",
    }

    def __init__(self):
        self._dealtap_driver = create_dealtap_driver()
        self._dealtap_driver.locator_dictionary = self.LOCATOR_DICT

    def verify_agent_page_contains_agent_video(self):
        return self._dealtap_driver.is_element_visible('agent video link')
