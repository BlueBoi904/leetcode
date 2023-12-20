def is_subsequence(s: str, t: str) -> bool:
    count = 0
    size = len(s)
    for x in t:
        if count == size:
            break
        if x == s[count]:
            count += 1

    return size == count

