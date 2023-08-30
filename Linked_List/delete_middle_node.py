# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_middle(head: [ListNode]) -> [ListNode]:
    fast = slow = head
    if fast.next:
        fast = fast.next
    else:
        return None
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    slow.next = slow.next.next

    return head
