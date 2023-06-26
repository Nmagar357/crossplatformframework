from appium.webdriver.common.appiumby import AppiumBy


class SectionsArticleLocators:

    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.log = log
        self.driver = driver

    def sf_lede_headline_text(self):
        self.log.info("Finding section front 'lede(Lead) article' headline text.")
        return self.driver.find_element(AppiumBy.ID, "row_sf_lede_headline")

    def sf_row_headline_text_list(self):
        self.log.info("Finding section front 'row article' headline text list.")
        return self.driver.find_elements(AppiumBy.ID, "row_sf_headline")

    def sf_saved_for_later_ribbon_list(self):
        self.log.info("Finding section front 'saved for later' ribbon list.")
        return self.driver.find_elements(AppiumBy.ID, "sf_footer_save_container")

    def non_subscriber_offline_gateway_popup(self):
        self.log.info("Finding Non Subscriber user offline gateway popup")
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "text_you_have_free_articles_mc")
