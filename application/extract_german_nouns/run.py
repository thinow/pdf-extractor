import sys

from .extractor import GermanNounsExtractor

extractor = GermanNounsExtractor(
    file_path=sys.argv[1], page_number=int(sys.argv[2])
)
extractor.extract()
