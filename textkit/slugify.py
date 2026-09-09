"""Slugify utility functions."""

import re


def slugify(text: str) -> str:
    """Convert a string into a URL-safe slug.

    Args:
        text: The input string to convert

    Returns:
        A URL-safe slug with non-alphanumeric characters replaced by hyphens
    """
    if not text:
        return ""

    # Replace non-alphanumeric characters with hyphens
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text)

    # Remove leading and trailing hyphens
    slug = slug.strip("-")

    # Convert to lowercase
    slug = slug.lower()

    return slug
