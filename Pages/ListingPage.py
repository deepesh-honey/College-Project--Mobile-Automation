import time

from Pages.BasePage import BasePage
from Utilities.scroll_util_88 import ScrollUtil
from appium.webdriver.common.appiumby import AppiumBy


class ListingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def tapOnProduct(self, productName):
        #ScrollItem:
        ScrollUtil.scrollToTextByAndroidUiAutomator(productName, self.driver)


    def discountItemCheck(self):

        previous_page_source = ''
        current_page_source = self.driver.page_source

        while current_page_source != previous_page_source:
            previous_page_source = current_page_source

            allItemNames = self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[contains(@text, '% off')]")

            for item in allItemNames:
                print(item.text)
                dicountTag = item.text
                if '% off' in dicountTag:
                    time.sleep(1)
                else:
                    print('No discount available')

            try:
                self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollForward()' )

            except Exception as e:
                print("Reached the end of the list.")
                break

            time.sleep(2)
            current_page_source = self.driver.page_source











