import sys

from .extractor import GermanNounsExtractor

FILE = sys.argv[1]

GermanNounsExtractor(FILE).extract()
