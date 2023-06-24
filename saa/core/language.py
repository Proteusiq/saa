from abc import abstractmethod, ABC, abstractproperty
from dataclasses import dataclass


@dataclass
class Luga(ABC):
    @abstractproperty
    def time(self) -> dict:
        pass

    @abstractproperty
    def number_connector(self) -> str:
        pass

    @abstractproperty
    def connect_format(self) -> str:
        pass

    @abstractproperty
    def numbers(self) -> dict[int, str]:
        pass

    @abstractmethod
    def time_logic(hour: int, minute: int) -> tuple[int, int, str, str]:
        pass

    @abstractmethod
    def post_logic(text: str) -> str:
        pass


class Language(Luga):
    """All language needs to be alias as Language"""
