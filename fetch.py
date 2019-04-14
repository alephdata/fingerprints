import os
import yaml
import unicodecsv
from normality import stringify
from urllib.request import urlopen
# TODO: https://en.wikipedia.org/wiki/Types_of_business_entity

CSV_URL = 'https://docs.google.com/spreadsheets/d/1Cw2xQ3hcZOAgnnzejlY5Sv3OeMxKePTqcRhXQU8rCAw/pub?gid=0&single=true&output=csv'  # noqa


def fetch():
    out_path = os.path.dirname(__file__)
    out_path = os.path.join(out_path, 'fingerprints', 'data', 'types.yml')
    fh = urlopen(CSV_URL)
    types = {}
    for row in unicodecsv.DictReader(fh):
        name = stringify(row.get('Name'))
        abbr = stringify(row.get('Abbreviation'))
        if name is None or abbr is None:
            continue
        if name in types and types[name] != abbr:
            print(name, types[name], abbr)
        types[name] = abbr
        # print abbr, name

    with open(out_path, 'w') as fh:
        yaml.safe_dump({'types': types}, fh,
                       indent=2,
                       allow_unicode=True,
                       canonical=False,
                       default_flow_style=False)


if __name__ == '__main__':
    fetch()
