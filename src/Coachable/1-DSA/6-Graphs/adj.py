"""
Graph = (V, E)
V -> no.of vertices
E -> no.of edjes
"""


class AdjacencyMatrix:

    # _v -> total vertices, _e -> total edges
    def __init__(self, total_vertices=5, total_edjes=5):
        self._v = total_vertices
        self._e = total_edjes

        self.adj = [[False] * self._v for _ in range(self._v)]
        # print("totoal sub arrays", len(self.adj))
        # print("totoal subsub arrays", len(self.adj[0]))

    def V(self):
        return self._v

    def E(self):
        return self._e

    # returns all the neighbours of vertex v
    def adj(self, v):
        result = []
        for link in self.adj[v]:
            result.append(link) if link else None
        return result


adj1 = AdjacencyMatrix()
# print(adj1.adj)
