
class SessionActions:
    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.driver = driver
        self.log = log

    def get_session_capabilities(self):
        self.log.info("Getting session capabilities.")
        desired_caps = self.driver.capabilities
        self.log.debug(desired_caps)
        return desired_caps

    def go_back(self, times=1):
        self.log.info("Back button navigation: times={0}".format(times))
        for x in range(times):
            self.log.info("Tapping back.")
            self.driver.back()

    def save_screenshot_as_png(self, file_path):
        # file_name, file_path: same, Returns: boolean_value: True, False
        self.log.info("Taking a screenshot of the current page: {0}".format(file_path))
        screenshot = self.driver.save_screenshot(file_path)
        if screenshot is False:
            self.log.warn("Screenshot failed!")
        return screenshot

    def get_page_source(self):
        self.log.info("Getting the current application hierarchy XML or page source.")
        source = self.driver.page_source
        self.log.debug(source)
        return source

    def get_orientation(self):
        self.log.info("Getting device orientation.")
        orientation = self.driver.orientation
        return orientation

    def set_orientation(self, orientation_value='LANDSCAPE'):
        self.log.info("Setting device orientation: {0}".format(orientation_value))
        assert orientation_value in ['LANDSCAPE', 'PORTRAIT']
        self.driver.orientation = orientation_value

    def get_geo_location(self):
        self.log.info("Getting GEO location.")
        geo_location = self.driver.location()
        return geo_location

    def set_geo_location(self, latitude, longitude, altitude):
        # { latitude, longitude, altitude(optional) }: numeric values
        self.log.info("Setting GEO location: {0}".format(latitude, longitude, altitude))
        self.driver.set_location(latitude, longitude, altitude)

    def get_log(self, log_type='server'):
        # log_type: Type of Appium log that which will be returned i.e. 'driver', 'browser', 'client', 'server' etc.
        self.log.info("Getting logs with log type: '{0}'".format(log_type))
        logs = self.driver.get_log(log_type)
        self.log.debug(logs)
        return logs

    def get_device_settings(self):
        self.log.info("Getting device settings.")
        result = self.driver.get_settings()
        self.log.debug(result)
        return result

    def execute_shell_command(self, command):
        self.log.info("Executing driver shell command: {0}".format(command))
        response = self.driver.execute_driver(command)
        self.log.debug("Response: '{0}'".format(response))
        return response
