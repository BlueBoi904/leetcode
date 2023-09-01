from collections import deque

def print_all_nodes(root):
    queue = deque([root])

    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()

            print(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)