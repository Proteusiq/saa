from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Luga(ABC):
    time: ClassVar[dict]
    number_connector: ClassVar[str]
    connect_format: ClassVar[str]
    numbers: ClassVar[dict[int, str]]

    @staticmethod
    @abstractmethod
    def time_logic(hour: int, minute: int) -> tuple[int, int, str, str]: ...

    @staticmethod
    @abstractmethod
    def post_logic(text: str) -> str: ...


class Language(Luga):
    """All language needs to be alias as Language"""
