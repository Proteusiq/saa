from datetime import time

import pytest
from saa.core.plugins import supported_languages
from saa.core.watch import Watch

Chinese = supported_languages.get("zh")

test_cases = [
    (time(hour=2, minute=22), Chinese, "两点二十二"),
    (time(hour=6, minute=2), Chinese, "六点两分"),
    (time(hour=10, minute=10), Chinese, "十点十分"),
    (time(hour=11, minute=40), Chinese, "十一点四十"),
    (time(hour=11, minute=50), Chinese, "差十分十二点"),
    (time(hour=13, minute=15), Chinese, "一点一刻"),
    (time(hour=13, minute=30), Chinese, "一点半"),
    (time(hour=13, minute=45), Chinese, "差一刻两点"),
    (time(hour=23, minute=25), Chinese, "十一点二十五"),
    (time(hour=23, minute=52), Chinese, "十一点五十二"),
]


@pytest.mark.parametrize("test_input, language, test_output", test_cases)
def test_clocks(test_input, language, test_output):
    clock = Watch(language=language)
    assert test_output == clock(test_input)


test_periods_cases = [
    (time(hour=0, minute=0), Chinese, "零点"),
    (time(hour=2, minute=0), Chinese, "两点"),
    (time(hour=12, minute=0), Chinese, "十二点"),
    (time(hour=13, minute=0), Chinese, "一点"),
    (time(hour=14, minute=0), Chinese, "两点"),
    (time(hour=16, minute=0), Chinese, "四点"),
    (time(hour=19, minute=0), Chinese, "七点"),
    (time(hour=20, minute=0), Chinese, "八点"),
]


@pytest.mark.parametrize("test_input, language, test_output", test_periods_cases)
def test_cases(test_input, language, test_output):
    clock = Watch(language=language)
    assert test_output == clock(test_input)
