from test.application.newsreader.android.page_locators.saved_for_later_locators import SavedForLaterLocators


class SavedForLaterActions:

    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.log = log
        self.driver = driver

        self.saved_for_later_locators = SavedForLaterLocators(driver, log)

    def click_log_in_button(self):
        self.log.info("Clicking 'Log In' button.")
        self.saved_for_later_locators.log_in_button().click()

    def click_article_save_button(self):
        self.log.info("Clicking article save button.")
        self.saved_for_later_locators.article_save_button().click()

    def get_dont_have_account_title_text(self):
        self.log.info("Getting 'Don’t have an account? Create one' element text.")
        return self.saved_for_later_locators.create_account_link_text().text

    def is_log_in_button_displayed(self):
        self.log.info("Checking 'Log In' button is displayed.")
        return self.saved_for_later_locators.log_in_button().is_displayed()

    def click_create_account_link_text(self):
        self.log.info("Clicking 'CREATE A FREE ACCOUNT link text'")
        self.saved_for_later_locators.create_account_link_text().click()

    def is_saved_for_later_ribbon_displayed(self):
        self.log.info("Checking saved for later ribbon is displayed.")
        return self.saved_for_later_locators.saved_for_later_ribbon().is_displayed()

