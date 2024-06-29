from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities import configReader
from Utilities.LogsUtil import Logger
import logging
log = Logger(__name__, logging.INFO)

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(AppiumBy.XPATH, configReader.readConfig("locators", locator)).click()

        elif str(locator).endswith("_ACCESSIBILITY_ID"):
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, configReader.readConfig("locators", locator)).click()

        elif str(locator).endswith("_ANDROID_UIAUTOMATOR"):
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, configReader.readConfig("locators", locator)).click()

        elif str(locator).endswith("_ID"):
            self.driver.find_element(AppiumBy.ID, configReader.readConfig("locators", locator)).click()

        elif str(locator).endswith("_CLASS_NAME"):
            self.driver.find_element(AppiumBy.CLASS_NAME, configReader.readConfig("locators", locator)).click()


        log.logger.info("Clicking on a Element "+ str(locator))

    def clickIndex(self, locator, index):
        if str(locator).endswith("_XPATH"):
            self.driver.find_elements(AppiumBy.XPATH, configReader.readConfig("locators", locator))[index].click()

        elif str(locator).endswith("_ACCESSIBILITY_ID"):
            self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, configReader.readConfig("locators", locator))[index].click()

        elif str(locator).endswith("_ANDROID_UIAUTOMATOR"):
            self.driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, configReader.readConfig("locators", locator))[index].click()

        elif str(locator).endswith("_ID"):
            self.driver.find_elements(AppiumBy.ID, configReader.readConfig("locators", locator))[index].click()

        log.logger.info("Clicking on a Element "+ str(locator) + "with index : " +str(index))


    def type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(AppiumBy.XPATH, configReader.readConfig("locators", locator)).send_keys(value)

        elif str(locator).endswith("_ACCESSIBILITY_ID"):
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, configReader.readConfig("locators", locator)).send_keys(value)

        elif str(locator).endswith("_ANDROID_UIAUTOMATOR"):
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, configReader.readConfig("locators", locator)).send_keys(value)

        elif str(locator).endswith("_ID"):
            self.driver.find_element(AppiumBy.ID, configReader.readConfig("locators", locator)).send_keys(value)

        elif str(locator).endswith("_CLASS_NAME"):
            self.driver.find_element(AppiumBy.CLASS_NAME, configReader.readConfig("locators", locator)).send_keys(value)

        log.logger.info("Clicking on a Element "+ str(locator) + "entered the value as : " + str(value))


    def getText(self, locator):
        if str(locator).endswith("_XPATH"):
            return self.driver.find_element(AppiumBy.XPATH, configReader.readConfig("locators", locator)).text

        elif str(locator).endswith("_ACCESSIBILITY_ID"):
            return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, configReader.readConfig("locators", locator)).text

        elif str(locator).endswith("_ANDROID_UIAUTOMATOR"):
            return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, configReader.readConfig("locators", locator)).text

        elif str(locator).endswith("_ID"):
            return self.driver.find_element(AppiumBy.ID, configReader.readConfig("locators", locator)).text

        #log.logger.info("Clicking on a Element "+ str(locator))


    def wait_click(self, locator, timeout):

        if str(locator).endswith("_XPATH"):
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((AppiumBy.XPATH, configReader.readConfig("locators", locator)))).click()

        elif str(locator).endswith("_ACCESSIBILITY_ID"):
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, configReader.readConfig("locators", locator)))).click()

        elif str(locator).endswith("_ANDROID_UIAUTOMATOR"):
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, configReader.readConfig("locators", locator)))).click()

        elif str(locator).endswith("_ID"):
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((AppiumBy.ID, configReader.readConfig("locators", locator)))).click()

        log.logger.info("Clicking on a Element "+ str(locator))

    def clear_field(self, locator, timeout):

        if str(locator).endswith("_XPATH"):
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, configReader.readConfig("locators", locator)))).clear()

        elif str(locator).endswith("_ACCESSIBILITY_ID"):
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, configReader.readConfig("locators", locator)))).clear()

        elif str(locator).endswith("_ANDROID_UIAUTOMATOR"):
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR, configReader.readConfig("locators", locator)))).clear()

        elif str(locator).endswith("_ID"):
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((AppiumBy.ID, configReader.readConfig("locators", locator)))).clear()

        log.logger.info("Clicking on a Element " + str(locator))

