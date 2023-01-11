"""

You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

 

Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
Example 2:

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.
Example 3:

Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.


"""

from collections import Counter


def count_consistent_strings(allowed: str, words: list[str]) -> int:
    count = 0

    def is_good_word(word: str, allowed_char_map=Counter(allowed)):
        # Return true or false

        for char in word:
            if char not in allowed_char_map:
                return False

        return True

    for word in words:
        if is_good_word(word):
            count += 1

    return count
