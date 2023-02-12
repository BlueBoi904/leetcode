"""

085. Sum of Digits in the Minimum Number
Easy
102
146
company
Amazon
Given an integer array nums, return 0 if the sum of the digits of the minimum integer in nums is odd, or 1 otherwise.



Example 1:

Input: nums = [34,23,1,24,75,33,54,8]
Output: 0
Explanation: The minimal element is 1, and the sum of those digits is 1 which is odd, so the answer is 0.
Example 2:

Input: nums = [99,77,33,66,55]
Output: 1
Explanation: The minimal element is 33, and the sum of those digits is 3 + 3 = 6 which is even, so the answer is 1.


Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100

"""

# First attempt solution

def sumOfDigits(self, nums: List[int]) -> int:
    min_num = min(nums)

    # Function to get sum of digits 
    def getSum(n):
        
        sum = 0
        for digit in str(n): 
        sum += int(digit)      
        return sum
    is_odd = getSum(min_num) % 2 != 0

    if is_odd:
        return 0
    else:
        return 1


