import pytest
from saa.luga import English
from saa.core import Converter

test_cases = [
    (45, English, "forty five"),
    (13, English, "thirteen"),
]


@pytest.mark.parametrize("test_input, language, test_output", test_cases)
def test_numbers(test_input, language, test_output):
    convert = Converter(language=language)
    assert test_output == convert(test_input)
