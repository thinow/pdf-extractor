import pytest

from contextlib import redirect_stdout
from io import StringIO

from application.extract_german_nouns.extractor import GermanNounsExtractor

SAMPLE_DIR = 'tests/extract_german_nouns/resources/'

SAMPLE_FILES = [
    'sample-0.txt',
    'sample-1.txt',
    'sample-2.txt'
]


@pytest.mark.parametrize("file", SAMPLE_FILES)
def test_extract_nouns_from_sample(snapshot, file):
    # given
    output = StringIO()
    extractor = GermanNounsExtractor(
        file_path=SAMPLE_DIR + file,
        first_character=['a', 'ä']
    )

    # when
    with redirect_stdout(output):
        extractor.extract()

    # then
    snapshot.assert_match(output.getvalue())
