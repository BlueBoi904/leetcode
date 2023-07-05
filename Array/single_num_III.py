from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        res = []
        for count in counts:
            if counts[count] == 1:
                res.append(count)
        return res
