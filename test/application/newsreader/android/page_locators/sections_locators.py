from appium.webdriver.common.appiumby import AppiumBy


class SectionsLocators:

    def __init__(self, driver, log):
        self.name = __class__.__name__
        self.log = log
        self.driver = driver

    def content_layout(self):
        self.log.info("Finding screen 'content layout'.")
        return self.driver.find_element(AppiumBy.ID, "android:id/content")

    def search_articles_text_field(self):
        self.log.info("Finding 'Search Article' text field.")
        return self.driver.find_element(AppiumBy.ID, "Search")

    def first_most_popular_section_article(self):
        self.log.info("Finding first 'Most Popular' article.")
        return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("Most Popular")')

    def most_popular_layout(self):
        self.log.info("Finding 'Most Popular' layout.")
        return self.driver.find_element(AppiumBy.ID, 'Most Popular')

    def most_popular_section(self):
        self.log.info("Finding 'Most Popular' section.")
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "See more of our Most Popular stories")

    def opinion_section(self):
        self.log.info("Finding 'Opinion' section.")
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "MORE IN OPINION")

    def world_section(self):
        self.log.info("Finding 'World' section.")
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "MORE IN WORLD")

    def us_section(self):
        self.log.info("Finding 'U.S.' section.")
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "MORE IN U.S.")

    def business_section(self):
        self.log.info("Finding 'Business' section.")
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "MORE IN BUSINESS")

    def games_section(self):
        self.log.info("Finding 'Games' section.")
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "MORE IN GAMES")

    def saved_for_later_section(self):
        self.log.info("Finding 'Saved For Later' section.")
        return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("Saved for Later")')

    def recently_viewed_section(self):
        self.log.info("Finding 'Recently Viewed' section.")
        return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("Recently Viewed")')

    def politics_section(self):
        self.log.info("Finding 'Politics' section.")
        return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("Politics")')

    def reader_center_section(self):
        self.log.info("Finding 'Reader Center' section.")
        return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("Reader Center")')

    def theater_section(self):
        self.log.info("Finding 'Theater' section.")
        return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("Theater")')

    def podcasts_section(self):
        self.log.info("Finding 'Podcast' section.")
        return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("Podcasts")')

    def travel_section(self):
        self.log.info("Finding 'Travel' section.")
        return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("Travel")')

    def the_learning_network_section(self):
        self.log.info("Finding 'The Learning Network' section.")
        return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("The Learning Network")')

    def books_section(self):
        self.log.info("Finding 'Books' section.")
        return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("Books")')

    def offline_snack_bar_text(self):
        self.log.info("Finding 'Offline snackbar' text.")
        return self.driver.find_element(AppiumBy.ID, "snackbar_text")

