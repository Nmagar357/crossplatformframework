from appium.webdriver.common.appiumby import AppiumBy
from test.core.common.constants.appium_constants import *

TYPES = {
    ANDROID: [
        AppiumBy.ACCESSIBILITY_ID,
        AppiumBy.ANDROID_UIAUTOMATOR,
        AppiumBy.CLASS_NAME,
        AppiumBy.ID,
        AppiumBy.IOS_UIAUTOMATION,
        AppiumBy.NAME,
        AppiumBy.XPATH
    ],
    IOS: [
        AppiumBy.ACCESSIBILITY_ID,
        AppiumBy.CLASS_NAME,
        AppiumBy.ID,
        AppiumBy.IOS_CLASS_CHAIN,
        AppiumBy.IOS_PREDICATE,
        AppiumBy.IOS_UIAUTOMATION,
        AppiumBy.NAME,
        AppiumBy.XPATH
    ],
    WEB: [
        AppiumBy.ID,
        AppiumBy.CLASS_NAME,
        AppiumBy.NAME,
        AppiumBy.TAG_NAME,
        AppiumBy.LINK_TEXT,
        AppiumBy.PARTIAL_LINK_TEXT,
        AppiumBy.CSS_SELECTOR,
        AppiumBy.XPATH
    ]
}