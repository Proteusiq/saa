from dataclasses import dataclass
from saa.core.language import Luga

@dataclass(init=False, eq=False, repr=False, frozen=False)
class Deutsch(Luga):
    time = {
        "to": "{minute} {time_indicator} vor {hour} Uhr",
        "past": "{minute} {time_indicator} nach {hour} Uhr",
        0: "{hour} Uhr",
        15: "Viertel nach {hour}",
        45: "Viertel vor {hour}",
        30: "Halb {hour}",
    }
    number_connector = "und"
    connect_format = "{0}{1}{2}"
    numbers = {
        0: "null",
        1: "ein",   # ein und zwanzig /  eine Minute / ein Uhr
        2: "zwei",
        3: "drei",
        4: "vier",
        5: "fünf",
        6: "sechs",
        7: "sieben",
        8: "acht",
        9: "neun",
        10: "zehn",
        11: "elf",
        12: "zwölf",
        13: "dreizehn",
        14: "vierzehn",
        15: "fünfzehn",
        16: "sechzehn",
        17: "siebzehn",
        18: "achtzehn",
        19: "neunzehn",
        20: "zwanzig",
        30: "dreißig",
        40: "vierzig",
        50: "fünfzig",
    }

    @staticmethod
    def time_logic(hour, minute) -> tuple[int, int, str, str]:
        if minute in [0, 15, 30, 45]:
            if minute == 45 or minute == 30:
                hour += 1
            return (hour, minute, '', '')  

        is_to = "to" if minute > 30 else "past"
        time_indicator = "Minuten" if minute not in [1,59] else "Minute"

        if is_to == "to":
            hour += 1
            minute = 60 - minute

        if minute <= 20 or minute == 30 or minute == 40 or minute == 50:   
            if minute == 1:  
                minute = Deutsch.numbers[minute][1] if is_to == 'to' else Deutsch.numbers[minute][0]
            else:
                minute = Deutsch.numbers[minute]
        else:
            tens = minute // 10 * 10
            ones = minute % 10
            minute = Deutsch.connect_format.format(Deutsch.numbers[ones], Deutsch.number_connector, Deutsch.numbers[tens])

        hour = Deutsch.numbers[hour]

        return hour, minute, is_to, time_indicator


    @staticmethod
    def post_logic(hour, minute, is_to, time_indicator) -> str:
        if is_to:  
            return Deutsch.time[is_to].format(minute=minute, time_indicator=time_indicator, hour=hour)
        else:  
            return Deutsch.time[minute].format(hour=hour)
        
class Language(Deutsch):
    pass


