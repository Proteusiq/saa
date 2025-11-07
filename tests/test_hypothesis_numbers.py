"""Property-based tests for number conversion using hypothesis.

These tests verify that the Converter handles all valid inputs correctly
and properly rejects invalid inputs, catching edge cases that example-based
testing might miss.
"""

from hypothesis import given
from hypothesis import strategies as st

from saa.core.numbers import Converter
from saa.core.plugins import supported_languages


@given(st.integers(min_value=0, max_value=59))
def test_converter_accepts_valid_range(number: int) -> None:
    """Test that converter accepts all valid numbers 0-59 for all languages.

    Property: All numbers in the valid range should be convertible without error.
    This catches any gaps in language number definitions or edge cases in boundaries.
    """
    for lang_code in supported_languages:
        language_class = supported_languages[lang_code]
        language = language_class()
        converter = Converter(language=language)
        result = converter(number)
        # Property: Result must be a non-empty string
        assert isinstance(result, str)
        assert len(result) > 0


@given(st.one_of(st.integers(max_value=-1), st.integers(min_value=60)))
def test_converter_rejects_out_of_range(number: int) -> None:
    """Test that converter rejects numbers outside valid range.

    Property: Numbers outside 0-59 must raise ValueError for all languages.
    This ensures consistent error handling and boundary validation.
    """
    for lang_code in supported_languages:
        language_class = supported_languages[lang_code]
        language = language_class()
        converter = Converter(language=language)
        try:
            converter(number)
            raise AssertionError(f"Expected ValueError for {number}")
        except ValueError as e:
            # Property: Error message should contain the number and range info
            assert str(number) in str(e)
            assert "0-59" in str(e)


@given(st.integers(min_value=0, max_value=59))
def test_converter_consistency(number: int) -> None:
    """Test that converter produces consistent results for same input.

    Property: Calling converter multiple times with same input produces same output.
    This catches any state mutations or randomness that would be problematic.
    """
    for lang_code in supported_languages:
        language_class = supported_languages[lang_code]
        language = language_class()
        converter = Converter(language=language)
        result1 = converter(number)
        result2 = converter(number)

        # Same input must always produce same output
        assert result1 == result2
        # Repeated calls should not change the result
        assert result1 == converter(number)


@given(st.integers(min_value=0, max_value=59))
def test_converter_result_is_string_for_all_languages(number: int) -> None:
    """Test that all converters return strings for all valid inputs.

    Property: Output type must always be string, regardless of language or input.
    This ensures consistent API contract across all language implementations.
    """
    for lang_code in supported_languages:
        language_class = supported_languages[lang_code]
        language = language_class()
        converter = Converter(language=language)
        result = converter(number)
        assert isinstance(result, str), (
            f"Converter for {lang_code} returned {type(result)} instead of str"
        )
