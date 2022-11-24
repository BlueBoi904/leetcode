"""

404. Sum of Left Leaves
Easy
4.1K
265
company
Bloomberg
company
Adobe
company
Apple
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0


Constraints:

The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumOfLeftLeaves(root: TreeNode) -> int:

    def process_subtree(subtree, is_left):

        # Base case: If this subtree is empty, return 0
        if subtree is None:
            return 0

        # Base case: This is a leaf node.
        if subtree.left is None and subtree.right is None:
            return subtree.val if is_left else 0

        # Recursive case: return result of adding the left and right subtrees.
        return process_subtree(subtree.left, True) + process_subtree(subtree.right, False)

    return process_subtree(root, False)
