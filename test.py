# coding: utf-8
import fingerprints

tests = [
    u'Foo (Bar) Corp',
    u'ähnlIIch',
    'Open S.A.R.L.',
    'Mr. Boaty McBoatface',
    u'РАДИК ІВАН ЛЬВОВИЧ',
    u'КУШНАРЬОВ ДМИТРО ВІТАЛІЙОВИЧ',
    u'Foo (Bar) CORPORATION',
    'Mr. Sherlock Holmes',
    'Siemens Aktiengesellschaft',
    'New York, New York',
    u'Foo Gesellschaft mit beschränkter Haftung',
    'Software und- Systemgesellschaft mit beschr Haftung'
]

for test in tests:
    out = fingerprints.generate(test)
    print out
