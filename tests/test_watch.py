from datetime import datetime, time

import pytest
from saa import Clock

test_cases = [
    (time(hour=13, minute=30), "da", "halvto"),
    ("13:15", "da", "kvart over et"),
    (datetime(day=5, month=2, year=2022, hour=13, minute=45), "da", "kvart i to"),
    (time(hour=13, minute=45), "en", "quarter to two"),
    (datetime(day=5, month=2, year=2022, hour=13, minute=15), "en", "quarter past one"),
]


@pytest.mark.parametrize("test_input, language, test_output", test_cases)
def test_watches(test_input, language, test_output):
    clock = Clock(language=language)
    assert test_output == clock(test_input)
