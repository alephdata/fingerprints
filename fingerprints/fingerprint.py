import logging
from typing import Optional
from normality import collapse_spaces, stringify

from fingerprints.constants import WS
from fingerprints.types import replace_types
from fingerprints.cleanup import clean_entity_prefix, clean_name_ascii
from fingerprints.cleanup import clean_brackets

log = logging.getLogger(__name__)


def fingerprint(
    text: Optional[str], keep_order: bool = False, keep_brackets: bool = False
) -> Optional[str]:
    text = stringify(text)
    if text is None:
        return None

    # this needs to happen before the replacements
    text = text.lower()
    text = clean_entity_prefix(text)

    if not keep_brackets:
        text = clean_brackets(text)

    # Super hard-core string scrubbing
    text = clean_name_ascii(text)
    text = replace_types(text)

    if keep_order:
        text = collapse_spaces(text)
    elif text is not None:
        # final manicure, based on openrefine algo
        parts = [p for p in text.split(WS) if len(p)]
        text = WS.join(sorted(set(parts)))

    if text is None or not len(text):
        return None

    return text
