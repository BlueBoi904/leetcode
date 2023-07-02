"""



"""

from collections import Counter


class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        counts = Counter(nums)
        res = []
        for count in counts:
            if counts[count] == 1:
                res.append(count)

        res.sort()
        if len(res):
            return res[-1]
        else:
            return -1
