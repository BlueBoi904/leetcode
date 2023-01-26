"""

897. Increasing Order Search Tree
Easy
3.7K
641
company
Adobe
company
Facebook
company
Amazon
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.



Example 1:


Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
Example 2:


Input: root = [5,1,7]
Output: [1,null,5,null,7]


Constraints:

The number of nodes in the given tree will be in the range [1, 100].
0 <= Node.val <= 1000

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# First attempt, success!
def increasingBST(root: TreeNode) -> TreeNode:
    # Inorder Traversal
    nodes = []

    def dfs(node: TreeNode):
        if node is None:
            return

        dfs(node.left)

        nodes.append(node.val)

        dfs(node.right)

    dfs(root)

    # Now arrange the values in nodes into a tree with only right children
    new_root = TreeNode(nodes[0].val)
    curr = new_root
    for i in range(1, len(nodes)):
        curr.right = TreeNode(nodes[i])
        curr = curr.right

    return new_root


# Optimized solution

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right
