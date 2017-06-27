# coding: utf-8
import os
import re

from fingerprints.constants import WS

DATA_PATH = os.path.join(os.path.dirname(__file__), 'data')

PERSON_PREFIXES_RAW = ['Mr', 'Mrs', 'Mister', 'Miss', 'Madam', 'Madame',
                       'Monsieur', 'Mme', 'Mmme', 'Herr', 'Hr', 'Frau',
                       'Fr', 'The', u'Fräulein', 'Senor', 'Senorita',
                       'Sr', 'Sir', 'Lady']


def build_prefixes():
    """Build a regex to delete personal prefixes like Mr., Mrs."""
    person_prefixes = [p.lower().strip() for p in PERSON_PREFIXES_RAW]
    person_prefixes = '\\.?\\b|'.join(person_prefixes)
    person_prefixes = '^(%s\\.?\\b)' % person_prefixes
    return re.compile(person_prefixes, re.U)


def remove_person_prefix(text):
    """Remove personal prefix, such as Mr., Mrs., etc."""
    if not hasattr(remove_person_prefix, '_regex'):
        remove_person_prefix._regex = build_prefixes()
    return remove_person_prefix._regex.sub(WS, text)
