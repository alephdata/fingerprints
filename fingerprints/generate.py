import logging
from normality import collapse_spaces, stringify

from fingerprints.constants import BRACKETED, WS
from fingerprints.replacers import replace_types
from fingerprints.text import clean_strict
from fingerprints.prefix import remove_person_prefix

log = logging.getLogger(__name__)


def generate(text, keep_order=False):
    text = stringify(text)
    if text is None:
        return

    # this needs to happen before the replacements
    text = text.lower()
    text = remove_person_prefix(text)

    # remove any text in brackets
    text = BRACKETED.sub(WS, text)

    # super hard-core string scrubbing
    text = clean_strict(text)
    text = replace_types(text)

    if keep_order:
        text = collapse_spaces(text)
    else:
        # final manicure, based on openrefine algo
        parts = [p for p in text.split(WS) if len(p)]
        text = WS.join(sorted(set(parts)))

    if not len(text):
        return None

    return text
