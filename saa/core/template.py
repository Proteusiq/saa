class TemplateLogic:
    def __init__(self, language):
        self.language = language

    def __call__(self, hour, minute):
        return self.convert(hour, minute)

    def convert(self, hour, minute):
        time_logic = self.language.time_logic
        time = self.language.time

        if minute in time:
            hour, *_, is_minutes = time_logic(hour, minute)
            return hour, minute, time[minute].replace("is_minutes", is_minutes)
        else:
            hour, minute, is_to, is_minutes = time_logic(hour, minute)

            return hour, minute, time[is_to].replace("is_minutes", is_minutes)
