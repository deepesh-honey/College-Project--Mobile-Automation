import time
from Pages.BasePage import BasePage
from Utilities.scroll_util_88 import ScrollUtil

class ProductDetailPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def navigateToCart(self):
        # Navigate to Cart:
        ScrollUtil.scrollToTextByAndroidUiAutomator("Add to Cart", self.driver)

        time.sleep(2)
        try:
            self.click("navigateCart_XPATH")
        except:
            pass

        self.wait_click("directNavigateCart_ID", 20)



