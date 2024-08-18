from datetime import time

import pytest
from saa.core.plugins import supported_languages
from saa.core.watch import Watch

Russian = supported_languages.get("ru")

test_cases = [
    (time(hour=2, minute=0), Russian, "два часа"),
    (time(hour=5, minute=0), Russian, "пять часов"),
    (time(hour=12, minute=50), Russian, "без десяти час"),
    (time(hour=12, minute=55), Russian, "без пяти час"),
    (time(hour=13, minute=0), Russian, "один час"),
    (time(hour=13, minute=5), Russian, "пять минут второго"),
    (time(hour=13, minute=15), Russian, "пятнадцать минут второго"),
    (time(hour=13, minute=20), Russian, "двадцать минут второго"),
    (time(hour=13, minute=30), Russian, "половина второго"),
    (time(hour=13, minute=40), Russian, "без двадцати два"),
    (time(hour=13, minute=45), Russian, "без пятнадцати два"),
    (time(hour=13, minute=50), Russian, "без десяти два"),
    (time(hour=13, minute=55), Russian, "без пяти два"),
]


@pytest.mark.parametrize("test_input, language, test_output", test_cases)
def test_clocks(test_input, language, test_output):
    clock = Watch(language=language)
    assert test_output == clock(test_input)


test_plural_cases = [
    (time(hour=12, minute=17), Russian, "двенадцать семнадцать"),
    (time(hour=12, minute=26), Russian, "двенадцать двадцать шесть"),
    (time(hour=13, minute=1), Russian, "час ноль одна"),
    (time(hour=13, minute=2), Russian, "час ноль две"),
    (time(hour=13, minute=11), Russian, "час одиннадцать"),
]


@pytest.mark.parametrize("test_input, language, test_output", test_plural_cases)
def test_cases(test_input, language, test_output):
    clock = Watch(language=language)
    assert test_output == clock(test_input)
