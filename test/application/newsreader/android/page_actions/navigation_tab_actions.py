from appium.webdriver.common.appiumby import AppiumBy

from test.application.newsreader.android.page_locators.navigation_tab_locators import NavigationTabLocators


class NavigationTabActions:

    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.log = log
        self.driver = driver

        self.nav_tab_locators = NavigationTabLocators(driver, log)

    def click_today_tab_button(self):
        self.log.info("Clicking 'Today' button.")
        self.nav_tab_locators.today_tab().click()

    def click_for_you_tab_button(self):
        self.log.info("Clicking 'For You' button.")
        self.nav_tab_locators.for_you_tab().click()

    def click_sections_tab_button(self):
        self.log.info("Clicking 'Sections' button.")
        self.nav_tab_locators.sections_tab().click()

    def get_selected_tab_text(self):
        self.log.info("Checking for currently selected tab.")
        tab_selected_parent = self.nav_tab_locators.selected_tab_parent_element()
        tab_text = tab_selected_parent.find_element(AppiumBy.CLASS_NAME, "android.widget.TextView").text
        self.log.debug("Currently selected tab: '{0}'".format(tab_text))
        return tab_text
