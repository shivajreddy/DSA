# write a dfs to find if there is a cycle
g = {
    0: [1],
    1: [0],
}


def has_cycle(graph):
    n = len(graph)
    visited = [0] * (n + 1)
    rec_stack = set()

    def dfs(node):
        if node in rec_stack:
            return True

        visited[node] = 1
        rec_stack.add(node)

        for child in graph[node]:
            if dfs(child):
                return True
        rec_stack.remove(node)
        return False

    for key in g.keys():
        if not visited[key]:
            if dfs(key):
                return True
    return False


print(has_cycle(g))
