from selenium.common import NoSuchElementException

from test.application.newsreader.android.page_locators.sections_locators import SectionsLocators


class SectionsActions:

    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.log = log
        self.driver = driver

        self.sections_locators = SectionsLocators(driver, log)

    def click_games_section(self):
        self.log.info("Clicking 'Games' section.")
        self.sections_locators.games_section().click()

    def click_most_popular_section(self):
        self.log.info("Clicking 'Most Popular' section.")
        self.sections_locators.first_most_popular_section_article().click()

    def click_opinion_section(self):
        self.log.info("Clicking 'Opinion' section.")
        self.sections_locators.opinion_section().click()

    def click_politics_section(self):
        self.log.info("Clicking 'Politics' section.")
        self.sections_locators.politics_section().click()

    def click_recently_viewed_section(self):
        self.log.info("Clicking 'Recently Viewed' section.")
        self.sections_locators.recently_viewed_section().click()

    def click_search_articles_text_field(self):
        self.log.info("Clicking 'Search Articles' text field/button.")
        self.sections_locators.search_articles_text_field().click()

    def is_most_popular_section_displayed(self):
        self.log.info("Is 'Most Popular' section displayed?")
        return self.sections_locators.first_most_popular_section_article().is_displayed()

    def is_games_section_displayed(self):
        self.log.info("Is 'Games' section displayed?")
        return self.sections_locators.games_section().is_displayed()

    def is_offline_error_shown(self, offline_search_locators):
        self.log.info("Is 'device is offline' error on the sections tab shown?")
        try:
            offline_search_locators.device_offline_element()
            return True
        except NoSuchElementException:
            self.log.debug(msg="'Device is offline' error not found on sections tab.")
            return False

    def is_opinion_section_displayed(self):
        self.log.info("Is 'Opinion' section displayed?")
        return self.sections_locators.opinion_section().is_displayed()

    def is_search_articles_text_field_enabled(self):
        self.log.info("Is 'Search Articles' text field enabled?")
        return self.sections_locators.search_articles_text_field().is_enabled()

    def click_saved_for_later_section(self):
        self.log.info("Clicking 'Saved For Later' section.")
        self.sections_locators.saved_for_later_section().click()

    def click_books_section(self):
        self.log.info("Clicking 'Books' section.")
        self.sections_locators.books_section().click()

    def click_most_popular_section_article(self):
        self.log.info("Clicking first 'Most Popular' article.")
        self.sections_locators.first_most_popular_section_article().click()
