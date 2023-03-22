"""

159. Longest Substring with At Most Two Distinct Characters
Medium
2K
32
company
Bloomberg
company
Amazon
company
Microsoft
Given a string s, return the length of the longest 
substring
 that contains at most two distinct characters.



Example 1:

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.
Example 2:

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.


Constraints:

1 <= s.length <= 105
s consists of English letters.
Accepted
224.8K
Submissions
417.9K
Acceptance Rate
53.8%

    """


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        result = 0
        chars = defaultdict(int)
        start = 0
        for i, c in enumerate(s):
            chars[c] += 1

            while len(chars) > 2:
                start_char = s[start]
                chars[start_char] -= 1
                if chars[start_char] == 0:
                    del chars[start_char]

                start += 1

            result = max(result, i - start + 1)

        return result


print(lengthOfLongestSubstringTwoDistinct("eceba"))
print(lengthOfLongestSubstringTwoDistinct("eceba"))
