from typing import List

"""

        0
        1
        2
        3


        bfs -> visited set, 

    Disjoin sets

"""


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
        print("union: ", a, b)
        a_parent, b_parent = self.find_parent(a), self.find_parent(b)

        if a_parent == b_parent == -1:
            if a < b:  # mark a as the parent
                self.arr[b] = a
                self.arr[a] -= 1
            else:  # mark b as parent
                self.arr[a] = b
                self.arr[b] -= 1
            print("arr=", self.arr)
            return True

        # cycle
        if a_parent == b_parent:
            print("arr=", self.arr)
            return False

        # Update sets
        if a_parent < b_parent:  # mark a as the parent
            self.arr[b] = a_parent
            self.arr[a] -= 1
        else:  # mark b as the parent
            self.arr[a] = b_parent
            self.arr[b] -= 1

        print("arr=", self.arr)
        return True


class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)
        for a, b in edges:
            if not uf.union_sets(a, b):
                print("Stop: FALSE")
                return False

        print("Stop: TRUE")
        return True


# TESTS
sol = Solution()

n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
assert sol.valid_tree(n, edges) == True

n = 5
assert sol.valid_tree(n, edges) == False
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
