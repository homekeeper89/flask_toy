from abc import ABCMeta, abstractmethod
from dataclass.user_data import UserData


class BaseWorker(metaclass=ABCMeta):
    def __init__(self, user_data: UserData):
        self.email = user_data.email
        self.password = user_data.password

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
