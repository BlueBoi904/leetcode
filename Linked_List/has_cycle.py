# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# First attempt, caching
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cache = {}
        curr = head

        while curr:
            curr = curr.next
            if curr in cache:
                return True
            cache[curr] = True

        return False


# Optimized solution


def hasCycle(head: Optional[ListNode]) -> bool:
    node_1, node_2 = head, head

    while node_2 and node_2.next:
        node_1 = node_1.next
        node_2 = node_2.next.next
        if node_1 == node_2:
            return True

    return False
