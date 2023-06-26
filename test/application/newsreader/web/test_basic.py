import time
import unittest

from test.core.global_setup import GlobalSetup


class TestBasic(unittest.TestCase):

    global_setup = GlobalSetup()
    log = None
    TARGET_URL = None

    @classmethod
    def setUpClass(self):
        self.name = __class__.__name__
        self.platform = 'Web'
        self.TARGET_URL = 'http://www.nytimes.com'
        self.global_setup.setup()
        self.driver = self.global_setup.driver
        self.log = self.global_setup.log

    @classmethod
    def tearDownClass(self):
        self.global_setup.core_driver.teardown()

    @unittest.skip("Skipping... [if self.global_setup.setup(url=self.TARGET_URL) ]")
    def test_00_basic_target_page_already_loaded(self):
        self.log.info(msg="Starting Test")
        time.sleep(10)
        self.log.info(msg="Finishing Test")

    # @unittest.skip("Skipping... [if self.global_setup.setup() ]")
    def test_01_basic_target_page_loading(self):
        self.log.info(msg="Starting Test")
        self.driver.get(self.TARGET_URL)
        time.sleep(10)
        self.log.info(msg="Finishing Test")