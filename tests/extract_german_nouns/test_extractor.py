from contextlib import redirect_stdout
from io import StringIO

from application.extract_german_nouns.extractor import GermanNounsExtractor

SAMPLE_DICTIONARY = 'tests/extract_german_nouns/duden_dictionary_sample.pdf'
ANY_PAGE = 152


def test_extract_sample_of_dictionary(snapshot):
    # given
    extractor = GermanNounsExtractor(SAMPLE_DICTIONARY, ANY_PAGE)
    output = StringIO()

    # when
    with redirect_stdout(output):
        extractor.extract()

    # then
    snapshot.assert_match(output.getvalue(), 'german_nouns_from_sample')
