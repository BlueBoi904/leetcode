"""

965. Univalued Binary Tree
Easy
1.6K
60
company
Google
Twilio
A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.



Example 1:


Input: root = [1,1,1,1,1,null,1]
Output: true
Example 2:


Input: root = [2,2,2,5,2]
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 100].
0 <= Node.val < 100

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# First attempt, dfs works well!!


def is_univaled_tree(root: Treenode):
    my_set = set()

    def dfs(node: TreeNode):
        if node is None:
            return
        my_set.add(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)

    return len(my_set) == 1

# Second attempt bfs


def isUnivaluedTree(root: TreeNode):
    val = root.val
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node.val != val:
            return False
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return True


# Faster solution

class Solution:
    def isUnivalTree(self, root) -> bool:
        def helper(curr):
            if curr == None:
                return True
            if curr.val != root.val:
                return False
            return helper(curr.left) and helper(curr.right)
        return helper(root)
