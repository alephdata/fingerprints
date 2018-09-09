# coding: utf-8
import re
import logging
from normality import collapse_spaces, ascii_text, category_replace

from fingerprints.constants import WS

log = logging.getLogger(__name__)

CHARACTERS_REMOVE_RE = re.compile(r'[\.\']')
NAME_PATTERN = r'^\W*((%s)\.?\s+)*(?P<term>.*?)([\'’]s)?\W*$'
PERSON_PREFIXES_RAW = ['Mr', 'Mrs', 'Mister', 'Miss', 'Madam', 'Madame',
                       'Monsieur', 'Mme', 'Mmme', 'Herr', 'Hr', 'Frau',
                       'Fr', 'The', u'Fräulein', 'Senor', 'Senorita',
                       'Sr', 'Sir', 'Lady']
ORG_PREFIXES_RAW = ['The', 'A', 'de', 'of']
ALL_PREFIXES_RAW = PERSON_PREFIXES_RAW + ORG_PREFIXES_RAW
ALL_PREFIXES_RAW = '|'.join(ALL_PREFIXES_RAW)
ALL_PREFIXES = re.compile(NAME_PATTERN % ALL_PREFIXES_RAW, re.I | re.U)


def clean_entity_name(name):
    match = ALL_PREFIXES.match(name)
    if match is not None:
        text = match.group('term')
    return text


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
