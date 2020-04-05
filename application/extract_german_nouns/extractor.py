import re

# Regular expression :
# [{first_character}][a-zßäüö\\|]+ reflects a capitalised word (may contain german accents and pipes)
# , ? should be followed by a comma and optionally a space
# d(ie|er|as) should be followed by a comma and an article
PATTERN = '([{first_character}][a-zßäüö\\|]+), ?d(ie|er|as)'


# TODO require first letters as an argument

# TODO include lines with hints in-between
# Au|ber|gi|ne [...], die;

class GermanNounsExtractor:

    def __init__(self, file_path: str, first_character: list) -> None:
        self.file_path = file_path
        self.regexp = self.compile_regexp(first_character)

    @staticmethod
    def compile_regexp(first_character: list):
        first_character_as_str = ''.join(first_character).upper()
        return re.compile(
            PATTERN.format(first_character=first_character_as_str)
        )

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
