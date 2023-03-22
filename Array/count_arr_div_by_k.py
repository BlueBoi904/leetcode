"""

2183. Count Array Pairs Divisible by K
Hard
666
33
company
tcs
company
Paypal
Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) such that:

0 <= i < j <= n - 1 and
nums[i] * nums[j] is divisible by k.


Example 1:

Input: nums = [1,2,3,4,5], k = 2
Output: 7
Explanation:
The 7 pairs of indices whose corresponding products are divisible by 2 are
(0, 1), (0, 3), (1, 2), (1, 3), (1, 4), (2, 3), and (3, 4).
Their products are 2, 4, 6, 8, 10, 12, and 20 respectively.
Other pairs such as (0, 2) and (2, 4) have products 3 and 15 respectively, which are not divisible by 2.
Example 2:

Input: nums = [1,2,3,4], k = 5
Output: 0
Explanation: There does not exist any pair of indices whose corresponding product is divisible by 5.


Constraints:

1 <= nums.length <= 105
1 <= nums[i], k <= 105

    """


import math
from collections import Counter


def countPairs(nums: list[int], k: int):
    cnt = Counter(math.gcd(n, k) for n in nums)
    res = 0
    for n in cnt:
        for b in cnt:
            if n <= b and n*b % k == 0:
                res += cnt[n]*cnt[b] if n < b else cnt[n]*(cnt[n]-1) // 2
    return res
