import time

from Pages.LoginScreen import LoginScreen
from Pages.HomeScreen import HomePage
from Pages.CartPaymentScreen import CartToPayment
from Pages.ValidateOrder import ThankYouPage
from TestCases.BaseTest import BaseTest


class Test_PlaceOrder(BaseTest):

    def test_placeOrder(self):
        #Login Flow:
        #login = LoginScreen(self.driver)
        #login.LoginUser()

        #HomePage:
        home = HomePage(self.driver)
        home.searchItem()

        #Cart & Payment Flow:
        payment = CartToPayment(self.driver)
        payment.proceedToPayment()

        #Thank You Page:
        validateOrder = ThankYouPage(self.driver)
        validateOrder.validateThankYouPage()



