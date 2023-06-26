from appium.webdriver.common.appiumby import AppiumBy


class SearchLocators:

    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.log = log
        self.driver = driver

    def search_field(self):
        self.log.info("Finding Search EditText field")
        return self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")

    def saved_article_title(self):
        self.log.info("Finding saved article title text")
        return self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='‘Naatu Naatu’ From ‘RRR’ Is a Worldwide Hit, but It Draws on Very Local Traditions']")
