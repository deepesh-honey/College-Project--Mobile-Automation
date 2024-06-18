import time

from Pages.BasePage import BasePage
from Utilities.scroll_util_88 import ScrollUtil


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def searchItem(self):

        #SearchItem:
        self.wait_click("search_field_ID", 20)
        self.type("search_bar_ID","Sony Speaker")
        self.driver.press_keycode(66)

        #ScrollItem:
        ScrollUtil.scrollToTextByAndroidUiAutomator("Sony SRS-XB100", self.driver)
        ScrollUtil.scrollToTextByAndroidUiAutomator("Add to Cart", self.driver)

        #Navigate to Cart:
        time.sleep(2)
        try:
            self.click("navigateCart_XPATH")
        except:
            pass

        #Direct Cart:
        self.wait_click("directNavigateCart_ID",20)





