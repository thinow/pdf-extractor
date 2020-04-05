import sys

from .extractor import GermanNounsExtractor

FILE = sys.argv[1]
FIRST_CHAR = ['a']  # TODO not hard-code the first char in the runner

GermanNounsExtractor(FILE, FIRST_CHAR).extract()
