"""

16. 3Sum Closest
Medium
8.7K
466
company
Amazon
company
Adobe
company
Facebook
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

"""


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        d, ans = float("inf"), 0
        for i in range(len(nums) - 2):
            s, e = i + 1, len(nums) - 1
            while(s < e):
                sum = nums[i] + nums[s] + nums[e]
                if sum == target: return sum
                if abs(sum - target) < d:
                    d = abs(sum - target)
                    ans = sum
                if sum < target: s += 1
                else: e -= 1
        
        return ans
