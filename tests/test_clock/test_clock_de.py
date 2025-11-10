from datetime import time

import pytest

from saa.core.plugins import supported_languages
from saa.core.watch import Watch

Deutsch = supported_languages.get("de")

test_cases = [
    (time(hour=13, minute=45), Deutsch, "viertel vor zwei"),
    (time(hour=13, minute=15), Deutsch, "viertel nach eins"),
    (time(hour=13, minute=30), Deutsch, "halb zwei"),
    (time(hour=12, minute=45), Deutsch, "viertel vor eins"),
    (time(hour=13, minute=0), Deutsch, "ein Uhr"),
    (time(hour=13, minute=13), Deutsch, "dreizehn Minuten nach eins"),
]


@pytest.mark.parametrize("test_input, language, test_output", test_cases)
def test_clocks(test_input, language, test_output):
    clock = Watch(language=language)
    assert test_output == clock(test_input)


test_plural_cases = [
    (time(hour=13, minute=1), Deutsch, "eine Minute nach eins"),
    (time(hour=6, minute=17), Deutsch, "siebzehn Minuten nach sechs"),
    (time(hour=7, minute=3), Deutsch, "drei Minuten nach sieben"),
    (time(hour=5, minute=40), Deutsch, "zwanzig Minuten vor sechs"),
    (time(hour=8, minute=14), Deutsch, "vierzehn Minuten nach acht"),
    (time(hour=7, minute=46), Deutsch, "vierzehn Minuten vor acht"),
    (time(hour=14, minute=30), Deutsch, "halb drei"),
    (time(hour=9, minute=20), Deutsch, "zwanzig Minuten nach neun"),
    (time(hour=5, minute=40), Deutsch, "zwanzig Minuten vor sechs"),
    (time(hour=18, minute=15), Deutsch, "viertel nach sechs"),
    (time(hour=17, minute=45), Deutsch, "viertel vor sechs"),
    (time(hour=21, minute=30), Deutsch, "halb zehn"),
    (time(hour=12, minute=30), Deutsch, "halb eins"),
    (time(hour=1, minute=30), Deutsch, "halb zwei"),
    (time(hour=0, minute=0), Deutsch, "zwölf Uhr"),
    (time(hour=0, minute=15), Deutsch, "viertel nach zwölf"),
]


@pytest.mark.parametrize("test_input, language, test_output", test_plural_cases)
def test_cases(test_input, language, test_output):
    clock = Watch(language=language)
    assert test_output == clock(test_input)


edge_case_tests = [
    # quarter hours without "Uhr"
    (time(hour=0, minute=15), Deutsch, "viertel nach zwölf"),
    (time(hour=6, minute=45), Deutsch, "viertel vor sieben"),
    # half hours without "Uhr"
    (time(hour=10, minute=30), Deutsch, "halb elf"),
    (time(hour=23, minute=30), Deutsch, "halb zwölf"),
    # single minute cases (Minute vs Minuten)
    (time(hour=10, minute=1), Deutsch, "eine Minute nach zehn"),
    (time(hour=20, minute=59), Deutsch, "eine Minute vor neun"),
    # exact hours with "Uhr"
    (time(hour=0, minute=0), Deutsch, "zwölf Uhr"),
    (time(hour=12, minute=0), Deutsch, "zwölf Uhr"),
    (time(hour=6, minute=0), Deutsch, "sechs Uhr"),
]


@pytest.mark.parametrize("test_input, language, test_output", edge_case_tests)
def test_edge_cases(test_input, language, test_output):
    """Test edge cases for German time expressions."""
    clock = Watch(language=language)
    assert test_output == clock(test_input)
