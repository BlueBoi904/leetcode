from collections import Counter


def ransom_note(ransom_note: str, magazine: str):
    mag = Counter(magazine)
    note = Counter(ransom_note)
    return all(mag[c] >= note[c] for c in note)

print(ransom_note("a", "b"))

print(ransom_note("aa", "ab"))

print(ransom_note("aa", "aab"))

