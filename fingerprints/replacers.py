import os
import re
import json
from functools import lru_cache
from typing import Dict, Optional, Callable, Match, Pattern

from fingerprints.cleanup import clean_strict

DATA_PATH = os.path.join(os.path.dirname(__file__), "types.json")


class TypesReplacer(object):
    def __init__(self, replacements: Dict[str, str]) -> None:
        pairs = [(k.strip(), v) for (k, v) in replacements.items()]
        pairs = [(k, v) for (k, v) in pairs if len(k)]
        self.replacements = dict(pairs)
        forms = self.replacements.keys()
        forms_sorted = sorted(forms, key=lambda ct: -1 * len(ct))
        forms_regex = "\\b(%s)\\b" % "|".join(forms_sorted)
        self.matcher = re.compile(forms_regex, re.U)

    def get_canonical(self, match: Match[str]) -> str:
        return self.replacements.get(match.group(1), match.group(1))

    def __call__(self, text: str) -> str:
        return self.matcher.sub(self.get_canonical, text)


def build_replacer() -> Callable[[str], str]:
    replacements: Dict[str, str] = {}
    with open(DATA_PATH, "r") as fh:
        types = json.load(fh).get("types", {})
        # Compile person prefixes into a regular expression.
        for form, canonical in types.items():
            form = clean_strict(form)
            canonical = clean_strict(canonical)
            if form is None or canonical is None:
                continue
            form = form.lower()
            canonical = canonical.lower()
            if form == canonical:
                continue
            replacements[form] = canonical

    while True:
        has_deref = False
        for form, canonical in replacements.items():
            deref = replacements.get(canonical)
            if deref is not None:
                has_deref = True
                if form == deref:
                    replacements.pop(form)
                else:
                    replacements[form] = deref

        if not has_deref:
            break

    return TypesReplacer(replacements)


@lru_cache(maxsize=None)
def get_replacer() -> Callable[[str], str]:
    return build_replacer()


def replace_types(text: Optional[str]) -> Optional[str]:
    """Chomp down company types to a more convention form."""
    if text is None:
        return None
    return get_replacer()(text)


@lru_cache(maxsize=None)
def get_remover(clean: Callable[[Optional[str]], Optional[str]]) -> Pattern[str]:
    names = set()
    with open(DATA_PATH, "r") as fh:
        types = json.load(fh).get("types", {})
        # Compile person prefixes into a regular expression.
        for items in types.items():
            for item in items:
                item = clean(item)
                if item is not None:
                    names.add(item)
    forms = "(%s)" % "|".join(names)
    return re.compile(forms, re.U)


def remove_types(
    text: Optional[str], clean: Callable[[Optional[str]], Optional[str]] = clean_strict
) -> Optional[str]:
    """Remove company type names from a piece of text.

    WARNING: This converts to ASCII by default, pass in a different
    `clean` function if you need a different behaviour."""
    text = clean(text)
    if text is None:
        return None
    return get_remover(clean).sub("", text).strip()
