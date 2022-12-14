"""

Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

 

Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
 

Constraints:

The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.

"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.total_sum = 0

    def rangeSumBST(self, root: list[TreeNode], low: int, high: int) -> int:

        def dfs(node):
            if node is None:
                return

            if node.val >= low and node.val <= high:
                self.total_sum += node.val

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return self.total_sum


# Faster solution

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root == None:
            return 0
        if (root.val < low or root.val > high):
            return self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        else:
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)


# Using stack

def rangeSumBST(self, root: list[TreeNode], low: int, high: int) -> int:
    r = 0
    q = [root]
    while q:
        c = q.pop()
        if c:
            if low <= c.val <= high:
                r += c.val
            if c.val > low:
                q.append(c.left)
            if c.val < high:
                q.append(c.right)
    return r
