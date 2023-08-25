# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(head: [ListNode]) -> [ListNode]:
    if head is None:
        return head
    fast = head.next
    slow = head
    while fast:
        fast = fast.next
        slow = slow.next


