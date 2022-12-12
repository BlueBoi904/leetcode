"""

1682. Longest Palindromic Subsequence II
Medium
128
26
Codenation
A subsequence of a string s is considered a good palindromic subsequence if:

It is a subsequence of s.
It is a palindrome (has the same value if reversed).
It has an even length.
No two consecutive characters are equal, except the two middle ones.
For example, if s = "abcabcabb", then "abba" is considered a good palindromic subsequence, while "bcb" (not even length) and "bbbb" (has equal consecutive characters) are not.

Given a string s, return the length of the longest good palindromic subsequence in s.

 

Example 1:

Input: s = "bbabab"
Output: 4
Explanation: The longest good palindromic subsequence of s is "baab".
Example 2:

Input: s = "dcbccacdb"
Output: 4
Explanation: The longest good palindromic subsequence of s is "dccd".

"""


def longest_palindrome_subseq(s: str):
    # Track length of longest good palindromic sub.
    longest_pal = 0

    def is_good_pal(s: str):

        return True

    # Check each sub if it is a good pal, check against max length.

    return longest_pal
