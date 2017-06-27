import re
import logging
from normality import collapse_spaces, ascii_text, category_replace

from fingerprints.constants import WS

log = logging.getLogger(__name__)
CHARACTERS_REMOVE_RE = re.compile(r'[\.\']')


def clean_strict(text):
    """Super-hardcore string scrubbing."""
    # transliterate to ascii
    text = ascii_text(text)
    # replace punctuation and symbols
    text = CHARACTERS_REMOVE_RE.sub('', text)
    text = category_replace(text)
    # pad out for company type replacements
    text = ''.join((WS, collapse_spaces(text), WS))
    return text
