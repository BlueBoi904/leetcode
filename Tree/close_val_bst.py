class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.ans = root.val

        def helper(root):
            if root == None: return
            if abs(self.ans - target) > abs(root.val - target):
                self.ans = root.val
            elif abs(self.ans - target) == abs(root.val - target):
                if root.val < self.ans:
                    self.ans = root.val

            helper(root.left)
            helper(root.right)

        helper(root)

        return self.ans
