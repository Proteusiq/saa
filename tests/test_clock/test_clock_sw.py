from datetime import time

import pytest
from saa.core.plugins import supported_languages
from saa.core.watch import Watch

Swahili = supported_languages.get("sw")

test_cases = [
    (time(hour=13, minute=45), Swahili, "saa nane kasorobo mchana"),
    (time(hour=13, minute=15), Swahili, "saa saba na robo mchana"),
    (time(hour=13, minute=30), Swahili, "saa saba na nusu mchana"),
    (time(hour=20, minute=0), Swahili, "saa mbili usiku"),
    (time(hour=19, minute=25), Swahili, "saa moja na dakika ishirini na tano jioni"),
    (time(hour=19, minute=41), Swahili, "saa mbili kasoro dakika kumi na tisa usiku"),
]


@pytest.mark.parametrize("test_input, language, test_output", test_cases)
def test_clocks(test_input, language, test_output):
    clock = Watch(language=language)
    assert test_output == clock(test_input)


test_periods_cases = [
    (time(hour=0, minute=0), Swahili, "saa sita asubuhi"),
    (time(hour=13, minute=0), Swahili, "saa saba mchana"),
    (time(hour=16, minute=0), Swahili, "saa kumi jioni"),
    (time(hour=19, minute=0), Swahili, "saa moja jioni"),
    (time(hour=20, minute=0), Swahili, "saa mbili usiku"),
]


@pytest.mark.parametrize("test_input, language, test_output", test_periods_cases)
def test_cases(test_input, language, test_output):
    clock = Watch(language=language)
    assert test_output == clock(test_input)
