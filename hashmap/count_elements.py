class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = collections.Counter(arr)
        return sum(v for k, v in count.items() if count[k + 1])


def count_elements(arr: list[int]):
    count = 0
    hash_set = set(arr)
    for x in arr:
        if (x + 1) in hash_set:
            count += 1
    return count
