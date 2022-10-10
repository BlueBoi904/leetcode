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
    n, m = len(s1), len(s2)

    if n > m:
        return False

    target_hash = sum(hash(char) for char in s1)
    cur_hash = sum(hash(char) for char in s2[:n])

    if cur_hash == target_hash:
        return True

    # sliding window
    for right in range(n, m):

        # remove the pass char and add the new char
        left = right - n
        cur_hash += hash(s2[right]) - hash(s2[left])

        if cur_hash == target_hash:
            return True

    return False


check_inclusion("ab", "eidbaooo")
