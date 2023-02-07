import io
import csv
import yaml
from typing import Dict, Set
from urllib.request import urlopen
from normality import slugify, stringify

from fingerprints.types.common import TYPES_PATH

ELF_URL = "https://www.gleif.org/about-lei/code-lists/iso-20275-entity-legal-forms-code-list/2021-10-21-elf-code-list-v1.4.1.csv"
OCCRP_URL = "https://docs.google.com/spreadsheets/d/1Cw2xQ3hcZOAgnnzejlY5Sv3OeMxKePTqcRhXQU8rCAw/pub?gid=0&single=true&output=csv"

TypesData = Dict[str, Set[str]]


def load_elf(types: TypesData):
    fh = urlopen(ELF_URL)
    fh = io.TextIOWrapper(fh, encoding="utf-8")
    for row in csv.DictReader(fh):
        data = {}
        for label, value in row.items():
            label = label.split("(")[0]
            data[slugify(label, sep="_")] = value
        # print(data)
        abb_translit = data["abbreviations_transliterated"].split(";")
        name_translit = data["entity_legal_form_name_transliterated_name"]
        abb_local = data["abbreviations_local_language"].split(";")
        name_local = data["entity_legal_form_name_local_name"]
        abb_all = []
        # for abb in chain(abb_translit, abb_local):
        for abb in abb_translit:
            abb = abb.strip()
            if len(abb):
                abb_all.append(abb)
        labels = set(abb_all)
        for abb in abb_local:
            abb = abb.strip()
            if len(abb):
                labels.add(abb)
        if len(name_translit):
            labels.add(name_translit)
        if len(name_local):
            labels.add(name_local)
        for abb in abb_all:
            other = set(labels)
            other.remove(abb)
            if abb not in types:
                types[abb] = other
            else:
                types[abb].update(other)


def load_occrp(types: TypesData):
    fh = urlopen(OCCRP_URL)
    fh = io.TextIOWrapper(fh, encoding="utf-8")
    for row in csv.DictReader(fh):
        name = stringify(row.get("Name"))
        abb = stringify(row.get("Abbreviation"))
        if name is None or abb is None:
            continue
        # print(name, abb)
        if abb not in types:
            types[abb] = set()
        types[abb].add(name)


def build() -> None:
    types: TypesData = {}
    load_elf(types)
    load_occrp(types)

    # from pprint import pprint
    # pprint(types)
    out = []
    for type_, forms in sorted(types.items()):
        out.append({"main": type_, "forms": sorted(forms)})

    with open(TYPES_PATH, "wb") as fh:
        fh.write(
            yaml.dump(
                {"types": out},
                allow_unicode=True,
                encoding="utf-8",
                sort_keys=False,
            )
        )


if __name__ == "__main__":
    build()
