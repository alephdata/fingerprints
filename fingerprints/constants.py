import re

COLLAPSE = re.compile(r'\s+', re.U)
BRACKETED = re.compile(r'(\([^\(\)]*\)|\[[^\[\]]*\])')
WS = ' '

# Unicode character classes, see:
# http://www.fileformat.info/info/unicode/category/index.htm
CATEGORIES = {
    'C': None,
    'M': None,
    'Z': WS,
    'P': None,
    'S': None
}

# Some hints for the normalizer:
PERSON = 1
COMPANY = 2
ADDRESS = 3
ANY = 4
