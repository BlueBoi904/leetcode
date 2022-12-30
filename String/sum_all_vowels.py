"""

2063. Vowels of All Substrings
Medium
591
21
Given a string word, return the sum of the number of vowels ('a', 'e', 'i', 'o', and 'u') in every substring of word.

A substring is a contiguous (non-empty) sequence of characters within a string.

Note: Due to the large constraints, the answer may not fit in a signed 32-bit integer. Please be careful during the calculations.



"""
from itertools import combinations

# First attempt, accepted but too slow


def count_vowels(word: str):
    # setup vowels list
    total = 0
    vowels = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True}

    def get_vowel_count(s: str):
        count = 0
        for char in s:
            if char in vowels:
                count += 1
        return count
    res = [word[x:y] for x, y in combinations(range(len(word) + 1), r=2)]
    for sub_str in res:
        total += get_vowel_count(sub_str)
    return total
    # Find each substring of the word and sum the vowel counts


def countVowels(word: str):
    n = len(word)
    res = 0
    for i in range(n):
        if word[i] in "aeiou":
            res += (i + 1) * (n - i)
    return res


print(count_vowels("aba"))
print(count_vowels("abc"))
print(count_vowels("ltcd"))
