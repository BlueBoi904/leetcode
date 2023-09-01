from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def largest_val(root: TreeNode):
    queue, res = deque([root]), []
    while queue and root:
        curr_max = float("-inf")

        for _ in range(len(queue)):  # Continue iteration through the tree
            node = queue.popleft()
            curr_max = max(curr_max,node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

        res.append(curr_max)
    return res