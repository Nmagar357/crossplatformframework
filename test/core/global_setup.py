import os

from test.core.common.constants.appium_constants import *
from test.core.common.constants.driver_constants import *

from test.core.host_systems import HostSystems
from test.core.driver.driver import CoreDriver
from test.core.mobile.app_actions import AppActions
from test.core.utilities.deeplink_handler import DeeplinkHandler
from test.core.utilities.log_utility import LogUtility

try:
    LOG_LEVEL = os.environ[LOG_LEVEL]
except:
    os.environ[LOG_LEVEL] = VERBOSE


class GlobalSetup:

    driver = None
    selenium = None
    device_id = None
    log = None
    bundle_id = None
    port = None
    browser_name = None
    is_mobile = False
    is_web = False
    is_api = False
    is_cross_platform = False

    user = os.environ.get('USER')
    app = os.environ.get('APP')
    platform = os.environ.get('PLATFORM')
    device = os.environ.get('DEVICE')
    browser = 'chrome' if not os.environ.get('BROWSER') else os.environ.get('BROWSER')
    load_strategy = 'none' if not os.environ.get('LOAD_STRATEGY') else os.environ.get('LOAD_STRATEGY')
    os.environ[IGNORE_DEPRECATION_WARN] = 'true'

    def __init__(self):
        self.name = __class__.__name__
        self.host_systems = HostSystems()
        self.dl = self.host_systems.dl

        if 'ARCHIVE_PATH' not in os.environ:
            from test.core.setup_handler import SetupHandler
            SetupHandler()

        self.log = LogUtility()
        self.CONSOLE_PATH = os.environ.get('CONSOLE_PATH')
        self.log.setup(self.CONSOLE_PATH)
        self.core_driver = CoreDriver(self.host_systems, self.log)

    def setup(self, cross_platform=False):
        self.log.debug(msg="Setting up driver capabilities")

        if self.platform in [ANDROID, IOS]:
            self.core_driver.compile_desired_capabilities(
                user=self.user,
                platform=self.platform,
                application=self.app,
                device=self.device
            )
            self.port = 4723
            self.is_mobile = True

        elif self.platform == WEB:
            self.options = self.core_driver.compile_browser_options(
                browser=self.browser,
                load_strategy=self.load_strategy
            )
            self.port = None
            self.is_web = True

        elif self.platform == API:
            self.is_api = True
            raise NotImplementedError("Platform: 'API' has not yet been implemented!")

        if self.is_cross_platform is True or cross_platform is True:
            self.options = self.core_driver.compile_browser_options(
                browser=self.browser,
                load_strategy=self.load_strategy
            )
            # self.port = None
            drivers = self.core_driver.setup(port=self.port, is_mobile=self.is_mobile, is_web=self.is_web,
                is_api=self.is_api, is_cross_platform=True)
            self.driver = drivers[0]
            self.selenium = drivers[1]
        else:
            self.driver = self.core_driver.setup(port=self.port, is_mobile=self.is_mobile, is_web=self.is_web,
                is_api=self.is_api, is_cross_platform=False)

        if self.platform in [ANDROID, IOS]:
            self.desired_caps = self.core_driver.desired_caps
            self.device_id = self.desired_caps['udid']
            self.package_name = self.core_driver.bundle_id
            
        elif self.platform == WEB:
            self.browser_name = self.core_driver.browser_name

        # Core Module Extensions
        self.deeplink = DeeplinkHandler(self.driver, self.log)
        self.app_actions = AppActions(self.driver, self.log)

        self.log.space()

    def teardown(self):
        self.log.space()
        self.log.teardown()
        self.core_driver.teardown()

    def setup_routine(self, reset=True, ab_variants=True):
        if reset is True:
            self.log.debug("Resetting driver...")
            self.app_actions.reset_driver()
        if ab_variants is True:
            self.log.debug("Setting AB Test Variants...")
            self.deeplink.set_package_to_ab_test_case(ab_test=self.deeplink.AB_TEST_CASES.APP_tab_discovery)
            self.deeplink.set_package_to_ab_test_case(ab_test=self.deeplink.AB_TEST_CASES.APP_FTUX_AndroidNotifications)
            self.app_actions.activate_app(self.package_name)
        self.log.space()
