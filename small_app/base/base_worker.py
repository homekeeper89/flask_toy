import os
from abc import ABCMeta, abstractmethod
from konfig import Config
from dataclass.user_data import UserData


class BaseWorker(metaclass=ABCMeta):
    def __init__(self, conf: str = None):
        self.conf = conf

    @property
    def conf(self):
        return self.__conf

    @conf.setter
    def conf(self, value: str):
        user_info: dict = Config(os.path.join(os.getcwd(), "small_app/") + "conf.ini")
        if user_info:
            self.email = user_info.get("email")
            self.password = user_info.get("password")

    # @abstractmethod
    # def go_to_login(self):
    #     pass

    # @abstractmethod
    # def enter_information(self):
    #     pass

    # @abstractmethod
    # def set_driver(self):
    #     pass

    # @abstractmethod
    # def execute(self):
    #     pass
