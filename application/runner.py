import sys

from pdfminer.high_level import extract_text

FILE = sys.argv[1]
PAGE_NUMBER = int(sys.argv[2])

text = extract_text(FILE, page_numbers=[PAGE_NUMBER])

print(text)
