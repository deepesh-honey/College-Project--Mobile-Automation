import time

from Pages.BasePage import BasePage


class LoginScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    def LoginUser(self):

        #Launch Screen:
        self.wait_click("allow_notification_ID","40")
        self.click("select_language_ACCESSIBILITY_ID")
        self.click("submit_language_selection_ID")
        try:
            self.click("skip_signin_ID")
        except:
            pass

        #Login Flow:
        self.click("account_ANDROID_UIAUTOMATOR")
        time.sleep(18)
        self.click("signin_ACCESSIBILITY_ID")

        #Credential:
        time.sleep(4)
        self.type("email_CLASS_NAME","Pate your Username")
        time.sleep(2)
        self.click("continue_btn_CLASS_NAME")
        time.sleep(4)
        self.type("pass_CLASS_NAME", "Paste your Password")
        time.sleep(2)
        self.click("continue_btn_CLASS_NAME")

        #Home:
        self.click("click_ANDROID_UIAUTOMATOR")






