# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
