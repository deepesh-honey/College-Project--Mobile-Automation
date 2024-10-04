import time

from Pages.BasePage import BasePage
from Utilities.scroll_util_88 import ScrollUtil


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def searchItem(self, searchItem):

        #SearchItem:
        self.wait_click("search_field_ID", 20)
        self.type("search_bar_ID",searchItem)
        self.driver.press_keycode(66)







