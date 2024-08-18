import pytest
from saa.core.numbers import Converter
from saa.core.plugins import supported_languages

Russian = supported_languages.get("ru")
test_cases = [
    (45, Russian, "сорок пять"),
    (13, Russian, "тринадцать"),
    (7, Russian, "семь"),
]


@pytest.mark.parametrize("test_input, language, test_output", test_cases)
def test_numbers(test_input, language, test_output):
    convert = Converter(language=language)
    assert test_output == convert(test_input)
