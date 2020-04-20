from contextlib import redirect_stdout
from io import StringIO

import pytest

from application.extract_german_nouns.extractor import GermanNounsExtractor

SAMPLE_DIR = 'tests/extract_german_nouns/resources/'

SAMPLES = [
    ('sample-0.txt', ['a', 'ä']),
    ('sample-1.txt', ['a', 'ä']),
    ('sample-2.txt', ['a', 'ä']),
]


@pytest.mark.parametrize("sample", SAMPLES)
def test_extract_nouns_from_sample(snapshot, sample):
    # given
    file, first_character = sample

    output = StringIO()
    extractor = GermanNounsExtractor(
        file_path=SAMPLE_DIR + file,
        first_character=first_character
    )

    # when
    with redirect_stdout(output):
        extractor.extract()

    # then
    snapshot.assert_match(output.getvalue())
