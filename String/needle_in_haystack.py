"""

28. Find the Index of the First Occurrence in a String
Medium
924
73
company
Amazon
company
Bloomberg
company
Google
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
Accepted
1.5M
Submissions
3.9M
Acceptance Rate
37.7%


"""


def needle_in_hay(haystack: str, needle: str):

    # Needle not found in haystack
    return haystack.find(needle)
