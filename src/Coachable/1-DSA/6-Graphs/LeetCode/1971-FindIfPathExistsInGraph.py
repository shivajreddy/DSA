from collections import defaultdict
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        # create a adj_list
        hm = defaultdict(list)
        for u, v in edges:
            hm[u].append(v)
            hm[v].append(u)

        visited = [0 for _ in range(n)]

        stack = [source]

        while stack:  # O(n)
            curr = stack.pop()

            if curr == destination: return True

            if not visited[curr]:

                visited[curr] = 1

                for child in hm[curr]:  # O(n)
                    stack.append(child)

        return False


''' using Recursion
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        # create a adj_list
        hm = defaultdict(list)
        for u, v in edges:
            hm[u].append(v)
            hm[v].append(u)

        visited = [0 for _ in range(n)]

        def dfs(node):
            if node == destination:
                return True

            if not visited[node]:
                visited[node] = True
                for child in hm[node]:
                    if dfs(child):
                        return True
            return False

        return dfs(source)
'''
