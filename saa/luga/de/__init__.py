from dataclasses import dataclass
from saa.core.language import Luga


@dataclass(init=False, eq=False, repr=False, frozen=False)
class Deutsch(Luga):
    time = {
        "to": "{minute} time_indicator vor {hour} Uhr",
        "past": "{minute} time_indicator nach {hour} Uhr",
        0: "{hour} Uhr",
        15: "viertel nach {hour}",
        45: "viertel vor {hour}",
        30: "halb {hour}",
    }
    number_connector = "und"
    connect_format = "{2}{1}{0}"
    numbers = {
        0: "null",
        1: "ein",  # ein und zwanzig /  eine Minute / ein Uhr
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
        is_to = "to" if minute >= 30 else "past"
        time_indicator = "Minuten" if minute not in (1, 59) else "Minute"

        if is_to == "to":
            hour += 1
            minute = 60 - minute

        return hour, minute, is_to, time_indicator

    @staticmethod
    def post_logic(text: str) -> str:
        if text in ("viertel nach ein", "viertel vor ein", "halb ein"):
            text += "s"

        text = text.replace("ein Minute", "eine Minute").replace("null", "zwölf")

        return text


class Language(Deutsch):
    pass
