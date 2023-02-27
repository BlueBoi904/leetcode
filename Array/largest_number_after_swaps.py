"""

2231. Largest Number After Digit Swaps by Parity
Easy
413
242
ZScaler
You are given a positive integer num. You may swap any two digits of num that have the same parity (i.e. both odd digits or both even digits).

Return the largest possible value of num after any number of swaps.

 

Example 1:

Input: num = 1234
Output: 3412
Explanation: Swap the digit 3 with the digit 1, this results in the number 3214.
Swap the digit 2 with the digit 4, this results in the number 3412.
Note that there may be other sequences of swaps but it can be shown that 3412 is the largest possible number.
Also note that we may not swap the digit 4 with the digit 1 since they are of different parities.
Example 2:

Input: num = 65875
Output: 87655
Explanation: Swap the digit 8 with the digit 6, this results in the number 85675.
Swap the first digit 5 with the digit 7, this results in the number 87655.
Note that there may be other sequences of swaps but it can be shown that 87655 is the largest possible number.
 

"""


class Solution:
    def largestInteger(self, num: int) -> int:
        num = str(num)
        lst = [int(x) for x in num]
        odd_lst = [x for x in lst if x % 2 == 1]
        even_lst = [x for x in lst if x % 2 == 0]
        odd_lst = sorted(odd_lst, reverse=True)
        even_lst = sorted(even_lst, reverse=True)
        oi = ei = 0
        result = []
        for i, x in enumerate(num):
            xi = int(x)
            if xi % 2 == 1:
                result.append(odd_lst[oi])
                oi += 1
            else:
                result.append(even_lst[ei])
                ei += 1
        result = [str(x) for x in result]
        result = "".join(result)
        result = int(result)
        return result
