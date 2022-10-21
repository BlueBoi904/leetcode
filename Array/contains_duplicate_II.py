"""

219. Contains Duplicate II
Easy
4K
2.3K
company
Airbnb
company
Palantir Technologies
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.



Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105

"""


def containsNearbyDuplicate(nums: list, k: int):
    lookup = {}

    for i in range(len(nums)):
        num = nums[i]
        # If num is present in lookup and satisfy the condition return True
        if num in lookup and abs(lookup[num]-i) <= k:
            return True

        # If num is not present in lookup then add it to lookup
        lookup[num] = i

    return False


print(containsNearbyDuplicate([1, 2, 3, 1], 3))  # => true
print(containsNearbyDuplicate([1, 0, 1, 1], 1))  # => true
print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # => false
