from datetime import time, datetime
from functools import singledispatch
from typing import Union
from saa.core.watch import Watch
from saa.core.plugins import supported_languages

SUPPORTED_LANGUAGES = {luga for luga in supported_languages.keys()}
TimeType = Union[str, time, datetime]


@singledispatch
def inputs(_: TimeType) -> time:
    """Input Parser

    Accepts string, time or datetime and return time object

    Args:
        _ (TimeType): string, time or datetime object

    Raises:
        NotImplementedError: shell for dispatching

    Returns:
        time: python time object
    """
    raise NotImplementedError


@inputs.register(str)
def _(time: str) -> time:
    return datetime.strptime(time, "%H:%M").time()


@inputs.register(datetime)
def _(time: datetime) -> time:
    return time.time()


@inputs.register(time)
def _(time: time) -> time:
    return time


class Clock:
    def __init__(self, language: str):
        if language not in SUPPORTED_LANGUAGES:
            raise ValueError(f"{language} not yet supported")

        self.language = supported_languages.get(language)

    def convert(self, time: TimeType) -> str:
        """Transform time to spoken expressions

        Args:
            time (TimeType): string, time or datetime object

        Returns:
            str: spoken expressions
        """
        watch = Watch(self.language)
        time = inputs(time)
        return watch(time)

    def __call__(self, time: TimeType) -> str:
        return self.convert(time)
