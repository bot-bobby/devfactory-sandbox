import pytest
from textkit.slugify import slugify

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("Hello, World!", "hello-world"),
        ("  Multiple   spaces ", "multiple-spaces"),
        ("already-a-slug", "already-a-slug"),
        ("", ""),
        ("___", ""),
    ],
)
def test_slugify(input_text: str, expected_output: str):
    assert slugify(input_text) == expected_output
