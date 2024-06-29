import time

from Pages.BasePage import BasePage

class CartToPayment(BasePage):

    def proceedToPayment(self,validateCartItem):

        #ValidateCart
        item_name = self.getText("validateCart_ANDROID_UIAUTOMATOR")
        print(item_name)
        validText = (validateCartItem)
        assert validText in item_name

        #SelectDeliveryAddress:
        self.wait_click("proceedCart_XPATH",20)
        try:
            self.wait_click("deliverAddress_XPATH",20)
        except:
            pass

        #PaymentandPlaceOrder:
        try:
            self.wait_click("continuePayment_XPATH",20)
        except:
            pass

        self.wait_click("placeOrder_XPATH",20)
