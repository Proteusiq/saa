from datetime import time, datetime
from functools import singledispatchmethod
from typing import Union
from saa.core.clock import Clock
from saa.core.plugins import supported_languages

SUPPORTED_LANGUAGES = [luga for luga in supported_languages.keys()]
TimeType = Union[str, time, datetime]

class Watch:

    def __init__(self, language:str):
        if language not in SUPPORTED_LANGUAGES:
            raise ValueError(f"{language} not yet supported")
        
        self.language = supported_languages.get(language)

    @singledispatchmethod
    def inputs(self, _:TimeType) -> time:
        raise NotImplementedError
    
    @inputs.register(str)
    def _(self, time:str) -> time:
        return datetime.strptime(time, "%H:%M").time()
        
    @inputs.register(datetime)
    def _(self, time:datetime) -> time:
        return time.time()
    
    @inputs.register(time)
    def _(self, time:time) -> time:
        return time
    
    def convert(self, time:TimeType) -> str:
        clock = Clock(self.language)
        time = self.inputs(time)
        return clock(time)

    def __call__(self, time:TimeType) -> str:
        return self.convert(time)




