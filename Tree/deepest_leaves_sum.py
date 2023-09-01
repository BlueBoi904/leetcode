from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def deepest_leaves_sum(root):
    queue, queue_2 = deque([root]), deque([root])
    res = 0
    depth = 1
    curr_depth = 1
    while queue and root:
        depth += 1

        for _ in range(len(queue)):  # Continue iteration through the tree
            node = queue.popleft()
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)


    while queue_2:
        curr_depth += 1

        for _ in range(len(queue_2)):  # Continue iteration through the tree
            node = queue_2.popleft()
            if curr_depth == depth:
                res += node.val
            if node.left: queue_2.append(node.left)
            if node.right: queue_2.append(node.right)

    return res
