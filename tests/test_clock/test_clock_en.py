from datetime import time

import pytest
from saa.core.plugins import supported_languages
from saa.core.watch import Watch

English = supported_languages.get("en")

test_cases = [
    (time(hour=13, minute=45), English, "quarter to two"),
    (time(hour=13, minute=15), English, "quarter past one"),
    (time(hour=13, minute=30), English, "half past one"),
]


@pytest.mark.parametrize("test_input, language, test_output", test_cases)
def test_clocks(test_input, language, test_output):
    clock = Watch(language=language)
    assert test_output == clock(test_input)


test_plural_cases = [
    (time(hour=13, minute=1), English, "one minute past one"),
    (time(hour=6, minute=17), English, "seventeen minutes past six"),
]


@pytest.mark.parametrize("test_input, language, test_output", test_plural_cases)
def test_cases(test_input, language, test_output):
    clock = Watch(language=language)
    assert test_output == clock(test_input)
