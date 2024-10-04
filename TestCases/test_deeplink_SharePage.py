import pytest

from Pages.CartPaymentScreen import CartToPayment
from Pages.HomeScreen import HomePage
from Pages.ValidateOrder import ThankYouPage
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider


class Test_DeeplinkShare(BaseTest):

    @pytest.mark.parametrize("searchItem", dataProvider.get_data("deeplinkProduct"))
    def test_placeOrder(self, searchItem):


        # HomePage:
        home = HomePage(self.driver)
        home.searchItem(searchItem)


