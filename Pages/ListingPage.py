import time

from Pages.BasePage import BasePage
from Utilities.scroll_util_88 import ScrollUtil


class ListingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def tapOnProduct(self, productName):
        #ScrollItem:
        ScrollUtil.scrollToTextByAndroidUiAutomator(productName, self.driver)





