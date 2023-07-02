# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self, val=0, left=None, right=None):
        self.res = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            self.res.append(node.val)
            dfs(node.right)

        dfs(root)
        return self.res


class Solution_2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        dfs = []
        res = []
        curr = root
        while curr is not None or dfs:
            while curr is not None:
                dfs.append(curr)
                curr = curr.left

            curr = dfs.pop()
            res.append(curr.val)
            curr = curr.right

        return res
