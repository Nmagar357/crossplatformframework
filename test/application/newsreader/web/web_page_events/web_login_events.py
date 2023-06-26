from test.application.newsreader.web.web_page_actions.web_login_actions import WebLoginActions
from test.core.global_setup import GlobalSetup


class WebLoginEvents:
    selenium = GlobalSetup().selenium


    def __init__(self, selenium, log):
        self.name = __class__.__name__
        self.selenium = selenium
        self.log = log

        self.login_actions = WebLoginActions(selenium, log)

    def web_login_routine(self, username, password):
        self.login_actions.input_email_text_field(username)
        self.login_actions.click_continue_button()
        self.login_actions.input_password_text_field(password)
        self.login_actions.click_log_in_button()
