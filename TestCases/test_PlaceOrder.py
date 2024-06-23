import time

import pytest

from Pages.LoginScreen import LoginScreen
from Pages.HomeScreen import HomePage
from Pages.CartPaymentScreen import CartToPayment
from Pages.ValidateOrder import ThankYouPage
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider


class Test_PlaceOrder(BaseTest):

    @pytest.mark.parametrize("searchItem, productName",dataProvider.get_data("searchData"))
    def test_placeOrder(self, searchItem, productName):
        #Login Flow: Marked commented.
        #login = LoginScreen(self.driver)
        #login.LoginUser()

        #HomePage:
        home = HomePage(self.driver)
        home.searchItem(searchItem, productName)

        #Cart & Payment Flow:
        payment = CartToPayment(self.driver)
        payment.proceedToPayment()

        #Thank You Page:
        validateOrder = ThankYouPage(self.driver)
        validateOrder.validateThankYouPage()



