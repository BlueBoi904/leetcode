class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_between(head: ListNode, left: int, right: int) -> ListNode:
    if not head:
        return None

    curr = head
    prev = None

    for _ in range(left - 1):
        prev = curr
        curr = curr.next

    tail = curr
    connect = prev

    for _ in range(right - left + 1):
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    if connect:
        connect.next = prev
    else:
        head = prev

    tail.next = curr
    return head