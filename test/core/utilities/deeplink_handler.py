import os
import time

from test.core.common.constants import deeplink_constants
from test.core.utilities.lib.ab_test_directory import AB_TEST_VARIANTS


class DeeplinkHandler:

    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.driver = driver
        self.log = log
        self.package_name = self.driver.capabilities['appPackage']
        self.AB_TEST_CASES = deeplink_constants
        self.AB_TEST_VARIANTS = AB_TEST_VARIANTS

    def set_package_to_ab_test_case(self, ab_test, case_index=1):
        """
        This is the main function of the DeeplinkHandler, used to set an A/B Test Case variant.

        Example Use:
        deeplink = DeeplinkHandler(log)
        deeplink.set_package_to_ab_test_case(ab_test=deeplink.AB_TEST_CASES.APP_FTUX_AndroidNotifications)

        Args:
            ab_test: str() -> deeplink_constants defined A/B test name
            case_index: int() -> index of A/B test variant in ab_test_directory.AB_TEST_VARIANTS (default=1)

        Returns:

        """
        self.log.info("Setting ab_test='{0}' to case_index='{1}' on package='{2}'".format(ab_test, case_index, self.package_name))
        case = self.__case_picker(ab_test, case_index)
        deeplink_message = self.__get_ab_test_deeplink_message(ab_test, case, self.package_name)
        deeplink_command = self.__get_deeplink_command(deeplink_message, self.package_name)
        os.system(deeplink_command)
        time.sleep(1)
        if ab_test == 'APP_tab_discovery':
            self.driver.activate_app(self.package_name)
            time.sleep(1)
            self.driver.terminate_app(self.package_name)
            time.sleep(0.5)


    def __case_picker(self, ab_test, index):
        self.log.debug("Picking ab_test='{0}' variant with index='{1}'".format(ab_test, index))
        try:
            case = self.AB_TEST_VARIANTS[ab_test][index]
        except KeyError:
            raise Exception("ab_test='{0}' not found!".format(ab_test))
        except IndexError:
            raise Exception("ab_test='{0}' has no case variant at index='{0}' !".format(ab_test, index))
        return case

    def __get_ab_test_deeplink_message(self, ab_test, case, package_name):
        self.log.info("Getting deeplink message for: ab_test='{0}' case='{1}'".format(ab_test, case))
        base_package = package_name.split('.')[1]
        self.log.debug("base_package='{0}'".format(base_package))
        deeplink_message = "{0}://abra?{1}={2}".format(base_package, ab_test, case)
        self.log.debug("deeplink_message='{0}'".format(deeplink_message))
        return deeplink_message

    def __get_deeplink_command(self, deeplink_message, package_name, intent='android.intent.action.VIEW'):
        self.log.info("Getting deeplink command")
        deeplink_command = 'adb shell am start -a {0} -d "{1}" {2}'.format(intent, deeplink_message, package_name)
        self.log.debug("deeplink_command='{0}'".format(deeplink_command))
        return deeplink_command


if __name__ == '__main__':
    # Module Test
    deeplink = DeeplinkHandler()  # Must comment-out all self.log / log references to run internally
    ab_test = deeplink.AB_TEST_CASES.APP_FTUX_AndroidNotifications
    deeplink.set_package_to_ab_test_case(ab_test)
