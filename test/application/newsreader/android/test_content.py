import unittest

from test.application.newsreader.android.constants.newsreader_constants import DEVICE_OFFLINE_POPUP, TODAY_TAB_TEXT
from test.core.global_setup import GlobalSetup
from test.application.newsreader.android.page_events.login_events import LoginEvents
from test.application.newsreader.android.page_actions.content_actions import ContentActions
from test.core.mobile.device_actions import DeviceActions


class TestContent(unittest.TestCase):
    global_setup = GlobalSetup()
    log = None
    driver = None
    device_actions = None

    @classmethod
    def setUpClass(cls):
        cls.name = __class__.__name__
        cls.global_setup.setup()
        cls.driver = cls.global_setup.driver
        cls.log = cls.global_setup.log
        cls.login_events = LoginEvents(cls.driver, cls.log)
        cls.content_actions = ContentActions(cls.driver, cls.log)

        cls.device_actions = DeviceActions(cls.driver, cls.log)

    def setUp(self):
        if not self.device_actions.get_wifi_on_state():
            self.log.info("Turning wi-fi to 'on' state.")
            self.driver.toggle_wifi()

        self.assertTrue(self.device_actions.get_wifi_on_state(), "Verification failed: Wi-fi is 'OFF'.")

        self.driver.reset()

    @classmethod
    def tearDownClass(self):
        if not self.device_actions.get_wifi_on_state():
            self.log.info("Turning wi-fi to 'on' state.")
            self.driver.toggle_wifi()

        self.assertTrue(self.device_actions.get_wifi_on_state(), "Verification failed: Wi-fi is 'OFF'.")

        self.global_setup.core_driver.teardown()

    def test_00_today_tab_online_content(self):
        self.log.debug(msg="Starting Test_00: Verifying online-mode 'Today' tab content.")

        self.login_events.skip_app_welcome_pages()

        self.assertEqual(self.content_actions.get_selected_tab_text(), TODAY_TAB_TEXT,
                         msg="Verification failed: Current tab is not today tab.")

        self.assertTrue(self.content_actions.is_online_content_shown(),
                        "Verification failed: No content found on today tab.")

    def test_01_today_tab_offline_content(self):
        self.log.debug(msg="Starting Test_01: Verifying offline-mode 'Today' tab content.")

        if self.device_actions.get_wifi_on_state():
            self.log.info("Turning wi-fi to 'off' state.")
            self.driver.toggle_wifi()

        self.assertFalse(self.device_actions.get_wifi_on_state(), msg="Verification failed: Wi-fi is 'ON'.")

        self.login_events.skip_app_welcome_pages()

        self.assertEqual(self.content_actions.get_selected_tab_text(), TODAY_TAB_TEXT,
                         msg="Verification failed: Current tab is not today tab.")

        self.assertTrue(self.content_actions.is_offline_pop_up_shown(),
                        msg="Verification failed: 'Device offline' pop-up not found on today tab.")
        self.assertEqual(self.content_actions.get_offline_pop_up_text(), DEVICE_OFFLINE_POPUP,
                         msg="Verification failed: 'Device offline' pop-up text matched.")
