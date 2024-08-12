import pytest
from saa.core.numbers import Converter
from saa.core.plugins import supported_languages

Chinese = supported_languages.get("zh")
test_cases = [
    (45, Chinese, "四十五"),
    (13, Chinese, "十三"),
    (22, Chinese, "二十二"),
]


@pytest.mark.parametrize("test_input, language, test_output", test_cases)
def test_numbers(test_input, language, test_output):
    convert = Converter(language=language)
    assert test_output == convert(test_input)
