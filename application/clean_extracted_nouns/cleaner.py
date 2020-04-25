class Cleaner:
    def clean(self):
        raise DuplicatedNounsError([
            {'noun': 'foo', 'articles': ['der', 'die']},
            {'noun': 'bar', 'articles': ['der', 'das']}
        ])


class DuplicatedNounsError(Exception):

    def __init__(self, duplicates: list) -> None:
        self.duplicates = duplicates

    def get_duplicated_nouns(self) -> list:
        return self.duplicates
