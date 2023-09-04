# First solution works well
def range_sum_bst(root, low: int, high: int):
    self.sum = 0

    def dfs(node):
        if node is None:
            return

        val = node.val

        if val <= high and val >= low:
            self.sum += val
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return self.sum

# Using stack
def range_sum(root, low: int, high: int):
    r = 0
    stack = [root]
    while stack:
        c = stack.pop()
        if c:
            if low <= c.val <= high:
                r += c.val
            if c.val > low:
                stack.append(c.left)
            if c.val < high:
                stack.append(c.right)
    return r

# Optimized solution using binary search

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        ans = 0
        if low <= root.val <= high:
            ans += root.val
        if low < root.val:
            ans += self.rangeSumBST(root.left, low, high)
        if root.val < high:
            ans += self.rangeSumBST(root.right, low, high)

        return ans

