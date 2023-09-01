class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue, res = deque([root]), []
        while queue and root:
            res.append(queue[-1].val) # This code gives us the right most node on each lvl

            for _ in range(len(queue)): # Continue iteration through the tree
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        return res