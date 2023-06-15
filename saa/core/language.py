from abc import abstractmethod, ABC, abstractproperty
from dataclasses import dataclass


@dataclass
class Luga(ABC):
    @abstractproperty
    def time(self):
        pass

    @abstractproperty
    def number_connector(self):
        pass

    @abstractproperty
    def connect_format(self):
        pass

    @abstractproperty
    def numbers(self):
        pass

    @abstractmethod
    def time_logic(self):
        pass

    @abstractmethod
    def post_logic(text: str) -> str:
        pass


class Language(Luga):
    """All language needs to be alias as Language"""
