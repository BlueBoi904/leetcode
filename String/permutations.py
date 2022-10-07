"""

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.


"""
from collections import Counter


def check_inclusion(s1, s2):
    s1_count = Counter(s1)
    s2_count = Counter(s2)
    print(s1_count)
    print(s2_count)
    pass


check_inclusion("ab", "eidbaooo")
