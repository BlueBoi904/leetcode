# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


def max_level_sum(root) -> int:
    q = deque()
    q.append(root)
    total = float('-inf')
    level = 0
    depth = 1
    while q:
        curr = sum([node.val for node in q])
        if curr > total:
            total = curr
            level = depth
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        depth += 1
    return level
