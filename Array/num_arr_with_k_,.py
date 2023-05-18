class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        seen = set()
        i = ans = cur = 0
        for j in range(n):
            cur += nums[j]
            while nums[j] in seen or j + 1 - i > k:
                seen.remove(nums[i])
                cur -= nums[i]
                i += 1
            seen.add(nums[j])
            if j + 1 - i == k:
                ans = max(ans, cur)
        return ans or 0
