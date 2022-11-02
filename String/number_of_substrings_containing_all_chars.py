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

from itertools import combinations


class Solution:
    def __init__(self) -> None:
        self.sub_count = 0

    def numberOfSubstrings(self, s: str) -> int:
        def get_all_substrings(string):
            length = len(string) + 1
            return [string[x:y] for x, y in combinations(range(length), r=2)]

        subs = get_all_substrings(s)
        for sub in subs:
            if 'a' in sub and 'b' in sub and 'c' in sub:
                self.sub_count += 1
        return self.sub_count


def number_of_sub_strings(s: str):
    left = ans = curr = 0

    for right in range(len(arr)):
        # do logic here to add arr[right] to curr

        while WINDOW_CONDITION_BROKEN:
            # remove arr[left] from curr
            left += 1

        # update ans

    return ans


print(Solution().numberOfSubstrings("abcabc"))  # => 10
