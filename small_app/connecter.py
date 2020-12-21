import string
from selenium import webdriver
import selenium

from konfig import Config
import os


class Connecter:
    WAITTING_SECONDS = 15

    def __init__(self, target_url):
        self.target_url = target_url
        self.driver: selenium = "chrome"
        self.user_info = Config(os.path.join(os.getcwd(), "small_app/") + "conf.ini")

    @property
    def driver(self):
        return self.__driver

    @driver.setter
    def driver(self, value):
        if value == "chrome":
            self.__driver = webdriver.Chrome("/usr/local/bin/chromedriver")
            self.__driver.implicitly_wait(self.WAITTING_SECONDS)
        print(f"{value} driver is ready")

    @property
    def user_info(self):
        return self.__user_info

    @user_info.setter
    def user_info(self, value):
        user = value.get_map("user")
        print(f"login_info : {user}")
        self.__user_info = user

    def get_elem_by_xpath(self, xpath: str) -> selenium.webdriver.remote.webelement.WebElement:
        try:
            return self.driver.find_element_by_xpath(xpath)
        except Exception as e:
            print(f"[Error] {e}")
            return None

    def execute(self):
        self.driver.get(self.target_url)

        self.do_login()
        self.type_email_password()

        close_xpath = '//*[@id="__BVID__261___BV_modal_body_"]/div[1]'
        self.close_pop_up(close_xpath)

        request_list = '//*[@id="app-body"]/div/div[3]/div/ul'
        request_list = self.get_elem_by_xpath(request_list).find_elements_by_tag_name("li")

        self.filter_requests(request_list)
        return self.driver.quit()

    def filter_requests(self, requests: list):
        for index, request in enumerate(requests):
            print(f"{index + 1} 번째 request")
            request.click()
            try:
                self.close_pop_up('//*[@id="quote-consulting-tutorial___BV_modal_header_"]/button')
            except Exception as e:
                print("pop up 없음")
            import ipdb

            ipdb.set_trace()
            # self.go_back()
            # self.delete_request_item()

            break

    def check_words(self):
        xpath = '//*[@id="app-body"]/div/div/div[1]/div/div[5]/ul'
        elem = self.get_elem_by_xpath(xpath)
        item_to_learn = elem.find_elements_by_tag_name("p")[1].text

    def delete_request_item(self, xpath=None):
        delete_btn_xpath = '//*[@id="app-body"]/div/div[3]/div/ul/li[1]/div/a/div[2]/div[5]/span[2]'
        self.click(delete_btn_xpath)
        delete_confirm_xpath = "/html/body/div[5]/div/div[3]/button[1]"
        self.click(delete_confirm_xpath)

    def go_back(self):
        self.driver.execute_script("window.history.go(-1)")

    def close_pop_up(self, xpath: str):
        elem = self.get_elem_by_xpath(xpath)
        elem.click()

    def do_login(self):
        login_xpath = '//*[@id="app-header"]/div[3]/ul/li[4]/a'
        login_btn = self.get_elem_by_xpath(login_xpath)
        login_btn.click()

    def type_email_password(self):
        email_xpath = '//*[@id="__BVID__229"]'
        email_input = self.get_elem_by_xpath(email_xpath)
        email_input.send_keys(self.__user_info.get("email", "empty"))

        pwd_xpath = '//*[@id="__BVID__231"]'
        pwd_input = self.get_elem_by_xpath(pwd_xpath)
        pwd_input.send_keys(self.__user_info.get("password", "pwd"))

        login_submit_elem = self.get_elem_by_xpath(
            '//*[@id="app-body"]/div/div/form/div/div[4]/button'
        )
        login_submit_elem.click()

    def click(self, xpath: str):
        elem = self.get_elem_by_xpath(xpath)
        elem.click()

