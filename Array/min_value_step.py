class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        return max(1, 1 - min(accumulate(nums)))
