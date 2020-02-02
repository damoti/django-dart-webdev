import sys
from time import sleep

import pexpect
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver, Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


class MySeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver(options=chrome_options)
        cls.selenium.implicitly_wait(10)
        cls.webdev = pexpect.spawn('webdev serve', cwd='dart_test_app')
        cls.webdev.logfile = sys.stdout.buffer
        cls.webdev.expect('Succeeded', timeout=90)

    @classmethod
    def tearDownClass(cls):
        cls.webdev.terminate(True)
        cls.selenium.quit()
        super().tearDownClass()

    def test_dart_is_running(self):
        self.selenium.get(self.live_server_url)
        output = self.selenium.find_element_by_id("output")
        sleep(3)
        self.assertEqual(output.text, 'Your Dart app is running.')
