""""

387. First Unique Character in a String
Easy
6.9K
231
company
Amazon
company
Bloomberg
company
Microsoft
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.

"""


from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen_char = {}
        char_count = Counter(s)

        for i in range(len(s)):
            char = s[i]

            if char not in seen_char:
                seen_char[char] = 1

        def is_unique(char: str):

            return char_count[char] == 1

        for i in range(len(s)):
            char = s[i]
            if is_unique(char):
                return i

        return -1
