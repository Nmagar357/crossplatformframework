from appium.webdriver.common.appiumby import AppiumBy


class NavigationTabLocators:

    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.log = log
        self.driver = driver

    def today_tab(self):
        self.log.info("Finding 'Today' tab.")
        # return self.driver.find_element(AppiumBy.ID, "Today")
        return self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Today']")

    def for_you_tab(self):
        self.log.info("Finding 'For You' tab.")
        # return self.driver.find_element(AppiumBy.ID, "For You")
        return self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='For You']")

    def sections_tab(self):
        self.log.info("Finding 'Sections' tab.")
        # return self.driver.find_element(AppiumBy.ID, "Sections")
        return self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sections']")

    def selected_tab_parent_element(self):
        self.log.info("Finding selected tab's parent element.")
        return self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@selected='true']")
