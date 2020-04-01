import re

from pdfminer.high_level import extract_text

# Regular expression :
# ([A-Z] )? can be prefixed by a single character (first line of the page)
# [a-zßäüö\\|]+) reflect a word (may contain german accents and pipes)
# , d(ie|er|as) should be followed by a comma and an article
# (;|:| \(.+\):| 〈Pl) should be followed by some special patterns (semicolon, or plural between braces)
PATTERN = r'([A-Z] )?([a-zßäüö\\|]+), d(ie|er|as)(;|:| \(.+\):| 〈Pl)'
FLAGS = re.IGNORECASE


class GermanNounsExtractor:

    def __init__(self, file_path: str, page_number: int) -> None:
        self.file_path = file_path
        self.page_number = page_number

    def extract(self) -> None:
        text = extract_text(self.file_path, page_numbers=[self.page_number])
        regexp = re.compile(PATTERN, FLAGS)
        for line in text.splitlines():
            match = regexp.match(line)
            if match:
                word = match.group(2).replace('|', '')
                article = 'd' + match.group(3)
                print(f'{word}\t{article}')
