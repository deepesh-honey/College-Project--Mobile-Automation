from appium.webdriver.common.appiumby import AppiumBy

class ScrollUtil:

    @staticmethod
    def scrollToTextByAndroidUiAutomator(text, driver):
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, ("new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains(\""+text+"\").instance(0))")).click()

    @staticmethod
    def swipeUp(howmanyswipes, driver):
        for i in range(1, howmanyswipes+1):
            driver.swipe(600, 1490, 680, 300, 1000)

    @staticmethod
    def swipeDown(howmanyswipes, driver):
        for i in range(1, howmanyswipes+1):
            driver.swipe(650, 1490, 780, 2000, 1000)

    @staticmethod
    def swipeRight(howmanyswipes, driver):
        for i in range(1, howmanyswipes + 1):
            driver.swipe(1100, 1300, 120, 1200, 1000)

    @staticmethod
    def swipeLeft(howmanyswipes, driver):
        for i in range(1, howmanyswipes + 1):
            driver.swipe(120, 600, 1100, 600, 1000)





