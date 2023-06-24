class TemplateLogic:
    def __init__(self, language):
        self.language = language

    def __call__(self, hour, minute):
        return self.convert(hour, minute)

    def convert(self, hour, minute):
        time_logic = self.language.time_logic
        time = self.language.time

        if minute in time:
            hour, *_, time_indicator = time_logic(hour, minute)
            return hour, minute, time[minute].replace("time_indicator", time_indicator)
        else:
            hour, minute, is_to, time_indicator = time_logic(hour, minute)

            return hour, minute, time[is_to].replace("time_indicator", time_indicator)
