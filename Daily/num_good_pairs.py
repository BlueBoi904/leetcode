from collections import defaultdict


def num_identical_pairs(nums: list[int]) -> int:
    counts = defaultdict(int)
    ans = 0

    for num in nums:
        ans += counts[num]
        counts[num] += 1

    return ans
