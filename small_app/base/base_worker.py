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
    def conf(self, value: str = "conf.ini"):
        user_info: dict = Config(os.path.join(os.getcwd(), "small_app/") + value)
        if user_info:
            self.user_data = UserData(**user_info)

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
