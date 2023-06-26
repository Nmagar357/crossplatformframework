from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from test.application.newsreader.android.page_locators.login_locators import LoginLocators
from test.core.common.actions.common_actions import CommonActions


class LoginActions:

    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.driver = driver
        self.log = log

        self.login_locators = LoginLocators(driver, log)
        self.common_actions = CommonActions(driver, log)

    def click_account_button(self):
        self.log.info("Clicking account button")
        self.login_locators.account_button().click()

    def click_continue_button(self):
        self.log.info("Clicking continue button")
        self.login_locators.continue_button().click()

    def click_continue_without_subscription_button(self):
        self.log.info("Clicking continue without subscribing button")
        self.login_locators.continue_without_subscribing_button().click()

    def click_email_text_field(self):
        self.log.info("Clicking email text field")
        self.login_locators.email_text_field().click()

    def click_log_in_button(self):
        self.log.info("Clicking log in button")
        self.login_locators.log_in_button().click()

    def click_log_in_or_register_button(self):
        self.log.info("Clicking log in or register button")
        self.login_locators.log_in_or_register_button().click()

    def click_log_out_button(self):
        self.log.info("Clicking logout button")
        self.login_locators.log_out_button().click()

    def click_log_out_button_popup_confirm(self):
        self.log.info("Clicking logout button popup confirm")
        self.login_locators.popup_log_out_button().click()

    def click_not_now_button(self):
        self.log.info("Clicking 'Not Now' button")
        self.login_locators.not_now_button().click()

    def click_welcome_continue_button(self):
        self.log.info("Clicking continue button")
        self.login_locators.welcome_continue_button().click()

    def get_username_field_text(self):
        self.log.info("Getting username field text")
        return self.login_locators.username_field().text

    def input_email_text_field(self, username_email_text):
        self.log.info("Sending string '{0}' to email_text_field.".format(username_email_text))
        ActionChains(self.driver).click(self.login_locators.email_text_field()).send_keys(username_email_text).perform()
        # return self.events.click_and_send_keys(self.login.email_text_field(), username_email_text)

    def input_password_text_field(self, password_text):
        self.log.info("Sending string '{0}' to password_text_field.".format(password_text))
        ActionChains(self.driver).click(self.login_locators.password_text_field()).send_keys(password_text).perform()
        # return self.events.click_and_send_keys(self.login.password_text_field(), password_text)

    def wait_for_login_screen_to_disappear(self, timeout=10):
        self.log.info("Waiting for 'Log in' page to disappear")
        self.common_actions.wait_for_element_not_displayed(AppiumBy.ACCESSIBILITY_ID, "Log In", timeout=timeout)