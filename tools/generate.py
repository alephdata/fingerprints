import os
import io
import csv
import json
from pprint import pprint  # noqa
from normality import stringify
from urllib.request import urlopen

CSV_URL = "https://docs.google.com/spreadsheets/d/1Cw2xQ3hcZOAgnnzejlY5Sv3OeMxKePTqcRhXQU8rCAw/pub?gid=0&single=true&output=csv"  # noqa


def fetch():
    file_path = os.path.dirname(__file__)
    out_path = os.path.join(file_path, "..", "fingerprints", "types.json")
    types = {}
    fh = urlopen(CSV_URL)
    fh = io.TextIOWrapper(fh, encoding="utf-8")
    for row in csv.DictReader(fh):
        name = stringify(row.get("Name"))
        abbr = stringify(row.get("Abbreviation"))
        if name is None or abbr is None:
            continue
        if name in types and types[name] != abbr:
            print(name, types[name], abbr)
        types[name] = abbr
        # print abbr, name

    elf_path = os.path.join(file_path, "elf-code-list.csv")
    with open(elf_path, "r") as fh:
        for row in csv.DictReader(fh):
            pprint(dict(row))

    with open(out_path, "w") as fh:
        json.dump({"types": types}, fh)


if __name__ == "__main__":
    fetch()
