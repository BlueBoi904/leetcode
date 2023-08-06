class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        avgList = [-1] * len(nums)
        rollingSum, length = 0, 2 * k

        for i in range(len(nums)):
            rollingSum += nums[i]
            if i >= length:
                avgList[i - k] = rollingSum // (length + 1)
                rollingSum -= nums[i - length]

        return avgList
