# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.9] - 2025-11-07

### Added
- Property-based testing with hypothesis library to catch edge cases and blind spots
- Comprehensive property-based tests for number converter (test_hypothesis_numbers.py)
  - Tests all valid numbers (0-59) are handled correctly across all languages
  - Validates proper rejection of out-of-range numbers with meaningful error messages
  - Verifies consistency and output type guarantees
- Comprehensive property-based tests for clock/watch (test_hypothesis_watch.py)
  - Tests all valid hour/minute combinations (0-23, 0-59) across all languages
  - Tests consistency and edge cases for special minutes (0, 15, 30, 45)
  - Validates hour wrapping behavior

### Fixed
- Swahili time_logic missing @staticmethod decorator (bug discovered by hypothesis)
- Swahili hour wrapping bug when minute > 30 (hour 24 now correctly wraps to 0)

## Unreleased
