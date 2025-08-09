from typing import List
import collections


class Solution:
    def findCircleNum(self, matrix: List[List[int]]) -> int:
        """ DFS
        n = len(matrix[0])
        count = 0

        visited = [False for _ in range(n)]
        stack = []

        for x in range(n):

            if not visited[x]:
                count += 1
                stack.append(x)

                while stack:

                    curr = stack.pop()

                    if not visited[curr]:

                        visited[curr] = True

                        for v in range(n):
                            if not visited[v] and matrix[curr][v]:
                                stack.append(v)

        return count
        """

        """BFS
        """
        n = len(matrix)
        visited = [0 for _ in range(n)]  # to track which nodes are already visited
        q = collections.deque()  # we need q for BFS traversal

        count = 0  # count of unique paths

        # for every node starting from 0 to n-1
        for node in range(n):
            if not visited[node]:
                visited[node] = 1
                count += 1  # self cyclic nodes are counted here
                q.append(node)  # now for this node, lets look at all the childs it has
                # along with which child nodes have an edge

                while q:
                    u = q.popleft()
                    # traverse through all the chidren
                    for v in range(n):
                        if not visited[v] and matrix[u][v]:
                            visited[v] = 1
                            q.append(v)

        return count
