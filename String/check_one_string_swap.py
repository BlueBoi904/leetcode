"""

1790. Check if One String Swap Can Make Strings Equal
Easy
738
35
company
Bloomberg
company
DoorDash
company
Square
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.



Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".
Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.
Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.


Constraints:

1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.


"""

from collections import Counter

def areAlmostEqual(s1: str, s2: str) -> bool:
    count = 0
    for ch1, ch2 in zip(s1, s2):
        if ch1 != ch2:
            count += 1
    return (Counter(s1) == Counter(s2)) and (count == 0 or count == 2)


areAlmostEqual("bank", "kanb")
areAlmostEqual("attack", "defend")
areAlmostEqual("kelb", "kelb")
