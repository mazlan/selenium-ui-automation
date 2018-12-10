from core.driver import get_dealtap_driver_from_factory, DealTapWebDriver

DRIVER = None


class DealTapAut(object):
    def launch(self):
        dealtap_driver = get_dealtap_driver_from_factory()
        global DRIVER
        DRIVER = dealtap_driver.launch_aut()

    def close_browser(self):
        global DRIVER
        dealtap_driver = DealTapWebDriver(DRIVER)
        dealtap_driver.quit_aut()


def create_dealtap_driver():
    global DRIVER
    return get_dealtap_driver_from_factory(DRIVER)
