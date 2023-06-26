from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test.application.newsreader.web.web_page_locators.web_login_locators import WebLoginLocators
from test.core.global_setup import GlobalSetup


class WebLoginActions:
    selenium = GlobalSetup().selenium

    def __init__(self, selenium, log):
        self.name = __class__.__name__
        self.selenium = selenium
        self.log = log

        self.wait = WebDriverWait(selenium, 10)  # Adjust the timeout (10 seconds in this example)
        self.login_locators = WebLoginLocators(selenium, log)

    def click_login_button(self):
        self.log.info("Clicking log in button")
        self.wait.until(EC.element_to_be_clickable(self.login_locators.login_button()))
        self.login_locators.login_button().click()

    def click_subscribe_now_button(self):
        self.log.info("Clicking Subscribe Now button")
        self.wait.until(EC.element_to_be_clickable(self.login_locators.subscribe_now_button()))
        self.login_locators.subscribe_now_button().click()

    def click_account_button(self):
        self.log.info("Clicking account button")
        self.wait.until(EC.element_to_be_clickable(self.login_locators.account_button()))
        self.login_locators.account_button().click()

    def click_continue_button(self):
        self.log.info("Clicking continue button")
        self.wait.until(EC.element_to_be_clickable(self.login_locators.continue_button()))
        self.login_locators.continue_button().click()

    def input_email_text_field(self, username):
        self.log.info("Clicking email text field")
        self.wait.until(EC.element_to_be_clickable(self.login_locators.email_text_field()))
        self.login_locators.email_text_field().send_keys(username)

    def input_password_text_field(self, password):
        self.log.info("Clicking email text field")
        self.wait.until(EC.element_to_be_clickable(self.login_locators.password_text_field()))
        self.login_locators.password_text_field().send_keys(password)

    def click_log_in_button(self):
        self.log.info("Clicking log in button")
        self.wait.until(EC.element_to_be_clickable(self.login_locators.log_in_button()))
        self.login_locators.log_in_button().click()

    def click_web_article(self):
        self.log.info("Clicking article")
        self.wait.until(EC.element_to_be_clickable(self.login_locators.web_article()))
        self.login_locators.web_article().click()

    def web_article_heading_text(self):
        self.log.info("Clicking article heading text")
        self.wait.until(EC.element_to_be_clickable(self.login_locators.web_article_front_headline()))
        return self.login_locators.web_article_front_headline().text

    def click_web_article_save_button(self):
        self.log.info("Clicking article Save button")
        self.wait.until(EC.element_to_be_clickable(self.login_locators.article_save_button()))
        self.login_locators.article_save_button().click()

