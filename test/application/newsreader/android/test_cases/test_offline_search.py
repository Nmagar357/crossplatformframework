import unittest

from test.application.newsreader.android.constants.newsreader_constants import ARTICLE_KEYWORDS_RRR, ARTICLE_TITLE_RRR, \
    SECTIONS_TAB_TEXT
from test.application.newsreader.android.page_actions.sections_actions import is_offline_error_shown
from test.core.global_setup import GlobalSetup
from test.core.mobile.device_actions import DeviceActions
from test.application.newsreader.android.page_actions.navigation_tab_actions import NewsreaderAppActions
from test.application.newsreader.android.page_events.search_events import SearchEvents
from test.application.newsreader.android.page_events.login_events import LoginEvents
from test.application.newsreader.android.page_actions.offline_search_actions import OfflineSearchActions


class TestOfflineSearch(unittest.TestCase):
    global_setup = GlobalSetup()
    log = None
    driver = None
    device_actions = None
    offline_search_actions = None

    @classmethod
    def setUpClass(cls):
        cls.name = __class__.__name__
        cls.global_setup.setup()
        cls.log = cls.global_setup.log
        cls.driver = cls.global_setup.driver
        cls.login_events = LoginEvents(cls.driver, cls.log)
        cls.search_events = SearchEvents(cls.driver, cls.log)
        cls.device_actions = DeviceActions(cls.driver, cls.log)
        cls.offline_search_actions = OfflineSearchActions(cls.driver, cls.log)
        cls.newsreader_app_actions = NewsreaderAppActions(cls.driver, cls.log)

        cls.device_actions.turn_on_wifi()

    @classmethod
    def tearDownClass(cls):
        cls.global_setup.core_driver.teardown()

    def setUp(self):
        self.log.debug(msg="{0}.setUp()".format(self.name))
        self.driver.reset()
        self.login_events.skip_app_welcome_pages()

        self.offline_search_actions.select_sections_tab()
        tab_name = self.newsreader_app_actions.get_selected_tab_text()
        self.assertEqual(tab_name, SECTIONS_TAB_TEXT, msg="Setup failure: Current tab is '{0}', instead of expected 'Sections' tab.".format(tab_name))

        self.device_actions.turn_off_wifi()
        wifi_state = self.device_actions.get_wifi_on_state()
        self.assertFalse(wifi_state, msg="Setup failure: Wifi failed to turn 'OFF'")

    def tearDown(self):
        self.device_actions.turn_on_wifi()
        wifi_state = self.device_actions.get_wifi_on_state()
        self.assertTrue(wifi_state, msg="Teardown failure: Wifi failed to turn 'ON'.")

        self.log.debug(msg="{0}.tearDown()".format(self.name))
        self.log.space()

    def test_00_offline_sections_keywords_search(self):
        self.log.begin_test()

        self.search_events.search_for_articles_with_keywords(ARTICLE_KEYWORDS_RRR)
        error_check_result = is_offline_error_shown(self.offline_search_actions.log,
                                                    self.offline_search_actions.offline_search_locators)
        self.assertTrue(error_check_result, msg="Verification failed: 'Device is offline' error not found on sections tab.")

        self.offline_search_actions.click_newest_search_filter_button()
        error_check_result = is_offline_error_shown(self.offline_search_actions.log,
                                                    self.offline_search_actions.offline_search_locators)
        self.assertTrue(error_check_result, msg="Verification failed: 'Device is offline' error not found on 'Newest' search filter tab.")

    def test_01_offline_sections_title_search(self):
        self.log.begin_test()

        self.search_events.search_for_articles_with_title(ARTICLE_TITLE_RRR)
        error_check_result = is_offline_error_shown(self.offline_search_actions.log,
                                                    self.offline_search_actions.offline_search_locators)
        self.assertTrue(error_check_result, msg="Verification failed: 'Device is offline' error not found on sections tab.")

        self.offline_search_actions.click_oldest_search_filter_button()
        error_check_result = is_offline_error_shown(self.offline_search_actions.log,
                                                    self.offline_search_actions.offline_search_locators)
        self.assertTrue(error_check_result, msg="Verification failed: 'Device is offline' error not found on 'Oldest' search filter tab.")
