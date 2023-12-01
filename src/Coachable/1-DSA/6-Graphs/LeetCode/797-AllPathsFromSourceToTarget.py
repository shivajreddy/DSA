from collections import defaultdict
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        n = len(graph)
        # create an adj_list
        hm = defaultdict(list)

        for node in range(n):
            hm[node] = graph[node]

        # start with a random node
        stack = [[0]]
        visited = [False for _ in range(n)]
        result = []

        while stack:
            path = stack.pop()
            curr = path[-1]
            print(f'path={path}, curr={curr}, hm[curr]={hm[curr]}')

            if curr == n - 1:
                result.append(path)

            for child in hm[curr]:

                if not visited[child]:
                    new_path = path + [child]
                    stack.append(new_path)

        return result


def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    n = len(graph)
    # create an adj_list
    hm = defaultdict(list)

    for node in range(n):
        hm[node] = graph[node]

    # start with a random node
    stack = [[0]]
    visited = [False for _ in range(n)]
    result = []

    while stack:
        path = stack.pop()
        curr = path[-1]
        print(f'path={path}, curr={curr}, hm[curr]={hm[curr]}')

        if curr == n - 1:
            result.append(path)

        for child in hm[curr]:

            if not visited[child]:
                new_path = path + [child]
                stack.append(new_path)

    return result
