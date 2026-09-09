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


def truncate(text: str, max_len: int) -> str:
    """Truncate a string at the last word boundary before max_len, adding an ellipsis.

    Args:
        text: The input string to truncate
        max_len: The maximum length of the result (including ellipsis)

    Returns:
        The truncated string with an ellipsis if needed
    """
    if len(text) <= max_len:
        return text

    # If max_len is less than 3, we can't fit an ellipsis, so just truncate to max_len
    if max_len < 3:
        return text[:max_len]

    # Find the last space within the allowed length (accounting for 3 characters of ellipsis)
    last_space = text.rfind(" ", 0, max_len - 3)

    # If no space is found, fallback to hard character cut
    if last_space == -1:
        return text[: max_len - 3] + "..."

    # Return the text up to the last space, plus ellipsis
    return text[:last_space] + "..."
