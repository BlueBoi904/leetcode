# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        pass

    def findSecondMinimumValue(self, root]) -> int:
        if root.left is None:
            return -1

        left, right = root.left.val, root.right.val
        if left == root.val:
            left = self.findSecondMinimumValue(root.left)
        if right == root.val:
            right = self.findSecondMinimumValue(root.right)

        return min(left, right) if left != -1 and right != -1 else max(left, right)
