from appium.webdriver.common.appiumby import AppiumBy


class OfflineSearchLocators:

    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.log = log
        self.driver = driver

    def newest_search_filter_button(self):
        self.log.info("Finding 'Newest' search filter button.")
        return self.driver.find_element(AppiumBy.ID, "com.nytimes.android:id/search_newest")

    def oldest_search_filter_button(self):
        self.log.info("Finding 'Oldest' search filter button.")
        return self.driver.find_element(AppiumBy.ID, "com.nytimes.android:id/search_oldest")

    def device_offline_element(self):
        self.log.info("Finding 'Device offline' text.")
        return self.driver.find_element(AppiumBy.ID,"com.nytimes.android:id/no_results_verbiage")
