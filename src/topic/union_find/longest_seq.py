from typing import List


class UnionFind:
    def __init__(self) -> None:
        self.val_to_parent_map = {}
        self.size_map = {}
        self.max_size = 0

    def find(self, x: int) -> int:
        if self.val_to_parent_map[x] != x:
            self.val_to_parent_map[x] = self.find(self.val_to_parent_map[x])
        return self.val_to_parent_map[x]

    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.val_to_parent_map[root_x] = root_y
            self.size_map[root_y] += self.size_map[root_x]
            self.max_size = max(self.max_size, self.size_map[root_y])

    def add(self, x):
        if x not in self.val_to_parent_map:
            self.val_to_parent_map[x] = x
            self.size_map[x] = 1
            self.max_size = max(1, self.max_size)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        UF = UnionFind()

        for num in nums:
            UF.add(num)

        for num in nums:
            if num - 1 in UF.val_to_parent_map:
                UF.union(num, num - 1)

        print("")
        print(UF.val_to_parent_map)
        print(UF.size_map)
        print(UF.max_size)
        return UF.max_size


sol = Solution()
sol.longestConsecutive([100, 3, 200, 4, 2, 1])
sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
