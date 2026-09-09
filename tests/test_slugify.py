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
            ("Café Münster", "cafe-munster"),
            ("Hello World!", "hello-world"),
            ("123 @#$% abc", "123-abc"),
            ("São Paulo", "sao-paulo"),
            ("Naïve", "naive"),
            ("résumé", "resume"),
        ],
    )
    def test_slugify(self, input_text: str, expected: str) -> None:
        """Test slugify with various inputs."""
        assert slugify(input_text) == expected

    def test_slugify_separator(self) -> None:
        """Test slugify with custom separator."""
        assert slugify("Café Münster", separator="_") == "cafe_munster"
        assert slugify("Hello World!", separator=".") == "hello.world"
