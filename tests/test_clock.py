import pytest
from saa.luga import English, Danish
from saa.core.clock import Clock
from datetime import time



test_cases = [
    (time(hour=13,minute=45), English, "quarter to two"),
    (time(hour=13,minute=15), English, "quarter past one"),
    (time(hour=13,minute=30), English, "half past one"),
    (time(hour=13,minute=30), Danish, "halvto"),
    (time(hour=13,minute=15), Danish, "kvart over et"),
    (time(hour=13,minute=45), Danish, "kvart i to"),
    
]

@pytest.mark.parametrize("test_input, language, test_output", test_cases)
def test_clocks(test_input, language, test_output):
    assert test_output == Clock(test_input, language=language).read(raw=False)


test_plural_cases = [
    (time(hour=13,minute=1), English, "one minute past one"),
    (time(hour=6,minute=17), English, "seventeen minutes past six"),
    (time(hour=13,minute=1), Danish, "et minut over et"),
    (time(hour=7,minute=3), Danish, "tre minutter over syv"),
    
]

@pytest.mark.parametrize("test_input, language, test_output", test_cases)
def test_cases(test_input, language, test_output):
    assert test_output == Clock(test_input, language=language).read(raw=False)