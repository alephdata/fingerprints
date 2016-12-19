import re
import six
import logging
from normality import collapse_spaces, ascii_text, category_replace

from fingerprints.constants import WS

log = logging.getLogger(__name__)
CHARACTERS_REMOVE_RE = re.compile(r'[\.\']')


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


def clean_replacement(text):
    """Apply scrubbing to replacement terms."""
    return clean_strict(six.text_type(text).lower())
