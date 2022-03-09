from abc import ABC, abstractmethod


class Login(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def singout(self):
        pass
