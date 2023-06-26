import unittest
from test.core.global_setup import GlobalSetup
from test.application.newsreader.android.constants.newsreader_constants import DONT_HAVE_ACCOUNT_TEXT
from test.application.newsreader.android.page_events.today_events import TodayEvents
from test.application.newsreader.android.page_events.login_events import LoginEvents
from test.application.newsreader.android.page_actions.saved_for_later_actions import SavedForLaterActions
from test.application.newsreader.android.page_actions.recently_viewed_actions import RecentlyViewedActions


class TestSavedForLater(unittest.TestCase):
    global_setup = GlobalSetup()
    log = None
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.name = __class__.__name__
        cls.global_setup.setup()
        cls.log = cls.global_setup.log
        cls.driver = cls.global_setup.driver
        cls.today_events = TodayEvents(cls.driver, cls.log)
        cls.login_events = LoginEvents(cls.driver, cls.log)
        cls.saved_for_later_actions = SavedForLaterActions(cls.driver, cls.log)
        cls.recently_viewed_actions = RecentlyViewedActions(cls.driver, cls.log)

    @classmethod
    def tearDownClass(cls):
        cls.global_setup.core_driver.teardown()

    def setUp(self):
        self.log.debug(msg="{0}.setUp()".format(self.name))
        self.driver.reset()
        self.login_events.skip_app_welcome_pages()

    def tearDown(self):
        self.log.debug(msg="{0}.tearDown()".format(self.name))
        self.log.space()

    def test_00_saved_for_later_without_log_in(self):
        self.log.begin_test()
        self.today_events.navigate_to_saved_for_later_section()
        log_in_button_result = self.saved_for_later_actions.is_log_in_button_displayed()
        self.assertTrue(log_in_button_result,
                        msg="Verification failed: 'Log in' button is not displayed: {0}, expected 'True'.".format(
                            log_in_button_result))

        dont_have_account_text = self.saved_for_later_actions.get_dont_have_account_title_text()
        self.assertEqual(dont_have_account_text, DONT_HAVE_ACCOUNT_TEXT,
                         msg="Verification failed: 'Don't have account?' request not found.")

        self.driver.back()
        self.driver.back()
        self.today_events.navigate_to_most_popular_section()
        self.saved_for_later_actions.click_article_save_button()
        cancel_button_result = self.recently_viewed_actions.is_cancel_button_displayed()
        self.assertTrue(cancel_button_result,
                        msg="Verification failed: 'Cancel' button is not displayed: {0}, expected 'True'.".format(
                            cancel_button_result))

        log_in_button_result = self.recently_viewed_actions.is_log_in_button_displayed()
        self.assertTrue(log_in_button_result,
                        msg="Verification failed: 'Login' button is not displayed: {0}, expected 'True'.".format(
                            log_in_button_result))
