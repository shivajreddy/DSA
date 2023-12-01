"""
Depth First Search
"""


class Node:
    def __init__(self, val: int, neighbors: list | None = None):
        self.val = val
        self.neighbors = neighbors


node_1, node_2, node_3, node_4 = Node(1), Node(2), Node(3), Node(4)
node_5, node_6, node_7 = Node(5), Node(6), Node(7)
graph_adj_vertices = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
]

n = 7
visited = [0 for _ in range(n + 1)]
matrix = [[]]
matrix = graph_adj_vertices


def dfs(node: int):
    u = node
    print(u)
    # if the given node is not visited
    if not visited[u]:
        # mark it as visited
        visited[u] = 1

        for v in range(n):
            # if there is an edge, and v is not visited
            if matrix[u][v] and not visited[v]:
                dfs(v)


dfs(1)

'''
B: E
E: S, W
I: W, Y
M: I
O: B, E, Y
P: 
S: B, E, I, M, O, P
W: M
Y: 

    O
   /|\
  B E Y
    /\
   S  W
  /|\
 I M P

  | B E I M O P S W Y
---------------------
B | 0 0 0 0 0 0 0 1 0
E | 0 1 1 0 0 0 0 1 0
I | 1 1 0 0 0 0 0 0 0
M | 0 0 0 0 0 0 1 0 0
O | 1 0 0 0 0 0 0 1 1
P | 0 0 0 0 0 0 0 0 0
S | 0 0 0 1 1 1 1 1 1
W | 0 0 0 0 0 1 0 0 0
Y | 0 0 0 0 0 0 0 0 0

  | Y  W  S  P  O  M  I  E  B
------------------------------
Y | 0  0  0  0  0  0  0  0  0
W | 0  0  0  0  0  1  0  0  0
S | 0  0  0  1  1  1  1  1  1
P | 0  0  0  0  0  0  0  0  0
O | 1  0  0  0  0  0  0  1  1
M | 0  0  0  0  0  0  1  0  0
I | 1  1  0  0  0  0  0  0  0
E | 0  1  1  0  0  0  0  0  0
B | 0  0  0  0  0  0  0  1  0

'''
