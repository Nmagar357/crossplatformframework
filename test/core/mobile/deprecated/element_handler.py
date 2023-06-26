from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import ElementNotVisibleException as ENVE
from selenium.common.exceptions import ElementNotSelectableException as ENSE
from selenium.webdriver.support.wait import WebDriverWait
from test.core.common.constants.driver_constants import PLATFORM_NAME
from test.core.utilities.lib.locator_types import TYPES


class ElementHandler:

    log = None

    def __init__(self, driver, log):
        self.name = 'ElementHandler'
        self.driver = driver
        self.log = log
        self.platform_name = self.driver.capabilities[PLATFORM_NAME]
        self.wait = WebDriverWait(driver=self.driver, timeout=25, poll_frequency=1, ignored_exceptions=[ENVE, ENSE])
        self.LOCATOR_TYPES = TYPES

    def find(self, locator_type, locator_string):
        """
        Internal driver.find_element() function with extended functionality.
        Finds first matching element in the current element tree.
        Args:
            locator_type: str(), AppiumBy locator string
            locator_string: str(), Locator element string

        Returns: obj(), Any Single DOM Element, or None
        """
        locator_type, locator_string = self._process_extended_locators(locator_type, locator_string)

        if locator_type in self.LOCATOR_TYPES[self.platform_name]:
            return self._find_element(locator_type, locator_string)
        else:
            raise Exception("Handling of locator_type='{0}' with locator_string='{1}' is not supported.". format(locator_type, locator_string))

    def find_within(self, parent_element, locator_type, locator_string):
        """
        Internal Element.find_element() function with extended functionality.
        Finds a single element within a parent element container.
        Args:
            parent_element: obj(), Active Appium element
            locator_type: str(), AppiumBy locator string
            locator_string: str(), Locator element string

        Returns: obj(), Any Single DOM Element, or None
        """
        locator_type, locator_string = self._process_extended_locators(locator_type, locator_string)

        if locator_type in self.LOCATOR_TYPES[self.platform_name]:
            return self._find_element_within(parent_element, locator_type, locator_string)
        else:
            raise Exception("Handling of locator_type='{0}' with locator_string='{1}' is not supported.". format(locator_type, locator_string))

    def find_all(self, locator_string, locator_type):
        """
        Internal driver.find_elements() function with extended functionality.
        Finds all elements in the current element tree.
        Args:
            locator_type: str(), AppiumBy locator string
            locator_string: str(), Locator element string

        Returns: list[obj()], All found DOM Elements, or None
        """
        locator_type, locator_string = self._process_extended_locators(locator_type, locator_string)

        if locator_type in self.LOCATOR_TYPES[self.platform_name]:
            return self._find_all_elements(locator_type, locator_string)
        else:
            raise Exception("Handling of locator_type='{0}' with locator_string='{1}' is not supported.". format(locator_type, locator_string))

    def find_all_within(self, parent_element, locator_type, locator_string):
        """
        Internal Element.find_element() function with extended functionality.
        Finds all elements within a parent element container.
        Args:
            parent_element: obj(), Active Appium element
            locator_type: str(), AppiumBy locator string
            locator_string: str(), Locator element string

        Returns: obj(), Any Single DOM Element, or None
        """
        locator_type, locator_string = self._process_extended_locators(locator_type, locator_string)

        if locator_type in self.LOCATOR_TYPES[self.platform_name]:
            return self._find_element_within(parent_element, locator_type, locator_string)
        else:
            raise Exception("Handling of locator_type='{0}' with locator_string='{1}' is not supported.". format(locator_type, locator_string))

    def _find_element(self, locator_type, locator_string):
        # Private handling function
        self.log.info("Finding element [locator_type={0} locator_string={1}]".format(locator_type, locator_string))
        return self.wait.until(lambda x: x.find_element(locator_type, locator_string))

    def _find_element_within(self, parent_element, locator_type, locator_string):
        # Private handling function
        self.log.info("Finding child element [locator_type={0} locator_string={1}]".format(locator_type, locator_string))
        return self.wait.until(lambda x: parent_element.find_element(locator_type, locator_string))

    def _find_all_elements(self, locator_type, locator_string):
        # Private handling function
        self.log.info("Finding all elements [locator_type={0} locator_string={1}]".format(locator_type, locator_string))
        return self.wait.until(lambda x: x.find_elements(locator_type, locator_string))

    def _find_all_elements_within(self, parent_element, locator_type, locator_string):
        # Private handling function
        self.log.info("Finding all child elements [locator_type={0} locator_string={1}]".format(locator_type, locator_string))
        return self.wait.until(lambda x: parent_element.find_elements(locator_type, locator_string))

    def _process_extended_locators(self, locator_type, locator_string):
        # Private handling function
        if locator_type.lower() == "des":
            locator_type = AppiumBy.ANDROID_UIAUTOMATOR
            locator_string = 'UiSelector().description("{0}")'.format(locator_string)
        elif locator_type.lower() == "index":
            locator_type = AppiumBy.ANDROID_UIAUTOMATOR
            locator_string = 'UiSelector().index({0})'.format(int(locator_string))
        elif locator_type.lower() == "text":
            locator_type = AppiumBy.ANDROID_UIAUTOMATOR
            locator_string = 'text("{0}")'.format(locator_string)
        else:
            self.log.verbose("Extended locators process completed without changes.")

        return locator_type, locator_string
