from selenium.common import NoSuchElementException
from test.application.newsreader.android.page_locators.content_locators import ContentLocators


class ContentActions:

    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.log = log
        self.driver = driver

        self.content_locators = ContentLocators(driver, log)

    def get_offline_pop_up_text(self):
        self.log.info("Getting device offline pop-up text")
        return self.content_locators.device_offline_pop_up().text

    def is_online_content_shown(self):
        self.log.debug("Verifying the Today tab shows content layout.")
        try:
            self.content_locators.online_content_element()
            return True
        except NoSuchElementException:
            self.log.debug(msg="NoSuchElementException: No content found on Today tab.")
            return False

    def is_offline_pop_up_shown(self):
        self.log.info("Verifying the Today tab is showing 'device offline' pop-up.")
        try:
            self.content_locators.device_offline_pop_up()
            return True
        except NoSuchElementException:
            self.log.debug(msg="NoSuchElementException: 'Device offline' pop-up not found on Today tab.")
            return False
