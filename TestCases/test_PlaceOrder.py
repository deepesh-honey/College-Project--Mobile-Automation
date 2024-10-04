import time

import pytest

from Pages.ListingPage import ListingPage
from Pages.LoginScreen import LoginScreen
from Pages.HomeScreen import HomePage
from Pages.CartPaymentScreen import CartToPayment
from Pages.ProductDetailPage import ProductDetailPage
from Pages.ValidateOrder import ThankYouPage
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider
from Pages.MyOrderPage import MyOrders

class Test_PlaceOrder(BaseTest):

    @pytest.mark.parametrize("searchItem, productName, validateCartItem",dataProvider.get_data("searchData"))
    def test_placeOrder(self, searchItem, productName, validateCartItem):

        #Search Item:
        home = HomePage(self.driver)
        home.searchItem(searchItem)

        #Tap on that Item:
        listingPage = ListingPage(self.driver)
        listingPage.tapOnProduct(productName)

        #Navigate to cart:
        productDetailPage = ProductDetailPage(self.driver)
        productDetailPage.navigateToCart()

        #Cart & Payment Flow:
        payment = CartToPayment(self.driver)
        payment.proceedToPayment(validateCartItem)

        #Thank You Page:
        validateOrder = ThankYouPage(self.driver)
        validateOrder.validateThankYouPage()


    @pytest.mark.parametrize("cancelProductName, validateCanceledProductName", dataProvider.get_data("cancelProductData"))
    def test_cancelOrder(self,cancelProductName, validateCanceledProductName):

        navigateTo_MyOrderPage = ThankYouPage(self.driver)
        navigateTo_MyOrderPage.navigateToMyorders()

        myorderPage = MyOrders(self.driver)
        myorderPage.cancelOrder(cancelProductName)

        validateCacelOrder = MyOrders(self.driver)
        validateCacelOrder.validateCanceledOrder(validateCanceledProductName)









