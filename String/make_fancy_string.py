"""



"""


def max_fancy_string(s):
    # start with first letter of s
    res = s[0]

    # initialize count of consecutive letters to 1
    curr = 1

    for i in range(1, len(s)):
        # if current character and previous character are equal then increase count else reset to 1
        if s[i] == s[i-1]:
            curr += 1
        else:
            curr = 1

        # if count of consecutive characters is less than 3 then add the current character to result string
        if curr < 3:
            res += s[i]

    return res
