import string
from selenium import webdriver
import requests
import selenium


class Connecter:
    WAITTING_SECONDS = 15

    def __init__(self, target_url):
        self.target_url = target_url
        self.driver: selenium = "chrome"

    @property
    def driver(self):
        return self.__driver

    @driver.setter
    def driver(self, value):
        if value == "chrome":
            self.__driver = webdriver.Chrome("/usr/local/bin/chromedriver")
            self.__driver.implicitly_wait(self.WAITTING_SECONDS)
        print(f"{value} driver is ready")

    def get_elem_by_xpath(xpath: string):
        try:
            return self.driver.find_element_by_xpath(xpath)
        except Exception as e:
            print(f"[Error] {e}")
            return None

    def execute(self):
        self.driver.get(self.target_url)

        self.do_login()
        self.type_email_password()

        return self.driver.quit()

    def do_login(self):
        login_xpath = '//*[@id="app-header"]/div[3]/ul/li[4]/a'
        login_btn = self.get_elem_by_xpath(login_xpath)
        login_btn.click()

    def type_email_password(self):
        email_xpath = '//*[@id="__BVID__229"]'
        email_input = self.get_elem_by_xpath(email_xpath)
        email_input.send_keys("kkk")

        pwd_xpath = '//*[@id="__BVID__231"]'
        pwd_input = self.get_elem_by_xpath(pwd_xpath)
        pwd_input.send_keys("kk")

        login_submit_elem = self.get_elem_by_xpath(
            '//*[@id="app-body"]/div/div/form/div/div[4]/button'
        )
        login_submit_elem.click()
