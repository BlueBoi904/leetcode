"""

    1180. Count Substrings with Only One Distinct Letter
Easy
312
48
Virtu Financial
company
Amazon
Given a string s, return the number of substrings that have only one distinct letter.



Example 1:

Input: s = "aaaba"
Output: 8
Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
"aaa" occurs 1 time.
"aa" occurs 2 times.
"a" occurs 4 times.
"b" occurs 1 time.
So the answer is 1 + 2 + 4 + 1 = 8.
Example 2:

Input: s = "aaaaaaaaaa"
Output: 55


Constraints:

1 <= s.length <= 1000
s[i] consists of only lowercase English letters.
Accepted
23.3K
Submissions
29.4K
Acceptance Rate
79.1%

    """

from collections import Counter


def count_letters(s: str):
    # Check all substrings, keep track of the number of sub strings that have one distint letter
    subs = []
    sub_counter = 0
    for i in range(len(s)):
        for j in range(i, len(s)):

            subs.append(s[i:j + 1])

    for sub in subs:
        sub_count = Counter(sub)
        if len(sub_count.keys()) == 1:
            sub_counter += 1

    return sub_counter

# Faster solution


class Solution:
    def countLetters(self, s: str) -> int:
        # Check all substrings, keep track of the number of sub strings that have one distint letter
        total = 1
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                count = 1
            total += count
        return total


count_letters("aaaba")  # => 8
count_letters("aaaaaaaaaa")  # => 55
