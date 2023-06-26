import subprocess
from test.core.common.constants.commands import *
from test.core.common.constants.device_constants import *
from test.core.common.constants.driver_constants import *
from appium.webdriver.extensions.android.network import NetSpeed


class DeviceActions:

    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.driver = driver
        self.log = log
        self.CONNECTIONS = {
            OFF: 0,
            AIRPLANE_MODE: 1,
            WIFI_ONLY:2,
            DATA_ONLY:4,
            DATA_AND_WIFI: 6
        }

    # Display Touch Actions #

    def flick(self, from_x, from_y, to_x, to_y):
        # Usage: driver.flick(100, 100, 100, 400)
        self.log.info("Flicking the screen: 'from={0} to={1}'".format([from_x, from_y], [to_x, to_y]))
        self.driver.flick(from_x, from_y, to_x, to_y)

    def scroll_to(self, element_from, element_to):
        # Usage: driver.scroll(el1, el2)
        self.log.info("Scrolling from element to element.")
        self.driver.scroll(element_from, element_to)

    def shake(self):
        self.log.info("Shaking the device.")
        self.driver.shake()

    def swipe(self, x1, x2, y1, y2, ms=1000):
        self.log.info("Swiping screen with: x1={0} x2={1} y1={2} y2={3} ms={4}".format(x1, x2, y1, y2, ms))
        self.driver.swipe(start_x=x1, start_y=y1, end_x=x2, end_y=y2, duration=ms)

    def tap(self, coordinates, time_ms=100):
        #  Usage: driver.tap([(100, 20), (100, 60), (100, 100)], 500)
        self.log.info("Tapping on screen at coordinates: {0} with duration: {1}".format(coordinates, time_ms))
        self.driver.tap(positions=coordinates, duration=time_ms)

    # -------------------- #

    def get_device_time(self):
        result = self.driver.get_device_time()
        self.log.debug("Device time='{0}'".format(result))
        return result

    def get_display_density(self):
        result = self.driver.get_display_density()
        self.log.debug("Display density='{0}'".format(result))
        return result

    def get_system_bars(self):
        # Returns device's current display system bars (Notification (top) & Navigation (bottom))
        self.log.info("Getting system bar information.")
        result = self.driver.get_system_bars()
        self.log.debug(result)
        return result

    def hide_keyboard(self):
        if self.driver.is_keyboard_shown() is True:
            self.log.info("Keyboard is displayed. Hiding keyboard.")
            self.driver.hide_keyboard()
        else:
            self.log.info("Keyboard is not displayed, unable to hide.")

    def toggle_device_power(self, state=ON):
        # Turns device power ON ('on') or OFF ('off')
        self.log.info("Setting device power state to: '{0}'".format(state))
        self.driver.set_power_ac(ac_state=state)

    def press_keycode(self, keycode):
        self.log.info("Pressing keycode='{0}'".format(keycode))
        self.driver.press_keycode(keycode)

    def press_keyevent(self, keyevent):
        self.log.info("Pressing keyevent='{0}'".format(keyevent))
        self.driver.keyevent(keyevent)

    # Locking Functionality #

    def lock(self):
        self.log.info("Locking device screen.")
        self.driver.lock()

    def unlock(self):
        self.log.info("Unlocking device screen.")
        self.driver.unlock()

    def is_locked(self):
        result = self.driver.is_locked()
        if result is True:
            self.log.info("Device screen is locked.")
        elif result is False:
            self.log.info("Device screen is unlocked.")
        else:
            self.log.warn("is_locked={0}".format(result))
        return result

    # -------------------- #

    # Network Functionality #

    def get_wifi_on_state(self):
        self.log.info("Checking wifi_on state...")
        result = int(subprocess.check_output(ADB_CHECK_WIFI_ON.split()))
        if result == 1:
            self.log.debug("Wifi is ON")
            return True
        elif result == 0:
            self.log.debug("Wifi is OFF")
            return False
        else:
            raise Exception("[get_wifi_on_state] Failed to interpret result: {0}".format(result))

    def set_network_connection(self, type=DATA_AND_WIFI):
        # [ANDROID ONLY]
        # Sets a network connection between [OFF, AIRPLANE_MODE, WIFI_ONLY, DATA_ONLY, DATA_AND_WIFI]
        self.log.info("Setting network connection type to: '{0}'".format(type))
        assert type.lower() in self.CONNECTIONS
        self.driver.set_network_connection(self.CONNECTIONS[type.lower()])

    def set_data_network_speed(self, type=FULL):
        # [ANDROID ONLY] IF: set_network_connection(type=DATA_ONLY)
        # Sets a network speed for Data Network in [FULL, GSM, LTE, GPRS]
        self.log.info("Setting network connection type to: '{0}'".format(type))
        assert type in NetSpeed
        self.driver.set_network_speed(type)

    def toggle_wifi(self):
        result = self.driver.toggle_wifi()
        self.log.info("Network WIFI toggle result: '{0}'".format(result))
        return result

    # -------------------- #

    def reset_orientation(self):
        self.log.info("Resetting device orientation (Portrait)")
        self.driver.orientation = PORTRAIT

    def set_orientation(self, orientation=PORTRAIT):
        self.log.info("Setting device orientation to: '{0}'".format(orientation))
        if orientation is LANDSCAPE:
            self.driver.orientation = LANDSCAPE
        elif orientation is PORTRAIT:
            self.driver.orientation = PORTRAIT
        else:
            self.log.warn("'{0}' is not a valid orientation!".format(orientation))

    # Recording Functionality #

    def save_screenshot(self, filename):
        # Usage: driver.save_screenshot('/Screenshots/foo.png')
        self.log.info("Saving screenshot with path: '{0}'".format(filename))
        self.driver.save_screenshot(filename)

    def screen_recording_start(self):
        self.log.info("Starting screen recording.")
        self.driver.start_recording_screen()

    def screen_recording_stop(self):
        self.log.info("Stopping screen recording.")
        self.driver.stop_recording_screen()

    # -------------------- #
    def turn_on_wifi(self):
        if not self.get_wifi_on_state():
            self.log.info("Turning wi-fi to 'on' state.")
            return self.driver.toggle_wifi()

    def turn_off_wifi(self):
        if self.get_wifi_on_state():
            self.log.info("Turning wi-fi to 'off' state.")
            return self.driver.toggle_wifi()

    # -- Complex Display Actions -- #

    def swipe_layout_find_target(self, layout_el, target_id=None, target_str=None, direction='UP', ms=1000, max_try=5):
        self.log.info("Scrolling '{0}' to find element:".format(direction))
        self.log.info("target_id={0}, target_str={1}".format(target_id, target_str))
        layout_bounds = layout_el.rect  # {'height': *, 'width': *, 'x': *, 'y': *}
        buff_factor = 0.2  # buffer for layout in-bounds (10%)

        if direction in ['UP', 'DOWN']:
            from_x = int(layout_bounds['width'] / 2) + layout_bounds['x']
            to_x = int(layout_bounds['width'] / 2) + layout_bounds['x']
            buffer = int(layout_bounds['height'] * buff_factor)
            if direction == 'UP':
                from_y = (layout_bounds['y'] + layout_bounds['height']) - buffer
                to_y = layout_bounds['y'] + buffer
            elif direction == 'DOWN':
                from_y = layout_bounds['y'] + buffer
                to_y = (layout_bounds['y'] + layout_bounds['height']) - buffer
            else:
                raise Exception("Not a valid direction={0}".format(direction))

        elif direction in ['LEFT', 'RIGHT']:
            raise NotImplementedError

        else:
            raise Exception("Given direction='{0}' does not match expected directions!".format(direction))

        cycle = 1
        self.driver.implicitly_wait(3)
        while True:
            try:
                self.swipe(x1=from_x, x2=to_x, y1=from_y, y2=to_y, ms=ms)
                self.driver.find_element(target_id, target_str)
                break
            except:
                if cycle > max_try:
                    self.driver.implicitly_wait(20)
                    raise Exception("Could not find target element within max_try={0}".format(max_try))
                else:
                    self.log.info("Continue swipe for: target_id={0}, target_str={1}".format(target_id, target_str))
                    cycle+=1

        self.driver.implicitly_wait(20)
        self.log.info("Swipe found target element={0}".format(target_str))
