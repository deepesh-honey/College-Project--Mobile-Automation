import time

from Pages.BasePage import BasePage

class CartToPayment(BasePage):

    def proceedToPayment(self):

        #ValidateCart
        item_name = self.getText("validateCart_ANDROID_UIAUTOMATOR")
        print(item_name)
        validText = "Sony SRS-XB100 Wireless Bluetooth Portable Lightweight Super-Compact Travel Speaker, Extra-Durable IP67 Waterproof & Dustproof, 16 Hrs Batt, Versatile Strap, Extra Bass & Hands-Free Calling-Black"
        assert validText in item_name

        #SelectDeliveryAddress:
        self.click("proceedCart_XPATH")
        try:
            time.sleep(3)
            self.click("deliverAddress_XPATH")
        except:
            pass

        #PaymentandPlaceOrder:
        try:
            time.sleep(3)
            self.click("continuePayment_XPATH")
        except:
            pass

        time.sleep(2)
        self.click("placeOrder_XPATH")
