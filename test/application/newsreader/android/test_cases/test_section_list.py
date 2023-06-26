import unittest
from test.application.newsreader.android.page_actions.sections_actions import SectionsActions
from test.core.global_setup import GlobalSetup


class TestSectionsList(unittest.TestCase):
    global_setup = GlobalSetup()
    driver = None
    log = None
    login_events = None

    @classmethod
    def setUpClass(cls):
        cls.name = __class__.__name__
        cls.global_setup.setup()
        cls.driver = cls.global_setup.driver
        cls.log = cls.global_setup.log
        cls.section_list_actions = SectionsActions(cls.driver, cls.log)

    @classmethod
    def tearDownClass(cls):
        cls.global_setup.core_driver.teardown()

    def test_00_validate_search_box_most_popular_games_opinion_section(self):
        self.section_list_actions.click_sections_button()
        result1 = self.section_list_actions.is_search_articles_text_field_enabled()
        self.assertTrue(result1, msg="Verification of search article field failed! Expected 'True' but got '{0}'".format(result1))

        result2 = self.section_list_actions.is_most_popular_section_displayed()
        self.assertTrue(result2, msg="Verification of most popular section failed! Expected 'True' but got '{0}'".format(result2))

        result3 = self.section_list_actions.is_games_section_displayed()
        self.assertTrue(result3, msg="Verification of games section failed! Expected 'True' but got '{0}'".format(result3))

        self.section_list_actions.scroll_from_games_to_most_popular_section()

        result4 = self.section_list_actions.is_opinion_section_displayed()
        self.assertTrue(result4, msg="Verification of opinion section failed! Expected 'True' but got '{0}'".format(result4))
