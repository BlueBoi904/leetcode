"""

1044. Longest Duplicate Substring
Hard
2K
369
company
Amazon
company
Apple
company
Google

Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".

 

Example 1:

Input: s = "banana"
Output: "ana"

Example 2:

Input: s = "abcd"
Output: ""

 

Constraints:

    2 <= s.length <= 3 * 104
    s consists of lowercase English letters.

Accepted
62.1K
Submissions
203.2K
Acceptance Rate
30.6%

"""

from collections import defaultdict
from functools import reduce
from itertools import accumulate

from collections import Counter
# First attempt

def longestDupSubstring(s: str) -> str:
    longest_duplicate = ""
    res = [s[i: j] for i in range(len(s))
           for j in range(i + 1, len(s) + 1)]
    counts = Counter(res)
    for key in counts:
        if counts[key] > 1:
            if len(key) > len(longest_duplicate):
                longest_duplicate = key
    
    return longest_duplicate

# Optimized solution



class Solution:
    def longestDupSubstring(self, s: str) -> str:
        suffixes, ans = sorted([s[-i:] for i in range(1, len(s) + 1)]), ""
        for s1, s2 in zip(suffixes[::-1], suffixes[-2::-1]):  # faster w/ ::-1
            i = len(ans)  # to compare first i chars of s1, s2 faster
            if s1[:i] != s2[:i]:  # includes len(s1)<i or len(s2)<i (s1!=s2)
                continue
            ans = s1[:i]
            # for x, y in zip(s1[i:], s2[i:]):
            #     if x != y:
            #         break
            #     ans += x
            while i < min(len(s1), len(s2)) and s1[i] == s2[i]:
                i = i + 1
            ans = s1[:i]
        return ans


print(longestDupSubstring("banana"))  # => "ana"
print(longestDupSubstring("abcd"))  # => ""
