import os

from test.core.common.constants.driver_constants import *


class SetupHandler:

    def __init__(self):
        self.name = __class__.__name__
        from test import root
        from test.core.host_systems import HostSystems

        host_systems = HostSystems()
        dl = host_systems.dl

        os.environ[DATA_REPORT_PATH] = "{0}{1}application{1}newsreader{1}data{1}reports".format(root.ROOT_DIR, dl)
        os.environ[REPORT_DIR_NAME] = host_systems.configure_report_directory()

        if ARCHIVE_PATH not in os.environ:
            os.environ[ARCHIVE_PATH] = "{0}".format(os.environ[DATA_REPORT_PATH]) + dl + os.environ[REPORT_DIR_NAME]
            os.mkdir(os.environ[ARCHIVE_PATH])

            os.environ[RESULTS_NAME] = 'results'
            os.environ[RESULTS_DIR] = "{0}".format(os.environ[ARCHIVE_PATH] + dl + os.environ[RESULTS_NAME])
            os.mkdir(os.environ[RESULTS_DIR])

        if CONSOLE_PATH not in os.environ:
            os.environ['CONSOLE_LOG_FILE_NAME'] = "console_log.txt"
            os.environ[CONSOLE_PATH] = "{0}".format(os.environ[ARCHIVE_PATH] + dl + os.environ['CONSOLE_LOG_FILE_NAME'])

        if RESULT_XML_PATH not in os.environ:
            os.environ['RESULT_XML_FILE_NAME'] = "results.xml"
            os.environ['RESULT_JSON_FILE_NAME'] = "results.json"
            os.environ[RESULT_XML_PATH] = "{0}".format(os.environ[ARCHIVE_PATH] + dl + os.environ['RESULT_XML_FILE_NAME'])

    def cleanup_result_data(self):
        if CLEANUP_ARCHIVE in os.environ:
            if os.environ[CLEANUP_ARCHIVE] is True:
                if EXPIRATION_DATE in os.environ:
                    cleanup_older_than = os.environ[EXPIRATION_DATE]
                else:
                    cleanup_older_than = 30
                archive_dirs = os.environ[DATA_REPORT_PATH]

                # 1. Create logic to check for dir name (ex: '20230101_1443198')
                # 2. Split each dir name on underscore '_' (ex: '20230101')
                # 3. Check date of dir.
                # 4. If date equal or older than cleanup_older_than integer, delete files and remove dir.

