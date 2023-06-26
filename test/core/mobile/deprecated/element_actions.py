

class ElementActions:

    def __init__(self, driver, log):
        self.name = 'ElementActions'
        self.driver = driver
        self.log = log

    def clear(self, element):
        # Clears a text field of all characters in it
        try:
            self.log.info("Clearing an element's text field.")
            element.clear()
        except:
            self.log.warn("Clear text field was unsuccessful!")

    def click(self, element):
        # Single clicks on an element
        try:
            self.log.info("Clicking on an element.")
            element.click()
        except:
            self.log.warn("Click was unsuccessful!")

    def double_click(self, element):
        # Double-clicks on an element
        try:
            self.log.info("Double-clicking on an element.")
            element.double_click()
        except:
            self.log.warn("Double-click was unsuccessful!")

    def send_keys(self, element, text):
        # Sends one character into a text field (appending to existing characters on teh field)
        try:
            self.log.info("Sending character ['{0}'] to an element's text field.".format(text))
            element.send_keys(text)
        except:
            self.log.warn("Sending character ['{0}'] was unsuccessful!".format(text))

    def send_string(self, element, text):
        # Sends an entire string to a text/password field
        try:
            self.log.info("Inserting text string ['{0}'] to an element's text field.".format(text))
            element.insert(text)
        except:
            self.log.warn("Insert text string ['{0}'] was unsuccessful!".format(text))
