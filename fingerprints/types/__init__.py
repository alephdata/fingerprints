from typing import Optional
from normality import collapse_spaces

from fingerprints.cleanup import clean_strict
from fingerprints.types.replacer import get_replacer, NormFunc


def replace_types(text: Optional[str]) -> Optional[str]:
    """Chomp down company types to a more convention form."""
    return get_replacer()(text)


def remove_types(text: Optional[str], clean: NormFunc = clean_strict) -> Optional[str]:
    """Remove company type names from a piece of text.

    WARNING: This converts to ASCII by default, pass in a different
    `clean` function if you need a different behaviour."""
    text = clean(text)
    removed = get_replacer(clean, remove=True)(text)
    return collapse_spaces(removed)
