from collections import defaultdict
def group_anagrams(strs: list):
    groups = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))
        groups[key].append(s)

    return groups.values()