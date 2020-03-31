import re

from pdfminer.high_level import extract_text

# TODO exclude unexpected words : e.g. die Renten
# TODO explain the regular expression

# Regular expression :
# [A-Za-zßäüö\\|]+) matches all the words (can contain accents and pipes)
# , d(ie|er|as) matches the words only followed by a comma and an article
PATTERN = r'([A-Za-zßäüö\\|]+), d(ie|er|as)'
FLAGS = re.IGNORECASE


class GermanNounsExtractor:

    def __init__(self, file_path: str, page_number: int) -> None:
        self.file_path = file_path
        self.page_number = page_number

    def extract(self) -> None:
        text = extract_text(self.file_path, page_numbers=[self.page_number])
        for line in text.splitlines():
            match = re.match(PATTERN, line, FLAGS)
            if match:
                word = match.group(1).replace('|', '')
                article = 'd' + match.group(2)
                print(f'{word}\t{article}')
