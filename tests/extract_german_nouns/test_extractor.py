from contextlib import redirect_stdout
from io import StringIO

from application.extract_german_nouns.extractor import GermanNounsExtractor

SAMPLE_DICTIONARY = 'tests/extract_german_nouns/resources/duden_dictionary_sample.pdf'
ANY_PAGE = 153


def test_print_nouns_from_single_page_of_dictionary_sample(snapshot):
    # given
    output = StringIO()
    extractor = GermanNounsExtractor(SAMPLE_DICTIONARY)

    # when
    with redirect_stdout(output):
        extractor.print_nouns_from_single_page(ANY_PAGE)

    # then
    snapshot.assert_match(output.getvalue())


def test_extract_text_from_pdf(snapshot):
    # given
    extractor = GermanNounsExtractor(SAMPLE_DICTIONARY)

    # when
    text = extractor.extract_text(50)

    # then
    snapshot.assert_match(text)
