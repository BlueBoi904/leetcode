from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzag_level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
    queue = [root] if root else []
    res = []
    c = 0
    while (len(queue)):
        l = len(queue)
        row = []
        for i in range(l):
            ele = queue.pop(0)
            row += [ele.val]
            if ele.left: queue.append(ele.left)
            if ele.right: queue.append(ele.right)
        if c % 2 == 0:
            res += [row]
        else:
            res += [row[::-1]]
        c += 1
    return res