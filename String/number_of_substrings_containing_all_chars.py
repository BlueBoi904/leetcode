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

import collections


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        j, result, counter = 0, 0, collections.Counter()
        for i, c in enumerate(s):
            counter[c] += 1
            while len(counter) == 3:
                result += len(s) - i
                counter[s[j]] -= 1
                if not counter[s[j]]:
                    del counter[s[j]]
                j += 1
        return result


print(number_of_sub_strings("abcabc"))  # => 10
