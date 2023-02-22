"""

316. Remove Duplicate Letters
Medium
6.5K
419
company
Amazon
Oracle
company
Google
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is
the smallest in lexicographical order
among all possible results.



Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"


Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.

"""


def removeDuplicateLetters(s: str) -> str:
    # Create a set
    rindex = {c: i for i, c in enumerate(s)}
    stack = []
    for i, c in enumerate(s):
        if c not in stack:
            while stack and c < stack[-1] and i < rindex[stack[-1]]:
                stack.pop()
            stack.append(c)
        # else: c exists in stack
        # if stack[-1] == c: don't need to need to delete stack[-1] and append c
        # if stack[j] == c and j < len(stack) - 1: because of the stack properties,
        # the stack is lexicographically smaller than the new one after deleting stack[j] and appending c
    return ''.join(stack)


print(removeDuplicateLetters("bcabc"))
