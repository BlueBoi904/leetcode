"""

23. Merge k Sorted Lists
Hard
15.6K
585
company
Amazon
company
Microsoft
company
Facebook
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.

    """


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# First


def merge_k_lists(lists):
    vals = []

    def traverse(node: TreeNode):
        curr = node
        while curr:
            vals.append(curr.val)
            curr = curr.next
    # Traverse all lists and add their values to arr
    for head in lists:
        # Do something here
        traverse(head)
    # Check for an empty list
    # Sort the list
    vals.sort()
    if not vals:
        return

    new_head = ListNode(vals.pop(0))
    temp = new_head
    for val in vals:
        new_node = ListNode(val)
        temp.next = new_node
        temp = temp.next

    return new_head
