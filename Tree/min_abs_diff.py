def min_abs_diff(root):
    def dfs(node):
        if not node:
            return

        left = dfs(node.left)
        values.append(node.val)
        right = dfs(node.right)

    values = []
    dfs(root)
    ans = float("inf")
    for i in range(1, len(values)):
        ans = min(ans, values[i] - values[i - 1])

    return ans
