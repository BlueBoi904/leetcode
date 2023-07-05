from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = Counter(nums)

        for count in counts:
            if counts[count] == 1:
                return count
