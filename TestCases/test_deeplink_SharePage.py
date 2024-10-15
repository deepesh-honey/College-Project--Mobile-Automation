import pytest


from Pages.HomeScreen import HomePage
from Pages.ListingPage import ListingPage
from Pages.ProductDetailPage import ProductDetailPage
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider


class Test_DeeplinkShare(BaseTest):

    @pytest.mark.parametrize("searchItem, productName, sharePlatform, personNameToShare", dataProvider.get_data("deeplinkProduct"))
    def test_deeplink(self, searchItem, productName, sharePlatform, personNameToShare):

        # HomePage:
        home = HomePage(self.driver)
        home.searchItem(searchItem)

        listingPage = ListingPage(self.driver)
        listingPage.tapOnProduct(productName)

        productDetailPage = ProductDetailPage(self.driver)
        productDetailPage.shareDeeplink(sharePlatform, personNameToShare, productName)

