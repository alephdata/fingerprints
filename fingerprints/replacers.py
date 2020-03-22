import io
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
    with io.open(DATA_PATH, 'r', encoding='utf-8') as fh:
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
