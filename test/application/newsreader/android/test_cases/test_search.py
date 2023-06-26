import unittest

from test.application.newsreader.android.constants.newsreader_constants import ARTICLE_KEYWORDS_RRR, ARTICLE_TITLE_RRR
from test.core.global_setup import GlobalSetup
from test.core.common.constants.app_constants import *
from test.application.newsreader.android.page_events.search_events import SearchEvents
from test.application.newsreader.android.page_locators.search_locators import SearchLocators


class TestSearch(unittest.TestCase):
    global_setup = GlobalSetup()
    log = None
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.name = __class__.__name__
        cls.global_setup.setup()
        cls.driver = cls.global_setup.driver
        cls.log = cls.global_setup.log
        cls.search_events = SearchEvents(cls.driver, cls.log)
        cls.search_locators = SearchLocators(cls.driver, cls.log)

    @classmethod
    def tearDownClass(cls):
        cls.global_setup.core_driver.teardown()

    def setUp(self):
        self.driver.launch_app()
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.terminate_app(BUNDLE_NYTIMES_ANDROID)

    def test_00_search_article_keywords(self):
        self.log.info(msg="Starting Test: Search article with the keywords")
        self.search_events.search_for_articles_with_keywords(ARTICLE_KEYWORDS_RRR)
        self.log.info("Verify article keywords presence")
        assert self.search_locators.search_keywords_result().__contains__(
            ARTICLE_KEYWORDS_RRR.casefold()), "Error: Article keywords verification failed"
        self.log.debug("Article keywords verification passed")

    def test_01_search_article_title(self):
        self.log.info(msg="Starting Test: Search article with the Title")
        self.search_events.search_for_articles_with_title(ARTICLE_TITLE_RRR)
        self.log.info("Verify article title presence")
        assert self.search_locators.search_title_result().__contains__(
            ARTICLE_TITLE_RRR.casefold()), "Error: Article title verification failed"
        self.log.debug("Article title verification passed")
