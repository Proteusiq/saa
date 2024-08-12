from datetime import time

import pytest
from saa.core.plugins import supported_languages
from saa.core.watch import Watch

Danish = supported_languages.get("da")

test_cases = [
    (time(hour=13, minute=30), Danish, "halvto"),
    (time(hour=13, minute=15), Danish, "kvart over et"),
    (time(hour=13, minute=45), Danish, "kvart i to"),
    (time(hour=12, minute=45), Danish, "kvart i et"),
    (time(hour=13, minute=0), Danish, "klokken et"),
    (time(hour=13, minute=13), Danish, "tretten minutter over et"),
]


@pytest.mark.parametrize("test_input, language, test_output", test_cases)
def test_clocks(test_input, language, test_output):
    clock = Watch(language=language)
    assert test_output == clock(test_input)


test_plural_cases = [
    (time(hour=13, minute=1), Danish, "et minut over et"),
    (time(hour=7, minute=3), Danish, "tre minutter over syv"),
    (time(hour=5, minute=40), Danish, "tyve minutter i seks"),
    (time(hour=8, minute=14), Danish, "fjorten minutter over otte"),
    (time(hour=7, minute=46), Danish, "fjorten minutter i otte"),
    (time(hour=14, minute=30), Danish, "halvtre"),
    (time(hour=9, minute=20), Danish, "tyve minutter over ni"),
    (time(hour=5, minute=40), Danish, "tyve minutter i seks"),
    (time(hour=18, minute=15), Danish, "kvart over seks"),
    (time(hour=17, minute=45), Danish, "kvart i seks"),
    (time(hour=21, minute=30), Danish, "halvti"),
    (time(hour=12, minute=30), Danish, "halvet"),
    (time(hour=1, minute=30), Danish, "halvto"),
]


@pytest.mark.parametrize("test_input, language, test_output", test_plural_cases)
def test_cases(test_input, language, test_output):
    clock = Watch(language=language)
    assert test_output == clock(test_input)
