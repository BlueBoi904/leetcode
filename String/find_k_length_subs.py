"""

1100. Find K-Length Substrings With No Repeated Characters
Medium
470
9
company
Amazon
Given a string s and an integer k, return the number of substrings in s of length k with no repeated characters.



Example 1:

Input: s = "havefunonleetcode", k = 5
Output: 6
Explanation: There are 6 substrings they are: 'havef','avefu','vefun','efuno','etcod','tcode'.
Example 2:

Input: s = "home", k = 5
Output: 0
Explanation: Notice k can be larger than the length of s. In this case, it is not possible to find any substring.


Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
1 <= k <= 104

"""


def k_len_subs(s: str, k: int):
    l = 0

    for r in len(s):
        pass


print(k_len_subs("havefunonleetcode", 5))  # => 6
