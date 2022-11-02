"""

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.



Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".
Example 3:

Input: s = "abc"
Output: 1


Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.

"""


class Solution:
    def number_of_sub_strings(self, s: str) -> int:
        results = 0
        letters = defaultdict(int)
        l = 0
        for r in range(len(s)):
            letters[s[r]] += 1
            while len(letters.keys()) == 3:
                letters[s[l]] -= 1
                if letters[s[l]] == 0:
                    del letters[s[l]]
                results += len(s) - r
                l += 1
        return results

        return count
