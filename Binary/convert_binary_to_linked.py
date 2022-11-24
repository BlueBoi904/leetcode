"""

1290. Convert Binary Number in a Linked List to Integer
Easy
3.3K
142
Oracle
company
Amazon
company
Uber
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.



Example 1:


Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0


Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.
Accepted
345K
Submissions
418K
Acceptance Rate
82.5%

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# First attempt successfull.


def convert_list_to_binary(head: ListNode):
    res = ''
    curr = head
    while curr:
        res += str(curr.val)
        curr = curr.next

    return int(res, 2)


# Faster solution

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s = ""
        while head:
            s += str(head.val)
            head = head.next
        return int(s, 2)
