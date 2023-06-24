import pytest
from saa.core.numbers import Converter
from saa.core.plugins import supported_languages

Swahili = supported_languages.get("sw")
test_cases = [
    (45, Swahili, "arobaini na tano"),
    (13, Swahili, "kumi na tatu"),
]


@pytest.mark.parametrize("test_input, language, test_output", test_cases)
def test_numbers(test_input, language, test_output):
    convert = Converter(language=language)
    assert test_output == convert(test_input)
