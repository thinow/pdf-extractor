import re

# Regular expression :
# [A-ZßÄÜÖ][a-zßäüö\\|]+ reflects a capitalised word (may contain german accents and pipes)
# , ? should be followed by a comma and optionally a space
# d(ie|er|as) should be followed by a comma and an article
PATTERN = r'([A-ZßÄÜÖ][a-zßäüö\\|]+), ?d(ie|er|as)'


class GermanNounsExtractor:

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.regexp = re.compile(PATTERN)

    def extract(self) -> None:
        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file:
                for item in line.split('. '):
                    self.extract_from_line(item)

    def extract_from_line(self, line):
        match = self.regexp.match(line)
        if match:
            word = match.group(1).replace('|', '')
            article = 'd' + match.group(2)
            print(f'{word}\t{article}')
