from sys import stderr

from .cleaner import Cleaner, DuplicatedNounsError


def err_print(message: str):
    print(message, file=stderr)


try:
    Cleaner().clean()
except DuplicatedNounsError as cause:
    err_print("Error: the file contains duplicated nouns.")
    for duplicate in cause.get_duplicated_nouns():
        err_print(f"{duplicate['noun']}\t{','.join(duplicate['articles'])}")
