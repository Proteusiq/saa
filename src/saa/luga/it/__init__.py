from dataclasses import dataclass

from saa.core.language import Luga


@dataclass(init=False, eq=False, repr=False, frozen=False)
class Italian(Luga):
    time = {
        "to": "{minute} time_indicator a {hour}",
        "past": "{minute} time_indicator e {hour}",
        0: "{hour}",
        15: "un quarto e {hour}",
        45: "un quarto a {hour}",
        30: "mezzo e {hour}",
    }
    number_connector = ""
    connect_format = "{0}{1}{2}"
    numbers = {
        0: "zero",
        1: "uno",
        2: "due",
        3: "tre",
        4: "quattro",
        5: "cinque",
        6: "sei",
        7: "sette",
        8: "otto",
        9: "nove",
        10: "dieci",
        11: "undici",
        12: "dodici",
        13: "tredici",
        14: "quattordici",
        15: "quindici",
        16: "sedici",
        17: "diciassette",
        18: "diciotto",
        19: "diciannove",
        20: "venti",
        30: "trenta",
        40: "quaranta",
        50: "cinquanta",
    }

    @staticmethod
    def time_logic(hour, minute) -> tuple[int, int, str, str]:
        is_to = "to" if minute > 30 else "past"
        time_indicator = "minuti" if minute not in (1, 59) else "minuto"

        if is_to == "to":
            hour += 1
            minute = 60 - minute

        return hour, minute, is_to, time_indicator

    @staticmethod
    def post_logic(text: str) -> str:
        # handle "zero" hour (midnight) → "dodici" (twelve)
        text = text.replace("zero", "dodici")

        # handle singular "minuto" with gender agreement
        text = text.replace("uno minuto", "un minuto")

        return text


class Language(Italian):
    pass
