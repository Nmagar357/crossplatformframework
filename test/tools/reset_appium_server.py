import os


class ResetAppium:

    def __init__(self):
        self.name = __class__.__name__
        self.__check_appium_server = 'pgrep -f "appium"'
        self.__kill_server = 'kill -9'

    def kill_appium_server(self):
        while True:
            print("[{0}] Checking for running appium servers".format(self.name))
            result = os.popen(self.__check_appium_server).read()
            if result != '':
                print("[{0}] Killing appium servers...".format(self.name))
                os.popen('{0} {1}'.format(self.__kill_server, result))
            else:
                print("[{0}] No running appium servers found.".format(self.name))
                return

if __name__ == '__main__':
    reset = ResetAppium()
    reset.kill_appium_server()