import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys

from Pages.BasePage import BasePage


class MyOrders(BasePage):
    def cancelOrder(self,cancelProductName):

        max_attempts = 3
        attempt = 0

        while attempt < max_attempts:
            try:
                self.wait_click("searchOrder_XPATH",20)
                self.clear_field("searchOrder_XPATH",20)

                self.type("searchOrder_XPATH",cancelProductName)
                self.driver.press_keycode(66)

                product_found = self.wait_click("selectItem_ANDROID_UIAUTOMATOR",20)
                if product_found:
                    break
            except TimeoutException:
                pass
            attempt += 1

        #ViewOrderDetails:
        self.wait_click("view_OrderDetails_XPATH",20)
        self.wait_click("cancelItem_XPATH",20)
        self.wait_click("checkedCancelItem_XPATH",20)


    def validateCanceledOrder(self, validateCanceledProductName):
        self.wait_click("filter_XPATH",20)
        self.wait_click("cancelFilter_XPATH",20)
        self.wait_click("applyFilter_XPATH",20)

        canceledProductName = self.getText("productName_XPATH")
        print(canceledProductName)
        validCancelOrderName = (validateCanceledProductName)
        assert validCancelOrderName in canceledProductName

        cancelTag = self.getText("cancelTag_XPATH")
        print(cancelTag)
        validCancelTag = ("Cancelled")
        assert validCancelTag in cancelTag







