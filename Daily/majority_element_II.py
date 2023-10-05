class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        target = len(nums) // 3
        d = Counter(nums)

        for key in d:
            if d[key] > target:
                ans.append(key)

        return ans

