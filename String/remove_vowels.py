"""

Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.



Example 1:

Input: s = "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
Example 2:

Input: s = "aeiou"
Output: ""

"""


def remove_vowels(s):
    # Remove any char that is a va
    new_string = ''
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    for char in s:
        if char not in vowel_list:
            new_string += char

    return new_string
