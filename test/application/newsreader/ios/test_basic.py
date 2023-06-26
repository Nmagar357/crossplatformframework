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
        self.platform = 'iOS'
        self.global_setup.setup()
        self.driver = self.global_setup.driver
        self.log = self.global_setup.log
        self.package_name = self.global_setup.package_name

    @classmethod
    def tearDownClass(self):
        self.global_setup.core_driver.teardown()

    def __test_case_name(self):
        return inspect.currentframe().f_back.f_code.co_name

    def test_00_basic_app_running(self):
        self.log.info(msg="Starting Test")
        self.log.info(msg="Application running in foreground for 5 sec...")
        time.sleep(5)
        self.log.info(msg="Sending App to background for 5 sec...")
        self.driver.background_app(5)
        self.log.info(msg="Finishing Test")