

class AppActions:

    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.driver = driver
        self.package_name = self.driver.capabilities['appPackage']
        self.activity_name = self.driver.capabilities['appActivity']
        self.app_path = self.driver.capabilities['app']
        self.log = log

    def activate_app(self, bundle_id=None):
        if bundle_id is None:
            bundle_id = self.package_name
        self.log.info("Activating application to foreground: {0}".format(bundle_id))
        self.driver.activate_app(bundle_id)
        self.log.info("App activated.")


    def background_app(self, sec=3):
        self.log.info("Backgrounding application, for '{0}' seconds.".format(sec))
        self.driver.background_app(sec)
        self.log.info("App returned to foreground.")

    def get_app_strings(self):
        # language code:"en"(optional), Path to the string file: string"/path/to/file"(optional)
        self.log.info("Getting app strings...")
        result = self.driver.app_strings()
        self.log.info("App strings: '{0}'".format(result))
        return result

    def install_app(self, app_path=None):
        if app_path is None:
            app_path = self.app_path
        self.log.info("Installing application from path: '{0}'".format(app_path))
        result = self.driver.install_app(app_path)
        self.log.info(result)
        return result

    def is_app_installed(self, bundle_id=None):
        if bundle_id is None:
            bundle_id = self.package_name
        self.log.info("Checking application installed state: {0}".format(bundle_id))
        result = self.driver.is_app_installed(bundle_id)
        self.log.info(result)
        return result

    def query_app_state(self, bundle_id=None, by_string=False):
        if bundle_id is None:
            bundle_id = self.package_name
        states = {'0': 'not installed', '1':'stopped', '2':'suspended', '3':'background', '4':'foreground'}
        self.log.info("Getting application state.")
        result = self.driver.query_app_state(self, bundle_id)
        if by_string is True:
            status = states[result]
        else:
            status = result
        self.log.info("Current app state: {0}".format(status))
        return result

    def remove_app(self, bundle_id=None):
        if bundle_id is None:
            bundle_id = self.package_name
        self.log.info("Removing application: {0}".format(bundle_id))
        result = self.driver.remove_app(bundle_id)
        self.log.info(result)
        return result

    def reset_driver(self):
        self.log.info("Resetting driver.")
        result = self.driver.reset()
        self.log.info(result)
        return result

    def start_activity(self, bundle_id=None, activity_name=None):
        if bundle_id is None:
            bundle_id = self.package_name
            activity_name = self.activity_name
        self.log.info("Starting application: {0} with activity: {1}".format(bundle_id, activity_name))
        result = self.driver.start_activity(bundle_id, activity_name)
        self.log.info(result)
        return result

    def terminate_app(self, bundle_id=None):
        if bundle_id is None:
            bundle_id = self.package_name
        self.log.info("Terminating application: {0}".format(bundle_id))
        result = self.driver.terminate_app(bundle_id)
        self.log.info(result)
        return result
