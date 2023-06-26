from test.application.newsreader.android.page_actions.navigation_tab_actions import NavigationTabActions
from test.application.newsreader.android.page_actions.sections_actions import SectionsActions
from test.core.mobile.device_actions import DeviceActions
from test.application.newsreader.android.page_actions.search_actions import SearchActions


class SearchEvents:

    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.driver = driver
        self.log = log

        self.search_actions = SearchActions(driver, log)
        self.sections_actions = SectionsActions(driver, log)
        self.device_actions = DeviceActions(driver, log)
        self.nav_tab_actions = NavigationTabActions(driver, log)

    def search_for_articles_with_keywords(self, search_string):
        self.nav_tab_actions.click_sections_tab_button()
        self.sections_actions.click_search_articles_text_field()
        self.search_actions.input_search_text_field_string(search_string)
        self.device_actions.hide_keyboard()
        self.search_actions.submit_search()

    def search_for_articles_with_title(self, search_string):
        self.nav_tab_actions.click_sections_tab_button()
        self.sections_actions.click_search_articles_text_field()
        self.search_actions.input_search_text_field_string(search_string)
        self.device_actions.hide_keyboard()
        self.search_actions.submit_search()
