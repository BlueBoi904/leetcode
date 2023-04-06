class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:

        nums = [n for n in nums if n % 2 == 0]
        nums.sort()
        return max(nums, key=nums.count) if len(nums) > 0 else -1
