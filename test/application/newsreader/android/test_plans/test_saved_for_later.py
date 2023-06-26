import unittest

from appium.webdriver.common.appiumby import AppiumBy
from test.core.mobile.device_actions import DeviceActions
from test.core.global_setup import GlobalSetup
from test.application.newsreader.android.page_events.login_events import LoginEvents
from test.application.newsreader.android.page_locators.login_locators import LoginLocators
from test.application.newsreader.android.page_locators.sections_locators import SectionsLocators
from test.application.newsreader.android.page_actions.sections_actions import SectionsActions
from test.application.newsreader.android.page_locators.search_locators import SearchLocators
from test.application.newsreader.android.page_actions.saved_for_later_actions import SavedForLaterActions
from test.application.newsreader.android.page_locators.saved_for_later_locators import SavedForLaterLocators
from test.application.newsreader.android.page_actions.sections_article_actions import SectionsArticleActions
from test.application.newsreader.android.page_events.today_events import TodayEvents
from test.core.common.constants.app_constants import *
from test.application.newsreader.android.constants.newsreader_constants import *

class TestSavedForLater(unittest.TestCase):
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
        cls.sections_actions = SectionsActions(cls.driver, cls.log)
        cls.search_locators = SearchLocators(cls.driver, cls.log)
        cls.saved_for_later_actions = SavedForLaterActions(cls.driver, cls.log)
        cls.saved_for_later_locators = SavedForLaterLocators(cls.driver, cls.log)
        cls.sections_article_actions = SectionsArticleActions(cls.driver, cls.log)
        cls.section_locators = SectionsLocators(cls.driver, cls.log)
        cls.today_events = TodayEvents(cls.driver, cls.log)

    @classmethod
    def tearDownClass(cls):
        cls.global_setup.core_driver.teardown()

    def setUp(self):
        self.global_setup.setup_routine(reset=True, ab_variants=True)

    def tearDown(self):
        self.device_actions.turn_on_wifi()

    # TID: NR-A-SFL-01
    def test_01_anonymous_access(self):
        self.log.begin_test()
        self.login_events.skip_app_welcome_pages(permission=ALLOW)
        self.today_events.navigate_to_saved_for_later_section()

        empty_title_text = self.saved_for_later_locators.empty_title().text
        self.assertEqual(SAVE_EMPTY_TITLE_LOGIN, empty_title_text, "Assert failure: empty_title_text='{0}'".format(empty_title_text))

        empty_description_text = self.saved_for_later_locators.empty_description().text
        self.assertEqual(SAVE_EMPTY_DESC, empty_description_text, "Assert failure: empty_description_text='{0}'".format(empty_description_text))

        create_account_link_text = self.saved_for_later_locators.create_account_link_text().text
        self.assertEqual(CREATE_ACCOUNT_TITLE, create_account_link_text, "Assert failure: create_account_link_text='{0}'".format(create_account_link_text))

        self.saved_for_later_actions.click_create_account_link_text()
        email_text_field_displayed = self.login_locators.email_text_field().get_attribute('displayed')
        self.assertTrue(email_text_field_displayed, "Assert failure: email_text_field_displayed='{0}'".format(email_text_field_displayed))

        continue_button_displayed = self.login_locators.continue_button().get_attribute('displayed')
        self.assertTrue(continue_button_displayed, "Assert failure: continue_button_displayed='{0}'".format(continue_button_displayed))

    # Test ID: NR-A-SFL-02
    def test_02_non_subscriber_access(self):
        self.log.begin_test()
        self.login_events.skip_app_welcome_pages(permission=ALLOW)
        self.today_events.navigate_to_saved_for_later_section()
        self.saved_for_later_actions.click_log_in_button()
        self.login_events.login_routine(NON_SUBSCRIBER_USER_ID, NON_SUBSCRIBER_USER_PASSWORD)

        start_saving_stories_text = self.saved_for_later_locators.empty_title().text
        self.assertEqual(SAVE_EMPTY_TITLE, start_saving_stories_text, "Assert failure: start_saving_stories_text='{0}'".format(start_saving_stories_text))

        empty_description_text = self.saved_for_later_locators.empty_description().text
        self.assertEqual(SAVE_EMPTY_DESC, empty_description_text, "Assert failure: empty_description_text='{0}'".format(empty_description_text))

    # TID: NR-A-SFL-03
    def test_03_subscriber_access(self):
        self.log.begin_test()
        self.login_events.skip_app_welcome_pages(permission=ALLOW)
        self.today_events.navigate_to_saved_for_later_section()
        self.saved_for_later_actions.click_log_in_button()
        self.login_events.login_routine(SUBSCRIBER_USER_ID, SUBSCRIBER_USER_PASSWORD)

        saved_article_title_text = self.search_locators.saved_article_title().text
        self.assertEqual(ARTICLE_TITLE_RRR, saved_article_title_text, "Assert failure: saved_article_title_text='{0}'".format(saved_article_title_text))

    # Test ID: NR-A-SFL-04
    def test_04_new_non_subscriber_save_ribbon_behavior(self):
        self.log.begin_test()
        self.login_events.skip_app_welcome_pages(permission=ALLOW)
        self.today_events.navigate_to_politics_section()

        section_article_text = self.sections_article_actions.get_sf_lede_article_headline_text()
        self.sections_article_actions.click_saved_for_later_ribbon(by_index=0)

        self.login_locators.popup_log_in_button().click()
        self.login_events.login_routine(NON_SUBSCRIBER_USER_ID, NON_SUBSCRIBER_USER_PASSWORD)

        article_saved_toast_text = self.driver.find_element(AppiumBy.ID, "snackbar_text").text
        self.assertEqual(ARTICLE_SAVED_TEXT, article_saved_toast_text, "Assert failure: article_saved_toast_text='{0}'".format(article_saved_toast_text))

        self.driver.back()
        self.sections_actions.click_saved_for_later_section()

        saved_article_text = self.sections_article_actions.get_sf_row_article_headline_text(by_index=0)
        self.assertEqual(section_article_text, saved_article_text, "Assert failure: saved_article_text='{0}'".format(saved_article_text))

        self.driver.back()
        self.sections_actions.click_politics_section()
        self.sections_article_actions.click_saved_for_later_ribbon(by_index=0)

        article_unsaved_toast_text = self.driver.find_element(AppiumBy.ID, "snackbar_text").text
        self.assertEqual(ARTICLE_UNSAVED_TEXT, article_unsaved_toast_text, "Assert failure: article_unsaved_toast_text='{0}'".format(article_unsaved_toast_text))

        self.driver.back()
        self.sections_actions.click_saved_for_later_section()

        start_saving_stories_text = self.saved_for_later_locators.empty_title().text
        self.assertEqual(SAVE_EMPTY_TITLE, start_saving_stories_text,  "Assert failure: start_saving_stories_text='{0}'".format(start_saving_stories_text))

    # TID: NR-A-SFL-05
    def test_new_non_subscriber_login_offline_behavior(self):
        self.log.begin_test()

        # 1. Launch the App
        # 2. Tap on "Not Now"
        # 3. Tap on Continue without Subscribing
        # 4. Tap Allow if the “Allow NYTimes to send notifications” popup appears
        # 5. Tap on the continue button
        self.login_events.skip_app_welcome_pages(permission=ALLOW)

        # 6. Tap on the Sections Tab
        # 7. Scroll down and tap on the Saved for Later section
        self.today_events.navigate_to_saved_for_later_section()

        # 8. Put the device offline
        self.device_actions.turn_off_wifi()

        # 9. Tap on Login OR Create an Account link
        self.saved_for_later_actions.click_log_in_button()

        # 10. Verify offline snack bar message: "Your device is offline. Please check your internet connection and Try again." is displayed
        offline_snackbar_text = self.section_locators.offline_snack_bar_text().text
        self.assertEqual(DEVICE_OFFLINE_SNACKBAR, offline_snackbar_text, "Assert failure: offline_snackbar_text='{0}'".format(offline_snackbar_text))