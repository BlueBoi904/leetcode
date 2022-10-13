"""

1108. Defanging an IP Address
Easy
1.3K
1.6K
company
Facebook

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".



Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"



Constraints:

The given address is a valid IPv4 address.

Accepted
453K
Submissions
507.2K
Acceptance Rate
89.3%

"""

# First attempt


def defangIPaddr(address):
    res = []
    for char in address:
        to_add_char = char
        if char == ".":
            to_add_char = '[.]'

        res.append(to_add_char)

    return ''.join(res)
