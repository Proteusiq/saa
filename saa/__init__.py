from importlib import metadata
from saa.clock import Clock

__version__ = metadata.version(__package__)
__all__ = ("Clock",)
