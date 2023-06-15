import pytest
from saa.core.numbers import Converter
from saa.core.plugins import supported_languages

English = supported_languages.get("en")
test_cases = [
    (45, English, "forty five"),
    (13, English, "thirteen"),
]


@pytest.mark.parametrize("test_input, language, test_output", test_cases)
def test_numbers(test_input, language, test_output):
    convert = Converter(language=language)
    assert test_output == convert(test_input)
