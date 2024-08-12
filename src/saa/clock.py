from datetime import datetime, time
from functools import singledispatch
from typing import Union

from saa.core.plugins import supported_languages
from saa.core.watch import Watch

SUPPORTED_LANGUAGES = {luga for luga in supported_languages}
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
def _(t: str) -> time:
    return datetime.strptime(t, "%H:%M").time()


@inputs.register(datetime)
def _(t: datetime) -> time:
    return t.time()


@inputs.register(time)
def _(t: time) -> time:
    return t


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
