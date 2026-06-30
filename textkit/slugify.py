import re

def slugify(text: str) -> str:
    """Convert a string to a URL-friendly slug."""
    if not text:
        return ""
    
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = re.sub(r'[^a-zA-Z0-9]+', '-', text).strip('-')
    
    # Replace multiple hyphens with a single one
    slug = re.sub(r'-+', '-', cleaned_text)
    
    return slug.lower()
