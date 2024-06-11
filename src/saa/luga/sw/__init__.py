from dataclasses import dataclass
from saa.core.language import Luga


@dataclass(init=False, eq=False, repr=False, frozen=False)
class Swahili(Luga):
    time = {
        "to": "saa {hour} kasoro dakika {minute} time_indicator",
        "past": "saa {hour} na dakika {minute} time_indicator",
        0: "saa {hour} time_indicator",
        15: "saa {hour} na robo time_indicator",
        45: "saa {hour} kasorobo time_indicator",
        30: "saa {hour} na nusu time_indicator",
    }

    number_connector = "na"
    connect_format = "{0} {1} {2}"
    numbers = {
        0: "sifuri",
        1: "moja",
        2: "mbili",
        3: "tatu",
        4: "nne",
        5: "tano",
        6: "sita",
        7: "saba",
        8: "nane",
        9: "tisa",
        10: "kumi",
        11: "kumi na moja",
        12: "kumi na mbili",
        13: "kumi na tatu",
        14: "kumi na nne",
        15: "kumi na tano",
        16: "kumi na sita",
        17: "kumi na saba",
        18: "kumi na nane",
        19: "kumi na tisa",
        20: "ishirini",
        30: "thelathini",
        40: "arobaini",
        50: "hamsini",
    }

    def time_logic(hour, minute) -> tuple[int, int, str, str]:
        is_to = "to" if minute > 30 else "past"
        if is_to == "to":
            hour += 1
            minute = 60 - minute
        time_indicator = Swahili.day_divisions.get(hour)

        if 0 <= hour <= 6:
            hour += 6
        else:
            hour -= 6

        return hour, minute, is_to, time_indicator

    day_divisions = {
        0: "asubuhi",
        1: "asubuhi",
        2: "asubuhi",
        3: "asubuhi",
        4: "asubuhi",
        5: "asubuhi",
        6: "asubuhi",
        7: "asubuhi",
        8: "asubuhi",
        9: "asubuhi",
        10: "asubuhi",
        11: "asubuhi",
        12: "mchana",
        13: "mchana",
        14: "mchana",
        15: "mchana",
        16: "jioni",
        17: "jioni",
        18: "jioni",
        19: "jioni",
        20: "usiku",
        21: "usiku",
        22: "usiku",
        23: "usiku",
    }

    @staticmethod
    def post_logic(text: str) -> str:
        return text


class Language(Swahili):
    pass
