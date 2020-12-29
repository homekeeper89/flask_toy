from typing import Generator, List
from selenium import webdriver
import selenium

from konfig import Config
import os
import datetime
import time


class Connecter:
    WAITTING_SECONDS = 15

    def __init__(self, target_url, need_words: List[str] = [""], ben_words: List[str] = [""]):
        self.target_url = target_url
        self.driver: selenium = "chrome"
        self.user_info = Config(os.path.join(os.getcwd(), "small_app/") + "conf.ini")
        self.need_words: List[str] = need_words
        self.ben_words: List[str] = ben_words

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

        self.click_login()
        self.type_email_password()

        close_xpath = '//*[@id="__BVID__261___BV_modal_body_"]/div[1]'
        self.close_pop_up(close_xpath)

        while True:
            scroll = self.infinity_scroll()
            height = scroll.send(None)

            if not height:
                break

            request_list = '//*[@id="app-body"]/div/div[3]/div/ul'
            request_list = self.get_elem_by_xpath(request_list).find_elements_by_tag_name("li")
            print(len(request_list))

            scroll.send(height)
        return

        # self.filter_requests(request_list)
        # return self.driver.quit()

    def infinity_scroll(self, timeout: int = 1) -> Generator:
        scroll_pause_time = timeout
        while True:
            last_height = self.driver.execute_script("return document.body.scrollHeight")

            height = yield last_height
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            time.sleep(scroll_pause_time)

            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if height == new_height:
                return

    def filter_requests(self, requests: list):
        for index, request in enumerate(requests):
            print(f"{index + 1} 번째 request")
            message = request.text
            try:
                self.check_words(message)
                self.make_log(message, "selected")
            except ValueError as v:
                print(v.args)
                self.make_log(message)

    def make_log(self, messages: str, state: str = "delete"):
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        today = f"[{state}]_" + now
        messages = messages.replace("\n", " ").replace("삭제", "")
        with open(today, "a") as file:
            file.write(messages + "\n")

    def check_words(self, message: str) -> bool:
        messages = message.replace(",", "").split(" ")
        if list(set(self.need_words) & set(messages)):
            return True
        raise ValueError(messages)

    def delete_request_item(self, xpath=None):
        delete_btn_xpath = '//*[@id="app-body"]/div/div[3]/div/ul/li[1]/div/a/div[2]/div[5]/span[2]'
        self.click(delete_btn_xpath)
        delete_confirm_xpath = "/html/body/div[5]/div/div[3]/button[1]"
        self.click(delete_confirm_xpath)

    def go_back(self):
        self.driver.execute_script("window.history.go(-1)")

    def close_pop_up(self, xpath: str):
        self.click(xpath)

    def click_login(self):
        login_xpath = '//*[@id="app-header"]/div[3]/ul/li[4]/a'
        self.click(login_xpath)

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

