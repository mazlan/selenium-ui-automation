import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from settings import CLIENT_NAME, Client, LAUNCH_MODE, LaunchMode, URL, LocatorType


class LauncherNotSupported(Exception):
    pass


class LaunchModeNotSupported(Exception):
    pass


class InvalidLocatorException(Exception):
    pass


list_of_supported_locator_type = (
    LocatorType.id,
    LocatorType.name,
    LocatorType.xpath,
    LocatorType.link_text,
    LocatorType.partial_link_text,
    LocatorType.tag,
    LocatorType.class_name,
    LocatorType.css,
)

dictionary_of_locator_type_and_description = {
    LocatorType.id: By.ID,
    LocatorType.name: By.NAME,
    LocatorType.xpath: By.XPATH,
    LocatorType.link_text: By.LINK_TEXT,
    LocatorType.partial_link_text: By.PARTIAL_LINK_TEXT,
    LocatorType.tag: By.TAG_NAME,
    LocatorType.class_name: By.CLASS_NAME,
    LocatorType.css: By.CSS_SELECTOR
}


def wait_till_browser_is_ready(func):
    def ensure_browser_is_in_ready_state(self, *agrs):
        WebDriverWait(self.driver, self.wait_timeout).until(
            lambda driver:
            driver.execute_script(
                'return document.readyState == "complete";'),
            'page is not completely loaded'
        )
        return func(self, *agrs)

    return ensure_browser_is_in_ready_state


def wait_till_element_is_visible(func):
    def ensure_element_visible(self, *args):
        locator = args[0]
        WebDriverWait(self.driver, self.wait_timeout).until(
            lambda driver:
            self.is_element_visible(locator)
        )
        return func(self, *args)

    return ensure_element_visible


class Launcher(object):
    def launch(self):
        raise NotImplemented("launch method not implemented")


class ChromeLauncher(Launcher):
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.add_argument("--disable-infobars")
        self.chrome_options.add_argument("--test-type")
        if os.name == 'posix':
            self.chrome_options.add_argument("--kiosk")
        else:
            self.chrome_options.add_argument("--start-maximized")

    def launch(self):
        web_driver = webdriver.Chrome(chrome_options=self.chrome_options)
        web_driver.get(URL)
        return web_driver


class DealTapDriver(object):
    def click(self, name_of_item):
        raise NotImplemented

    def get_text(self, name_of_item):
        raise NotImplemented

    def launch_aut(self):
        raise NotImplemented

    def quit_aut(self):
        raise NotImplemented


class DealTapWebDriver(DealTapDriver):
    def __init__(self, driver=None):
        self.driver = driver
        self.locator_dictionary = None
        self.wait_timeout = 20

    def launch_aut(self):
        launcher = get_launcher_from_factory()
        driver = launcher.launch()
        return driver

    @wait_till_element_is_visible
    def click(self, name_of_item):
        element = self.find_element(name_of_item)
        element.click()

    @wait_till_element_is_visible
    def get_text(self, name_of_item):
        element = self.find_element(name_of_item)
        return element.text

    @wait_till_element_is_visible
    def set_text(self, name_of_item, text_to_set, append=False):
        element = self.find_element(name_of_item)
        if append:
            element.send_keys(text_to_set)
        else:
            element.clear()
            element.send_keys(text_to_set)

    @wait_till_browser_is_ready
    def find_element(self, name_of_locator):
        locator_description = self.locator_dictionary[name_of_locator]
        locator_type = locator_type_detector(locator_description)
        locator_description = locator_description.replace("{}=".format(locator_type), "", 1)

        return self.driver.find_element(
            dictionary_of_locator_type_and_description[locator_type],
            locator_description
        )

    def is_element_visible(self, locator):
        try:
            element = self.find_element(locator)
            return element.is_displayed() and element.is_enabled()
        except NoSuchElementException:
            return False

    def quit_aut(self):
        self.driver.quit()

    def execute_javascript(self, script, *args):
        return self.driver.execute_script(script, *args)


def get_launcher_from_factory():
    if CLIENT_NAME == Client.CHROME:
        return ChromeLauncher()
    else:
        raise LauncherNotSupported()


def get_dealtap_driver_from_factory(driver=None):
    if LAUNCH_MODE == LaunchMode.WEB:
        return DealTapWebDriver(driver)
    else:
        raise LaunchModeNotSupported()


def locator_type_detector(locator_description):
    actual_locator_type = locator_description[0: locator_description.find('=')]
    locator = list([locator for locator in list_of_supported_locator_type if locator == actual_locator_type])

    if len(locator) != 1:
        raise InvalidLocatorException("locator named {} is not a valid locator ".format(actual_locator_type))

    return locator[0]
