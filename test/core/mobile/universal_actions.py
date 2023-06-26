from test.core.common.constants.appium_constants import ANDROID


class UniversalActions:

    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.driver = driver
        self.log = log

    def back_button(self):
        self.log.info("Tapping Back button.")
        self.driver.back()

    def home_button(self):
        self.log.info("Tapping Home button.")
        self.driver.press_keycode(3)

    def appswitch_button(self):
        self.log.info("Tapping AppSwitch button.")
        if self.driver.platform == ANDROID:
            self.driver.press_keycode(3)
            self.driver.press_keycode(187)
        else:
            raise NotImplementedError
