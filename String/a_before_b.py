"""

Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string. Otherwise, return false.



Example 1:

Input: s = "aaabbb"
Output: true
Explanation:
The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
Hence, every 'a' appears before every 'b' and we return true.
Example 2:

Input: s = "abab"
Output: false
Explanation:
There is an 'a' at index 2 and a 'b' at index 1.
Hence, not every 'a' appears before every 'b' and we return false.
Example 3:

Input: s = "bbb"
Output: true
Explanation:
There are no 'a's, hence, every 'a' appears before every 'b' and we return true.


Constraints:

1 <= s.length <= 100
s[i] is either 'a' or 'b'.

"""

from collections import Counter


def check_string(s: str):
    counts = Counter(s)
    a_count = counts['a']
    curr_a_count = 0

    for char in s:
        if char == 'a':
            curr_a_count += 1

        else:
            if curr_a_count != a_count:
                return False

    return True


print(check_string("aaabbb"))
print(check_string("abab"))
print(check_string("bbb"))
