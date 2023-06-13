import pytest
from saa.luga import English, Danish
from saa.core.numbers import Converter

test_cases = [
    (45, English, "forty five"),
    (25, Danish, "femogtyve"),
    (13, English, "thirteen"),
    (14, Danish, "fjorten"),
]


@pytest.mark.parametrize("test_input, language, test_output", test_cases)
def test_numbers(test_input, language, test_output):
    assert test_output == Converter(language=language)(test_input)
