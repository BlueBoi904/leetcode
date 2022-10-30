class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        # keep track of the number of good pairs
        good_pairs_count = 0
        # Use a hash map to hold num as key and index as value

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    good_pairs_count += 1

        return good_pairs_count
