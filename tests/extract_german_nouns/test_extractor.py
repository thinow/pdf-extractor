from contextlib import redirect_stdout
from io import StringIO

from application.extract_german_nouns.extractor import GermanNounsExtractor

SAMPLE_DIR = 'tests/extract_german_nouns/resources/'


def test_extract_nouns_from_sample(snapshot):
    # given
    output = StringIO()
    extractor = GermanNounsExtractor(SAMPLE_DIR + 'sample-1.txt')

    # when
    with redirect_stdout(output):
        extractor.extract()

    # then
    getvalue: str = output.getvalue()
    snapshot.assert_match(getvalue)
