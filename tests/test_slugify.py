"""Tests for slugify function."""

import pytest

from textkit import slugify, truncate


class TestSlugify:
    """Test cases for slugify function."""

    @pytest.mark.parametrize(
        "input_text,expected",
        [
            ("Hello, World!", "hello-world"),
            ("  Multiple   spaces ", "multiple-spaces"),
            ("already-a-slug", "already-a-slug"),
            ("___", ""),
            ("", ""),
        ],
    )
    def test_slugify(self, input_text: str, expected: str) -> None:
        """Test slugify with various inputs."""
        assert slugify(input_text) == expected


class TestTruncate:
    """Test cases for truncate function."""

    @pytest.mark.parametrize(
        "input_text,max_len,expected",
        [
            # String within limit - should return original
            ("Short", 10, "Short"),
            ("A bit longer but still within limit", 30, "A bit longer but still..."),
            # String needing truncation at word boundary
            ("This is a very long title that needs to be truncated", 20, "This is a very..."),
            # String with no spaces
            ("supercalifragilisticexpialidocious", 10, "superca..."),
            # Edge cases with small max length
            ("Short", 3, "..."),  # No space found - fallback to hard char cut (0 chars + ...)
            ("Short", 2, "Sh"),  # No space found - fallback to hard char cut (1 char + ...)
            (
                "Short",
                1,
                "S",
            ),  # No space found - fallback to hard char cut (0 chars + ... -> only 1 char)
            ("Short", 0, ""),  # No space found - no room for anything
            # Max length exactly for ellipsis
            ("A very long string", 3, "..."),
            # No space found - should fallback to hard cut
            ("ThisIsAVeryLongWordWithoutSpaces", 10, "ThisIsA..."),
        ],
    )
    def test_truncate(self, input_text: str, max_len: int, expected: str) -> None:
        """Test truncate with various inputs."""
        assert truncate(input_text, max_len) == expected
