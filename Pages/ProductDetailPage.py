import time

from appium.webdriver.common.appiumby import AppiumBy

from Pages.BasePage import BasePage
from Utilities import configReader
from Utilities.scroll_util_88 import ScrollUtil

class ProductDetailPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigateToCart(self):
        #Navigate to Cart:
        ScrollUtil.scrollToTextByAndroidUiAutomator("Add to Cart", self.driver)

        time.sleep(2)
        try:
            self.click("navigateCart_XPATH")
        except:
            pass

        self.wait_click("directNavigateCart_ID", 20)


    def shareDeeplink(self, sharePlatform, personNameToShare, productName):
        #Share page:
        self.wait_click("shareBtn_XPATH", 20)
        self.wait_click("moreBtn_XPATH", 20)

        time.sleep(10)
        shareOptions = self.driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.TextView')
        for option in shareOptions:
            if option.text == sharePlatform:
                option.click()
                time.sleep(5)
                break

        self.wait_click('search_1_XPATH', 10)
        self.type('searchPerson_CLASS_NAME', personNameToShare)
        self.wait_click('selectPerson1_XPATH', 20)
        self.wait_click('sendBtn_XPATH', 20)
        self.wait_click('sendBtn_XPATH', 20)

        #Switch to Whatsapp:
        self.switchApp('com.whatsapp','com.whatsapp.HomeActivity')
        self.wait_click('search_2_ID', 10)
        self.type('searchPerson_CLASS_NAME', personNameToShare)
        self.wait_click('selectPerson2_XPATH', 20)
        self.wait_click('sharedLink_XPATH',20)
        self.wait_click('assertProductName_XPATH',20)
        product = self.getText('assertProductName_XPATH')
        actualName = productName
        assert product in actualName
