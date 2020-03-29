import sys
import re

from pdfminer.high_level import extract_text

FILE = sys.argv[1]
PAGE_NUMBER = int(sys.argv[2])

text = extract_text(FILE, page_numbers=[PAGE_NUMBER])

pattern = r'([A-Z\\|]+), d(ie|er|as)'  # TODO include accents
flags = re.MULTILINE | re.IGNORECASE

for line in text.splitlines():
    match = re.match(pattern, line, flags)
    if match:
        article = 'd' + match.group(2)
        word = match.group(1).replace('|', '')
        print(f'{article} {word} ')

# TODO exlude unexpected words : e.g. die Renten
