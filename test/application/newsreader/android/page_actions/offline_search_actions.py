from test.application.newsreader.android.page_locators.offline_search_locators import OfflineSearchLocators


class OfflineSearchActions:

    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.log = log
        self.driver = driver

        self.offline_search_locators = OfflineSearchLocators(driver, log)

    def click_newest_search_filter_button(self):
        self.log.info("Clicking 'newest' search filter button.")
        return self.offline_search_locators.newest_search_filter_button().click()

    def click_oldest_search_filter_button(self):
        self.log.info("Clicking 'oldest' search filter button.")
        return self.offline_search_locators.oldest_search_filter_button().click()
