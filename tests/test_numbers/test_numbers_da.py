import pytest
from saa.core.numbers import Converter
from saa.core.plugins import supported_languages

Danish = supported_languages.get("da")

test_cases = [
    (25, Danish, "femogtyve"),
    (14, Danish, "fjorten"),
]


@pytest.mark.parametrize("test_input, language, test_output", test_cases)
def test_numbers(test_input, language, test_output):
    convert = Converter(language=language)
    assert test_output == convert(test_input)
