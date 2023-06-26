from appium.webdriver.common.appiumby import AppiumBy


class LoginLocators:

    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.driver = driver
        self.log = log

    def account_button(self):
        self.log.info("Finding account button")
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "account")

    def continue_button(self):
        self.log.info("Finding continue button")
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Continue with Email")

    def not_now_button(self):
        self.log.info("Finding 'Not Now' button")
        return self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Not now']")

    def continue_without_subscribing_button(self):
        self.log.info("Finding 'Continue without subscribing' button")
        return self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Continue without subscribing']")

    def welcome_continue_button(self):
        self.log.info("Finding continue button")
        return self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Continue']")

    def email_text_field(self):
        self.log.info("Finding email text field")
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Email Address")

    def log_in_button(self):
        self.log.info("Finding log in button")
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Log In")

    def log_in_or_register_button(self):
        self.log.info("Finding log in or register button")
        return self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Log In or Register']")

    def password_text_field(self):
        self.log.info("Finding password text field")
        return self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[2]/android.view.View")

    def username_field(self):
        self.log.info("Finding username text filed")
        return self.driver.find_element(AppiumBy.XPATH, '//android.widget.LinearLayout[@content-desc="Username"]/android.widget.RelativeLayout/android.widget.TextView[1]')

    def log_out_button(self):
        self.log.info("Finding log out button")
        return self.driver.find_element(AppiumBy.XPATH, "//*[@text='Log Out']")

    def popup_log_out_button(self):
        self.log.info("Finding popup log out button")
        return self.driver.find_element(AppiumBy.ID, "android:id/button1")

    def popup_log_in_button(self):
        self.log.info("Finding popup log in button")
        return self.driver.find_element(AppiumBy.ID, "android:id/button1")

    def logged_in_popup(self):
        self.log.info("Finding 'You are now logged in.' snackbar text")
        return self.driver.find_element(AppiumBy.ID, "snackbar_text")

