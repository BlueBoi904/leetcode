# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middle_node(head: [ListNode]) -> [ListNode]:
    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow

