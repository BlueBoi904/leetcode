"""

148. Sort List
Medium
8.7K
269
company
Amazon
company
Apple
company
TikTok
Given the head of a linked list, return the list after sorting it in ascending order.



Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105


Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

"""

# Attempt #1


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sort_list(head: ListNode):
    if head is None:
        return None

    curr = head

    res = []
    while curr:
        res.append(curr.val)
        curr = curr.next

    res.sort()

    new_head = None
    for i in range(len(res)):
        new_head.next = ListNode(res[i])

    return new_head.next

# Attempt #2


class Solution:
    # Sort the list
    def sortList(self, head):
        if not head or not head.next:
            return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    # Get the middle of a linked list
    def getMid(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid
    # Merge the two lists

    def merge(self, head1, head2):
        dummy = tail = ListNode(None)
        while head1 and head2:
            if head1.val < head2.val:
                tail.next, tail, head1 = head1, head1, head1.next
            else:
                tail.next, tail, head2 = head2, head2, head2.next

        tail.next = head1 or head2
        return dummy.next


"""
Attempt #1 ->

    Runtime: 405 ms Beats 96.24%
    Memory: 45.1 MB Beats 8.23%




Attempt #2 ->

    Complexity: Time complexity is O(n log n), because it is classical complexity of merge sort. 

    Space complexity is O(log n), because we use recursion which can be log n deep.

    Runtime: 1821 ms Beats26.96%
            
    Memory: 36.5 MB Beats 55.37%




"""
