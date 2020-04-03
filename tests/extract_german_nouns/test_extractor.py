import pytest

from contextlib import redirect_stdout
from io import StringIO

from application.extract_german_nouns.extractor import GermanNounsExtractor

SAMPLE_DIR = 'tests/extract_german_nouns/resources/'


@pytest.mark.parametrize("file", ['sample-0.txt', 'sample-1.txt'])
def test_extract_nouns_from_sample(snapshot, file):
    # given
    output = StringIO()
    extractor = GermanNounsExtractor(SAMPLE_DIR + file)

    # when
    with redirect_stdout(output):
        extractor.extract()

    # then
    snapshot.assert_match(output.getvalue())
