from saa.core.numbers import Converter
from saa.core.template import TemplateLogic


class Watch:
    def __init__(self, language):
        self.language = language
        self.converter = Converter(language)

    def __call__(self, time):
        return self.convert(hour=time.hour, minute=time.minute)

    def convert(self, hour, minute, raw=False):
        if raw:
            return f"{self.converter(hour)} {self.converter(minute)}"

        hour, minute, read_template = TemplateLogic(self.language)(hour, minute)

        if hour > 12:
            hour = hour - 12

        return self.language.post_logic(
            read_template.format(
                hour=self.converter(hour),
                minute=self.converter(minute),
            )
        )

    def __repr__(self):
        return self.convert(raw=True)
