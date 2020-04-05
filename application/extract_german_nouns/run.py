import sys

from .extractor import GermanNounsExtractor

FIRST_CHARACTER = sys.argv[1]
FILE = sys.argv[2]

GermanNounsExtractor(FILE, [FIRST_CHARACTER]).extract()
