import time

import allure
import pytest
from allure_commons.types import AttachmentType
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium import webdriver



#For Failed SS:
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep



#Single Device Execution:
@pytest.fixture(scope='function')
def setup_teardown_Single_Device(request):
    print('Starting Appium Server')
    print('Launching Application')
    appium_service = AppiumService()
    appium_service.start()

    desired_capabilities = dict(

        platforName = 'Android',
        deviceName = 'Android',
        automationName = 'UiAutomator2',
        udid = 'R5CT12YXKSH',
        appActivity='com.amazon.mShop.home.HomeActivity',
        appPackage='in.amazon.mShop.android.shopping',
        #app = str(Path().absolute().parent) + '\\Apk\\amazon.apk',
        newCommandTimeout = 60000,
        noReset = True
    )

    capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)
    driver = webdriver.Remote('http://127.0.0.1:4723', options= capabilities_options)
    driver.implicitly_wait(10)

    request.cls.driver = driver

    yield driver
    print('Closing Application')

    time.sleep(2)
    #driver.quit()
    appium_service.stop()
    print('Closing Appium Server')



#For Failed SS:
@pytest.fixture()
def failure_test_ss(request, setup_teardown_Single_Device):
    yield
    item = request.node
    driver = setup_teardown_Single_Device
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)




#Parallel test Execution conftest file;

@pytest.fixture(params=["device1", "device2"], scope='module')
def setup_teardown_ParallelDevice(request):
    print('Starting Appium Server')
    print('Launching Application')
    global appium_service
    appium_service = AppiumService()
    appium_service.start()

    if request.param == "device1":  #It is used to configure for Setup request of device:1

        desired_capabilities = dict(
            platforName = 'Android',
            deviceName = 'Android',
            udid = 'emulator-5554',
            automationName = 'UiAutomator2',
            appPackage = 'com.goibibo',
            appActivity = 'com.goibibo.common.HomeActivity',
            noReset = True
        )


    if request.param == "device2":  # It is used to configure for Setup request of device:2

        desired_capabilities = dict(
            platforName='Android',
            deviceName='Android',
            udid='emulator-5556',
            automationName='UiAutomator2',
            appPackage='com.goibibo',
            appActivity='com.goibibo.common.HomeActivity',
            noReset=True
        )

    global driver
    capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)
    driver = webdriver.Remote('http://127.0.0.1:4723', options= capabilities_options)
    driver.implicitly_wait(10)

    yield driver
    print('Closing Application')

    time.sleep(2)
    driver.quit()
    appium_service.stop()
    print('Closing Appium Server')






