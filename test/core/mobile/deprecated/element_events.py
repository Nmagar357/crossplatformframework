from selenium.webdriver import ActionChains


class ElementEvents:

    def __init__(self, driver, log):
        self.name = 'ElementEvents'
        self.driver = driver
        self.log = log

    def click_and_send_keys(self, element, text):
        # Click and send text
        try:
            self.log.info("Clicking and sending text.")
            action = ActionChains(self.driver)
            action.click(element)
            action.send_keys(text)
            action.perform()
        except:
            self.log.warn("Clicking and sending text was unsuccessful!")
