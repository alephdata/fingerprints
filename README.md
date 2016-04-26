# fingerprints

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

## License

The MIT License (MIT)

Copyright (c) 2016 Friedrich Lindenberg

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
