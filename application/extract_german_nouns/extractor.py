import re

from pdfminer.high_level import extract_text

# TODO include Aal|strich, der [nach der schmalen, länglichen Form] (Zool.): l

# Regular expression :
# ([A-Z] )? can be prefixed by a single character (first line of the page)
# [a-zßäüö\\|]+) reflect a word (may contain german accents and pipes)
# , d(ie|er|as) should be followed by a comma and an article
# (;|:| \(.+\):| 〈Pl) should be followed by some special patterns (semicolon, or plural between braces)
PATTERN = r'([A-Z] )?([a-zßäüö\\|]+), d(ie|er|as)(;|:| \(.+\):| 〈Pl)'
FLAGS = re.IGNORECASE


class GermanNounsExtractor:

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.regexp = re.compile(PATTERN, FLAGS)

    def print_nouns_from_multiple_pages(self, from_page: int, to_page: int) -> None:
        for page_number in range(from_page, to_page + 1):
            self.print_nouns_from_single_page(page_number)

    def print_nouns_from_single_page(self, page) -> None:
        text = self.extract_text(page)
        for line in text.splitlines():
            match = self.regexp.match(line)
            if match:
                word = match.group(2).replace('|', '')
                article = 'd' + match.group(3)
                print(f'{word}\t{article}')

    def extract_text(self, page) -> str:
        return extract_text(self.file_path, page_numbers=[page - 1])
