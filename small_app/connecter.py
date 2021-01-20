import os
import datetime
import time

from typing import List, Dict, Generator
from selenium import webdriver

from konfig import Config
from pathlib import Path

import selenium
from selenium.webdriver.support import expected_conditions as EC

from custom_element import CustomElement


class Connecter:

    WAITTING_SECONDS = 15
    SELECTED_COUNT, DELETED_COUNT = 0, 0

    def __init__(
        self,
        target_url,
        need_words: List[str] = [""],
        ben_words: List[str] = [""],
        delete_mode: bool = False,
    ):
        self.target_url = target_url
        self.driver: selenium = "chrome"
        self.user_info = Config(os.path.join(os.getcwd(), "small_app/") + "conf.ini")
        self.need_words: List[str] = need_words
        self.ben_words: List[str] = ben_words
        self.delete_mode = delete_mode

    @property
    def driver(self) -> selenium:
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

        close_xpath = '//*[@id="__BVID__265___BV_modal_body_"]/div[1]'
        self.close_pop_up(close_xpath)
        while True:
            scroll = self.infinity_scroll_generator()
            height = scroll.send(None)

            if not height:
                break

            request_list_xpath = '//*[@id="app-body"]/div/div[3]/div/ul'
            request_list = self.get_elem_by_xpath(request_list_xpath).find_elements_by_tag_name(
                "li"
            )
            request_list_with_name = [
                {"name": request.text.split("\n")[0], "elem": request} for request in request_list
            ]

            request_list_with_name = self.make_request_in_screen(request_list_with_name)

            self.filter_requests(request_list_with_name)
            try:
                scroll.send(height)
            except StopIteration:
                break

        now = datetime.datetime.now().strftime("%Y_%m_%d")
        print(
            f"{now} 총 요청 : {self.SELECTED_COUNT}, 선택갯수 : {self.SELECTED_COUNT - self.DELETED_COUNT} 삭제갯수 : {self.DELETED_COUNT}"
        )
        return self.driver.quit()

    def make_request_in_screen(self, requests) -> List:
        requests_in_screen = []
        for _, request in enumerate(requests):
            celm = CustomElement(self.driver, request.get("elem"))
            if celm.is_elem_in_screen():
                requests_in_screen.append(request)
        return requests_in_screen

    def infinity_scroll_generator(self, timeout: int = 1) -> Generator:
        scroll_pause_time = timeout
        while True:
            last_height = self.driver.execute_script("return document.body.scrollHeight")

            height = yield last_height
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            time.sleep(scroll_pause_time)

            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if height == new_height:
                return

    def filter_requests(self, requests: List[Dict]):
        for _, request in enumerate(requests):
            self.SELECTED_COUNT += 1
            elem = request.get("elem")

            try:
                message = elem.text
                message = message.replace("\n", " ").replace("삭제", "")
                self.check_words(message)
                self.make_log(message, "selected")
            except ValueError as v:
                if self.delete_mode:
                    self.delete_request_item(elem)
                self.make_log(message)

    def make_log(self, message: str, state: str = "delete"):
        now = datetime.datetime.now().strftime("%Y_%m_%d")
        file_path = os.getcwd() + "/small_app/log/" + now
        Path(file_path).mkdir(parents=True, exist_ok=True)

        today = f"{file_path}/[{state}]"
        with open(today, "a") as file:
            file.write(message + "\n")

    def check_words(self, message: str) -> bool:
        messages = message.replace(",", "").split(" ")
        if list(set(self.need_words) & set(messages)):
            return True
        raise ValueError(f"필요한 단어 {self.need_words} 가 존재하지 않음")

    def delete_request_item(self, request: selenium):
        try:
            request.find_element_by_class_name("quote-btn").click()
        except selenium.common.exceptions.ElementClickInterceptedException as e:
            print("클릭 불가능한 요청 사항 name", request.text.split("\n")[0], e)
            return request

        delete_confirm_xpath = "/html/body/div[5]/div/div[3]/button[1]"
        self.click(delete_confirm_xpath)
        self.DELETED_COUNT += 1
        return True

    def go_back(self):
        self.driver.execute_script("window.history.go(-1)")

    def close_pop_up(self, xpath: str):
        self.click(xpath)

    def click_login(self):
        login_xpath = '//*[@id="app-header"]/div[3]/ul/li[4]/a'
        self.click(login_xpath)

    def type_email_password(self):
        email_xpath = '//*[@id="__BVID__231"]'
        email_input = self.get_elem_by_xpath(email_xpath)
        email_input.send_keys(self.__user_info.get("email", "empty"))

        pwd_xpath = '//*[@id="__BVID__233"]'
        pwd_input = self.get_elem_by_xpath(pwd_xpath)
        pwd_input.send_keys(self.__user_info.get("password", "pwd"))

        login_submit_elem = self.get_elem_by_xpath(
            '//*[@id="app-body"]/div/div/form/div/div[4]/button'
        )
        login_submit_elem.click()

    def click(self, xpath: str):
        elem = self.get_elem_by_xpath(xpath)
        elem.click()


if __name__ == "__main__":
    url = "https://soomgo.com/"
    need_words = ["파이썬", "python"]
    ben_words = ["자바", "Java", "C언어", "c언어"]
    obj = Connecter(url, need_words, ben_words, delete_mode=True)

    obj.execute()
