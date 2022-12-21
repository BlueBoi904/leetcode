"""


"""

from collections import defaultdict


def valid_path(n, edges, source, destination):
    graph = defaultdict(list)

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    seen = [False] * n

    def dfs(curr_node):
        if curr_node == destination:
            return True
        if not seen[curr_node]:
            seen[curr_node] = True
            for next_node in graph[curr_node]:
                if dfs(next_node):
                    return True
        return False

    return dfs(source)
