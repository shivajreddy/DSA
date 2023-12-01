from __future__ import annotations
import collections
import heapq
from typing import Tuple

'''
Given a DAG that is represented as a collection of edges, i.e. ["n1", 
"n2"] means that n1 precedes n2 (visually, n1 -> n2),
'''

'''
Create an adjacency list for it.
'''


def to_adjacency_list(edges: list[list[str]]) -> dict[str, list[str]]:
    hm = collections.defaultdict(list)
    for u, v in edges:
        hm[u].append(v)
        hm[
            v]  # since we go through all 'u' but 'v', so inititate empty
        # list for empty one's
    return hm


'''
Create an adjacency matrix for it where each 
respective cell contains 0 for unconnected and 1 for connected.
Index 0 represents "v1" and so on. 
'''


def to_adjacency_matrix(edges: list[list[str]]) -> list[list[int]]:
    hm = {}
    n = 0
    for u, v in edges:
        if u not in hm:
            hm[u] = n
            n += 1
        if v not in hm:
            hm[v] = n
            n += 1

    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for x, y in edges:
        u, v = hm[x], hm[y]
        matrix[u][v] = 1

    return matrix


'''
Suppose you’re given a list of graph edges where 
each edge is of the form ["e1", "e2"], meaning that 
"e1" is connected to "e2". You’re also given a source 
node s and destination node d.
'''

'''
Write an algorithm to return the distance of one of the shortest paths, 
where each connection costs 1 to traverse. Return -1 if there is no path.
'''


def find_shortest_path_distance(s: str, d: str, edges: list[list[str]]) -> int:
    graph = collections.defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v] = []

    paths = []
    visited = set()

    def dfs(path):
        node = path[-1]
        if node == d:
            paths.append(path)
            return
        if node not in visited:
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    new_path = path + [child]
                    dfs(new_path)
            path.pop()

    dfs([s])
    # print(f'paths={paths}')

    if not paths: return -1
    result = len(graph)
    for path in paths:
        result = min(result, len(path))
    return result - 1


'''
Modify the above algorithm to return the path itself. 
For the test inputs, the path will always exist.
'''


def find_shortest_path(s: str, d: str, edges: list[list[str]]) -> list[str]:
    graph = collections.defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v] = []

    paths = []
    visited = set()

    def dfs(path):
        node = path[-1]
        if node == d:
            paths.append(path)
            return
        if node not in visited:
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    new_path = path + [child]
                    dfs(new_path)
            path.pop()

    dfs([s])
    result = paths[0]
    for path in paths:
        if len(path) < len(result):
            result = path
    return result


'''
Modify the above algorithm to work if each connection costs k where k > 0.
'''


def find_shortest_path_wt(s: str, d: str, edges: list[list[str]], k: int) -> \
list[str]:
    # since k is constant, smallest path is the path with least no. of edges
    return find_shortest_path(s, d, edges)


'''
Given a list of course prerequisites each in the form [0, 1] 
where 0 is a prerequisite of 1 and n, the total number of courses, 
write a function to output a valid course ordering, 
or None if not possible. Courses are numbered from 0 to n-1.
'''


def check_cycle(graph: dict[str, list[str]]) -> bool:
    def dfs(node, visited, curr_stack):
        visited.add(node)
        curr_stack.add(node)
        for child in graph[node]:
            if child in curr_stack:
                return True
            if child not in visited:
                if dfs(child, visited, curr_stack):
                    return True
        curr_stack.remove(node)
        return False

    visited, curr_stack = set(), set()
    for node in graph.keys():
        if node not in visited:
            if dfs(node, visited, curr_stack):
                return True
    return False


def find_valid_course_ordering_if_exists(prerequisites: list[list[int]],
                                         n: int) -> list[int] | None:
    graph = collections.defaultdict(list)
    for u, v in prerequisites:
        graph[u].append(v)
        graph[v]

    # if there is a cycle, then there cant be Top sort
    if check_cycle(graph): return None

    n = len(graph)

    def dfs(path, visited):
        node = path[-1]
        if node not in visited:
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    path.append(child)
                    dfs(path, visited)
            return path

    result = -1
    for node in range(n):
        all_courses_path = dfs([node], set())
        if len(all_courses_path) == n:
            result = all_courses_path
            break
    return result


'''
Suppose you’re given a list of graph edges where each edge is of the form 
("e1", "e2", 3), meaning that "e1" is connected to "e2" and has an 
edge weight of 3. The graph is connected. Write an algorithm to print 
out the an MST of the graph.

You can assume the graph is undirected for this problem. 
If there is an edge (e1, e2, 3) in the input,
you should assume there is an equivalent edge (e2, e1, 3) as well.
'''

'''
         e2
        /  \
      6/    \2
      /   4  \
    e1 ------ e3
     \
     5\
       \     3
        e4 ------ e5
'''


def output_mst(edges: list[tuple[str, str, int]]) -> list[tuple[str, str, int]]:
    # TODO: implement Prim's algorithm to find MST

    # build an adj_list
    graph = collections.defaultdict(list)

    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))

    n = len(graph)

    visited = set()
    pq = []
    heapq.heapify(pq)  # 1. make a priority queue

    heapq.heappush(pq, (0, None, "e1"))

    result = []

    while pq:
        edge_weight, parent_node, curr_node = heapq.heappop(pq)

        if curr_node in visited:
            continue

        visited.add(curr_node)

        if parent_node is not None:
            sorted_path = tuple(sorted((parent_node, curr_node)))
            result.append((sorted_path[0], sorted_path[1], edge_weight))
            # result.append((parent_node, curr_node, edge_weight))

        for neighbour_edge_weight, neighbour_node in graph[curr_node]:
            heapq.heappush(pq,
                           (neighbour_edge_weight, curr_node, neighbour_node))

    return result
