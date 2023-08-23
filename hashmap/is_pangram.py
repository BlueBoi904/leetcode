from collections import Counter


def check_if_pangram(sentence: str) -> bool:
    counts = Counter(sentence)
    return len(counts.keys()) == 26


