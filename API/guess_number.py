"""

374. Guess Number Higher or Lower
Easy
1.9K
256
company
Apple
company
Bloomberg
company
Adobe
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.



Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1


Constraints:

1 <= n <= 231 - 1
1 <= pick <= n

"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


def guessNumber(n) -> int:
    # Question lends itself to binary search, call api and half the input and adjust rather than calling the function on all inputs up to n.
    l, r = 0, n

    while l <= r:
        mid = (l + r) // 2
        if guess(mid) == 0:
            return mid
        elif guess(mid) == 1:
            l = mid + 1
        else:
            r = mid - 1

    return
