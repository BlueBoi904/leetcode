"""

1662. Check If Two String Arrays are Equivalent
Easy
1.9K
170
company
Apple
company
Facebook
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

 

Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
 
"""


def array_strings_are_equal(word1, word2):
    return ''.join(word1) == ''.join(word2)


print(array_strings_are_equal(["ab", "c"], ["a", "bc"]))
print(array_strings_are_equal(["abc", "d", "defg"], ["abcddefg"]))
