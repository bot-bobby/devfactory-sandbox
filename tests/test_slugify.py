"""Tests for slugify function."""

import pytest

from textkit import slugify


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
