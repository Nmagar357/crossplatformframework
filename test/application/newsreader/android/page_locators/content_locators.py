from appium.webdriver.common.appiumby import AppiumBy


class ContentLocators:

    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.log = log
        self.driver = driver

    def online_content_element(self):
        self.log.info("Finding 'Today' tab content layout.")
        return self.driver.find_element(AppiumBy.ID, "programming-list")

    def device_offline_pop_up(self):
        self.log.info("Finding 'Device is offline' pop-up.")
        return self.driver.find_element(AppiumBy.XPATH,
            "//android.widget.TextView[@text='Device is offline. Please check your Internet connection and try again.']"
        )
