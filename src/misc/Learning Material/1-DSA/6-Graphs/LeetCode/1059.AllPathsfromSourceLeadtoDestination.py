from collections import defaultdict
from typing import List


class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        visited = [0] * n
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            # graph[v]

        def dfs(path):
            node = path[-1]

            if visited[node] == -1:
                return False
            if visited[node] == 1:
                return True
            if not graph[node]:
                return node == destination

            visited[node] = -1
            for child in graph[node]:
                new_path = path + [child]
                if not dfs(new_path):
                    return False

            visited[node] = 1
            return True

        return dfs([source])
