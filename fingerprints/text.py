import six
import logging
from unicodedata import normalize, category

from fingerprints.latinize import latinize
from fingerprints.constants import CATEGORIES, COLLAPSE, WS

log = logging.getLogger(__name__)


def ensure_text(text):
    """Make sure ``text`` is a useful snippet of text."""
    if text is None:
        return

    if not isinstance(text, six.text_type):
        try:
            text = six.text_type(text)
        except Exception as ex:
            log.exception(ex)

    if not isinstance(text, six.text_type):
        try:
            text = text.decode('utf-8')
        except Exception as ex:
            log.exception(ex)
            return None

    text = text.strip()
    if len(text) < 2:
        return None
    return text


def category_replace(text):
    """Replace unicode categories in the given text."""
    word = []
    for character in normalize('NFKD', text):
        cat = category(character)[0]
        character = CATEGORIES.get(cat, character)
        if character is None:
            continue
        word.append(character)
    return ''.join(word)


def collapse(text):
    """Remove duplicate whitespaces."""
    return COLLAPSE.sub(WS, text).strip(WS)


def clean_strict(text):
    """Super-hardcore string scrubbing."""
    # transliterate to latin
    text = latinize(text)
    # replace punctuation and symbols
    text = category_replace(six.text_type(text))
    # pad out for company type replacements
    text = ''.join((WS, collapse(text), WS))
    return text


def clean_replacement(text):
    """Apply scrubbing to replacement terms."""
    return clean_strict(six.text_type(text).lower())
