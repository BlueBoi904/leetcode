"""

345. Reverse Vowels of a String
Easy
2.4K
2.1K
company
Apple
company
Yahoo
company
Uber
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.



Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"


Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

"""


def reverseVowels(s: str):
    vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}

    # Convert s to list for fast sweep
    s = list(s)

    # initialize two pointers at the two ends
    left = 0
    right = len(s)-1

    # left and right are moving toward each other
    # but they should't cross each other
    while left < right:

        # if both pointers are on vowels, sweep them.
        if s[left] in vowels and s[right] in vowels:
            s[left], s[right] = s[right], s[left]
            right -= 1
            left += 1

        # if any pointer is not on a vowel, move it by 1.
        elif s[left] not in vowels:
            left += 1
        else:
            right -= 1

    # join the modified list as a string and return it
    return ''.join(s)


print(reverseVowels("hello"))  # => "holle"
