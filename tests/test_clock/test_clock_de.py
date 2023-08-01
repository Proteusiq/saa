from datetime import time
import pytest
from saa.core.watch import Watch
from saa.core.plugins import supported_languages

German = supported_languages.get("de")

test_cases = [
    (time(hour=13, minute=45), German, "viertel vor zwei"),
    (time(hour=13, minute=15), German, "viertel nach eins"),
    (time(hour=13, minute=30), German, "halb zwei"),
]


@pytest.mark.parametrize("test_input, language, test_output", test_cases)
def test_clocks(test_input, language, test_output):
    clock = Watch(language=language)
    assert test_output == clock(test_input)


test_plural_cases = [
    (time(hour=13, minute=1), German, "eine Minute nach eins"),
    (time(hour=6, minute=17), German, "siebzehn Minuten nach sechs"),
]


@pytest.mark.parametrize("test_input, language, test_output", test_plural_cases)
def test_cases(test_input, language, test_output):
    clock = Watch(language=language)
    assert test_output == clock(test_input)
