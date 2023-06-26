from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException

from test.application.newsreader.android.page_locators.sections_article_locators import SectionsArticleLocators


class SectionsArticleActions:
    """
   # Introduction:
   The News Article Section Screen Elements are various components that make up the layout and presentation of news articles on a 'NYT' website or app.
   Each element serves a specific purpose in providing information and engaging the readers.
   Here's a detailed introduction to each of the elements present on 'Sections' screen:

   # Lede (Lead) Article:
   The Lede Article is typically the main or featured article displayed prominently at the top of the news section.
   It is usually larger and grabs the reader's attention.
   The lede article is considered the most important or significant news story of the moment and is intended to draw readers into the content.

   # Row Article:
   Row Articles are additional news articles displayed below the lede article.
   They are usually arranged in a row or grid format, allowing readers to scroll through and explore more stories.
   Row articles provide a wider range of news topics and allow for a more comprehensive news reading experience.

   # Lead Article Thumbnail:
   The Lead Article Thumbnail is a small image or picture associated with the lede article.
   It is displayed alongside the headline and description of the article.
   The thumbnail helps to visually represent the main story and can provide a glimpse into the article's content.

   # Row Article Thumbnail:
   Similar to the lead article thumbnail, the Row Article Thumbnail is a small image or picture associated with each row article.
   It serves the same purpose of providing a visual representation of the news story and can be helpful in quickly identifying the content of each article.

   # Lead Article Headline:
   The Lead Article Headline is the title or main heading of the lede article.
   It is typically larger and more prominent than the headlines of row articles.
   The headline aims to capture the essence of the news story and entice readers to click and read the full article.

   # Row Article Headline:
   The Row Article Headline refers to the titles or headings of the row articles.
   These headlines are usually displayed below each row article thumbnail.
   They provide a brief summary of the news story and are designed to catch the reader's attention.

   # Lead Article Description:
   The Lead Article Description is a short summary or excerpt of the lede article.
   It accompanies the lead article headline and thumbnail, providing additional context and enticing readers to click and read the full article.
   The description may highlight key points or the most intriguing aspects of the story.

   # Row Article Description:
   The Row Article Description is a brief summary or excerpt of each row article.
   It appears below the row article headline and thumbnail, providing a concise overview of the news story.
   The description helps readers quickly assess the content and decide which articles they are interested in reading.

   # Save Ribbon:
   The Save Ribbon is a feature that allows readers to bookmark or save articles for later.
   It is typically represented by an icon or button associated with each article.
   By clicking the save ribbon, readers can store articles they find interesting and want to revisit at a later time.

   # Share Ribbon:
   The Share Ribbon is a feature that enables readers to share articles with others through various platforms and social media channels.
   It is usually represented by an icon or button associated with each article.
   By clicking the share ribbon, readers can spread the news and engage in discussions with their network.

   # Time Stamp:
   The Time Stamp indicates when the article was published or last updated.
   It provides readers with the time reference of the news story, allowing them to understand the recency of the information.
   The time stamp can help readers prioritize and gauge the relevance of the articles based on their publication dates.

   # Functions and their working:

    1. get_sf_lede_article_headline_text():
    This function is designed to retrieve and return the headline text of the section front's lede article.
    It also includes logging statements to record the information for debugging or monitoring purposes.

    2. get_sf_row_article_headline_text(by_index):
    This function allows you to obtain the headline text of a specific row article on the section front by providing the index.
    It utilizes a list of headline texts and retrieves the desired headline using the provided index.
    Logging statements are included to record the process and the selected row article's index for monitoring and debugging purposes.

    3. click_saved_for_later_ribbon(by_index):
    This function is responsible for clicking on the saved for later ribbon of a specific article based on the provided index.
    It locates the corresponding element, performs the click operation, and returns the click action.
    The logging statements are included to provide information about the executed action.

    """

    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.log = log
        self.driver = driver

        self.sections_article_locators = SectionsArticleLocators(driver, log)

    def get_sf_lede_article_headline_text(self):
        self.log.info("Getting section front 'lede article' headline text.")
        lede_article_headline_text = self.sections_article_locators.sf_lede_headline_text().text
        self.log.info("Section front lede(lead) article headline text.: {0}.".format(lede_article_headline_text))
        return lede_article_headline_text

    def get_sf_row_article_headline_text(self, by_index):
        self.log.info("Getting section front 'row article' headline text.")
        row_article_text_list = self.sections_article_locators.sf_row_headline_text_list()
        row_article_headline_text = row_article_text_list[by_index].text
        self.log.info("Section front row article headline text.: {0}.".format(by_index))
        return row_article_headline_text

    def click_saved_for_later_ribbon(self, by_index):
        self.log.info("Clicking article 'index: {0}' saved for later ribbon.".format(by_index))
        saved_for_later_ribbon_list = self.sections_article_locators.sf_saved_for_later_ribbon_list()
        article_element = saved_for_later_ribbon_list[by_index]
        return article_element.click()

    def is_article_accessible(self):
        try:
            self.log.info("Finding article is accessible")
            self.sections_article_locators.non_subscriber_offline_gateway_popup()
            return True
        except NoSuchElementException:
            self.log.info("Found article is accessible")
            return False