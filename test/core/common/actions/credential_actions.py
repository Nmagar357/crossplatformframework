import datetime
import re
import string

class CredentialActions:

    def __init__(self):
        self.name = __class__.__name__


    def convert_base_email_to_unique_address(self, email_address):
        """
        Allows you to use a common base email account for tests that require each test run to use a unique email
        address. Function takes base email address, splits it with "@" sign, and appends "+<datetime_string>"
        between "user_name" and "address" string.
        Use:
            BASE_EMAIL = "neil.norton@gmail.com"
            test_email = convert_base_email_to_unique_address(BASE_EMAIL)
        Args:
            email_address: str() -> Base email address string to use
        Returns:
            str(),
                "some.user@nytimes.com"     -->     "some.user+20231214123455@nytimes.com"
                "nyt@gmail.com"             -->     "nyt+202201230808123@gmail.com"
        """
        prepend = email_address.split("@")[0]
        append = email_address.split("@")[1]
        date_string = str(datetime.datetime.now())[:-3]
        exclude = set(string.punctuation)
        date_string = ''.join(ch for ch in date_string if ch not in exclude)
        date_string = re.sub(r"\s+", '_', date_string)
        result_email = "{0}+{1}@{2}".format(prepend, date_string, append)
        return result_email