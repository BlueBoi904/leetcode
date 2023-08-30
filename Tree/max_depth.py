"""

559. Maximum Depth of N-ary Tree
Easy
2.4K
79
company
Microsoft
company
LinkedIn
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: 3
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5

"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def maxDepth(root: Node) -> int:
    def traverse_node(node, level):
        if len(result) == level:
            result.append([])
        result[level].append(node.val)
        for child in node.children:
            traverse_node(child, level + 1)

    result = []

    if root is not None:
        traverse_node(root, 0)
    return len(result)



# Alt solution


class Solution:
    def maxDepth(self, root: 'Node') -> int:

        if not root:
            return 0
        elif root.children:
            return 1 + max([self.maxDepth(c) for c in root.children])
        else:
            return
