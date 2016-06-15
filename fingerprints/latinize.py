# try:
#     import icu
#     # raise ImportError()

#     def latinize(text):
#         transliterator = icu.Transliterator.createInstance('Any-Latin')
#         return transliterator.transliterate(text)

# except ImportError:

from unidecode import unidecode


def latinize(text):
    return unidecode(text)
