import unittest
import time

from test.application.newsreader.web.web_page_actions.web_login_actions import WebLoginActions
from test.application.newsreader.web.web_page_events.web_login_events import WebLoginEvents
from test.application.newsreader.web.web_page_locators.web_login_locators import WebLoginLocators
from test.core.global_setup import GlobalSetup
from test.core.common.constants.app_constants import *
from test.application.newsreader.android.page_events.login_events import LoginEvents
from test.application.newsreader.android.page_events.today_events import TodayEvents
from selenium.webdriver.common.by import By



class TestCrossPlatform(unittest.TestCase):
    """
    Example Test to show how to use cross_platform feature. Only works for Mobile(Appium) WITH Selenium.
    Python "unittest" configuration, "Environment variables":
        USER=<user>;PLATFORM=<platform>;DEVICE=<device>;APP=<project>
    Optional:
        BROWSER=<browser>;LOAD_STRATEGY=<none|eager|normal>
    Defaults:
        BROWSER=chrome;LOAD_STRATEGY=none
    """

    global_setup = GlobalSetup()
    driver = None
    selenium = None
    log = None

    @classmethod
    def setUpClass(cls):
        cls.name = __class__.__name__
        cls.global_setup.setup(cross_platform=True)
        cls.driver = cls.global_setup.driver
        cls.selenium = cls.global_setup.selenium
        cls.log = cls.global_setup.log
        cls.package_name = cls.global_setup.package_name
        cls.driver.capabilities.update({
            "appActivity": "com.nytimes.android.onboarding.compose.ComposeOnboardingActivity"
        })

        cls.today_events = TodayEvents(cls.driver, cls.log)
        cls.login_events = LoginEvents(cls.driver, cls.log)
        cls.web_login_events = WebLoginEvents(cls.selenium, cls.log)
        cls.web_login_actions = WebLoginActions(cls.selenium, cls.log)
        cls.web_login_locators = WebLoginLocators(cls.selenium, cls.log)



    @classmethod
    def tearDownClass(cls):
        cls.global_setup.core_driver.teardown()

    def setUp(self):
        self.global_setup.setup_routine(reset=False, ab_variants=True)

    # TID: NR-A-SFL-01
    #@unittest.skip("This is an example test that should not be included in test runs.")
    def test_mobile_with_web(self):
        self.log.begin_test()
        self.selenium.get(("https://www.nytimes.com"))
        self.web_login_actions.click_login_button()
        self.web_login_events.web_login_routine(SUBSCRIBER_USER_ID, SUBSCRIBER_USER_PASSWORD)
        self.web_login_actions.click_web_article()
        article_heading = self.web_login_actions.web_article_heading_text()
        self.selenium.execute_script("return arguments[0].scrollIntoView(true);", self.web_login_locators.article_save_button())
        self.web_login_actions.click_web_article_save_button()
        self.selenium.quit()
        time.sleep(90)  # Arbitrary time to see both drivers working together.

    # TID: NR-A-SFL-09
    @unittest.skip("")
    def subscriber_cross_platform_save_article_behavior(self):
        self.log.begin_test()
        self.selenium.get(("https://www.nytimes.com"))
        time.sleep(90)
        self.web_login_actions.click_login_button()
        self.web_login_events.web_login_routine(SUBSCRIBER_USER_ID, SUBSCRIBER_USER_PASSWORD)


        time.sleep(90)  # Arbitrary time to see both drivers working together.


