import os
import re
import json

from fingerprints.cleanup import clean_strict

DATA_PATH = os.path.join(os.path.dirname(__file__), 'types.json')


class TypesReplacer(object):

    def __init__(self, replacements):
        replacements = [(k.strip(), v) for (k, v) in replacements.items()]
        replacements = [(k, v) for (k, v) in replacements if len(k)]
        self.replacements = dict(replacements)
        forms = self.replacements.keys()
        forms = sorted(forms, key=lambda ct: -1 * len(ct))
        forms = '\\b(%s)\\b' % '|'.join(forms)
        self.matcher = re.compile(forms, re.U)

    def get_canonical(self, match):
        return self.replacements.get(match.group(1), match.group(1))

    def __call__(self, text):
        return self.matcher.sub(self.get_canonical, text)


def build_replacer():
    replacements = {}
    with open(DATA_PATH, 'r') as fh:
        types = json.load(fh).get('types', {})
        # Compile person prefixes into a regular expression.
        for form, canonical in types.items():
            form = clean_strict(form).lower()
            canonical = clean_strict(canonical).lower()
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


def replace_types(text):
    """Chomp down company types to a more convention form."""
    if not hasattr(replace_types, '_replacer'):
        replace_types._replacer = build_replacer()
    return replace_types._replacer(text)


def remove_types(text, clean=clean_strict):
    """Remove company type names from a piece of text.

    WARNING: This converts to ASCII by default, pass in a different
    `clean` function if you need a different behaviour."""
    if not hasattr(remove_types, '_remove'):
        remove_types._remove = {}
    if clean not in remove_types._remove:
        names = set()
        with open(DATA_PATH, 'r') as fh:
            types = json.load(fh).get('types', {})
            # Compile person prefixes into a regular expression.
            for items in types.items():
                for item in items:
                    item = clean(item)
                    if item is not None:
                        names.add(item)
        forms = '(%s)' % '|'.join(names)
        remove_types._remove[clean] = re.compile(forms, re.U)
    text = clean(text)
    if text is not None:
        return remove_types._remove[clean].sub('', text).strip()
