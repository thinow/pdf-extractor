import re

from pdfminer.high_level import extract_text

# TODO include words really first word : Auf|bau|schu|le

# Regular expression :
# [a-zßäüö\\|]+) reflect a word (may contain german accents and pipes)
# , d(ie|er|as) should be followed by a comma and an article
# (;|:| \(.+\):| 〈Pl) should be followed by some special patterns (semicolon, or plural between braces)
PATTERN = r'([a-zßäüö\\|]+), d(ie|er|as)(;|:| \(.+\):| 〈Pl)'
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
                word = match.group(1).replace('|', '')
                article = 'd' + match.group(2)
                print(f'{word}\t{article}')
