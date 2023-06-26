import inspect
import os
import datetime

from pathlib import Path
from test.core.common.constants.driver_constants import *
from test.core.utilities.lib.text_colors import TextColor


class LogUtility:

    log_path = None
    log_file = None

    def __init__(self):
        self.name = __class__.__name__
        self.mute = False
        self.log_level = os.environ[LOG_LEVEL]
        self.log_levels = {
            VERBOSE: [TEST,VERBOSE,DEBUG,INFO,ALERT,WARN], # Every detail possible (all possible logs)
            DEBUG: [TEST,DEBUG,INFO,ALERT,WARN],  # Extra details including debugging variables (all data and info)
            INFO: [TEST,INFO,ALERT,WARN],  # Normal Test Case level detail included (steps, actions, events, etc.)
            ALERT: [TEST,ALERT,WARN], # Only high level information, alerts and warnings
            WARN: [TEST,WARN] # Only warnings and high level information
        }
        self.log_format = "{0} |{1}| [{2}] {3}"
        self.warn_format = "{0} [{1}] {2}\n"
        self.style = TextColor()
        self.formatting = {
            WARN: self.style.warn + self.style.bold + " | WARNING |\n",
            ALERT: self.style.orange + self.style.bold,
            INFO: self.style.green,
            DEBUG: self.style.white,
            VERBOSE: self.style.grey_light,
            TEST: self.style.grey_highlight
        }

    def setup(self, log_path):
        self.log_path = Path(log_path)
        self.log_path.touch(exist_ok=True)
        open(self.log_path, 'w+').close()
        self.log_file = open(self.log_path, 'a')

    def teardown(self):
        self.log_file.close()

    def warn(self, msg, tag=None):
        # Only "Warn" log messages are logged out
        _tag = self.__get_tag(inspect.stack(), tag)
        self.__handle_log_message(level=WARN, tag=_tag, msg=msg)

    def alert(self, msg, tag=None):
        # Only highest priority log messages with level "Warn & "Alert" are logged out
        _tag = self.__get_tag(inspect.stack(), tag)
        self.__handle_log_message(level=ALERT, tag=_tag, msg=msg)

    def info(self, msg, tag=None):
        # Only "Warn", "Alert" and "Info" log messages are logged out
        _tag = self.__get_tag(inspect.stack(), tag)
        self.__handle_log_message(level=INFO, tag=_tag, msg=msg)

    def debug(self, msg, tag=None):
        # "Warn", "Alert", "Info", and "Debug" log messages are logged out
        _tag = self.__get_tag(inspect.stack(), tag)
        self.__handle_log_message(level=DEBUG, tag=_tag, msg=msg)

    def verbose(self, msg, tag=None):
        # All log message types are logged out
        _tag = self.__get_tag(inspect.stack(), tag)
        self.__handle_log_message(level=VERBOSE, tag=_tag, msg=msg)

    def begin_test(self, tag=None):
        # Special Test Case start log message
        _tag = self.__get_tag(inspect.stack(), tag)
        self.__handle_log_message(level=TEST, tag=_tag, msg="Begin Test Case: {0}".format(_tag))

    def space(self):
        print("\n")
        self.log_file.write("\n")

    def __get_tag(self, stack, tag):
        if tag is not None:
            return tag
        else:
            class_name = stack[1][0].f_locals['self'].name
            method = stack[1][0].f_code.co_name
            return "{0}.{1}".format(class_name, method)

    def __get_timestamp(self):
        return str(datetime.datetime.now())[:-3]

    def __handle_log_message(self, level, tag, msg):
        if self.mute is True: return
        elif level not in self.log_levels[self.log_level]: return
        else:
            # Console Output
            if level == WARN:
                log_print_text = self.warn_format.format(self.__get_timestamp(), tag, msg)
            else:
                log_print_text = self.log_format.format(self.__get_timestamp(), level.upper()[:1], tag, msg)

            color_prepend = self.formatting[level]
            print("{0}{1}{2}".format(color_prepend, log_print_text, self.style.end))

            # Log File Output
            log_file_text = self.log_format.format(self.__get_timestamp(), level.upper()[:1], tag, msg)
            self.log_file.write(log_file_text + "\n")

