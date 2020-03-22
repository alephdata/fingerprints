import re
import logging
from normality import collapse_spaces, ascii_text, category_replace

from fingerprints.constants import WS

log = logging.getLogger(__name__)

CHARACTERS_REMOVE_RE = re.compile(r'[\.\']')

PREFIXES_RAW = ['Mr', 'Ms', 'Mrs', 'Mister', 'Miss', 'Madam', 'Madame',
                'Monsieur', 'Mme', 'Mmme', 'Herr', 'Hr', 'Frau',
                'Fr', 'The', 'Fräulein', 'Senor', 'Senorita',
                'Sr', 'Sir', 'Lady', 'The', 'de', 'of']
PREFIXES_RAW = '|'.join(PREFIXES_RAW)
NAME_PATTERN = r'^\W*((%s)\.?\s+)*(?P<term>.*?)([\'’]s)?\W*$'
NAME_PATTERN = NAME_PATTERN % PREFIXES_RAW
PREFIXES = re.compile(NAME_PATTERN, re.I | re.U)


def clean_entity_name(name):
    match = PREFIXES.match(name)
    if match is not None:
        name = match.group('term')
    return name


def clean_strict(text, boundary=WS):
    """Super-hardcore string scrubbing."""
    # transliterate to ascii
    text = ascii_text(text)
    if not isinstance(text, str):
        return None
    # replace punctuation and symbols
    text = CHARACTERS_REMOVE_RE.sub('', text)
    text = category_replace(text)
    # pad out for company type replacements
    return ''.join((boundary, collapse_spaces(text), boundary))
