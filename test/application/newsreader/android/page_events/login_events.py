from test.application.newsreader.android.page_actions.login_actions import LoginActions
from test.core.common.actions.system_actions import SystemActions
from test.core.common.constants.app_constants import ALLOW
from test.core.mobile.device_actions import DeviceActions


class LoginEvents:

    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.driver = driver
        self.log = log

        self.device_actions = DeviceActions(driver, log)
        self.login_actions = LoginActions(driver, log)
        self.system_actions = SystemActions(driver, log)

    def skip_app_welcome_pages(self, google_act=None, permission=ALLOW):
        self.login_actions.click_not_now_button()
        self.system_actions.handle_google_account_popup(select=google_act)
        self.login_actions.click_continue_without_subscription_button()
        self.system_actions.handle_permission_grant_popup(select=permission)
        self.login_actions.click_welcome_continue_button()

    def login_routine(self, username, password):
        self.login_actions.click_email_text_field()
        self.login_actions.input_email_text_field(username)
        self.login_actions.click_continue_button()
        self.login_actions.input_password_text_field(password)
        self.device_actions.hide_keyboard()
        self.login_actions.click_log_in_button()
        self.login_actions.wait_for_login_screen_to_disappear(timeout=10)

    def get_logged_in_username(self):
        return self.login_actions.get_username_field_text()
