def res(nums_1, nums_2):
    s2 = set(nums2)
    s1 = set(nums1)
    return [list(s1 - s2), list(s2 - s1)]
