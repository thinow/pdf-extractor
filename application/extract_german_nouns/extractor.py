import re

from pdfminer.high_level import extract_text

# TODO exclude unexpected words : e.g. die Renten
# TODO remove space at the end of the line
# TODO explain the regular expression

PATTERN = r'([A-Za-zßäüö\\|]+), d(ie|er|as)'
FLAGS = re.MULTILINE | re.IGNORECASE


class GermanNounsExtractor:

    def __init__(self, file_path: str, page_number: int) -> None:
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
