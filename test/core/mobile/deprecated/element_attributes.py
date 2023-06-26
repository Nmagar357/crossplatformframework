class ElementAttributes:

    def __init__(self, driver, log):
        self.name = 'ElementAttributes'
        self.driver = driver
        self.log = log

    def text(self, element):
        self.log.info("Getting TEXT of an Element...")
        text = element.text
        self.log.info("text= '{0}'".format(text))
        return text

    def name(self, element):
        self.log.info("Getting NAME of an Element...")
        name = element.tag_name
        self.log.info("name= '{0}'".format(name))
        return name

    def attribute(self, element, attribute_name):
        self.log.info("Getting ATTRIBUTE ('{0}') of an Element...".format(attribute_name))
        attribute = element.get_attribute(self, attribute_name)
        self.log.info("{0}= '{1}'".format(attribute_name, attribute))
        return attribute

    def selected(self, element):
        self.log.info("Checking Element is_selected()")
        result = element.is_selected()
        self.log.info("is_selected= {0}".format(result))
        return result

    def enabled(self, element):
        self.log.info("Checking Element is_enabled()")
        result = element.is_enabled()
        self.log.info("is_enabled= {0}".format(result))
        return result

    def displayed(self, element):
        self.log.info("Checking Element is_displayed()")
        result = element.is_displayed()
        self.log.info("is_displayed= {0}".format(result))
        return result

    def location(self, element):
        self.log.info("Checking Element location...")
        location = element.location
        self.log.info("location= {0}".format(location))
        return location

    def size(self, element):
        self.log.info("Checking Element size...")
        size = element.size
        self.log.info("size= '{0}'".format(size))
        return size

    def rect(self, element):
        self.log.info("Checking Element rect (x,y,h,w)...")
        rect = element.rect
        self.log.info("rect= '{0}'".format(rect))
        return rect

    def css_property(self, element, property_name):
        self.log.info("Checking Element css_property...")
        css_property = element.value_of_css_property(self, property_name)
        self.log.info("css_property= '{0}'".format(css_property))
        return css_property
