from fingerprints.fingerprint import fingerprint
from fingerprints.cleanup import clean_entity_name
from fingerprints.types import remove_types

generate = fingerprint

__all__ = ["fingerprint", "generate", "clean_entity_name", "remove_types"]
