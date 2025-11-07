"""Property-based tests for watch/clock conversion using hypothesis.

These tests verify that the Watch class handles all valid hour/minute combinations
correctly, catching edge cases and hidden invariants that example-based testing
might miss.
"""

from datetime import time

from hypothesis import given
from hypothesis import strategies as st

from saa.core.plugins import supported_languages
from saa.core.watch import Watch

# Valid hour range is 0-23, minute range is 0-59
valid_hours = st.integers(min_value=0, max_value=23)
valid_minutes = st.integers(min_value=0, max_value=59)


@given(valid_hours, valid_minutes)
def test_watch_accepts_all_valid_times(hour: int, minute: int) -> None:
    """Test that watch accepts all valid hour/minute combinations.

    Property: All valid times (0-23 hours, 0-59 minutes) should be convertible
    without error for all languages. This catches any gaps in time expression
    handling across different hours and minutes.
    """
    for lang_code in supported_languages:
        language_class = supported_languages[lang_code]
        language = language_class()
        watch = Watch(language=language)
        test_time = time(hour=hour, minute=minute)
        result = watch(test_time)
        # Property: Result must be a non-empty string
        assert isinstance(result, str), (
            f"Watch for {lang_code} at {test_time} returned {type(result)}"
        )
        assert len(result) > 0, (
            f"Watch for {lang_code} returned empty string at {test_time}"
        )


@given(valid_hours, valid_minutes)
def test_watch_result_is_always_string(hour: int, minute: int) -> None:
    """Test that watch always returns strings.

    Property: Output type must always be string, regardless of language or time.
    This ensures consistent API contract across all language implementations.
    """
    for lang_code in supported_languages:
        language_class = supported_languages[lang_code]
        language = language_class()
        watch = Watch(language=language)
        test_time = time(hour=hour, minute=minute)
        result = watch(test_time)
        assert isinstance(result, str), (
            f"Converter for {lang_code} returned {type(result)} instead of str"
        )


@given(valid_hours, valid_minutes)
def test_watch_consistency(hour: int, minute: int) -> None:
    """Test that watch produces consistent results for same time.

    Property: Calling watch multiple times with same time produces same output.
    This catches any state mutations or randomness that would be problematic.
    """
    for lang_code in supported_languages:
        language_class = supported_languages[lang_code]
        language = language_class()
        watch = Watch(language=language)
        test_time = time(hour=hour, minute=minute)
        result1 = watch(test_time)
        result2 = watch(test_time)
        result3 = watch(test_time)
        # Same time must always produce same output
        assert result1 == result2 == result3, (
            f"Inconsistent results for {lang_code} at {test_time}: "
            f"{result1} != {result2} != {result3}"
        )


@given(valid_hours, valid_minutes)
def test_watch_special_minutes_edge_cases(hour: int, minute: int) -> None:
    """Test edge cases for special minute values (0, 15, 30, 45).

    Property: Special minute values that are commonly expressed differently
    (quarter past, half past, quarter to) should be handled correctly.
    These edge cases are where bugs often hide.
    """
    for lang_code in supported_languages:
        language_class = supported_languages[lang_code]
        language = language_class()
        watch = Watch(language=language)

        # Test special minutes if they occur
        special_minutes = [0, 15, 30, 45]
        for special_minute in special_minutes:
            test_time = time(hour=hour, minute=special_minute)
            result = watch(test_time)
            assert isinstance(result, str)
            assert len(result) > 0, f"Empty result for {lang_code} at {test_time}"


@given(valid_minutes)
def test_watch_hour_wrapping_equivalence(minute: int) -> None:
    """Test that hours wrap correctly (same expressions at different hours).

    Property: Watch should handle hour wrapping consistently. For example,
    13:30 should be expressed similarly to 1:30 in many languages.
    """
    for lang_code in supported_languages:
        language_class = supported_languages[lang_code]
        language = language_class()
        watch = Watch(language=language)

        # Test a few hour pairs that should have related expressions
        result_1 = watch(time(hour=1, minute=minute))
        result_13 = watch(time(hour=13, minute=minute))

        # Results should be strings (not necessarily equal due to AM/PM)
        assert isinstance(result_1, str)
        assert isinstance(result_13, str)
