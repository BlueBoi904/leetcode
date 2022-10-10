"""

Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]

"""


def remove_nth_node(head, n: int):
    fast = slow = head

    for i in range(n):
        fast = fast.next

    if not fast:
        return head.next
    # then advance both fast and slow now they are nth postions apart
    # when fast gets to None, slow will be just before the item to be deleted
    while fast.next:
        slow = slow.next
        fast = fast.next
    # delete the node
    slow.next = slow.next.next
    return head
