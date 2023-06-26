import unittest
from test.application.newsreader.android.page_events.login_events import LoginEvents
from test.application.newsreader.android.page_events.recently_viewed_events import RecentlyViewedEvents
from test.core.common.constants.app_constants import *
from test.core.global_setup import GlobalSetup


class TestLogin(unittest.TestCase):
    global_setup = GlobalSetup()
    log = None
    login_events = None

    @classmethod
    def setUpClass(cls):
        cls.name = __class__.__name__
        cls.global_setup.setup()
        cls.driver = cls.global_setup.driver
        cls.log = cls.global_setup.log
        cls.driver.reset()
        cls.login_events = LoginEvents(cls.driver, cls.log)
        cls.recently_viewed_events = RecentlyViewedEvents(cls.driver, cls.log)

    @classmethod
    def tearDownClass(cls):
        cls.global_setup.core_driver.teardown()

    def test_login_valid_username_and_password_successful(self):
        self.login_events.skip_app_welcome_pages()
        self.login_events.login(SUBSCRIBER_USER_ID, SUBSCRIBER_USER_PASSWORD)
        result = self.login_events.get_logged_in_username()
        self.assertEqual(result, SUBSCRIBER_USER_ID, 'Verification of logged in user.')
        self.driver.reset()

    def test_login_successful_recently_viewed_valid_username_and_password(self):
        self.login_events.skip_app_welcome_pages()
        self.recently_viewed_events.navigate_to_recently_viewed_section()
        self.recently_viewed_events.log_in_with_account(SUBSCRIBER_USER_ID, SUBSCRIBER_USER_PASSWORD)
        self.recently_viewed_events.navigate_from_sections_to_account()
        result = self.login_events.get_logged_in_username()
        self.assertEqual(result, SUBSCRIBER_USER_ID, 'Verification of logged in user.')
        self.driver.reset()
