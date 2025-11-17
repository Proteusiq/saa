import pytest

from saa.core.numbers import Converter
from saa.core.plugins import supported_languages

Italian = supported_languages.get("it")
test_cases = [
    (45, Italian, "quarantacinque"),
    (13, Italian, "tredici"),
]


@pytest.mark.parametrize("test_input, language, test_output", test_cases)
def test_numbers(test_input, language, test_output):
    convert = Converter(language=language)
    assert test_output == convert(test_input)
