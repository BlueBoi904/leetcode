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
        a = b = c = 0                        # counter for letter a/b/c
        ans, i, n = 0, 0, len(s)             # i: slow pointer
        for j, letter in enumerate(s):       # j: fast pointer
            if letter == 'a':
                a += 1         # increment a/b/c accordingly
            elif letter == 'b':
                b += 1
            else:
                c += 1
            while a > 0 and b > 0 and c > 0:  # if all of a/b/c are contained, move slow pointer
                # count possible substr, if a substr ends at j, then there are n-j substrs to the right that are containing all a/b/c
                ans += n-j
                if s[i] == 'a':
                    a -= 1       # decrement counter accordingly
                elif s[i] == 'b':
                    b -= 1
                else:
                    c -= 1
                i += 1                       # move slow pointer
        return ans


print(number_of_sub_strings("abcabc"))  # => 10
