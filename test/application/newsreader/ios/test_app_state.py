import inspect
import unittest

from test.core.global_setup import GlobalSetup


class TestAppState(unittest.TestCase):

    global_setup = GlobalSetup()
    log = None
    possible_states = ['0=not installed', '1=stopped', '2=suspended', '3=background', '4=foreground']

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

    def setUp(self):
        self.log.begin_test()

    def tearDown(self):
        self.log.finish_tc()

    def __test_case_name(self):
        return inspect.currentframe().f_back.f_code.co_name

    # @unittest.skip("Skipping.")
    def test_00_app_state_foregrounded(self):
        self.log.begin_test()
        self.log.info(msg="Possible app states in {0}".format(self.possible_states))

        app_state = self.driver.query_app_state(self.package_name)
        self.assertEqual(4, app_state, msg="Current state of app: '{0}' should be '4'".format(self.package_name))

        self.log.info(msg="Actual app_state={0}".format(app_state))
        self.log.finish_tc()