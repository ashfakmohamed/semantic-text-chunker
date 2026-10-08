import pytest

from semantic_text_chunker import chunk_text


def test_chunks_respect_limit_and_overlap():
    chunks = chunk_text("one two three four five six seven", max_chars=13, overlap_words=1)
    assert all(len(chunk) <= 13 for chunk in chunks)
    assert chunks[0].split()[-1] == chunks[1].split()[0]


def test_rejects_impossible_single_word():
    with pytest.raises(ValueError):
        chunk_text("extraordinary", max_chars=5)
