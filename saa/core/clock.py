from saa.core.numbers import Converter
from saa.core.template import TemplateLogic


class Clock:
    def __init__(self, time, language):
        self.hour = time.hour
        self.minute = time.minute
        self.language = language
        self.converter = Converter(language)

    def read(self, raw=False):
        if raw:
            return f"{self.converter(self.hour)} {self.converter(self.minute)}"

        hour, minute, read_template = TemplateLogic(self.language)(self.hour, self.minute)

        
        return self.language.post_logic(read_template.format(hour=self.converter(hour), minute=self.converter(minute),))

    def __repr__(self):

        raw_time = self._task(raw=True)
        return raw_time


