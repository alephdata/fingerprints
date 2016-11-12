import logging
from normality import collapse_spaces

from fingerprints.constants import BRACKETED, WS
from fingerprints.data import COMPANY_TYPES, COMPANY_MAPPING, PERSON_PREFIX
from fingerprints.text import ensure_text, clean_strict

log = logging.getLogger(__name__)


def company_type_replacer(match):
    match = match.group(1)
    return COMPANY_MAPPING.get(match, match)


def generate(text, keep_order=False):
    text = ensure_text(text)
    if text is None:
        return

    # this needs to happen before the replacements
    text = text.lower()

    # try to remove personal prefix, such as Mr., Mrs.
    text = PERSON_PREFIX.sub(WS, text)

    # remove any text in brackets
    text = BRACKETED.sub(WS, text)

    # super hard-core string scrubbing
    text = clean_strict(text)
    text = COMPANY_TYPES.sub(company_type_replacer, text)

    if keep_order:
        text = collapse_spaces(text)
    else:
        # final manicure, based on openrefine algo
        parts = [p for p in text.split(WS) if len(p)]
        text = WS.join(sorted(set(parts)))

    if not len(text):
        return None

    return text
