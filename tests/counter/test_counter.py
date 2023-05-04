from src.pre_built.counter import count_ocurrences


def test_counter():
    path = "data/jobs.csv"

    word_counts = {
        "python": 1639,
        "javascript": 122,
    }

    for word, expected_count in word_counts.items():
        assert (
            count_ocurrences(path, word) == expected_count
        ), f"Unexpected count for {word}. Expected: {expected_count}."
        """Contagem inesperada para...""" """Esperada:"""
