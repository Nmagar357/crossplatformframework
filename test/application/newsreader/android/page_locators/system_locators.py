from appium.webdriver.common.appiumby import AppiumBy


class SystemLocators:

    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.log = log
        self.driver = driver

    def google_choose_account_popup(self):
        self.log.info("Finding 'Google Choose An Account' popup")
        return self.driver.find_element(AppiumBy.ID, 'com.google.android.gms:id/credential_picker_layout')

    def google_non_of_the_above_button(self):
        self.log.info("Finding 'Google None Of The Above' button")
        return self.driver.find_element(AppiumBy.ID, 'com.google.android.gms:id/cancel')

    def permission_grant_popup(self):
        self.log.info("Finding 'Permission Grant' popup")
        return self.driver.find_element(AppiumBy.ID, 'com.android.permissioncontroller:id/grant_dialog')

    def permission_grant_message(self):
        self.log.info("Finding 'Permission Grant' message")
        return self.driver.find_element(AppiumBy.ID, 'com.android.permissioncontroller:id/permission_message')

    def permission_grant_allow_button(self):
        self.log.info("Finding 'Permission Grant' allow button")
        return self.driver.find_element(AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')

    def permission_grant_deny_button(self):
        self.log.info("Finding 'Permission Grant' deny button")
        return self.driver.find_element(AppiumBy.ID, 'com.android.permissioncontroller:id/permission_deny_button')