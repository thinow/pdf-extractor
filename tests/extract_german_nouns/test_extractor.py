from contextlib import redirect_stdout
from io import StringIO

from application.extract_german_nouns.extractor import GermanNounsExtractor

SAMPLE_DICTIONARY = 'tests/extract_german_nouns/resources/duden_dictionary_sample.pdf'
ANY_PAGE = 153


def test_extract_single_page_of_dictionary_sample(snapshot):
    # given
    output = StringIO()
    extractor = GermanNounsExtractor(
        SAMPLE_DICTIONARY,
        from_page=ANY_PAGE,
        to_page=ANY_PAGE
    )

    # when
    with redirect_stdout(output):
        extractor.extract()

    # then
    snapshot.assert_match(output.getvalue())
