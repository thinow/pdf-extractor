import sys

from .extractor import GermanNounsExtractor

FILE = sys.argv[1]
FROM_PAGE = int(sys.argv[2])
TO_PAGE = int(sys.argv[3])

GermanNounsExtractor(FILE).print_nouns_from_multiple_pages(FROM_PAGE, TO_PAGE)
