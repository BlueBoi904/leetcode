"""

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.



Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false

"""

# First quick attempt, very slow memory and time complexity


def detect_capital(word: str):
    return word.isupper() or word.islower() or word.istitle()


# Optimized attempt

def detectCapital(word: str):
    return len(word) == 1 or word[1:].islower() or word.isupper()


print(detect_capital("USA"))  # => True

print(detect_capital("FlaG"))  # => False
