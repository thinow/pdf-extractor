import re

from pdfminer.high_level import extract_text

# TODO include accents [A-Za-zÀ-ÖØ-öø-ÿ]
# TODO exclude unexpected words : e.g. die Renten
# TODO explain the regular expression

PATTERN = r'([A-Z\\|]+), d(ie|er|as)'
FLAGS = re.MULTILINE | re.IGNORECASE


class GermanNounsExtractor:

    def __init__(self, file_path, page_number) -> None:
        self.file_path = file_path
        self.page_number = page_number

    def extract(self) -> None:
        text = extract_text(self.file_path, page_numbers=[self.page_number])
        for line in text.splitlines():
            match = re.match(PATTERN, line, FLAGS)
            if match:
                article = 'd' + match.group(2)
                word = match.group(1).replace('|', '')
                print(f'{article} {word} ')
