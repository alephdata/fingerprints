import re
import logging
from typing import Optional
from normality import collapse_spaces, ascii_text, category_replace

from fingerprints.constants import WS

log = logging.getLogger(__name__)

CHARACTERS_REMOVE_RE = re.compile(r"[\.\']")

PREFIXES_RAW_LIST = [
    "Mr",
    "Ms",
    "Mrs",
    "Mister",
    "Miss",
    "Madam",
    "Madame",
    "Monsieur",
    "Mme",
    "Mmme",
    "Herr",
    "Hr",
    "Frau",
    "Fr",
    "The",
    "Fräulein",
    "Senor",
    "Senorita",
    "Sr",
    "Sir",
    "Lady",
    "The",
    "de",
    "of",
]
PREFIXES_RAW = "|".join(PREFIXES_RAW_LIST)
NAME_PATTERN_ = r"^\W*((%s)\.?\s+)*(?P<term>.*?)([\'’]s)?\W*$"
NAME_PATTERN_ = NAME_PATTERN_ % PREFIXES_RAW
PREFIXES = re.compile(NAME_PATTERN_, re.I | re.U)


def clean_entity_name(name: str) -> str:
    match = PREFIXES.match(name)
    if match is not None:
        name = match.group("term")
    return name


def clean_strict(text: Optional[str], boundary: str = WS) -> Optional[str]:
    """Super-hardcore string scrubbing."""
    # transliterate to ascii
    text = ascii_text(text)
    if not isinstance(text, str):
        return None
    # replace punctuation and symbols
    text = CHARACTERS_REMOVE_RE.sub("", text)
    text = category_replace(text)
    text = collapse_spaces(text)
    if text is None:
        return None
    # pad out for company type replacements
    return "".join((boundary, text, boundary))
