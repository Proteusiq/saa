from datetime import time

import pytest

from saa.core.plugins import supported_languages
from saa.core.watch import Watch

Italian = supported_languages.get("it")

test_cases = [
    (time(hour=13, minute=45), Italian, "un quarto a due"),
    (time(hour=13, minute=15), Italian, "un quarto e uno"),
    (time(hour=13, minute=30), Italian, "mezzo e uno"),
]


@pytest.mark.parametrize("test_input, language, test_output", test_cases)
def test_clocks(test_input, language, test_output):
    clock = Watch(language=language)
    assert test_output == clock(test_input)


test_plural_cases = [
    (time(hour=13, minute=1), Italian, "un minuto e uno"),
    (time(hour=6, minute=17), Italian, "diciassette minuti e sei"),
    (time(hour=7, minute=3), Italian, "tre minuti e sette"),
    (time(hour=5, minute=40), Italian, "venti minuti a sei"),
    (time(hour=8, minute=14), Italian, "quattordici minuti e otto"),
    (time(hour=7, minute=46), Italian, "quattordici minuti a otto"),
    (time(hour=14, minute=30), Italian, "mezzo e due"),
    (time(hour=9, minute=20), Italian, "venti minuti e nove"),
    (time(hour=5, minute=40), Italian, "venti minuti a sei"),
    (time(hour=18, minute=15), Italian, "un quarto e sei"),
    (time(hour=17, minute=45), Italian, "un quarto a sei"),
    (time(hour=21, minute=30), Italian, "mezzo e nove"),
    (time(hour=12, minute=30), Italian, "mezzo e dodici"),
    (time(hour=1, minute=30), Italian, "mezzo e uno"),
    (time(hour=0, minute=0), Italian, "dodici"),
    (time(hour=0, minute=15), Italian, "un quarto e dodici"),
]


@pytest.mark.parametrize("test_input, language, test_output", test_plural_cases)
def test_cases(test_input, language, test_output):
    clock = Watch(language=language)
    assert test_output == clock(test_input)


edge_case_tests = [
    # quarter hours
    (time(hour=0, minute=15), Italian, "un quarto e dodici"),
    (time(hour=6, minute=45), Italian, "un quarto a sette"),
    # half hours
    (time(hour=10, minute=30), Italian, "mezzo e dieci"),
    (time(hour=23, minute=30), Italian, "mezzo e undici"),
    # single minute cases (minuto vs minuti)
    (time(hour=10, minute=1), Italian, "un minuto e dieci"),
    (time(hour=20, minute=59), Italian, "un minuto a nove"),
    # exact hours
    (time(hour=0, minute=0), Italian, "dodici"),
    (time(hour=12, minute=0), Italian, "dodici"),
    (time(hour=6, minute=0), Italian, "sei"),
]


@pytest.mark.parametrize("test_input, language, test_output", edge_case_tests)
def test_edge_cases(test_input, language, test_output):
    """Test edge cases for Italian time expressions."""
    clock = Watch(language=language)
    assert test_output == clock(test_input)
