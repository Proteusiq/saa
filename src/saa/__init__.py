from importlib import metadata

from saa.clock import Clock

__version__ = metadata.version(__package__)  # type: ignore # it is a string
__all__ = [
    "Clock",
]
