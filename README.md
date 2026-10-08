# Semantic Text Chunker

A dependency-free Python utility for splitting prose into LLM-friendly chunks with deterministic word overlap.

## Highlights

- Enforces a configurable character budget
- Preserves context with overlapping words
- Rejects invalid limits and impossible single-token inputs
- Includes tests, Ruff, and GitHub Actions

```python
from semantic_text_chunker import chunk_text

chunks = chunk_text(long_document, max_chars=500, overlap_words=12)
```

Run `pip install -r requirements-dev.txt`, then `ruff check .` and `python -m pytest -q`.

No license has been selected; all rights are reserved.
