"""

Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

"""

from itertools import combinations


def repeated_substring_pattern(s: str):
    # Add all substrings into a map
    i = (s+s).find(s, 1, -1)

    return i > 0


print(repeated_substring_pattern("abab"))
print(repeated_substring_pattern("aba"))
print(repeated_substring_pattern("abcabcabcabc"))
