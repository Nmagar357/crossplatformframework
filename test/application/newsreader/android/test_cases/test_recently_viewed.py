import unittest

from test.application.newsreader.android.page_actions.recently_viewed_actions import RecentlyViewedActions
from test.application.newsreader.android.page_events.login_events import LoginEvents
from test.application.newsreader.android.page_events.recently_viewed_events import RecentlyViewedEvents
from test.core.global_setup import GlobalSetup


class TestRecentlyViewed(unittest.TestCase):
    global_setup = GlobalSetup()
    driver = None
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
        cls.recently_viewed_actions = RecentlyViewedActions(cls.driver, cls.log)
        cls.recently_viewed_events = RecentlyViewedEvents(cls.driver, cls.log)

    @classmethod
    def tearDownClass(cls):
        cls.global_setup.core_driver.teardown()

    def test_00_recently_viewed_without_log_in(self):
        self.login_events.skip_app_welcome_pages()
        self.recently_viewed_events.navigate_to_recently_viewed_section()

        cancel_button = self.recently_viewed_actions.is_cancel_button_displayed()
        self.assertTrue(cancel_button, msg="Verification of Cancel button failed! Expected 'True' but got "
                                           "'{0}'".format(cancel_button))

        log_in_button = self.recently_viewed_actions.is_log_in_button_displayed()
        self.assertTrue(log_in_button, msg="Verification of Log In button failed! Expected 'True' but got "
                                           "'{0}'".format(log_in_button))
