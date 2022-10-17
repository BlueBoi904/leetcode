"""

Given the head of a singly linked list, reverse the list, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000


Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

"""


def reverse_list(head):
    curr = head
    # set head and prev nodes
    prev = None
    # Iterate through the linked list
    while curr:
        # hold next node in temp pointer
        next_temp = curr.next
        # set curr.next to prev
        curr.next = prev
        # set prev to curr
        prev = curr
        # set curr to next temp pointer
        curr = next_temp
    # Return prev
    return prev
