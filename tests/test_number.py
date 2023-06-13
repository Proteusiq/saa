import pytest
from saa.luga import English, Danish
from saa.core.numbers import Converter


@pytest.mark.parametrize("test_input, language, test_output", [(45, English, "forty five"), 
                                                               (25, Danish, "femogtyve"), 
                                                         (13, English, "thirteen")])
def test_numbers(test_input, language, test_output):
    
    assert test_output == Converter(language=language)(test_input)
