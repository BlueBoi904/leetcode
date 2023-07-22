class Solution:
    def sub_arr_sum(self, nums: List[int], k: int) -> int:
        data = {0: 1}
        curr_sum = 0
        count = 0
        for x in nums:
            curr_sum += x
            count += data.get(curr_sum - k, 0)
            data[curr_sum] = data.get(curr_sum, 0) + 1
        return count
