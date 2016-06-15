import os
import re
import yaml

from fingerprints.text import clean_replacement


data_file = os.path.join(os.path.dirname(__file__), 'data.yaml')
with open(data_file, 'r') as fh:
    data = yaml.load(fh)

# Compile person prefixes into a regular expression.
person_prefixes = [p.lower().strip() for p in data.get('person_prefix')]
person_prefixes = '|'.join(person_prefixes)
person_prefixes = '^(%s\b)' % person_prefixes
PERSON_PREFIX = re.compile(person_prefixes, re.U)


# Compile company type mappings:
COMPANY_MAPPING = {}
company_types = list()
for clean_form, other_forms in data.get('company_types').items():
    clean_form = clean_replacement(clean_form)
    for form in other_forms:
        form = clean_replacement(form)
        if form not in company_types:
            COMPANY_MAPPING[form] = clean_form
            company_types.append(form)

company_types = sorted(company_types, key=lambda ct: -1 * len(ct))
company_types = '(%s)' % '|'.join(company_types)
COMPANY_TYPES = re.compile(company_types, re.U)
