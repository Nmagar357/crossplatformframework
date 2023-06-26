from appium.webdriver.common.appiumby import AppiumBy

from test.application.newsreader.android.constants.newsreader_constants import PERM_NOTIFICATION_MSG
from test.application.newsreader.android.page_locators.system_locators import SystemLocators
from test.core.common.constants.app_constants import ALLOW, DENY
from test.core.common.constants.driver_constants import IMPLICIT_WAIT


class SystemActions:

    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.log = log
        self.driver = driver
        self.platform_version = int(self.driver.capabilities['platformVersion'])

        self.system_locators = SystemLocators(driver, log)

    def handle_google_account_popup(self, select=None):
        self.log.info("Checking for Google's 'Continue with' account popup...")

        self.driver.implicitly_wait(2)
        while True:
            try:
                if self.system_locators.google_choose_account_popup().is_displayed():
                    if select == None:
                        self.log.info("Selecting 'NONE OF THE ABOVE'")
                        self.system_locators.google_non_of_the_above_button().click()
                    else:
                        self.log.info("Selecting Account: '{0}'".format(select))
                        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='{0}']".format(select)).click()
            except:
                break

        self.driver.implicitly_wait(IMPLICIT_WAIT)

    def handle_permission_grant_popup(self, select=ALLOW):
        self.log.info("Checking for 'Notification Permission' popup handling...")

        if self.platform_version >= 13:
            self.log.info("Notification Permission expected [platform_version>=13]")
            cycle = 0
            self.driver.implicitly_wait(2)
            while True:
                try:
                    if self.system_locators.permission_grant_popup().is_displayed():
                        message_state = self.system_locators.permission_grant_message().text
                        if PERM_NOTIFICATION_MSG == message_state:
                            if select == ALLOW:
                                self.log.info("Clicking ALLOW button.")
                                self.system_locators.permission_grant_allow_button().click()
                            elif select == DENY:
                                self.log.info("Clicking DON'T ALLOW button.")
                                self.system_locators.permission_grant_deny_button().click()
                            else:
                                raise Exception("Unexpected input: select='{0}'".format(select))
                except:
                    cycle+=1
                    if cycle >= 1:
                        break
                    else:
                        continue
        else:
            self.log.info("Notification Permission not expected [platform_version<=12]")

        self.driver.implicitly_wait(IMPLICIT_WAIT)

