import os
import sys

from .extractor import GermanNounsExtractor

DIRECTORY = sys.argv[1]

FILES = [
    ('a.txt', ['A', 'Ä']),
    ('b.txt', ['B']),
    ('c.txt', ['C']),
    ('d.txt', ['D']),
    ('e.txt', ['E']),
    ('f.txt', ['F']),
    ('g.txt', ['G']),
    ('h.txt', ['H']),
    ('i.txt', ['I']),
    ('j.txt', ['J']),
    ('k.txt', ['K']),
    ('m.txt', ['M']),
    ('n.txt', ['N']),
    ('o.txt', ['O', 'Ö']),
    ('p.txt', ['P']),
    ('q.txt', ['Q']),
    ('r.txt', ['R']),
    ('s.txt', ['S']),
    ('t.txt', ['T']),
    ('u.txt', ['U', 'Ü']),
    ('v.txt', ['V']),
    ('w.txt', ['W']),
    ('x.txt', ['X']),
    ('y.txt', ['Y']),
    ('z.txt', ['Z'])
]

# validate the directory argument
if not os.path.isdir(DIRECTORY):
    raise ValueError(f'the first argument must be a directory. value = {DIRECTORY}')

# validate the content of the directory
for (file, _) in FILES:
    filepath = f'{DIRECTORY}/{file}'
    if not os.path.isfile(filepath):
        raise ValueError(f'the directory must contain the following file : {filepath}')

# extract nouns for each character
for (file, first_character) in FILES:
    filepath = f'{DIRECTORY}/{file}'
    GermanNounsExtractor(filepath, first_character).extract()
