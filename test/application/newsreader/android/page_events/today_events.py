from appium.webdriver.common.appiumby import AppiumBy

from test.core.mobile.device_actions import DeviceActions
from test.core.common.actions.common_actions import CommonActions
from test.application.newsreader.android.page_actions.sections_actions import SectionsActions
from test.application.newsreader.android.page_locators.sections_locators import SectionsLocators
from test.application.newsreader.android.page_actions.navigation_tab_actions import NavigationTabActions


class TodayEvents:

    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.log = log
        self.driver = driver

        self.device_actions = DeviceActions(driver, log)
        self.navigation_tab_actions = NavigationTabActions(driver, log)
        self.sections_actions = SectionsActions(driver, log)
        self.sections_locators = SectionsLocators(driver, log)
        self.common_actions = CommonActions(driver, log)

    def navigate_to_recently_viewed_section(self):
        # AB: discoveryTab
        self.navigation_tab_actions.click_sections_tab_button()
        self.device_actions.swipe_layout_find_target(
            layout_el=self.sections_locators.content_layout(),
            target_id=AppiumBy.XPATH,
            target_str="//android.widget.TextView[@text='Recently Viewed']",
            direction='UP'
        )
        self.common_actions.wait_for_element_not_displayed(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("Recently Viewed")', 2)
        self.sections_actions.click_recently_viewed_section()

    def navigate_to_saved_for_later_section(self):
        # AB: discoveryTab
        self.navigation_tab_actions.click_sections_tab_button()
        self.device_actions.swipe_layout_find_target(
            layout_el=self.sections_locators.content_layout(),
            target_id=AppiumBy.XPATH,
            target_str="//android.widget.TextView[@text='Saved for Later']",
            direction='UP'
        )
        self.common_actions.wait_for_element_not_displayed(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("Saved for Later")', 2)
        self.sections_actions.click_saved_for_later_section()

    def navigate_to_politics_section(self):
        # AB: discoveryTab
        self.navigation_tab_actions.click_sections_tab_button()
        self.device_actions.swipe_layout_find_target(
            layout_el=self.sections_locators.content_layout(),
            target_id=AppiumBy.XPATH,
            target_str="//android.widget.TextView[@text='Politics']",
            direction='UP'
        )
        self.common_actions.wait_for_element_not_displayed(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("Saved for Later")', 2)
        self.sections_actions.click_politics_section()

    def navigate_to_section_article(self):
        # AB: discoveryTab
        self.navigation_tab_actions.click_sections_tab_button()
        self.sections_actions.click_most_popular_section_article()
