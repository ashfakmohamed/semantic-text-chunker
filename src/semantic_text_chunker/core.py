def chunk_text(text: str, max_chars: int = 500, overlap_words: int = 8) -> list[str]:
    """Split prose into size-limited chunks while carrying word overlap forward."""
    if max_chars < 1:
        raise ValueError("max_chars must be positive")
    if overlap_words < 0:
        raise ValueError("overlap_words cannot be negative")

    words = text.split()
    if any(len(word) > max_chars for word in words):
        raise ValueError("a word is longer than max_chars")

    chunks: list[str] = []
    start = 0
    while start < len(words):
        end = start
        size = 0
        while end < len(words):
            added = len(words[end]) + (1 if end > start else 0)
            if end > start and size + added > max_chars:
                break
            size += added
            end += 1
        chunks.append(" ".join(words[start:end]))
        if end == len(words):
            break
        start = max(start + 1, end - overlap_words)
    return chunks
