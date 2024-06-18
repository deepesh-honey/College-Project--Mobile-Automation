import time

from Pages.BasePage import BasePage

class ThankYouPage(BasePage):

    def validateThankYouPage(self):
        thankYou_Page = self.getText("thankYouPage_XPATH")
        print(thankYou_Page)
        validText = "Order placed, thank you!"
        assert validText in thankYou_Page

