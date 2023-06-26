import os
import time
import unittest

from test.application.newsreader.android.page_actions.login_actions import LoginActions
from test.core.global_setup import GlobalSetup


class TestAppState(unittest.TestCase):

    global_setup = GlobalSetup()
    log = None
    driver = None
    possible_states = ['0=not installed', '1=stopped', '2=suspended', '3=background', '4=foreground']

    @classmethod
    def setUpClass(self):
        self.name = __class__.__name__
        self.platform = 'Android'
        self.global_setup.setup()
        self.driver = self.global_setup.driver
        self.log = self.global_setup.log
        self.package_name = self.global_setup.package_name

        self.login_actions = LoginActions(self.driver, self.log)

    @classmethod
    def tearDownClass(self):
        self.global_setup.core_driver.teardown()

    def setUp(self):
        self.log.debug(msg="{0}.setUp()".format(self.name))

    def tearDown(self):
        self.log.debug(msg="{0}.tearDown()".format(self.name))
        self.log.space()

    # @unittest.skip("Skipping.")
    def test_00_app_state_foregrounded(self):
        self.log.begin_test()
        self.log.info(msg="Possible app states in {0}".format(self.possible_states))

        app_state = self.driver.query_app_state(self.package_name)
        self.log.info(msg="Actual app_state={0}".format(app_state))
        self.assertEqual(4, app_state, msg="Current state of app: '{0}' should be '4'".format(self.package_name))


    # @unittest.skip("Skipping.")
    def test_01_app_state_background_to_foregrounded(self):
        self.log.begin_test()
        self.log.info(msg="Possible app states in {0}".format(self.possible_states))

        time.sleep(1)
        os.system('adb shell input keyevent KEYCODE_HOME')
        time.sleep(1)
        app_state_before = self.driver.query_app_state(self.package_name)
        self.log.info(msg="app_state_before={0}".format(app_state_before))
        self.assertEqual(3, app_state_before, msg="app_state_before: expected=3 , actual={0}".format(app_state_before))

        self.driver.activate_app(self.package_name)
        time.sleep(1)
        app_state_after = self.driver.query_app_state(self.package_name)
        self.log.info(msg="app_state_after={0}".format(app_state_after))
        self.assertEqual(4, app_state_after, msg="app_state_after: expected=4 , actual={0}".format(app_state_after))
