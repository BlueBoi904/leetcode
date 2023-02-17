"""

783. Minimum Distance Between BST Nodes
Easy
2.2K
351
company
Bloomberg
company
Amazon
company
Microsoft
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.



Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 100].
0 <= Node.val <= 105

"""

# Definition for a binary tree node.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# First solution


class Solution:
    def minDiffInBST(root: TreeNode) -> int:
        vals = []
        min_diff = 100000

        def dfs(node):
            if node is None:
                return
            vals.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        for i in range(len(vals) - 1):
            for j in range(i + 1, len(vals)):
                diff = abs(vals[i] - vals[j])
                min_diff = min(min_diff, diff)
        return min_diff

# Best solution


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: [TreeNode]) -> int:
        def dfs(node):
            if node:
                dfs(node.left)
                self.ans = min(self.ans, node.val - self.prev)
                self.prev = node.val
                dfs(node.right)

        self.prev = float('-inf')
        self.ans = float('inf')
        dfs(root)
        return self.ans
