import pytest
from saa.core.numbers import Converter
from saa.core.plugins import supported_languages

English = supported_languages.get("en")
Danish = supported_languages.get("da")

test_cases = [
    (-1, Danish, ValueError),
    (60, English, ValueError),
]


@pytest.mark.parametrize("test_input, language, test_error", test_cases)
def test_error(test_input, language, test_error):
    with pytest.raises(
        test_error, match=f"{test_input} is outside the clock's range number `0-59`"
    ):
        convert = Converter(language=language)
        _ = convert(test_input)
