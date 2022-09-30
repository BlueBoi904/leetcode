"""

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

 

Constraints:

    The number of nodes in the list is in the range [1, 100].
    1 <= Node.val <= 100



"""


def middleNode(head, n):
    # Check edge case
    fast = head

    slow = head

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
