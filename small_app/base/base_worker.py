import os
from abc import ABCMeta, abstractmethod
from selenium import webdriver

from konfig import Config
from dataclass.user_data import UserConfigData, FilterData


class BaseWorker(metaclass=ABCMeta):
    def __init__(self, conf: str = None, filter_data: FilterData = None):
        self.conf = conf
        self.__driver = None
        self.user_data: UserConfigData = None
        self.filter_data = filter_data

    @property
    def conf(self):
        return self.__conf

    @conf.setter
    def conf(self, value: str = "conf.ini"):
        user_info: dict = Config(os.path.join(os.getcwd(), "small_app/") + value).get_map("user")
        if user_info:
            self.user_data = UserConfigData(**user_info)
            print(self.user_data)
            self.set_driver(self.user_data.driver)

    def set_driver(self, value):
        if value == "chrome":
            self.__driver = webdriver.Chrome("/usr/local/bin/chromedriver")
            self.__driver.implicitly_wait(self.user_data.waiting_seconds)
        print(f"{value} driver is ready")

    # @abstractmethod
    # def go_to_login(self):
    #     pass

    # @abstractmethod
    # def enter_information(self):
    #     pass

    # @abstractmethod
    # def execute(self):
    #     pass
