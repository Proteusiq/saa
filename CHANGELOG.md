# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-05-30

### Changed
- **BREAKING:** `requires-python` raised from `>=3.8` to `>=3.12`.
- Build backend swapped from `pdm-backend` to `uv_build`.
- Type checker swapped from `pyright` to `ty`; checks now cover all of `src/`
  (previously scoped to `clock.py` only).
- `Luga` ABC modernized: `@abstractproperty` data members replaced with
  `ClassVar` annotations; `time_logic` / `post_logic` declared as
  `@staticmethod @abstractmethod` to match plugin implementations.
- Ruff config: added `target-version = "py312"` and enabled `B`, `RUF`,
  `SIM`, `UP` rule sets.
- `clock.py` uses `str | time | datetime` instead of `Union[...]`.
- CI workflows bumped to `astral-sh/setup-uv@v4`, unpinned patch Python
  version, added 3.12/3.13 matrix.
- Pre-commit config: dropped `black`; bumped ruff hook to `astral-sh/ruff-pre-commit@v0.9.5`.

### Added
- `[project]` metadata: `readme`, `license`, `license-files`, classifiers.
- `Makefile` and `.editorconfig` (beacon layout).
- `ty` as the project type checker.

### Removed
- `pyright` dev dependency.
- Stale rye-era `requirements.lock` and `requirements-dev.lock`.
- Deprecated `abstractproperty` usage.

### Fixed
- `[project.urls]` table (was incorrectly `[tool.urls]`, a no-op).
- Swahili `time_logic` used `day_divisions.get(hour)` (`str | None`) where
  a guaranteed `str` was required; switched to direct lookup.
- `[tool.uv] exclude-newer = "7 days"` was invalid (uv expects an ISO
  datetime); commented out.

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
