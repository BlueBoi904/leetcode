"""

Example 2: 2294. Partition Array Such That Maximum Difference Is K

Given an integer array nums and an integer k, split nums into subsequences, where each subsequences' maximum and minimum element is within k of each other.

What is the minimum number of subsequences needed?

For example, given nums = [3, 6, 1, 2, 5] and k = 2, the answer is 2. The subsequences are [3, 1, 2] and [6, 5].

"""


class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        ans = 1
        x = nums[0]

        for i in range(1, len(nums)):
            if nums[i] - x > k:
                x = nums[i]
                ans += 1

        return ans