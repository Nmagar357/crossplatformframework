import inspect
import time
import unittest

from test.core.global_setup import GlobalSetup


class TestBasic(unittest.TestCase):

    global_setup = GlobalSetup()
    log = None

    @classmethod
    def setUpClass(self):
        self.name = __class__.__name__
        self.platform = 'Android'
        self.global_setup.setup()
        self.driver = self.global_setup.driver
        self.log = self.global_setup.log
        self.package_name = self.global_setup.package_name

    @classmethod
    def tearDownClass(self):
        self.global_setup.core_driver.teardown()

    def setUp(self):
        self.log.debug(msg="{0}.setUp()".format(self.name))

    def tearDown(self):
        self.log.debug(msg="{0}.tearDown()".format(self.name))
        self.log.space()

    def test_00_basic_app_running(self):
        self.log.begin_test()

        from test.core.mobile.device_actions import DeviceActions
        device_actions = DeviceActions(self.driver, self.log)
        result = device_actions.get_wifi_on_state()
        print(result)
        time.sleep(5)
        # self.log.info(msg="Application running in foreground for 5 sec...")
        # time.sleep(5)
        # self.log.info(msg="Sending App to background for 5 sec...")
        # self.driver.background_app(5)
