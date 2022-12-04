from collections import Counter


class Solution:
    def isMajorityElement(self, nums: list[int], target: int) -> bool:
        return Counter(nums)[target] > (len(nums) / 2)
