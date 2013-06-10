import os
from common import AppiumTestCase


class AppiumIOSTestCase(AppiumTestCase):

    def setUp(self):
        app = os.path.join(os.path.dirname(__file__), "..", "..", "apps",
                           "SauceDashboard.app.zip")
        self.desired_caps = {
            'device': 'iPhone Simulator',
            'platform': 'Mac 10.8',
            'app': app,
            'version': '6.1',
        }
        AppiumTestCase.setUp(self)

    def test_iphone_app(self):
        uname = self.driver.find_element_by_name("userName")
        uname.send_keys("badusername")
        password = self.driver.find_element_by_name("userPassword")
        password.send_keys("badpassword")
        self.driver.find_element_by_tag_name("button").click()
        self.driver.switch_to_alert().accept()