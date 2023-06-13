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

        
        return read_template.format(hour=self.converter(hour), minute=self.converter(minute),)

    def __repr__(self):
        g = self._task(raw=False)
        return f"{g}"


if __name__ == "__main__":
    from saa.luga import English
    from datetime import datetime


    now = datetime.now().time()
    print(f"It is {now}")

    saa = Clock(time=now, language=English)
    print(saa.read(raw=False))

    # say = Converter(language=Danish)
    # print(say(NUMBER))
