

def min_abs_diff(root):
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
