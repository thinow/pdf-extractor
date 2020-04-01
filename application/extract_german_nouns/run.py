import sys

from .extractor import GermanNounsExtractor

extractor = GermanNounsExtractor(
    file_path=sys.argv[1],
    from_page=int(sys.argv[2]),
    to_page=int(sys.argv[3])
)
extractor.extract()
