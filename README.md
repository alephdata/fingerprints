# fingerprints

[![Build Status](https://travis-ci.org/alephdata/fingerprints.png?branch=master)](https://travis-ci.org/alephdata/fingerprints)

This library helps with the generation of fingerprints for entity data. A fingerprint
in this context is understood as a simplified entity identifier, derived from it's
name or address and used for cross-referencing of entity across different datasets.

## Usage

```python
import fingerprints

fp = fingerprints.generate('Mr. Sherlock Holmes')
assert fp == 'holmes sherlock'

fp = fingerprints.generate('Siemens Aktiengesellschaft')
assert fp == 'ag siemens'

fp = fingerprints.generate('New York, New York')
assert fp == 'new york'
```

## See also

* [Clustering in Depth](https://github.com/OpenRefine/OpenRefine/wiki/Clustering-In-Depth), part of the OpenRefine documentation discussing how to create collisions in data clustering.
* [probablepeople](https://github.com/datamade/probablepeople), parser for western names made by the brilliant folks at datamade.us.

