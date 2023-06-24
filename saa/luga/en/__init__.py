from dataclasses import dataclass
from saa.core.language import Luga


@dataclass(init=False, eq=False, repr=False, frozen=False)
class English(Luga):
    time = {
        "to": "{minute} time_indicator to {hour}",
        "past": "{minute} time_indicator past {hour}",
        0: "{hour} o'clock",
        15: "quarter past {hour}",
        45: "quarter to {hour}",
        30: "half past {hour}",
    }
    number_connector = "and"
    connect_format = "{0} {2}"
    numbers = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eightteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
    }

    @staticmethod
    def time_logic(hour, minute) -> tuple[int, int, str, str]:
        is_to = "to" if minute > 30 else "past"
        time_indicator = "minutes" if minute > 1 else "minute"

        if is_to == "to":
            hour += 1
            minute = 60 - minute

        return hour, minute, is_to, time_indicator

    @staticmethod
    def post_logic(text: str) -> str:
        return text


class Language(English):
    pass
