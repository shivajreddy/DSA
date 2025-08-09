# multistage graph using DP -> Tabulation method

# input
graph = [
    # 0  1  2  3  4  5  6  7  8
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
    [0, 0, 2, 1, 3, 0, 0, 0, 0],  # 1
    [0, 0, 0, 0, 0, 2, 3, 0, 0],  # 2
    [0, 0, 0, 0, 0, 6, 7, 0, 0],  # 3
    [0, 0, 0, 0, 0, 6, 8, 9, 0],  # 4
    [0, 0, 0, 0, 0, 0, 0, 0, 6],  # 5
    [0, 0, 0, 0, 0, 0, 0, 0, 4],  # 6
    [0, 0, 0, 0, 0, 0, 0, 0, 5],  # 7
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 8
]
stages = 4


# DP algorithm
def main():
    n = len(graph)
    cost = [0] * n
    dest = [0] * n
    path = [0] * (stages + 1)

    for node in range(n - 1, 0, -1):

        small = float('inf')
        for child in range(node + 1, n):
            if graph[node][child] != 0:
                if graph[node][child] + cost[child] < small:
                    small = graph[node][child] + cost[child]
                    dest[node] = child
        cost[node] = 0 if small == float('inf') else small

    path[1], path[stages] = 1, n - 1

    for idx in range(2, stages):
        path[idx] = dest[path[idx - 1]]

    print(cost)
    print(dest)
    print(path)


if __name__ == "__main__":
    main()
