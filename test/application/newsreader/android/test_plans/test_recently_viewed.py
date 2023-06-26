import unittest

from test.core.mobile.device_actions import DeviceActions
from test.core.global_setup import GlobalSetup
from test.application.newsreader.android.page_locators.login_locators import LoginLocators
from test.application.newsreader.android.page_events.login_events import LoginEvents
from test.application.newsreader.android.page_actions.recently_viewed_actions import RecentlyViewedActions
from test.application.newsreader.android.page_locators.recently_viewed_locators import RecentlyViewedLocators
from test.application.newsreader.android.page_actions.sections_actions import SectionsActions
from test.application.newsreader.android.page_actions.sections_article_actions import SectionsArticleActions
from test.application.newsreader.android.page_locators.sections_article_locators import SectionsArticleLocators
from test.application.newsreader.android.page_locators.sections_locators import SectionsLocators
from test.application.newsreader.android.page_events.today_events import TodayEvents
from test.core.mobile.session_actions import SessionActions
from test.application.newsreader.android.constants.newsreader_constants import *
from test.core.common.constants.app_constants import *

class TestRecentlyViewed(unittest.TestCase):
    global_setup = GlobalSetup()
    driver = None
    log = None

    @classmethod
    def setUpClass(cls):
        cls.name = __class__.__name__
        cls.global_setup.setup()
        cls.driver = cls.global_setup.driver
        cls.log = cls.global_setup.log
        cls.package_name = cls.global_setup.package_name
        cls.driver.capabilities.update({
            "appActivity": "com.nytimes.android.onboarding.compose.ComposeOnboardingActivity"
        })
        cls.device_actions = DeviceActions(cls.driver, cls.log)
        cls.login_events = LoginEvents(cls.driver, cls.log)
        cls.login_locators = LoginLocators(cls.driver, cls.log)
        cls.recently_viewed_actions = RecentlyViewedActions(cls.driver, cls.log)
        cls.recently_viewed_locators = RecentlyViewedLocators(cls.driver, cls.log)
        cls.sections_actions = SectionsActions(cls.driver, cls.log)
        cls.session_actions = SessionActions(cls.driver, cls.log)
        cls.sections_locators = SectionsLocators(cls.driver, cls.log)
        cls.sections_article_actions = SectionsArticleActions(cls.driver, cls.log)
        cls.sections_article_locators = SectionsArticleLocators(cls.driver, cls.log)
        cls.today_events = TodayEvents(cls.driver, cls.log)


    @classmethod
    def tearDownClass(cls):
        cls.global_setup.core_driver.teardown()

    def setUp(self):
        self.global_setup.setup_routine(reset=True, ab_variants=True)

    def tearDown(self):
        self.device_actions.turn_on_wifi()

    # TID: NR-A-RV-01
    # @unittest.skip("Debugging skip")
    def test_anonymous_access(self):
        self.log.begin_test()
        self.login_events.skip_app_welcome_pages(permission=ALLOW)
        self.today_events.navigate_to_recently_viewed_section()

        empty_title_text = self.recently_viewed_locators.empty_title().text
        self.assertEqual(LOGIN_EMPTY_TITLE, empty_title_text,
                         "Assert failure: empty_title_text='{0}'".format(empty_title_text))

        empty_description_text = self.recently_viewed_locators.empty_description().text
        self.assertEqual(LOGIN_EMPTY_DESC, empty_description_text,
                         "Assert failure: empty_description_text='{0}'".format(empty_description_text))

        log_in_button_text = self.recently_viewed_locators.log_in_button().text
        self.assertEqual(LOG_IN_BUTTON, log_in_button_text,
                         "Assert failure: log_in_button_text='{0}'".format(log_in_button_text))

        create_account_button_text = self.recently_viewed_locators.create_account_button().text
        self.assertEqual(CREATE_ACCOUNT_BUTTON, create_account_button_text,
                         "Assert failure: create_account_button_text='{0}'".format(create_account_button_text))

        self.recently_viewed_actions.click_log_in_button()
        login_displayed = self.login_locators.email_text_field().get_attribute('displayed')
        self.assertTrue(login_displayed, "Assert failure: login_displayed='{0}'".format(login_displayed))

    # TID: NR-A-RV-02
    # @unittest.skip("Debugging skip")
    def test_news_subscriber_access(self):
        self.log.begin_test()
        self.login_events.skip_app_welcome_pages(permission=ALLOW)
        self.today_events.navigate_to_recently_viewed_section()
        self.recently_viewed_actions.click_log_in_button()
        self.login_events.login_routine(SUBSCRIBER_USER_ID, SUBSCRIBER_USER_PASSWORD)
        self.session_actions.go_back()
        self.sections_actions.click_recently_viewed_section()

        empty_title_text = self.recently_viewed_locators.empty_title().text
        self.assertEqual(RECENTS_EMPTY_TITLE, empty_title_text,
                         "Assert failure: empty_title_text='{0}'".format(empty_title_text))

        empty_description_text = self.recently_viewed_locators.empty_description().text
        self.assertEqual(RECENTS_EMPTY_DESC, empty_description_text,
                         "Assert failure: empty_description_text='{0}'".format(empty_description_text))

    # TID: NR-A-RV-03
    # @unittest.skip("Debugging skip")
    def test_news_subscriber_articles_displayed(self):
        self.log.begin_test()
        self.login_events.skip_app_welcome_pages(permission=ALLOW)
        self.today_events.navigate_to_recently_viewed_section()

        self.recently_viewed_actions.click_log_in_button()
        self.login_events.login_routine(SUBSCRIBER_USER_ID, SUBSCRIBER_USER_PASSWORD)

        self.session_actions.go_back()
        self.sections_actions.click_politics_section()
        section_article_text = self.sections_article_actions.get_sf_lede_article_headline_text()
        self.sections_article_locators.sf_lede_headline_text().click()

        self.session_actions.go_back(2)
        self.sections_actions.click_recently_viewed_section()

        recently_viewed_article = self.recently_viewed_locators.article_heading().text
        self.assertEqual(recently_viewed_article, section_article_text,
                         "Assert failure: recently_viewed_article='{0}'".format(recently_viewed_article))

        self.recently_viewed_actions.click_recently_viewed_article()

        article_accessible_result = self.sections_article_actions.is_article_accessible()
        self.assertFalse(article_accessible_result,
                        "Assert failure: article_accessible_result ='{0}'".format(article_accessible_result))
        self.session_actions.go_back()

        article_timestamp = self.recently_viewed_locators.article_timestamp().is_displayed()
        self.assertTrue(article_timestamp, "Assert failure: article timestamp='{0}'".format(article_timestamp))

    # TID: NR-A-RV-07
    # @unittest.skip("Debugging skip")
    def test_non_subscriber_user_offline_mode(self):
        self.log.begin_test()
        self.login_events.skip_app_welcome_pages(permission=ALLOW)
        self.today_events.navigate_to_recently_viewed_section()

        self.recently_viewed_actions.click_log_in_button()
        self.login_events.login_routine(NON_SUBSCRIBER_USER_ID, NON_SUBSCRIBER_USER_PASSWORD)

        self.session_actions.go_back()
        self.sections_actions.click_politics_section()
        self.sections_article_locators.sf_lede_headline_text().click()

        self.device_actions.turn_off_wifi()
        self.session_actions.go_back()
        self.sections_article_locators.sf_lede_headline_text().click()

        offline_gateway = self.sections_article_locators.non_subscriber_offline_gateway_popup().text
        self.assertEqual(NOSUB_OFFLINE_GATEWAY_MSG, offline_gateway,
                         "Assert failure: Non Subscriber offline gateway popup='{0}'".format(offline_gateway))

    # TID: NR-A-RV-08
    # @unittest.skip("Debugging skip")
    def test_news_subscriber_offline_mode(self):
        self.log.begin_test()
        self.login_events.skip_app_welcome_pages(permission=ALLOW)
        self.today_events.navigate_to_recently_viewed_section()

        self.recently_viewed_actions.click_log_in_button()
        self.login_events.login_routine(SUBSCRIBER_USER_ID, SUBSCRIBER_USER_PASSWORD)

        self.session_actions.go_back()
        self.sections_actions.click_politics_section()
        self.sections_article_locators.sf_lede_headline_text().click()

        self.device_actions.turn_off_wifi()
        self.session_actions.go_back()
        self.sections_article_locators.sf_lede_headline_text().click()

        article_accessible_result = self.sections_article_actions.is_article_accessible()
        self.assertFalse(article_accessible_result,
                        "Assert failure: article_accessible_result ='{0}'".format(article_accessible_result))
