from test.core.global_setup import GlobalSetup
from selenium.webdriver.common.by import By


class WebLoginLocators:
    selenium = GlobalSetup().selenium

    def __init__(self, selenium, log):
        self.name = __class__.__name__
        self.selenium = selenium
        self.log = log

    def account_button(self):
        self.log.info("Finding account button")
        return self.selenium.find_element(By.LINK_TEXT, "Account")

    def login_button(self):
        self.log.info("Finding login button")
        return self.selenium.find_element(By.CSS_SELECTOR, "a[class='css-1kj7lfb'")

    def subscribe_now_button(self):
        self.log.info("Finding Subscribe Now button")
        return self.selenium.find_element(By.LINK_TEXT, "Subscribe now")

    def email_text_field(self):
        self.log.info("Finding email text field")
        return self.selenium.find_element(By.CSS_SELECTOR, "input[name='email']")

    def continue_button(self):
        self.log.info("Finding continue button")
        return self.selenium.find_element(By.CLASS_NAME, "css-1i3jzoq-buttonBox-buttonBox-primaryButton-primaryButton-Button")

    def password_text_field(self):
        self.log.info("Finding password text field")
        return self.selenium.find_element(By.CSS_SELECTOR, "input[name='password'")

    def log_in_button(self):
        self.log.info("Finding log in button")
        return self.selenium.find_element(By.CSS_SELECTOR, "button[type='submit']")

    def web_article(self):
        self.log.info("Finding Article")
        return self.selenium.find_element(By.CLASS_NAME, "css-xdandi")

    def web_article_front_headline(self):
        self.log.info("Finding Article headline")
        return self.selenium.find_element(By.ID, "link-4c3b4ac0")

    def article_save_button(self):
        self.log.info("Finding Article save button")
        return self.selenium.find_element(By.CLASS_NAME, "css-16pzdkq actionbar-button")

