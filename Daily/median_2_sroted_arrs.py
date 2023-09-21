class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Quick optimal solution in python
        nums = nums1 + nums2
        return statistics.median(nums)