import pytest
from saa.luga import English
from saa.core.clock import Clock
from datetime import time



test_cases = [
    (time(hour=13,minute=45), English, "quarter to two"),
    (time(hour=13,minute=45), English, "quarter to two"),
    (time(hour=13,minute=30), English, "half past one"),
    
]

@pytest.mark.parametrize("test_input, language, test_output", test_cases)
def test_clocks(test_input, language, test_output):
    assert test_output == Clock(test_input, language=language).read(raw=False)