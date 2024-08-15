from dataclasses import dataclass

from saa.core.language import Luga


@dataclass(init=False, eq=False, repr=False, frozen=False)
class Russian(Luga):
    time = {
        "to": "{hour} {minute}",
        0: "{hour} time_indicator",
        1: "{hour} ноль одна",
        2: "{hour} ноль две",
        3: "{hour} ноль три",
        4: "{hour} ноль четыре",
        5: "пять минут time_indicator",
        6: "{hour} ноль шесть",
        7: "{hour} ноль семь",
        8: "{hour} ноль восемь",
        9: "{hour} ноль девять",
        10: "десять минут time_indicator",
        15: "пятнадцать минут time_indicator",
        20: "двадцать минут time_indicator",
        30: "половина time_indicator",
        40: "без двадцати time_indicator",
        45: "без пятнадцати time_indicator",
        50: "без десяти time_indicator",
        55: "без пяти time_indicator",
    }

    number_connector = ""
    connect_format = "{0} {2}"
    numbers = {
        0: "ноль",
        1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять",
        10: "десять",
        11: "одиннадцать",
        12: "двенадцать",
        13: "тринадцать",
        14: "четырнадцать",
        15: "пятнадцать",
        16: "шестнадцать",
        17: "семнадцать",
        18: "восемнадцать",
        19: "девятнадцать",
        20: "двадцать",
        30: "тридцать",
        40: "сорок",
        50: "пятьдесят",
    }

    hour_endings = {
        0: "двенадцатого",
        1: "первого",
        2: "второго",
        3: "третьего",
        4: "четвертого",
        5: "пятого",
        6: "шестого",
        7: "седьмого",
        8: "восьмого",
        9: "девятого",
        10: "десятого",
        11: "одиннадцатого",
        12: "двенадцатого",
    }

    @staticmethod
    def num_text(num: int, texts: list[str]) -> str:
        last_digit = num % 10
        if 10 <= num <= 20 or last_digit == 0 or 5 <= last_digit <= 9:
            return texts[2]
        elif last_digit == 1:
            return texts[0]

        return texts[1]

    @staticmethod
    def time_logic(hour: int, minute: int) -> tuple[int, int, str, str]:
        time_indicator = Russian.num_text(hour, ["час", "часа", "часов"])

        if hour == 0:
            hour = 12

        if minute in [5, 10, 15, 20, 30, 40, 45, 50, 55]:
            hour += 1

        if hour > 12:
            hour -= 12

        if minute == 0:
            time_indicator = Russian.num_text(hour, ["час", "часа", "часов"])

        elif minute in Russian.time:
            if minute <= 30:
                time_indicator = Russian.hour_endings[hour]
            elif hour == 1:
                time_indicator = "час"
            else:
                time_indicator = "{hour}"

        return hour, minute, "to", time_indicator

    @staticmethod
    def post_logic(text: str) -> str:
        return text


class Language(Russian):
    pass
