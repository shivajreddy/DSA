from collections import deque, defaultdict
from typing import List


class UnionFind:
    def __init__(self, capacity: int) -> None:
        self.arr = [-1] * capacity

    # Find parent of the set
    def find_parent(self, x: int) -> int:
        x_parent = self.arr[x]

        # Path Compression
        while x_parent > -1:
            x_parent = self.find_parent(x_parent)
        self.arr[x] = x_parent

        return x_parent

    # Union two sets
    def union_sets(self, a: int, b: int) -> bool:
        print("union: ", a, b, self.arr)
        a_parent, b_parent = self.find_parent(a), self.find_parent(b)
        print("parents:", a_parent, b_parent)

        if a_parent == -1 and b_parent == -1:
            if a < b:  # mark a as the parent
                self.arr[b] = a
                self.arr[a] -= 1
            else:  # mark b as parent
                self.arr[a] = b
                self.arr[b] -= 1
            print("union-stop: ", a, b, self.arr)
            return True

        # cycle
        if a_parent == b_parent:
            print("union-stop: ", a, b, self.arr)
            return False

        # Update sets
        if a_parent < b_parent:  # mark a as the parent
            self.arr[b] = a
            self.arr[a] -= 1
        else:  # mark b as the parent
            self.arr[a] = b
            self.arr[b] -= 1

        print("union-stop: ", a, b, self.arr)
        return True


class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # return self.using_union_find(n, edges)
        # return self.using_dfs(n, edges)
        return self.using_bfs(n, edges)

    def using_union_find(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)
        for a, b in edges:
            if not uf.union_sets(a, b):
                print("Stop: FALSE")
                return False

        print("Stop: TRUE")
        return True

    def using_dfs(self, n: int, edges: List[List[int]]) -> bool:
        # build tree
        tree = defaultdict(set)
        for a, b in edges:
            if a == b:
                return False
            if a < b:
                tree[a].add(b)
            else:
                tree[b].add(a)

        def dfs(i, seen):
            if i in seen:
                return False
            seen.add(i)
            for child in tree[i]:
                if not dfs(child, seen):
                    return False
            return True

        seen = set()
        for i in range(n):
            if len(seen) == n:
                return True
            if not dfs(i, seen):
                return False
        return True

    def using_bfs(self, n: int, edges: List[List[int]]) -> bool:
        # build tree
        total_nodes = set()
        tree = defaultdict(set)
        for a, b in edges:
            if a == b:
                return False
            total_nodes.add(a)
            total_nodes.add(b)
            if a < b:
                tree[a].add(b)
            else:
                tree[b].add(a)

        if n != len(total_nodes):
            return False

        q = deque([0])
        seen = set()
        while q:
            node = q.popleft()
            if node in seen:
                return False
            seen.add(node)
            for child in tree[node]:
                q.append(child)

        return True


# TESTS -----------------------------------------------------------------------
sol = Solution()

assert sol.valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) == True

assert sol.valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) == False

assert sol.valid_tree(2, []) == False

assert not sol.valid_tree(
    10, [[0, 1], [5, 6], [6, 7], [9, 0], [3, 7], [4, 8], [1, 8], [5, 2], [5, 3]]
)
