import pytest


@pytest.mark.skip
def test_(tmpdir):
    file = build_file(tmpdir, [
        "Bbbbbbb",
        "Aaaaaaa",
        "Ccccccc",
    ])
    assert file.read() == "TBD"


def build_file(tmpdir, nouns: list):
    content = None  # TODO build content
    file = tmpdir.join("any-file.csv")
    file.write_text(content, encoding="utf-8")
    return file
