import time

from selenium.common import NoSuchElementException
from test.core.common.constants.driver_constants import IMPLICIT_WAIT


class CommonActions:

    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.driver = driver
        self.log = log

    def wait_for_element_not_displayed(self, locator_type, locator_string, timeout=10):
        self.driver.implicitly_wait(0)
        for x in range(timeout):
            try:
                state = self.driver.find_element(locator_type, locator_string).is_displayed()
                if state is True:
                    self.log.info("Waiting 1s...")
                    time.sleep(0.9)
            except NoSuchElementException:
                self.log.info("Continuing")
                break
            except Exception as E:
                self.log.warn("An unhandled exception occurred. Please review!")
                raise E
        self.driver.implicitly_wait(IMPLICIT_WAIT)