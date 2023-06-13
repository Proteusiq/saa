from saa.core.numbers import Converter




class TimeLogic:
    def __init__(self, language):

        self.language = language

    def __call__(self, hour, minute):
        return self.convert(hour, minute)

    def convert(self, hour, minute):

        time_logic = self.language.time_logic
        time = self.language.time
        
        if minute in time:
            return time[minute].format(minute=minute)
        else:
            hour, minute, is_to = time_logic(hour, minute)

            return time[is_to].format(hour=hour, minute=minute)


class Clock:
    def __init__(self, time, language):
        self.hour = time.hour
        self.minute = time.minute
        self.language = language
        self.converter = Converter(language)

    def read(self, raw=False):
 
        if raw:
            return f"{self.converter(self.hour)} {self.converter(self.minute)}"

        t = TimeLogic(self.language)(self.hour, self.minute)
        
        print(t)

    def __repr__(self):
        g = self._task(raw=False)
        return f"{g}"


if __name__ == "__main__":

    from saa.luga import English, Danish
    from datetime import datetime

    NUMBER = 59
    say = Converter(language=English)
    print(say(NUMBER))

    now = datetime.now().time()
    print(f"It is {now}")

    saa = Clock(time=now, language=English)
    print(saa.read(raw=False))


    # say = Converter(language=Danish)
    # print(say(NUMBER))