import io
import json
import os
import xmlrunner

from xmlrunner.extra.xunit_plugin import transform
from lxml2json import convert
from test.core.host_systems import HostSystems
from test.core.setup_handler import SetupHandler
from test.application.newsreader.android.test_plans.test_recently_viewed import *


# To run TestRunner, simply configure a regular python config (not a unittest config),
# using the same Environment parameters as before...
# Environment: USER=neilnorton;DEVICE=Pixel 5;APP=Newsreader;PLATFORM=Android


class TestRunner:

    SetupHandler()

    def __init__(self):
        self.name = __class__.__name__
        self.tests = []
        self.out = io.BytesIO()
        self.host_systems = HostSystems()
        self.dl = self.host_systems.dl
        self.plan_name = None
        self.result_dir = os.environ['ARCHIVE_PATH']
        self.console_log_file_name = os.environ['CONSOLE_LOG_FILE_NAME']
        self.xml_result_path = "{0}{1}{2}".format(self.result_dir, self.dl, os.environ['RESULT_XML_FILE_NAME'])
        self.report_json_dir = "{0}{1}{2}{1}".format(self.result_dir, self.dl, os.environ['RESULTS_DIR'])

    def test_declaration(self):
        print("\033[4mTest Pipeline:\033[0m")
        for test in self.tests:
            print("\033[102m{0}\033[0m".format(test.__class__.__name__))

    def run_tests(self):
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=self.out),
            failfast=False, buffer=False, catchbreak=False, exit=False)

    def write_plan_result_xml(self):
        with open(os.environ['RESULT_XML_PATH'], 'wb') as report:
            report.write(transform(self.out.getvalue()))

    def process_xml_results_to_json_result_file(self):
        print("Processing XML result data to JSON result file.")
        xml_data = self.__read_and_convert_xml_report(self.xml_result_path)
        self.__create_suite_result_data(xml_data)
        print("Finished writing JSON result files.")

    def __read_and_convert_xml_report(self, xml_report_path):
        print("Reading & converting XML result file data.")
        xml_file_data = open(xml_report_path).read()
        data = convert(xml_file_data)
        return data

    def __write_json_result_file(self, json_data, file_name='results.json'):
        file_path = "{0}{1}{2}".format(os.environ['RESULTS_DIR'], self.dl, file_name)
        with open(file_path, "w") as json_file:
            json_file.write(json_data)

    def __create_suite_result_data(self, data):
        print("Processing result data to formatted JSON data.")
        suites_data = data['testsuites']['testsuite']
        for test_suite in suites_data:
            if type(test_suite['testcase']) == type([]):
                suite = test_suite['testcase'][0]
            else:
                suite = test_suite['testcase']

            suite_name = suite['@']['classname'].split('test_cases.')[1].split('.')[1]
            file_name = "{0}.json".format(suite_name)
            json_data = json.dumps(test_suite)
            self.__write_json_result_file(json_data=json_data, file_name=file_name)



if __name__ == '__main__':
    runner = TestRunner()
    runner.test_declaration()
    runner.run_tests()
    runner.write_plan_result_xml()
    runner.process_xml_results_to_json_result_file()