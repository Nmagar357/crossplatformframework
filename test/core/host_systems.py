import datetime
import string
import sys
import re
from test import root

class HostSystems:

    host_os = None

    def __init__(self):
        self.name = __class__.__name__
        self.dl = ""
        self.__config_system_pathing()

    def __config_system_pathing(self):
        # print("[{0}] HostOS is: '{1}'".format(self.name, sys.platform))
        is_mac = sys.platform.startswith('darwin')
        is_win = sys.platform.startswith('win')

        if is_mac is True:
            self.dl = "/"
            self.host_os = 'mac'
            # print("[{0}] {1} delimiter string='/'".format(self.name, sys.platform))
        elif is_win is True:
            self.dl = "\\"
            self.host_os = 'windows'
            # print("[{0}] {1} delimiter string='\\'".format(self.name, sys.platform))
        else:
            raise Exception("[{0}] ERROR: '{1}' is not a supported Host OS system!".format(self.name, sys.platform))

        root.dl = self.dl

    def configure_report_directory(self):
        # Configures the data/reports directory name
        date_string = str(datetime.datetime.now())[:-3]
        exclude = set(string.punctuation)
        date_string = ''.join(ch for ch in date_string if ch not in exclude)
        date_string = re.sub(r"\s+", '_', date_string)
        return date_string