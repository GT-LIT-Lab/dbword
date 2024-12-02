"""Module for handling preprocessing of text data for `dbword` input types."""

import re

def preprocess(text:str) -> list[str]:
    """Preprocesses text data for `dbword` input types."""
    return consolidate(rm_invalid(rm_punct(listify(text))))

def consolidate(text:list[str]) -> list[str]:
    """Removes duplicate words from a list."""
    return list(dict.fromkeys(text))

def rm_invalid(text: list[str]) -> list[str]:
    """Removes numbers and hyphenated words from a list."""
    return [word for word in text if not re.search(r'\d|-', word)]

def rm_punct(text:list[str]) -> list[str]:
    """Removes punctuation from a string."""
    return [re.sub(r'[,.!?\"\'\']', '', word).lower() for word in text]

def listify(text:str) -> list[str]:
    """Converts a string to a list of words."""
    return text.split()