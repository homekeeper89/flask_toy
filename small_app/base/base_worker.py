from abc import ABCMeta, abstractmethod


class BaseWorker(metaclass=ABCMeta):
    @abstractmethod
    def register_information(self):
        pass

    @abstractmethod
    def go_to_login(self):
        pass

    @abstractmethod
    def enter_information(self):
        pass

    @abstractmethod
    def set_driver(self):
        pass

    @abstractmethod
    def execute(self):
        pass
