class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        # [1] sum of all numbers from 1 to n
        s = len(nums)*(len(nums)+1) // 2

        # [2] sum of all numbers in 'nums'
        a = sum(nums)

        # [3] sum of unique numbers in 'nums'
        u = sum(set(nums))

        # [4] the duplicate and missing numbers are
        return [a-u, s-u]
