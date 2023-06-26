from test.core.mobile.device_actions import DeviceActions
from test.application.newsreader.android.page_locators.search_locators import SearchLocators


class SearchActions:

    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.log = log
        self.driver = driver

        self.device_actions = DeviceActions(driver, log)
        self.search_locators = SearchLocators(driver, log)

    def click_search_text_field(self):
        self.log.info("Clicking search text field.")
        self.search_locators.search_field().click()

    def input_search_text_field_string(self, search_string):
        self.log.info("Input search text field string: '{0}'".format(search_string))
        return self.search_locators.search_field().send_keys(search_string)

    def submit_search(self):
        self.log.info("Submit search.")
        self.device_actions.press_keycode(66)
