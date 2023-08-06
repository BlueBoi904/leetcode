class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        run_sum = 0
        res = []
        for num in nums:
            run_sum += num
            res.append(run_sum)

        return res
