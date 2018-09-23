# coding: utf-8
import re
import six
import logging
from normality import collapse_spaces, ascii_text, category_replace

from fingerprints.constants import WS

log = logging.getLogger(__name__)

CHARACTERS_REMOVE_RE = re.compile(r'[\.\']')

PREFIXES_RAW = ['Mr', 'Ms', 'Mrs', 'Mister', 'Miss', 'Madam', 'Madame',
                'Monsieur', 'Mme', 'Mmme', 'Herr', 'Hr', 'Frau',
                'Fr', 'The', u'Fräulein', 'Senor', 'Senorita',
                'Sr', 'Sir', 'Lady', 'The', 'de', 'of']
PREFIXES_RAW = '|'.join(PREFIXES_RAW)
if six.PY2:
    PREFIXES_RAW = PREFIXES_RAW.encode('utf-8')
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
    # replace punctuation and symbols
    text = CHARACTERS_REMOVE_RE.sub('', text)
    text = category_replace(text)
    # pad out for company type replacements
    text = ''.join((boundary, collapse_spaces(text), boundary))
    return text
