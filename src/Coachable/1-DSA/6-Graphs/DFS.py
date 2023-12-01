"""
Depth First Search
"""
from collections import defaultdict

"""
    1 --- 2
    |\    | \
    | \   |  \
    |  4  |   6
    |   \ |  /
    |    \|/
    3 --- 5

"""

n = 6
edges = [[1, 3], [1, 4], [1, 2], [2, 5], [2, 6], [3, 5]]


def dfs(node: int):
    # create an adjacent list
    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    print(adj_list)

    visited = [False for _ in range(n + 1)]

    stack = [node]

    while stack:

        curr = stack.pop()

        if not visited[curr]:

            print(f"Visited:{curr}")

            visited[curr] = True

            for child in adj_list[curr]:
                stack.append(child)


dfs(1)
