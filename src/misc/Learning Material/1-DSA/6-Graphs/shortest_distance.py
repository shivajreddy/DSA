from collections import defaultdict, deque

edges = [["v1", "v2"], ["v1", "v3"], ["v2", "v4"], ["v2", "v5"], ["v4", "v3"], ["v5", "v6"], ["v6", "v4"]]
courses = [[0, 1], [1, 2], [0, 2], [1, 3], [2, 3]]
courses_none = [[0, 1], [1, 2], [2, 0]]

graph = [("e1", "e2", 6),
         ("e2", "e3", 2),
         ("e1", "e3", 4),
         ("e4", "e5", 3),
         ("e1", "e4", 5)]

mst = [("e2", "e3", 2),
       ("e4", "e5", 3),
       ("e1", "e3", 4),
       ("e1", "e4", 5)]

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


# ! BFS
def find_shortest_path_distance(s: str, d: str, edges: list[list[str]]) -> int:
    # build a graph from edges
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v] = []

    print(f"graph={graph}")

    q = deque()
    q.append([s])
    visited = set()
    paths = []

    while q:
        path = q.popleft()
        curr = path[-1]
        if curr == d:
            paths.append(path)
        if curr not in visited:
            visited.add(curr)

            for child in graph[curr]:
                if child not in visited:
                    new_path = path + [child]
                    q.append(new_path)

    if not paths:
        return -1
    result = paths[0]
    for path in paths:
        result = path if len(path) < len(result) else result
    return len(result) - 1


# ! DFS - Stack
def dfs_find_shortest_path_distance(s: str, d: str, edges: list[list[str]]) -> int:
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v] = []
    # print(f"graph={graph}")

    paths = []
    visited = set()

    def dfs(path):
        # print(f"path={path}")
        curr = path[-1]
        if curr == d:
            paths.append(path)
            return
        if curr not in visited:
            visited.add(curr)
            for child in graph[curr]:
                new_path = path + [child]
                dfs(new_path)
            path.pop()

    dfs([s])
    # print(f"paths={paths}")

    if not paths:
        return -1
    result = len(graph.keys())
    for path in paths:
        result = min(result, len(path))
    return result - 1


find_shortest_path_distance("v1", "v4", edges)

'''
Modify the above algorithm to return the path itself. 
For the test inputs, the path will always exist.
'''


def find_shortest_path(s: str, d: str, edges: list[list[str]]) -> list[str]:
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v] = []
    # print(f"graph={graph}")

    paths = []
    visited = set()

    def dfs(path):
        # print(f"path={path}")
        curr = path[-1]
        if curr == d:
            paths.append(path)
            return
        if curr not in visited:
            visited.add(curr)
            for child in graph[curr]:
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


def find_shortest_path_wt(s: str, d: str, edges: list[list[str]], k: int) -> list[str]:
    return find_shortest_path(s, d, edges)


'''
Given a list of course prerequisites each in the form [0, 1] 
where 0 is a prerequisite of 1 and n, the total number of courses, 
write a function to output a valid course ordering, 
or None if not possible. Courses are numbered from 0 to n-1.
'''


def check_cycle(graph: dict[str, list[str]]) -> bool:
    def dfs(node, visited, rec_stack):
        visited.add(node)
        rec_stack.add(node)
        for child in graph[node]:
            if child in rec_stack:
                return True
            if dfs(child, visited, rec_stack):
                return True
        rec_stack.remove(node)
        return False

    visited = set()
    rec_stack = set()
    for node in graph.keys():
        if node not in visited:
            if dfs(node, visited, rec_stack):
                return True
    return False


def find_valid_course_ordering_if_exists(prerequisites: list[list[int]], n: int) -> list[int] | None:
    # build a graph
    graph = defaultdict(list)
    for u, v in prerequisites:
        graph[u].append(v)
        graph[v]

    if check_cycle(graph):
        return None

    n = len(graph)

    def dfs(path, visited):
        node = path[-1]
        if node not in visited:
            visited.add(node)
            for child in graph[node]:
                print(f"child={child}, visited={visited}, path={path}")
                if child not in visited:
                    path.append(child)
                    dfs(path, visited)
            return path

    result = -1
    for node in range(n):
        print(f"for node:{node}")
        all_courses_path = dfs([node], set())
        if len(all_courses_path) == n:
            result = all_courses_path
            print(f"all_courses_path={all_courses_path} result={result}, for node={node}")
            break
    print(f"result={result}")
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


def output_mst(edges: list[tuple[str, str, int]]) -> list[tuple[str, str, int]]:
    pass


# ! TESTS
"""
def test_find_shortest_path_distance_1():
    assert find_shortest_path_distance("v1", "v4", edges) == 2


def test_find_shortest_path_distance_2():
    assert find_shortest_path_distance("v4", "v5", edges) == -1


def test_find_shortest_path_1():
    assert find_shortest_path("v1", "v4", edges) == ["v1", "v2", "v4"]


def test_find_shortest_path_2():
    assert find_shortest_path("v1", "v6", edges) == ["v1", "v2", "v5", "v6"]


def test_find_shortest_path_wt_1():
    assert find_shortest_path_wt("v1", "v6", edges, 5) == ["v1", "v2", "v5", "v6"]
"""


def test_find_valid_course_ordering_if_exists_1():
    assert find_valid_course_ordering_if_exists(courses, 4) == [0, 1, 2, 3]


def test_find_valid_course_ordering_if_exists_2():
    assert find_valid_course_ordering_if_exists(courses_none, 4) == None


def test_output_mst_1():
    assert set(output_mst(graph)) == set(mst)
