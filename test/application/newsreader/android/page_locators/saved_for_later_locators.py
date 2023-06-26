from appium.webdriver.common.appiumby import AppiumBy


class SavedForLaterLocators:

    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.log = log
        self.driver = driver

    def log_in_button(self):
        self.log.info("Finding 'Saved For Later' LOG IN button")
        return self.driver.find_element(AppiumBy.ID, "save_empty_login_button")

    def article_save_button(self, from_top=1):
        self.log.info("Finding save article icon number: '{0}'".format(from_top))
        return self.driver.find_element(AppiumBy.XPATH, "(//android.widget.LinearLayout[@content-desc='section_save'])[{0}]".format(from_top))

    def empty_title(self):
        self.log.info("Finding 'Saved For Later' empty title")
        return self.driver.find_element(AppiumBy.ID, "save_empty_title")

    def empty_description(self):
        self.log.info("Finding 'Saved For Later' empty description")
        return self.driver.find_element(AppiumBy.ID, "save_empty_desc")

    def create_account_link_text(self):
        self.log.info("Finding 'Saved For Later' CREATE A FREE ACCOUNT link text")
        return self.driver.find_element(AppiumBy.ID, "create_account_title")

    def saved_for_later_ribbon(self):
        self.log.info("Finding 'Saved For Later' article ribbon")
        return self.driver.find_element(AppiumBy.XPATH, "//android.widget.LinearLayout[@content-desc='section_save'][1]")
