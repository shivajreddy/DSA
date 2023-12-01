"""
Minimum Spanning Tree

Algorithm: Prim's Algorithm

1. maintain a min. PQ that sorts the edges based on min. edge cost
2. start with a random node 's'
3. while PQ is not empty:
    1. deque the next cheapest edge from PQ
    2. if the curr node is already visited skip it
    3. mark it as visited and add to the poll
    4. iterate over the curr node's edges and add all its edges to PQ

"""
import heapq
from collections import defaultdict, deque

_g = [
    ("e1", "e2", 6),
    ("e1", "e4", 5),
    ("e1", "e3", 4),
    ("e2", "e3", 2),
    ("e4", "e5", 3)
]

g = defaultdict(list)

for u, v, w in _g:
    g[u].append((w, v))
    g[v].append((w, u))

# print(g)

n = len(g)

edge_count = 0
inf = float('inf')
result = []

# BFS
root = "e1"  # arbitrary
visited = set()

# ( weight, parent_node, destination_node)
pq = [(0, None, root)]
heapq.heapify(pq)

while pq:
    # node, node_weight = q.popleft()
    node_weight, parent_node, curr_node = heapq.heappop(pq)

    if curr_node in visited:
        continue

    visited.add(curr_node)

    if parent_node is not None:
        print('final edge', parent_node, curr_node, node_weight)

    for neighbour_weight, neighbour in g[curr_node]:
        # q.append((neighbour, neighbour_weight))
        heapq.heappush(pq, (neighbour_weight, curr_node, neighbour))
