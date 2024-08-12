from dataclasses import dataclass

from saa.core.language import Luga


@dataclass(init=False, eq=False, repr=False, frozen=False)
class Chinese(Luga):
    time = {
        "to": "差{minute}time_indicator{hour}点",
        "past": "{hour}点{minute}time_indicator",
        0: "{hour}点",
        15: "{hour}点一刻",
        45: "差一刻{hour}点",
        30: "{hour}点半",
    }
    number_connector = ""
    connect_format = "{0}{2}"
    numbers = {
        0: "零",
        1: "一",
        2: "两",
        3: "三",
        4: "四",
        5: "五",
        6: "六",
        7: "七",
        8: "八",
        9: "九",
        10: "十",
        11: "十一",
        12: "十二",
        13: "十三",
        14: "十四",
        15: "十五",
        16: "十六",
        17: "十七",
        18: "十八",
        19: "十九",
        20: "二十",
        22: "二十二",
        30: "三十",
        32: "三十二",
        40: "四十",
        42: "四十二",
        50: "五十",
        52: "五十二",
    }

    @staticmethod
    def time_logic(hour, minute) -> tuple[int, int, str, str]:
        is_to = "past"
        if minute in [45, 50]:
            is_to = "to"
        if is_to == "to":
            hour += 1
            minute = 60 - minute

        time_indicator = "" if minute > 10 else "分"

        return hour, minute, is_to, time_indicator

    @staticmethod
    def post_logic(text: str) -> str:
        return text


class Language(Chinese):
    pass
