import time

import pytest

from Pages.ListingPage import ListingPage
from Pages.LoginScreen import LoginScreen
from Pages.HomeScreen import HomePage
from Pages.CartPaymentScreen import CartToPayment
from Pages.CartPaymentScreen import EmptyCart
from Pages.ProductDetailPage import ProductDetailPage
from Pages.ValidateOrder import ThankYouPage
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider
from Pages.MyOrderPage import MyOrders
from Utilities.scroll_util_88 import ScrollUtil

class Test_PlaceOrder(BaseTest):

    @pytest.mark.parametrize("searchItem, productName, validateCartItem",dataProvider.get_data("placeOrderData"))
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


class Test_DiscountonProducts(BaseTest):

    @pytest.mark.parametrize("globalsearchProduct", dataProvider.get_data("globalSearchItem"))
    def test_discountOnProduct(self, globalsearchProduct):

        cart = EmptyCart(self.driver)
        cart.directNavigateToCart()

        searchItem = HomePage(self.driver)
        searchItem.searchItem(globalsearchProduct)


        listingPage = ListingPage(self.driver)
        listingPage.discountItemCheck()










