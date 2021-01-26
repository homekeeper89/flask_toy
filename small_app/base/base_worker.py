import os
from abc import ABCMeta, abstractmethod
from selenium import webdriver

from konfig import Config
from dataclass.user_data import UserConfigData


class BaseWorker(metaclass=ABCMeta):
    def __init__(self, conf: str = None):
        self.conf = conf
        self.user_data = UserConfigData(**self.conf)
        self.driver = self.user_data.driver

    @property
    def conf(self):
        return self._conf

    @conf.setter
    def conf(self, value):
        self._conf = Config(os.path.join(os.getcwd(), "small_app/") + value).get_map("user")
        print(f"user_data [{self._conf}] is ready")

    @property
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self, value):
        if value == "chrome":
            self._driver = webdriver.Chrome("/usr/local/bin/chromedriver")
            self._driver.implicitly_wait(self.user_data.waiting_seconds)

        print(f"driver [{value}] is ready")

    @abstractmethod
    def go_to_login_page(self):
        pass

    @abstractmethod
    def type_login_information(self):
        pass

    @abstractmethod
    def execute(self):
        pass
