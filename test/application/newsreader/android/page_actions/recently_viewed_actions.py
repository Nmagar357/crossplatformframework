from test.application.newsreader.android.page_locators.recently_viewed_locators import RecentlyViewedLocators


class RecentlyViewedActions:

    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.log = log
        self.driver = driver

        self.recently_viewed_locators = RecentlyViewedLocators(driver, log)

    def click_more_options_ellipses(self):
        self.log.info("Clicking 'More Options' ellipses")
        self.recently_viewed_locators.more_options_ellipsis().click()

    def click_log_in_button(self):
        self.log.info("Clicking 'LOG IN' button")
        self.recently_viewed_locators.log_in_button().click()

    def is_cancel_button_displayed(self):
        self.log.info("Verifying Cancel button is Displayed")
        return self.recently_viewed_locators.cancel_button_popup().is_displayed()

    def is_log_in_button_displayed(self):
        self.log.info("Verifying 'LOG IN' button is Displayed")
        return self.recently_viewed_locators.log_in_button_popup().is_displayed()

    def click_recently_viewed_article(self):
        self.log.info("Clicking on Recently Viewed Article")
        return self.recently_viewed_locators.article_heading().click()
