# Graph

"""
Graph: connection of vertices with edges
G = (V,E) [where v is the set of vertices, E is the set of edges]

Directed Graph:
    - There is direction to the edges.
    - Also known as Di-Graph


If there is a cycle in Directed Graph it's called "Self-loop" Graph. ( 1.next = 1, here 1 connects to itself)

1 -> 4 when two nodes are connected with an edge, they are called "Adjacent Vertices" (can be 1 <-> 4)

4 <-> 3  these are two vertices that connect to each other. These are called "Parallel edges"

2->1, 3->1, 9->1 In this graph the "In-Degree" of node 1, is 3. In-Degree is the #.of incoming edges to a vertex

1->21, 1->5 In this graph the "Out-Degree" of node 1 is 2. Out-Degree is the #.of outgoing edges from a vertex



Simple Graph: A directed graph is a simple graph, when below conditions satisfy
    - If there are no self-loop vertices, and,
    - If there are no parallel-edges


Un-Directed Graph / Non-Directed Graph:
    - A graph where the vertices have no direction
    - Also known as Graph
    - There is only "Degree" but there is no "In-Degree" or "Out-Degree" since there is no direction


Non-Connected Graph:
    - when there are 2 or more components(graphs), that do not have connections with each other
    - If you join two components(graphs) by placing an edge between two vertices then it becomes a connected graph.
    - But if you remove that connection, then entire graph is now again un-connected with two separate components(graphs).
        - Such vertices whose connection removal will result in splitting the graph into sub-graphs(components) are called "Articulation Point"


Strong-Connected Graph:
    -

"""

"""
Represent the following graph in python
        1 ---- 2
        |      |
        |      |
        4 ---- 3
        \     /
         \   /
           5

    1   2   3   4   5   <-- rows
1   0   1   0   1   0
2   1   0   1   0   0
3   0   1   0   1   1
4   1   0   1   0   1
5   0   0   1   1   0

^
|
columns

matrix = [[0, 1, 0, 1, 0], [1, 0, 1, 0, 0], [0, 1, 0, 1, 1], [1, 0, 1, 0, 1], [0, 0, 1, 1, 0]]

"""


class Graph:

    def __init__(self, V):
        self._V = V  # private member for # of vertices
        self._E = 0  # number of edges
        self._edges = [[] for i in range(V)]

    def total_vertices(self):
        return self._V

    def total_edges(self):
        return self._E

    def add_edge(self, x, y):  # add an edge b/w x and y
        self._validate_vertex(x)
        self._validate_vertex(y)
        self._edges[x].append(y)
        self._edges[y].append(x)
        self._E += 1

    def _validate_vertex(self, v):
        if v < 0 or v >= self._V:
            raise Exception("vertex" + str(v) + " is not b/w 0 and " + str(self._V - 1))

    def __str__(self):
        return str(self._edges)
