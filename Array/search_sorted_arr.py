class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i

        return -1


def search(nums, target: int) -> int:
    try:
        return nums.index(target)
    except:
        return -1
