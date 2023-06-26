from appium.webdriver.common.appiumby import AppiumBy


class RecentlyViewedLocators:

    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.log = log
        self.driver = driver

    def more_options_ellipsis(self):
        self.log.info("Finding 'More options' ellipsis")
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "More options")

    def popup_message(self):
        self.log.info("Finding popup message")
        return self.driver.find_element(AppiumBy.ID, "android:id/message")

    def cancel_button_popup(self):
        self.log.info("Finding Cancel button on popup")
        return self.driver.find_element(AppiumBy.ID, "android:id/button2")

    def log_in_button_popup(self):
        self.log.info("Finding Log In button on popup")
        return self.driver.find_element(AppiumBy.ID, "android:id/button1")

    def empty_title(self):
        self.log.info("Finding 'Recently Viewed' empty title'")
        return self.driver.find_element(AppiumBy.ID, "recents_empty_title")

    def empty_description(self):
        self.log.info("Finding 'Recently Viewed' empty description'")
        return self.driver.find_element(AppiumBy.ID, "recents_empty_desc")

    def log_in_button(self):
        self.log.info("Finding 'Recently Viewed' LOG IN button")
        return self.driver.find_element(AppiumBy.ID, "recent_login_button")

    def create_account_button(self):
        self.log.info("Finding 'Recently Viewed' CREATE A FREE ACCOUNT button")
        return self.driver.find_element(AppiumBy.ID, "recent_subscribe_button")

    def article_heading(self):
        self.log.info("Finding Recently viewed article heading")
        return self.driver.find_element(AppiumBy.ID, "row_recently_viewed_headline")

    def article_timestamp(self):
        self.log.info("Finding Recently viewed article Timestamp")
        return self.driver.find_element(AppiumBy.ID, "row_recently_viewed_last_accessed")



