"""

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
Accepted
1.7M
Submissions
2.5M
Acceptance Rate
66.1%
Seen this question in a real interview before?
1/4

"""


def group_anagrams(strs: list):
    # create a dict to use a map holding group anagrams
    anagram_map = {}
    # We can sort each str and hold each in their own key
    res = []
    for s in strs:
        anagram = ''.join(sorted(s))
        if anagram not in anagram_map:
            anagram_map[anagram] = []

        anagram_map[anagram].append(s)

    for key in anagram_map:
        res.append(list(anagram_map[key]))

    return res


group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
group_anagrams([""])
group_anagrams(["a"])
group_anagrams(["", ""])
