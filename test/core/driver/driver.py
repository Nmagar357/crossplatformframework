import os
import json
import time
import warnings

from pathlib import Path
from selenium.common import WebDriverException
from test.core.common.constants.appium_constants import *
from test.core.common.constants.driver_constants import *
from test.core.common.constants.selenium_constants import *


class CoreDriver:

    def __init__(self, host_systems, log):
        self.name = __class__.__name__
        self.desired_caps = {}
        self.session_id = None
        self.bundle_id = None
        self.appium = None
        self.selenium = None
        self.options = None
        self.browser_name = None
        self.URL = None
        self.log = log
        self.host_systems = host_systems

    def setup(self, port=None, is_mobile=False, is_web=False, is_api=False, is_cross_platform=WEB):
        """
        Setup of webdriver object/s.
        Args:
            port: int(), port to connect server with
            is_mobile: bool(), is platform Mobile (Android/iOS)?
            is_web:  bool(), is platform Web?
            is_api: bool(), is platform API?
            is_cross_platform: bool(), is platform Mobile with Web?
        Returns: obj()/list(), driver/[appium, selenium]

        """
        self.log.verbose(msg="(port={0}, is_mobile={1}, is_web={2}, is_api={3}, is_cross_platform={4})"
            .format(port, is_mobile, is_web, is_api, is_cross_platform)
        )
        self.log.verbose(msg="{0}".format(self.desired_caps))

        if is_mobile is True:
            self.setup_mobile(port)
            if is_cross_platform is True:
                self.setup_web()
                return [self.appium, self.selenium]
            else:
                return self.appium

        elif is_web is True:
            self.setup_web()
            return self.selenium

        elif is_api is True:
            raise NotImplementedError("API server has not been implemented yet!")

        else:
            raise Exception("An unknown exception occurred trying to connect to the server!")

    def setup_mobile(self, port):
        self.log.verbose(msg="Connecting to Appium server...")
        self.log.debug(msg="implicitly_wait={0}".format(IMPLICIT_WAIT))
        self.URL = "{0}:{1}{2}".format(LOCALHOST_URL_PRE, port, LOCALHOST_URL_EXT)
        self.log.debug(msg="Server URL={0}".format(self.URL))
        self.appium = self.connect_remote_server(self.URL, self.desired_caps)
        if self.desired_caps['autoLaunch'] == 'true':
            self.log.verbose(msg="Launched target APP: '{0}'".format(self.bundle_id))
        self.bundle_id = self.__get_bundle_id()
        self.appium.implicitly_wait(IMPLICIT_WAIT)
        self.session_id = self.appium.session_id

    def setup_web(self):
        self.log.verbose(msg="Connecting to Selenium server...")
        self.log.debug(msg="implicitly_wait={0}".format(WEB_WAIT))
        self.log.debug(msg="set_script_timeout={0}".format(WEB_TIMEOUT_SCRIPT))
        self.log.debug(msg="set_page_load_timeout={0}".format(WEB_TIMEOUT_PAGE_LOAD))
        self.selenium = self.connect_selenium_server()
        self.selenium.implicitly_wait(WEB_WAIT)
        self.selenium.set_script_timeout(WEB_TIMEOUT_SCRIPT)
        self.selenium.set_page_load_timeout(WEB_TIMEOUT_PAGE_LOAD)

    def teardown(self):
        """
        Teardown function for the CoreDriver instances.
        :return:
        """
        self.log.verbose(msg="CoreDriver teardown")

        if self.bundle_id is not None:
            self.log.verbose(msg="Terminating target app: '{0}'".format(self.bundle_id))
            self.appium.terminate_app(self.bundle_id)
            self.log.verbose(msg="Terminating Appium driver")
            self.appium.quit()

        if self.browser_name is not None:
            self.log.verbose(msg="Closing web browser.")
            self.selenium.close()
            self.log.verbose(msg="Terminating Selenium driver")
            self.selenium.quit()

        self.log.teardown()

    def compile_browser_options(self, browser, load_strategy):
        browser = browser.lower()
        if browser == CHROME:
            from selenium.webdriver.chrome.options import Options as ChromeOptions
            self.options = ChromeOptions()

        elif browser == SAFARI:
            from selenium.webdriver.safari.options import Options as SafariOptions
            self.options = SafariOptions()

        elif browser == FIREFOX:
            from selenium.webdriver.firefox.options import Options as FirefoxOptions
            self.options = FirefoxOptions()

        elif browser == EDGE:
            from selenium.webdriver.edge.options import Options as EdgeOptions
            self.options = EdgeOptions()

        elif browser == IE:
            from selenium.webdriver.ie.options import Options as IeOptions
            self.options = IeOptions()

        else:
            raise NotImplementedError("A 'browser' with name: '{0}' has not been implemented!".format(browser))

        self.options.platform_name = self.host_systems.host_os
        self.options.page_load_strategy = load_strategy.lower()
        self.options.accept_insecure_certs = True
        self.options.add_argument("--window-size=1080,1920")
        self.options.add_argument('disable-infobars')
        self.options.add_experimental_option("useAutomationExtension", False)
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])

        return self.options

    def compile_desired_capabilities(self, user, platform, application, device):
        """
        Compiles the driver's desired_capabilities given the provided argument parameters.
        :param user: str(), local machine name, and string of <user>.json profile (ex: 'neilnorton')
        :param platform: str(), "Android", "iOS", or "Web"
        :param application: str(), name of application (ex: 'Newsreader')
        :param device: str(), name of the device (ex: "Pixel 6")
        :return: dict(), desired_capabilities
        """
        self.log.verbose(msg="Getting desired capability profile paths")
        desired_cap_paths = self.__get_desired_capability_paths(user=user)
        self.log.debug(msg=desired_cap_paths)
        core_json_file = open(desired_cap_paths["core_json_file"], "r")
        user_json_file = open(desired_cap_paths["user_json_file"], "r")

        core_json_data = json.load(core_json_file)
        user_json_data = json.load(user_json_file)

        self.log.verbose(msg="JSONs loaded. Compiling capabilities...")

        core_caps = core_json_data['Core']
        self.desired_caps.update(core_caps)
        platform_caps = core_json_data['Platform'][0][platform]
        self.desired_caps.update(platform_caps)
        application_caps = core_json_data['Application'][0][platform][0][application]
        self.desired_caps.update(application_caps)
        user_device_caps = user_json_data[platform]['Devices'][0][device]
        self.desired_caps.update(user_device_caps)
        apk_path_caps = user_json_data[platform]['Paths'][0][application]
        self.desired_caps.update(apk_path_caps)

        core_json_file.close()
        user_json_file.close()

        return self.desired_caps

    def connect_remote_server(self, url, desired_capabilities):
        from appium import webdriver

        attempt = 0

        while True:
            try:
                attempt += 1
                self.log.verbose(msg="Connecting to Appium server (attempt #{0})".format(attempt))
                if os.environ[IGNORE_DEPRECATION_WARN] == 'true':
                    with warnings.catch_warnings():
                        self.log.debug("Filtering: 'IGNORE', for type: 'DeprecatedWarning'")
                        warnings.filterwarnings(IGNORE, category=DeprecationWarning)
                        return webdriver.Remote(command_executor=url, desired_capabilities=desired_capabilities)
                else:
                    return webdriver.Remote(command_executor=url, desired_capabilities=desired_capabilities)

            except WebDriverException:
                import traceback
                traceback.print_exc()
                if attempt < 5:
                    self.log.alert(msg="Failed to connect to Appium server. Retrying...")
                    time.sleep(1)
                else:
                    self.log.warn(msg="Failed to connect to Appium server. Check server & device states!")
                    return False

    def connect_selenium_server(self):
        from selenium import webdriver
        from selenium.common import WebDriverException

        attempt = 0
        self.browser_name = self.options.default_capabilities['browserName']

        while True:
            try:
                attempt += 1
                self.log.verbose(msg="Connecting to selenium '{1}' server (attempt #{0})".format(attempt, self.browser_name))
                if self.browser_name == CHROME:
                    return webdriver.Chrome(options=self.options)
                elif self.browser_name == FIREFOX:
                    return webdriver.Firefox(options=self.options)
                elif self.browser_name == SAFARI:
                    return webdriver.Safari(options=self.options)
                elif self.browser_name == EDGE:
                    return webdriver.Edge(options=self.options)
                elif self.browser_name == IE:
                    return webdriver.Ie(options=self.options)
                else:
                    raise NotImplementedError

            except WebDriverException:
                import traceback
                traceback.print_exc()
                if attempt < 5:
                    self.log.alert(msg="Failed to connect to selenium server. Retrying...")
                    time.sleep(1)
                else:
                    self.log.warn(msg="Failed to connect to selenium server. Check server & desktop states!")
                    return False

    def __get_bundle_id(self):
        """
        Internal function to assign the package name or bundle id to the core driver variables.
        :return: None, Str
        """
        if self.desired_caps[PLATFORM_NAME] == ANDROID:
            bundle_id = self.desired_caps[APP_PACKAGE]
        elif self.desired_caps[PLATFORM_NAME] == IOS:
            bundle_id = self.desired_caps[BUNDLE_ID]
        else:
            raise NotImplementedError

        self.log.verbose(msg="Got bundle_id: {0}".format(bundle_id))
        return bundle_id

    def __get_desired_capability_paths(self, user):
        """
        Internal function to return correct paths for desired capability profiles HostOS dependent.
        :param user: str(), name of user json (ex: 'neilnorton.json' is 'neilnorton')
        :return: dict(), file paths for core_json_file and user_json_file
        """
        self.log.verbose(msg="Getting desired capability JSON paths")
        dl = self.host_systems.dl
        current_dir = os.path.abspath(__file__)
        core_dir = os.path.split(current_dir)[0].split("{0}driver".format(dl))[0]
        profiles_dir = "{0}{1}data{1}profiles".format(core_dir, dl)
        core_json_file = Path("{0}{1}core.json".format(profiles_dir, dl))
        user_json_file = Path("{0}{2}users{2}{1}.json".format(profiles_dir, user, dl))

        return {"core_json_file": core_json_file, "user_json_file": user_json_file}
