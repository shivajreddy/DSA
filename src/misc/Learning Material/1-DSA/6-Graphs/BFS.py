"""
Bread First Search
"""
import collections
from PlotGraph import plot_graph_from_edges


def create_adj_list(edges: list[list[int]]):
    adj_list = collections.defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list


def create_adj_matrix(total_nodes, edges: list[list[int]]):
    # result_matrix = [[False * (total_nodes + 1)] for _ in range(total_nodes + 1)]
    result_matrix = [[False for _ in range(total_nodes + 1)] for _ in range(total_nodes + 1)]
    for u, v in edges:
        result_matrix[u][v] = True
        result_matrix[v][u] = True
    return result_matrix


edges = [[1, 2], [1, 4], [2, 3], [3, 4], [3, 5], [4, 5]]
total_nodes = 5
adj_matrix = create_adj_matrix(total_nodes, edges)

'''
Graph:
        1 ---- 2
        |      |
        |      |
        4 ---- 3
         \    /
          \  /
            5

edges = [[1,2], [1,4], [2, 3], [3, 4], [3, 5], [4, 5]]
adj_matrix: [[T, F, T, F, F],
             [T, F, T, F, F],
             [T, F, T, F, F],
             [T, F, T, F, F]]

             v   v   v   v   v   v
             ⬇   ⬇   ⬇   ⬇   ⬇   ⬇
        x |  0   1   2   3   4   5  ⬅ rows
        ---------------------------
        0 |  -   -   -   -   -   -
    u ➡ 1 |  -   F   T   F   T   F
        2 |  -   T   F   T   F   F
        3 |  -   F   T   F   T   T
        4 |  -   T   F   T   F   T
        5 |  -   F   F   T   T   F
        ⬆
        columns
'''


def bfs(matrix, n, starting_vertex):
    # print("starting_vertex = ", starting_vertex)
    # create the adj_matrix
    q = collections.deque([starting_vertex])  # Queue to track all the
    visited = [False for _ in range(n + 1)]  # Track all the visited nodes
    visited[starting_vertex] = True

    while q:
        u = q.popleft()
        for v in range(n + 1):
            # print("v =", v)
            # if there is an edge between u&v and v is not visited
            if matrix[u][v] and not visited[v]:
                visited[v] = True
                q.append(v)
                print(f"u={u}, v={v} | visited={visited}")

    print("final visited=", visited)


bfs(adj_matrix, total_nodes, 1)
# plot_graph_from_edges(edges)
