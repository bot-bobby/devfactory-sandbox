"""Slugify utility functions."""

import re
import unicodedata


def slugify(text: str, separator: str = "-") -> str:
    """Convert a string into a URL-safe slug.

    Args:
        text: The input string to convert
        separator: The separator to use (default is "-")

    Returns:
        A URL-safe slug with non-alphanumeric characters replaced by the separator
    """
    if not text:
        return ""

    # Normalize Unicode characters to decompose accented characters
    normalized = unicodedata.normalize("NFKD", text)

    # Remove non-spacing marks (accents, etc.)
    without_accents = "".join(c for c in normalized if not unicodedata.combining(c))

    # Replace non-alphanumeric characters with the separator
    slug = re.sub(r"[^a-zA-Z0-9]+", separator, without_accents)

    # Remove leading and trailing separators
    slug = slug.strip(separator)

    # Convert to lowercase
    slug = slug.lower()

    return slug
